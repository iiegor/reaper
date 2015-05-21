#! /bin/sh

PYTHON=$(which pypy 2>/dev/null)
if [ -z "$PYTHON" ]; then
  PYTHON=python
fi

DATADIR=${1:-data}
REAPER=${2:-main.py}
ARGS='--cl'

mkdir $DATADIR 2>/dev/null || :
cd ${DATADIR}/

exec ${PYTHON} ../lib/${REAPER} ${ARGS}