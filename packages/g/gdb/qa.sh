#!/bin/bash

# Note:
# Occasionally we run into PR28561 - "[gdb/testsuite] Error due to not
# reading \r\n at end of mi prompt".
# https://sourceware.org/bugzilla/show_bug.cgi?id=28561
# Not sure how to filter for that.

# TODO:
#
# We run into FAILs like this:
# FAIL: gdb.base/options.exp: test-print: \
#   tab complete "thread apply all print " (clearing input line) (timeout)
# FAIL: gdb.base/options.exp: test-print: \
#   cmd complete "thread apply all print "
# in various test-cases.  One instance is reported here (
# https://sourceware.org/bugzilla/show_bug.cgi?id=27813 ).
# We could do a generic kfail for "(clearing input line) (timeout)", but that
# doesn't filter out the following FAIL.  We need to update the testsuite to
# emit only one FAIL for this, or alternatively, add a possibility in this
# script to KFAIL one and all following FAILs in the same test-case.

usage ()
{
    echo "usage: $0 <1-5>"
    echo "       $0 <6> <dir>"
    echo "Verify remote results at:"
    echo "  ./binaries-testsuite.distro.arch/gdb-testresults"
    echo "1: gdb.sum: Check for 'FAIL: .* internal error' (all configs)"
    echo "2: gdb.sum: Check for 'ERROR:'                  (all configs)"
    echo "3: gdb.log: Check for 'internal-error:'         (all configs)"
    echo "4: gdb.sum: Check FAIL and ERROR                (known clean configs)"
    echo "5: gdb.sum: Check gdb.suse PASS                 (all configs)"
    echo "Verify local results at:"
    echo "  \$dir"
    echo "6: gdb.sum: Check FAIL and ERROR"
}

if [ $# -eq 0 ]; then
    usage
    exit 1
fi

n="$1"
shift

if [ "$n" = "6" ]; then
    dir="$1"
    shift
fi

echo_line ()
{
    for n in "$@"; do
        echo "$n"
    done
}

join ()
{
    local char
    char="$1"
    shift

    local res
    res=""

    local first
    first=true
    for elem in "$@"; do
        if $first; then
            first=false
        else
            res+="$char"
        fi
        res+="$elem"
    done
    echo "$res"
}

report_sum ()
{
    local sum
    sum="$1"

    echo
    echo "$sum:"

    if [ ! -f "$sum" ]; then
	echo "MISSING"
	return
    fi

    kfail_re=$(join "|" "${kfail[@]}")
    echo FAILs:
    grep ^FAIL: "$sum" \
	| grep -E -v "$kfail_re"
    echo ERROR COUNT:
    grep -c ^ERROR: "$sum"
}

kfail=(
    # https://sourceware.org/bugzilla/show_bug.cgi?id=26971
    "FAIL: gdb.arch/amd64-init-x87-values.exp: check_x87_regs_around_init: check post FLD1 value of .fop"
    "FAIL: gdb.arch/amd64-init-x87-values.exp: check_x87_regs_around_init: check post FLD1 value of .fioff"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=24845
    "FAIL: gdb.base/step-over-syscall.exp: clone: displaced=off: single step over clone"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=19436#c1
    "FAIL: gdb.cp/no-dmgl-verbose.exp: setting breakpoint at 'f\(std::string\)'"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=25504
    "FAIL: gdb.threads/process-dies-while-detaching.exp: single-process: continue: .*: continue"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28065
    "FAIL: gdb.threads/access-mem-running-thread-exit.exp:"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=27813
    "FAIL: gdb.cp/cpcompletion.exp:"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=25503
    "FAIL: gdb.threads/signal-while-stepping-over-bp-other-thread.exp: step \(pattern 3\)"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=26915
    "FAIL: gdb.threads/schedlock.exp: schedlock=off: .*: other threads ran - unlocked"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28479
    "FAIL: gdb.mi/mi-nonstop.exp: wait for thread exit \(timeout\)"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=26273
    "FAIL: gdb.threads/gcore-stale-thread.exp: save a corefile"
    "FAIL: gdb.threads/gcore-stale-thread.exp: exited thread is current due to non-stop"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28467
    # -pie, x86_64 -m32 or i586.
    "FAIL: gdb.base/nodebug.exp: p/c \(int\) array_index\(\"abcdef\",2\)"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28617
    "FAIL: gdb.base/info-os.exp: get process groups \(timeout\)"
    "FAIL: gdb.base/info-os.exp: get threads \(timeout\)"
    "FAIL: gdb.base/info-os.exp: get file descriptors \(timeout\)"
    "FAIL: gdb.base/info-os.exp: get internet-domain sockets \(timeout\)"
    "FAIL: gdb.base/info-os.exp: get shared-memory regions \(timeout\)"
    "FAIL: gdb.base/info-os.exp: get semaphores \(timeout\)"
    "FAIL: gdb.base/info-os.exp: get message queues \(timeout\)"
    "FAIL: gdb.base/info-os.exp: info os unknown_entry \(timeout\)"
    "FAIL: gdb.base/info-os.exp: continue \(timeout\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=26284
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28275
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28343
    "FAIL: gdb.threads/detach-step-over.exp: .*internal error"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=26363
    "FAIL: gdb.xml/tdesc-reload.exp: .*internal error"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=26761
    "FAIL: gdb.base/gdb-sigterm.exp: .*internal error"
)

kfail_factory=(
    # https://sourceware.org/bugzilla/show_bug.cgi?id=27027
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28464
    "FAIL: gdb.ada/mi_var_access.exp: Create varobj \(unexpected output\)"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28463
    "FAIL: gdb.ada/set_pckd_arr_elt.exp: scenario=minimal: print va.t\(1\) := 15"
    "FAIL: gdb.ada/set_pckd_arr_elt.exp: scenario=minimal: continue to update_small for va.t"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28108
    "FAIL: gdb.base/langs.exp: up to foo in langs.exp"
    "FAIL: gdb.base/langs.exp: up to cppsub_ in langs.exp"
    "FAIL: gdb.base/langs.exp: up to fsub in langs.exp"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=27539
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(i\)"
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(i\) == &typeid\(typeof\(i\)\)"
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(cp\)"
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(cp\) == &typeid\(typeof\(cp\)\)"
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(ccp\)"
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(ccp\) == &typeid\(typeof\(ccp\)\)"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28461
    "FAIL: gdb.reverse/fstatat-reverse.exp: continue to breakpoint: marker2"
    # https://sourceware.org/pipermail/gdb-patches/2021-October/182449.html
    "FAIL: gdb.threads/current-lwp-dead.exp: continue to breakpoint: fn_return"
    # Similar error message to the one above, see if fixing that one fixes this.
    "FAIL: gdb.threads/clone-new-thread-event.exp: catch SIGUSR1"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=27238
    "FAIL: gdb.go/package.exp: setting breakpoint at package2.Foo"
    "FAIL: gdb.go/package.exp: going to first breakpoint \(the program exited\)"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28551
    "FAIL: gdb.go/package.exp: going to first breakpoint \\(GDB internal error\\)"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28468
    "FAIL: gdb.threads/signal-command-handle-nopass.exp: step-over (yes|no): signal SIGUSR1"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28477
    "FAIL: gdb.base/step-over-syscall.exp: clone: displaced=off: continue to marker \(clone\)"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28478
    "FAIL: gdb.gdb/selftest.exp: backtrace through signal handler"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=26867
    "FAIL: gdb.threads/signal-sigtrap.exp: sigtrap thread 1: signal SIGTRAP reaches handler"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28510
    "FAIL: gdb.debuginfod/fetch_src_and_symbols.exp: local_url: br main"
    "FAIL: gdb.debuginfod/fetch_src_and_symbols.exp: local_url: l"
)

case $n in
    1)
	# 'FAIL: .* internal error' in gdb.sum.
	# Test fail due to internal error.
	#
	# Todo: apply kfail_factory only on factory sum files.
	kfail+=("${kfail_factory[@]}")
	kfail_re=$(join "|" "${kfail[@]}")
	grep "^FAIL:.*internal error" binaries-testsuite*/gdb-testresults/*.sum \
	     | grep -E -v "$kfail_re"
	;;

    2)
	# 'ERROR:' in gdb.sum.
	# A dejagnu or tcl ERROR, may hide real problems.
	#
	kfail+=(
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=28323
	    "SLE-12.x86_64.*gdb.ada/mi_dyn_arr.exp"
	)

	kfail_re=$(join "|" "${kfail[@]}")
	grep -A1 "ERROR:.*no longer" binaries-testsuite*/gdb-testresults/*.sum \
	    | grep -E -v "ERROR|\--" | grep -E -v "$kfail_re"
	;;

    3)
	# 'internal-error' in gdb.log
	# Catch all internal-errors, not just the ones reported by dejagnu.
	#
	kfail+=(
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=26284
	    "infrun.c:[0-9]*: internal-error: int finish_step_over\(.*\): Assertion \`ecs->event_thread->control.trap_expected' failed."
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=26363
	    ".i586.*i386-linux-nat.c:[0-9]*: internal-error: Got request for bad register number 41."
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=26761
	    "thread.c:[0-9]*: internal-error: .* inferior_thread\(\): Assertion \`current_thread_ \!= nullptr' failed."
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=19675
	    "linux-nat.c:[0-9]*: internal-error: wait returned unexpected status"
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=28553
	    "infrun.c:[0-9]*: internal-error: thread .* needs a step-over, but not in step-over queue"
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=19675
	    "linux-nat.c:[0-9]*: internal-error: wait returned unexpected"
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=28604
	    "x86-linux-dregs.c:[0-9]*: internal-error: void x86_linux_update_debug_registers\(lwp_info\*\): Assertion \`lwp_is_stopped \(lwp\)' failed."
	)

	kfail_re=$(join "|" "${kfail[@]}")
	grep -a -H internal-error: binaries-testsuite.*/gdb-testresults/*.log \
	    | grep -a -v "maint.c:[0-9]" \
	    | grep -a -E -v "$kfail_re"
	;;

    4)
	sums=()

	# Note: below we avoid gdb-x86_64-suse-linux-m32.sum (the pie variant).
	# That one hasn't been cleaned up.
	
	# Known clean config: Leap 15.2 x86_64.
	config=openSUSE_Leap_15.2.x86_64/gdb-testresults
	sums+=("$config/gdb-x86_64-suse-linux-m64.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m64.sum"
	       "$config/gdb-x86_64-suse-linux-m32.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m32.sum")

	# Known clean config: Leap 15.3 x86_64
	config=openSUSE_Leap_15.3.x86_64/gdb-testresults
	sums+=("$config/gdb-x86_64-suse-linux-m64.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m64.sum"
	       "$config/gdb-x86_64-suse-linux-m32.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m32.sum")

	# Known clean config: SLE 15 x86_64.
	config=SLE-15.x86_64/gdb-testresults
	sums+=("$config/gdb-x86_64-suse-linux-m64.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m64.sum"
	       "$config/gdb-x86_64-suse-linux-m32.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m32.sum")

	# Known cleanish config: Factory x86_64.
	config=openSUSE_Factory.x86_64/gdb-testresults
	sums+=("$config/gdb-x86_64-suse-linux-m64.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m64.sum"
	       "$config/gdb-x86_64-suse-linux-m32.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m32.sum")	

	kfail+=("${kfail_factory[@]}")

	for sum in "${sums[@]}"; do
	    sum=binaries-testsuite.$sum
	    report_sum "$sum"
	done
	;;

    5)
	librpm=$(ls -1 binaries-testsuite*/gdb-testresults/*.sum \
		     | grep -v SLE-11)
	nolibrpm=$(ls -1 binaries-testsuite*/gdb-testresults/*.sum \
		     | grep SLE-11)
	grep -c "PASS: gdb.suse/zypper-hint.exp: zypper hint printed (librpm)" \
	     $librpm \
	    | grep -E -v ":1"
	grep -c "PASS: gdb.suse/zypper-hint.exp: zypper hint printed (no librpm)" \
	     $nolibrpm \
	    | grep -E -v ":1"
	;;

    6)
	sums=()

	mapfile -t < <(echo_line "$dir"/*-m64.-fno-PIE.-no-pie.sum)
	sums+=("${MAPFILE[@]}")
	mapfile -t < <(echo_line "$dir"/*-m64.sum)
	sums+=("${MAPFILE[@]}")
	mapfile -t < <(echo_line "$dir"/*-m32.-fno-PIE.-no-pie.sum)
	sums+=("${MAPFILE[@]}")
	mapfile -t < <(echo_line "$dir"/*-m32.sum)
	sums+=("${MAPFILE[@]}")

	# Assume this is factory.
	kfail+=("${kfail_factory[@]}")
	
	for sum in "${sums[@]}"; do
	    report_sum "$sum"
	done
	;;

    *)
	echo "Don't know how to handle arg: $n"
	exit 1
	;;
esac
