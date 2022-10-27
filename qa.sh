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
    echo "       $0 -local [ -sle12 | -factory ] <dir>"
    echo
    echo "Verify remote results at:"
    echo "  ./binaries-testsuite.distro.arch/gdb-testresults"
    echo "1: gdb.sum: Check for 'FAIL: .* internal error' (all configs)"
    echo "2: gdb.sum: Check for 'ERROR:'                  (all configs)"
    echo "3: gdb.log: Check for 'internal-error:'         (all configs)"
    echo "4: gdb.sum: Check FAIL and ERROR                (known clean configs)"
    echo "5: gdb.sum: Check gdb.suse PASS                 (all configs)"
    echo
    echo "Verify local results at:"
    echo "  \$dir"
    echo "-local: gdb.sum: Check FAIL and ERROR"
}

if [ $# -eq 0 ]; then
    usage
    exit 1
fi

n="$1"
shift

have_sle12=false
have_factory=false
have_aarch64=false
if [ "$n" = "-local" ]; then
    while [ $# -gt 1 ]; do
	case $1 in
	    -sle12)
		have_sle12=true
		;;
	    -factory)
		have_factory=true
		;;
	    -aarch64)
		have_aarch64=true
		;;
	    *)
		echo "Don't know how to handle arg: $1"
		usage
		exit 1
		;;
	esac
	shift 1
    done
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
    "FAIL: gdb.base/step-over-syscall.exp: clone: displaced=off: continue to marker \(clone\)"
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
    "FAIL: gdb.threads/watchthreads-threaded.exp: watchpoint on args\[3\] hit in thread"
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

    # If a test-case fails to compile, it's not a GDB FAIL, ignore.
    "FAIL: gdb.ada/.*\.exp: compilation .*\.adb"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=27539
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(i\)"
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(i\) == &typeid\(typeof\(i\)\)"
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(cp\)"
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(cp\) == &typeid\(typeof\(cp\)\)"
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(ccp\)"
    "FAIL: gdb.cp/typeid.exp: before starting: print &typeid\(ccp\) == &typeid\(typeof\(ccp\)\)"

    # Fails for i586.  Appearantly, glibc for i586 doesn't use vdso to do
    # syscalls.  Fedora test-case.
    "FAIL: gdb.base/set-solib-absolute-prefix.exp: backtrace with __kernel_vsyscall"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=28504
    "FAIL: gdb.arch/i386-sse.exp: check contents of data\[2\]"
    "FAIL: gdb.arch/i386-sse.exp: check contents of data\[3\]"
    "FAIL: gdb.arch/i386-sse.exp: check contents of data\[4\]"
    "FAIL: gdb.arch/i386-sse.exp: check contents of data\[5\]"
    "FAIL: gdb.arch/i386-sse.exp: check contents of data\[6\]"
    "FAIL: gdb.arch/i386-sse.exp: check contents of data\[7\]"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse addps"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse addss"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse addsubpd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse andpd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse blendps"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse cmppd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse cmpps"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse cmpss"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse comisd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse comiss"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse cvtdq2pd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse cvtpd2dq"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse cvtpd2ps"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse divpd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse divsd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse divss"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse mulps"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse mulss"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse orpd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse orps"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse pabsw"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse packsswb"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse ucomisd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse ucomiss"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse unpckhpd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse unpckhps"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse xorpd"
    "FAIL: gdb.reverse/i386-sse-reverse.exp: verify xmm2 after reverse xorps"

    # Fedora test.  Fails because it doesn't handle ppc64le.
    "FAIL: gdb.arch/powerpc-bcl-prologue.exp: powerpc arch test"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29419
    # https://sourceware.org/bugzilla/show_bug.cgi?id=29409
    "FAIL: gdb.opt/inline-small-func.exp: info breakpoints"
    "FAIL: gdb.ada/access_tagged_param.exp: continue"
    "FAIL: gdb.ada/inline-section-gc.exp: break callee.adb:22"
    "FAIL: gdb.ada/ptype_tagged_param.exp: ptype s, with debug info"
    "FAIL: gdb.ada/ref_param.exp: frame argument value printed"
    "FAIL: gdb.reverse/singlejmp-reverse.exp: next to v = 1"
    "FAIL: gdb.reverse/singlejmp-reverse.exp: next to f"
    "FAIL: gdb.reverse/singlejmp-reverse.exp: next to nodebug"
    "FAIL: gdb.reverse/singlejmp-reverse.exp: next to v = 3"
    "FAIL: gdb.reverse/singlejmp-reverse.exp: reverse-step"
    "FAIL: gdb.reverse/singlejmp-reverse.exp: reverse-next"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=25038
    "FAIL: gdb.reverse/test_ioctl_TCSETSW.exp: handle TCSETSW"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=26873
    "FAIL: gdb.threads/watchthreads-threaded.exp: threaded watch loop \(GDB internal error\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=28617
    "FAIL: gdb.base/info-os.exp: get file descriptors"
    "FAIL: gdb.base/info-os.exp: get internet-domain sockets"
    "FAIL: gdb.base/info-os.exp: get message queues"
    "FAIL: gdb.base/info-os.exp: get process groups"
    "FAIL: gdb.base/info-os.exp: get semaphores"
    "FAIL: gdb.base/info-os.exp: get shared-memory regions"
    "FAIL: gdb.base/info-os.exp: get threads"

    
) # kfail

kfail_sle12=(
    # https://sourceware.org/bugzilla/show_bug.cgi?id=26292
    "FAIL: gdb.base/checkpoint-ns.exp: .* \(timeout\)"
    "FAIL: gdb.base/checkpoint.exp: .* \(timeout\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29238
    "FAIL: gdb.cp/ambiguous.exp: all vars: print jv"
    "FAIL: gdb.cp/ambiguous.exp: all vars: print jva1"
    "FAIL: gdb.cp/ambiguous.exp: all vars: print jva1v"
    "FAIL: gdb.cp/ambiguous.exp: all vars: print jva2"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=25059
    "FAIL: gdb.cp/subtypes.exp:"
    "FAIL: gdb.base/max-depth-c\+\+.exp:"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29240
    "FAIL: gdb.base/align-c.exp: print _Alignof\(double\)"
    "FAIL: gdb.base/align-c.exp: print _Alignof\(long long\)"
    "FAIL: gdb.base/align-c.exp: print _Alignof\(unsigned long long\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29241
    "FAIL: gdb.guile/scm-type.exp: lang_cpp: test_range: on flexible array member: guile \(print \(type-range \(field-type \(type-field \(value-type \(value-dereference f\)\) \"items\"\)\)\)\)"
    "FAIL: gdb.guile/scm-type.exp: lang_cpp: test_range: on flexible array member: guile \(print \(value-subscript \(value-field \(value-dereference f\) \"items\"\) 0\)\)"
    "FAIL: gdb.guile/scm-type.exp: lang_cpp: test_range: on flexible array member: guile \(print \(value-subscript \(value-field \(value-dereference f\) \"items\"\) 1\)\)"

    # Cluster of gcc 4.8 ada FAILs, to be investigated, but not high priority.
    "FAIL: gdb.ada/info_locals_renaming.exp: info locals"
    "FAIL: gdb.ada/interface.exp: info locals"
    "FAIL: gdb.ada/length_cond.exp: cond 1 loc'first > 15"
    "FAIL: gdb.ada/length_cond.exp: cond 1 loc'last > 15"
    "FAIL: gdb.ada/length_cond.exp: cond 1 loc'length > 15"
    "FAIL: gdb.ada/null_overload.exp: print f\(r_access'\(null\)\)"
    "FAIL: gdb.ada/str_uninit.exp: print my_str"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29244
    "FAIL: gdb.arch/amd64-disp-step-avx.exp: running to main in runto"
    "FAIL: gdb.arch/amd64-init-x87-values.exp: check_setting_mxcsr_before_enable: running to main in runto"
    "FAIL: gdb.arch/amd64-init-x87-values.exp: check_setting_x87_regs_before_enable: running to main in runto"
    "FAIL: gdb.arch/amd64-init-x87-values.exp: check_x87_regs_around_init: running to main in runto"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: frame"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: starti prompt"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step back into _start \(the program is no longer running\)"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step back into foo \(the program is no longer running\)"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step into bar \(the program is no longer running\)"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step into foo \(the program is no longer running\)"    

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29245
    # Python-2 related.
    "FAIL: gdb.python/py-mi-cmd.exp: -pycmd bk3 \(unexpected output\)"
) # kfail_sle12

kfail_factory=(
    # https://sourceware.org/bugzilla/show_bug.cgi?id=27027
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28464
    "FAIL: gdb.ada/mi_var_access.exp: Create varobj \(unexpected output\)"
    "FAIL: gdb.ada/mi_var_access.exp: update at stop 2 \(unexpected output\)"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28463
    "FAIL: gdb.ada/set_pckd_arr_elt.exp: scenario=minimal: print va.t\(1\) := 15"
    "FAIL: gdb.ada/set_pckd_arr_elt.exp: scenario=minimal: continue to update_small for va.t"
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28108
    "FAIL: gdb.base/langs.exp: up to foo in langs.exp"
    "FAIL: gdb.base/langs.exp: up to cppsub_ in langs.exp"
    "FAIL: gdb.base/langs.exp: up to fsub in langs.exp"
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

    # https://sourceware.org/bugzilla/show_bug.cgi?id=28667
    "FAIL: gdb.reverse/watch-precsave.exp: watchpoint hit, fourth time \\(GDB internal error\\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29160
    "FAIL: gdb.ctf/.*.exp"
    "FAIL: gdb.base/ctf-.*.exp"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29196
    "FAIL: gdb.base/gdb11531.exp: watchpoint variable triggers at next"
    "FAIL: gdb.base/gdb11531.exp: watchpoint variable triggers at continue"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29247
    "FAIL: gdb.base/varargs.exp: print find_max_long_double_real\(4, ldc1, ldc2, ldc3, ldc4\)"
    
    # We get "value has been optimized out", which is possible for an optimized gdb, due
    # to optimization of function c_print_type.
    "FAIL: gdb.gdb/python-helper.exp: print \*type->main_type"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29253
    "FAIL: gdb.server/stop-reply-no-thread.exp: to_disable=threads: continue to main \(timeout\)"
    "FAIL: gdb.server/stop-reply-no-thread.exp: to_disable=threads: continue until exit \(timeout\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29706
    "FAIL: gdb.base/eof-exit.exp: with non-dump terminal: with bracketed-paste-mode on: close GDB with eof \(missed the prompt\)"

) # kfail_factory

kfail_aarch64=(
    # https://sourceware.org/bugzilla/show_bug.cgi?id=29408
    "FAIL: gdb.base/large-frame.exp: optimize=-O0: backtrace"
    "FAIL: gdb.base/large-frame.exp: optimize=-O1: backtrace"
    "FAIL: gdb.base/large-frame.exp: optimize=-O2: backtrace"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29405
    "FAIL: gdb.base/step-over-syscall.exp: (fork|vfork): displaced=(on|off): pc after stepi matches insn addr after syscall"
    "FAIL: gdb.base/step-over-syscall.exp: (fork|vfork): displaced=(on|off): check_pc_after_cross_syscall: single step over fork final pc"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29418
    "FAIL: gdb.ada/O2_float_param.exp: scenario=all: frame"
    "FAIL: gdb.ada/O2_float_param.exp: scenario=minimal: frame"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29420
    "FAIL: gdb.ada/convvar_comp.exp: print \\\$item.started"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29423
    "FAIL: gdb.base/watchpoint-unaligned.exp: continue \(timeout\)"
    "FAIL: gdb.base/watchpoint-unaligned.exp: size8twice write"
) # kfail_aarch64

case $n in
    1)
	# 'FAIL: .* internal error' in gdb.sum.
	# Test fail due to internal error.
	#
	# Todo: apply kfail_factory/kfail_sle12 only when appropriate.
	kfail+=("${kfail_factory[@]}")
	kfail+=("${kfail_sle12[@]}")
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
	    "infrun.c:[0-9]*: internal-error: finish_step_over: Assertion \`ecs->event_thread->control.trap_expected' failed."
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=26363
	    ".i586.*i386-linux-nat.c:[0-9]*: internal-error: Got request for bad register number 41."
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=26761
	    "thread.c:[0-9]*: internal-error: inferior_thread: Assertion \`current_thread_ \!= nullptr' failed."
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=19675
	    "linux-nat.c:[0-9]*: internal-error: wait returned unexpected status"
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=28553
	    "infrun.c:[0-9]*: internal-error: thread .* needs a step-over, but not in step-over queue"
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=19675
	    "linux-nat.c:[0-9]*: internal-error: wait returned unexpected"
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=28604
	    "x86-linux-dregs.c:[0-9]*: internal-error: void x86_linux_update_debug_registers\(lwp_info\*\): Assertion \`lwp_is_stopped \(lwp\)' failed."

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=28667
	    "record-full.c:[0-9]*: internal-error: ptid_t record_full_wait_1\(target_ops\*, ptid_t, target_waitstatus\*, target_wait_flags\): Assertion \`\(options & TARGET_WNOHANG\) != 0' failed."
	    # https://sourceware.org/bugzilla/show_bug.cgi?id=26873
	    "infrun.c:[0-9]*: internal-error: resume_1: Assertion \`!\(thread_has_single_step_breakpoints_set \(tp\) && step\)' failed."
	)

	kfail_re=$(join "|" "${kfail[@]}")
	grep -a -H internal-error: binaries-testsuite.*/gdb-testresults/*.log \
	    | grep -a -v "maint.c:[0-9]" \
	    | grep -a -E -v "$kfail_re"
	;;

    4)
	sums=()

	# Known clean config: Leap 15.3 x86_64
	config=openSUSE_Leap_15.3.x86_64/gdb-testresults
	sums+=("$config/gdb-x86_64-suse-linux-m64.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m64.sum"
	       "$config/gdb-x86_64-suse-linux-m32.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m32.sum")

	# Known clean config: Leap 15.3 i586
	config=openSUSE_Leap_15.3.i586/gdb-testresults
	sums+=("$config/gdb-i586-suse-linux-m32.-fno-PIE.-no-pie.sum"
	       "$config/gdb-i586-suse-linux-m32.sum")

	# Known clean config: Leap 15.4 x86_64
	config=openSUSE_Leap_15.4.x86_64/gdb-testresults
	sums+=("$config/gdb-x86_64-suse-linux-m64.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m64.sum"
	       "$config/gdb-x86_64-suse-linux-m32.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m32.sum")

	# Known clean config: Leap 15.4 i586
	config=openSUSE_Leap_15.4.i586/gdb-testresults
	sums+=("$config/gdb-i586-suse-linux-m32.-fno-PIE.-no-pie.sum"
	       "$config/gdb-i586-suse-linux-m32.sum")

	# Known clean config: SLE 15 x86_64.
	config=SLE-15.x86_64/gdb-testresults
	sums+=("$config/gdb-x86_64-suse-linux-m64.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m64.sum"
	       "$config/gdb-x86_64-suse-linux-m32.-fno-PIE.-no-pie.sum"
	       "$config/gdb-x86_64-suse-linux-m32.sum")

	for sum in "${sums[@]}"; do
	    sum=binaries-testsuite.$sum
	    report_sum "$sum"
	done

	(
	    # Known clean config: SLE 12 x86_64.
	    config=SLE-12.x86_64/gdb-testresults
	    sums=("$config/gdb-x86_64-suse-linux-m64.-fPIE.-pie.sum"
		  "$config/gdb-x86_64-suse-linux-m64.sum"
		  "$config/gdb-x86_64-suse-linux-m32.-fPIE.-pie.sum"
		  "$config/gdb-x86_64-suse-linux-m32.sum")

	    kfail+=("${kfail_sle12[@]}")

	    for sum in "${sums[@]}"; do
		sum=binaries-testsuite.$sum
		report_sum "$sum"
	    done
	)
	
	(
	    # Known cleanish config: Factory x86_64.
	    config=openSUSE_Factory.x86_64/gdb-testresults
	    sums=("$config/gdb-x86_64-suse-linux-m64.-fno-PIE.-no-pie.sum"
		  "$config/gdb-x86_64-suse-linux-m64.sum"
		  "$config/gdb-x86_64-suse-linux-m32.-fno-PIE.-no-pie.sum"
		  "$config/gdb-x86_64-suse-linux-m32.sum")	

	    # Known clean config: Factory i586
	    config=openSUSE_Factory.i586/gdb-testresults
	    sums+=("$config/gdb-i586-suse-linux-m32.-fno-PIE.-no-pie.sum"
		   "$config/gdb-i586-suse-linux-m32.sum")

	    kfail+=("${kfail_factory[@]}")

	    for sum in "${sums[@]}"; do
		sum=binaries-testsuite.$sum
		report_sum "$sum"
	    done
	)

	(
	    # Known clean config: SLE 15 aarch64.
	    config=SLE-15.aarch64/gdb-testresults
	    sums=("$config/gdb-aarch64-suse-linux.-fno-PIE.-no-pie.sum"
		   "$config/gdb-aarch64-suse-linux.sum")

	    kfail+=("${kfail_aarch64[@]}")

	    for sum in "${sums[@]}"; do
		sum=binaries-testsuite.$sum
		report_sum "$sum"
	    done
	)

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

    -local)
	sums=()
	for f in "$dir"/*.sum; do
	    mapfile -t < <(echo_line "$f")
 	    sums+=("${MAPFILE[@]}")
	done

	if [ ${#sums[@]} -ne 4 ] && [ ${#sums[@]} -ne 2 ]; then
	    echo "No summary files to check"
	    exit 1
	fi

	
	if $have_factory; then
	    kfail+=("${kfail_factory[@]}")
	fi
	if $have_sle12; then
	    kfail+=("${kfail_sle12[@]}")
	fi
	if $have_aarch64; then
	    kfail+=("${kfail_aarch64[@]}")
	fi

	for sum in "${sums[@]}"; do
	    report_sum "$sum"
	done
	;;

    *)
	echo "Don't know how to handle arg: $n"
	exit 1
	;;
esac
