#!/bin/bash
TEST_RESULT_FILE_BEFORE='test_results.before'
TEST_RESULT_FILE_AFTER='test_results.after'

function usage
{
  echo "usage: $0 buildroot [osc ARGUMENTS]"
  echo "       1. Run first time to create ${TEST_RESULT_FILE_BEFORE}."
  echo "       2. Make source changes."
  echo "       3. Run second time to create ${TEST_RESULT_FILE_AFTER}"
  echo "          and see changes in test results."
}

if [ -z $1 ]; then
  echo 'ERROR: missing a parameter: buildroot'
  usage
  exit 1
fi

if [ "$1" == "-h" ]; then
  usage
  exit 0
fi

export OSC_BUILD_ROOT=$1
shift
apiurl=`cat .osc/_apiurl 2>/dev/null`
if [ ! -z "$apiurl" ]; then
  apiurl="-A $apiurl"
fi
osc $apiurl build $@ --no-verify --with make_test -x valgrind *.spec 
if [ $? -ne 0 ]; then 
  echo "ERROR: build failed. See $OSC_BUILD_ROOT/.build.log for details."
  exit 1
fi
cat $OSC_BUILD_ROOT/.build.log \
      | sed 's:^\[[ 0-9]\+s\] ::' \
      | egrep 'TEST [0-9]+\/[0-9]+|SKIP.*reason' \
      | sed 's:.*\r::' \
      | sort \
    > ${TEST_RESULT_FILE_AFTER}
if [ ! -e ${TEST_RESULT_FILE_BEFORE} ]; then
  echo "Creating ${TEST_RESULT_FILE_BEFORE}"
  echo "Run $0 again AFTER source changes, to create ${TEST_RESULT_FILE_AFTER}."
  echo "Differences will be checked then."
  mv ${TEST_RESULT_FILE_AFTER} ${TEST_RESULT_FILE_BEFORE}
else
  echo --- DIFFERENCES -------------------------------------------
  diff -up $TEST_RESULT_FILE_BEFORE ${TEST_RESULT_FILE_AFTER}
  echo -----------------------------------------------------------
  echo "Do not forgot to "
  echo "rm ${TEST_RESULT_FILE_BEFORE} ${TEST_RESULT_FILE_AFTER}"
  echo
fi

