#! /bin/sh

PYTHON=$(which pypy 2>/dev/null)
if [ -z "$PYTHON" ]; then
  PYTHON=python
fi

ARG=${1}
DATADIR=${2:-data}
REAPER=${3:-main.py}

mkdir $DATADIR 2>/dev/null || :
cd ${DATADIR}/

exec ${PYTHON} ../lib/${REAPER} ${ARG}