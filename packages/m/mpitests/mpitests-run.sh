#!/bin/bash

export INHERIT_LOGDIR=$LOGDIR
export LOGDIR=${LOGDIR:-$(mktemp -d)}
export BUILDROOT=${BUILDROOT:-/}
export IMPLEM_LIST_DIR=${IMPLEM_LIST_DIR:-/usr/share/mpitests/implem.d}
IMPLEM_LIST=$(ls ${BUILDROOT}${IMPLEM_LIST_DIR}/* | xargs basename -a)


export glob_err=0
export skipped=0
runimplem(){
	local IMPLEM=$1

	case $IMPLEM in
		mvapich2-psm*)
			# Check that we have a PSM device
			# or it takes ages waiting for it and then fails.
			if [ ! -e /dev/ipath -a ! -e /dev/hfi1 ]; then
				echo "Implementation: $IMPLEM"
				echo -e "\t[SKIPPED] # No ipath device available"
				skipped=$(expr $skipped + 1)
				return 0
			fi
			;;
		openmpi3*)
			export RUN_EXTRA_ARGS="${RUN_EXTRA_ARGS} --oversubscribe"
			;;
	esac
	COMMAND=$(cat ${BUILDROOT}${IMPLEM_LIST_DIR}/$IMPLEM)
	if [ "$COMMAND" == "" ]; then
		echo "[FAILURE]"
		glob_err=$(expr $glob_err + 1)
		return 1
	fi
	eval ${BUILDROOT}$COMMAND
	if [ $? -ne 0 ]; then
		echo "[FAILURE]"
		glob_err=$(expr $glob_err + 1)
		return 1
	else
		echo "[SUCCESS]"
		return 0
	fi
}

echo "Logs are available in $LOGDIR"
for IMPLEM in $IMPLEM_LIST; do
	runimplem $IMPLEM
done

if [ $glob_err -ne 0 ]; then
	echo "[FAILURE] $glob_err implementation(s) have failed"
elif [ $skipped -ne 0 ]; then
	echo "[SKIPPED] No failure but $skipped implementation(s) skipped"
else
	echo "[SUCCESS] All implementations successfull!"
fi

if [ $glob_err -ne 0 ]; then
	echo " * [FAILURE] $glob_err failed"
	echo "# Logs are available in $LOGDIR"
	find $LOGDIR -type f | while read LOG; do
		echo "File: $LOG"
		cat "$LOG"
	done
else
	echo " * [SUCCESS]"
	if [ "$INHERIT_LOGDIR" == "" ]; then
		# Clear the logdir
		rm -Rf $LOGDIR
	else
		echo "# Logs are available in $LOGDIR"
	fi
fi
exit $glob_err
