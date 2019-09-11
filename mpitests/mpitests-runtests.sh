#!/bin/bash

export INHERIT_LOGDIR=$LOGDIR
export LOGDIR=${LOGDIR:-$(mktemp -d)}
export RUN_ARGS=${RUN_ARGS:-"-np 2"}
export FLAVOR=@IMPLEM@

IMB_TESTS="IMB-EXT IMB-MPI1 IMB-NBC IMB-RMA"

export implem_err=0

MPI_DIR=@MPI_HOME@
TEST_TOPDIR=${BUILDROOT}${MPI_DIR}/tests

runtest(){
	local TEST=$1
	shift 1
	local NAME=$(basename $TEST)

	echo -ne "\tTest: $TEST "
	if [ "$VERBOSE" != "" ]; then
		set -o pipefail
		eval mpirun "$RUN_ARGS" "$RUN_EXTRA_ARGS" $TEST "$*" | tee -a $LOGDIR/$IMPLEM/$NAME
	else
		eval mpirun "$RUN_ARGS" "$RUN_EXTRA_ARGS" $TEST "$*" >> $LOGDIR/$IMPLEM/$NAME
	fi
	if [ $? -ne 0 ]; then
		echo "[FAILURE]"
		implem_err=$(expr $implem_err + 1)
		return 1
	else
		echo "[SUCCESS]"
		return 0
	fi
}

implem_err=0
echo "Implementation: @IMPLEM@"
mkdir $LOGDIR/@IMPLEM@

. $MPI_DIR/bin/mpivars.sh || exit 1

if [ "$SHORT" != "" ]; then
	# Only run a few IMB benchmarks
	runtest $TEST_TOPDIR/IMB/IMB-MPI1
	runtest $TEST_TOPDIR/IMB/IMB-EXT
else
	# Run all benchmarks

	# OSU Benchmarks
	for TEST in $(ls $TEST_TOPDIR//osu-micro-benchmarks/mpi/*/osu_*); do
		runtest $TEST
	done

	# IMB
	for TEST in $IMB_TESTS; do
		runtest $TEST_TOPDIR/IMB/$TEST
	done

fi

if [ $implem_err -ne 0 ]; then
	echo " * [FAILURE] $implem_err failed"
else
	echo " * [SUCCESS]"
	if [ "$INHERIT_LOGDIR" == "" ]; then
		# Clear the logdir
		rm -Rf $LOGDIR
	fi
fi
exit $implem_err
