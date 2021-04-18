#!/usr/bin/env bash
##############################################################
# Compiles privex.curconv into a self-contained .pyz application,
# allowing it to be ran like a static executable on *NIX systems,
# so long as the system has Python 3 installed.
#
# By default, outputs the compiled PYZ into dist/pyz/conv.pyz
##############################################################

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
: ${ENTRY_POINT="privex/curconv/__main__.py"}
: ${REQ_FILE="requirements.txt"}
: ${COMPILE_PY=0}
: ${COMPILE_THREADS=6}
: ${COMPILE_VERS="3.7 3.8 3.9"}
: ${DEPS_DIR="./deps"}
: ${PY_EXE="python3"}
: ${PY_SHEBANG="#!/usr/bin/env python3"}
: ${OUT_DIR="${DIR}/dist/pyz"}
: ${OUT_NAME="conv.pyz"}
: ${COMPRESS_LEVEL=9}

COMPILE_VERS=($COMPILE_VERS)
#EXTRA_REQS=("idna<3")
SYNC_FILES=("${DIR}/privex" "${DIR}/LICENSE" "${DIR}/README.md" "${DIR}/requirements.txt")
#COMPILE_FILES=("privex" "$DEPS_DIR")

[[ -d "$OUT_DIR" ]] || mkdir -pv "$OUT_DIR"
#cd "$DIR"
TMPX=""

_cleanup-tmp() {
    tmplen="$(wc -c <<< "$TMPX")"
    if [[ -n "$TMPX" ]] && [[ -d "$TMPX" ]]; then
        if (( tmplen < 14 )); then
            >&2 echo -e "Temp dir '${TMPX}' path is shorter than 14 characters. Refusing to remove for safety."
        else
            >&2 echo -e "Removing temp dir '${TMPX}'"
            rm -rf "$TMPX"
        fi
    fi
}

_handle-error() {
    ret=$?
    >&2 echo -e "\n [!!!] Unexpected error occurred. Last return code: $ret \n"
    >&2 echo -e "\n [!!!] _handle-error arguments: $* \n"
    tmplen="$(wc -c <<< "$TMPX")"
    _cleanup-tmp
    return $ret
}

set -eu
set -o pipefail

trap "_cleanup-tmp" EXIT
trap "_handle-error" ERR

TMPX="$(mktemp -d)"
_ret=$?

echo -e "\n\n >>> Entering temporary dir: $TMPX \n"
cd "$TMPX"

echo -e "\n\n >>> Syncing files/folders into temp dir: ${SYNC_FILES[*]} \n"

rsync -avh --exclude '__pycache__' --progress "${SYNC_FILES[@]}" .

echo -e "\n\n >>> Copying entry point '${ENTRY_POINT}' to __main__.py and marking executable ...\n"

cp -v "$ENTRY_POINT" __main__.py
chmod +x __main__.py

echo -e "\n\n >>> Installing requirements from requirements file ${REQ_FILE} into deps dir: ${DEPS_DIR} \n"

"$PY_EXE" -m pip install -U -r "$REQ_FILE" --target "$DEPS_DIR"

echo -e "\n\n >>> Syncing requirements from deps dir ${DEPS_DIR} into temp root \n"

rsync -avh "${DEPS_DIR%/}/" ./
echo -e "\n\n >>> Removing deps dir ${DEPS_DIR} \n"
rm -rf "${DEPS_DIR}"

#echo -e "\n\n >>> Installing extra requirements '${EXTRA_REQS[*]}' into deps dir: ${DEPS_DIR} \n"
#
#"$PY_EXE" -m pip install -U "${EXTRA_REQS[@]}" --target "$DEPS_DIR"

echo -e "\n\n"
if (( COMPILE_PY )); then
#    for c in "${COMPILE_FILES[@]}"; do
    echo
    echo -e " >>> Compiling files into .pyc bytecode files."
    echo -e "     Threads: ${COMPILE_THREADS} \n\n"
    for pyv in "${COMPILE_VERS[@]}"; do
        echo -e "\n     >> Compiling for Python version $pyv \n"
        COMP_CMD="compileall"
        # On Python versions prior to 3.9, compileall lacks features such as -j and -o,
        # thus they require the third party tool 'compileall2' for forwards compatibility.
        case "$pyv" in
            3.4|3.5|3.6|3.7|3.8)
                if ! "python${pyv}" -m pip freeze | grep -q "compileall2"; then
                    "python${pyv}" -m pip install -U compileall2
                fi
                COMP_CMD="compileall2"
                ;;
        esac
        "python${pyv}" -m "$COMP_CMD" -j "$COMPILE_THREADS" -o 0 -o 1 -o 2 -f .
    done
#    done
fi


echo -e "\n\n >>> Compressing folder $TMPX into ZIP file 'compapp.zip'. Compression level: ${COMPRESS_LEVEL} \n"

zip -v -r "-${COMPRESS_LEVEL}" compapp.zip .

X_OUTPATH="${OUT_DIR%/}/${OUT_NAME#/}"
echo -e "\n\n >>> Concatonating shebang and outputting to ${X_OUTPATH} \n"

echo "$PY_SHEBANG" | cat - compapp.zip > "${X_OUTPATH}"

echo -e "\n\n >>> Marking executable: ${X_OUTPATH} \n"

chmod +x "$X_OUTPATH"

echo -e "\n\n +++ FINISHED +++ \n"



