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
    echo "       $0 -local [ -sle11 | -sle12 | -factory | -aarch64 | -powerpc64le | -s390 | -s390x ] <dir>"
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

have_sle11=false
have_sle12=false
have_factory=false
have_aarch64=false
have_powerpc64le=false
have_s390=false
have_s390x=false
if [ "$n" = "-local" ]; then
    while [ $# -gt 1 ]; do
	case $1 in
	    -sle11)
		have_sle11=true
		;;
	    -sle12)
		have_sle12=true
		;;
	    -factory)
		have_factory=true
		;;
	    -aarch64)
		have_aarch64=true
		;;
	    -powerpc64le|-ppc64le)
		have_powerpc64le=true
		;;
	    -s390)
		have_s390=true
		;;
	    -s390x)
		have_s390x=true
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
    "FAIL: gdb.threads/watchthreads-threaded.exp: watchpoint on args\[[1-3]\] hit in thread"
    "FAIL: gdb.threads/watchthreads-threaded.exp: watch args\[[1-3]\]"
    "FAIL: gdb.threads/watchthreads-threaded.exp: threaded watch loop"
    "FAIL: gdb.threads/watchthreads-threaded.exp: combination of threaded watchpoints = 30 \+ initial values"
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

    #https://sourceware.org/bugzilla/show_bug.cgi?id=29790
    "FAIL: gdb.arch/i386-pkru.exp: read value after setting value"
    "FAIL: gdb.arch/i386-pkru.exp: variable after reading pkru"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=28478
    "FAIL: gdb.gdb/selftest.exp: backtrace through signal handler"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29781
    "FAIL: gdb.mi/mi-multi-commands.exp: args=: look for second command output, command length .* \(timeout\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=27813
    "FAIL: .*.exp: .*tab complete .* \(clearing input line\) \(timeout\)"
    "FAIL: .*.exp: .*cmd complete .*"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=27027
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28464
    "FAIL: gdb.ada/mi_var_access.exp: Create varobj \(unexpected output\)"
    "FAIL: gdb.ada/mi_var_access.exp: update at stop 2 \(unexpected output\)"

    # Fragile test-case, requires glibc to fail in a certain way, ignore.
    "FAIL: gdb.base/gdb-rhbz1156192-recursive-dlopen.exp:"

    # GDB fails to print "Thread $x stopped" message for all threads, but
    # subsequent info threads shows all threads stopped, and a previous
    # info threads show all threads running.  Not harmful.
    "FAIL: gdb.threads/interrupt-while-step-over.exp: displaced-stepping=off: iter=[0-9]*: wait for stops \(timeout\)"
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

    # https://sourceware.org/bugzilla/show_bug.cgi?id=26967
    "FAIL: gdb.base/longjmp.exp: next over call_longjmp \(2\)"
    "FAIL: gdb.base/longjmp.exp: next over longjmp\(1\)"
    "FAIL: gdb.base/longjmp.exp: next over patt3"
    "FAIL: gdb.base/premature-dummy-frame-removal.exp: p some_func \(\)"
    "FAIL: gdb.base/premature-dummy-frame-removal.exp: set debug frame on"

    # Commit 2d77a94ff17 ("[gdb/testsuite] Require debug info for
    # gdb.tui/tui-layout-asm-short-prog.exp")
    "FAIL: gdb.tui/tui-layout-asm-short-prog.exp: check asm box contents"
    "FAIL: gdb.tui/tui-layout-asm-short-prog.exp: check asm box contents again"

    # Test-cases that use -static but may turn out to be PIE when using
    # unix/-fPIE/-fpie.
    "FAIL: gdb.base/break-entry.exp: running to .* in runto"
    "FAIL: gdb.base/catch-fork-static.exp: run to fork"
    "FAIL: gdb.threads/staticthreads.exp: continue to main's call of sem_post"
    "FAIL: gdb.threads/staticthreads.exp: handle SIG32 helps"
    "FAIL: gdb.threads/staticthreads.exp: running to main in runto"
    "FAIL: gdb.threads/staticthreads.exp: running to main in runto"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step back into _start"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step back into foo"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step into bar"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step into foo"

    # Fails on both i586 and s390x/-m31 for SLE-12-SP3, but does not reproduce
    # on s390x/-m31 for SLE-12-SP5 with trunk.
    "FAIL: gdb.guile/scm-disasm.exp: disassemble via memory port"
    "FAIL: gdb.guile/scm-disasm.exp: memory-port: disassemble"
) # kfail_sle12

kfail_sle11=(
    "${kfail_sle12[@]}"

    # For SLE-11, libipt is not enabled, so on intel we can run into
    # https://sourceware.org/bugzilla/show_bug.cgi?id=30073 affecting
    # many test-cases.
    "FAIL: gdb.btrace/"
    "FAIL: gdb.python/py-record-btrace"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=26956
    "FAIL: gdb.base/command-line-input.exp: print 1"

    # Due to using old python, 2.6.
    # For instance, "ValueError: zero length field name in format".
    "FAIL: gdb.python/py-autoloaded-pretty-printers-in-newobjfile-event.exp: print test"
    "FAIL: gdb.python/py-breakpoint.exp: test_bkpt_address: python gdb.Breakpoint\("  *{}".format\(str\(main_addr\)\)\)"
    "FAIL: gdb.python/py-framefilter.exp: info frame filter after disable frame filter"
    "FAIL: gdb.python/py-framefilter.exp: info frame filter after reenabling frame filter"
    "FAIL: gdb.python/py-framefilter.exp: info frame filter after setting priority"
    "FAIL: gdb.python/py-framefilter.exp: info frame filter before disable frame filter"
    "FAIL: gdb.python/py-framefilter.exp: info frame filter before setting priority"
    "FAIL: gdb.python/py-mi.exp: check tsrvw expression value \(unexpected output\)"
    "FAIL: gdb.python/py-mi.exp: check tsrvw varobj value \(unexpected output\)"
    "FAIL: gdb.python/py-mi.exp: create tsrvw varobj \(unexpected output\)"
    "FAIL: gdb.python/py-prettyprint.exp: c\+\+: print tsrvw"
    "FAIL: gdb.python/py-prettyprint.exp: c: print tsrvw"
    "FAIL: gdb.python/py-value.exp: attempt to construct large value with small buffer"
    "FAIL: gdb.python/py-value.exp: construct array value from buffer"
    "FAIL: gdb.python/py-value.exp: construct value from buffer"
    "FAIL: gdb.python/py-value.exp: print array value"
    "FAIL: gdb.python/py-value.exp: print first array element"
    "FAIL: gdb.python/py-value.exp: print out of bounds array element"
    "FAIL: gdb.python/py-value.exp: print second array element"
    "FAIL: gdb.python/py-value.exp: print third array element"

    # To be investigated.
    "FAIL: gdb.base/compare-sections.exp: after run to main: compare-sections -r"
    "FAIL: gdb.python/py-framefilter-thread.exp: bt no-filters"

    # Gdb runs out of virtual memory, we can expect an internal error.
    "FAIL: gdb.base/gcore-excessive-memory.exp: attach \(GDB internal error\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30154
    "FAIL: gdb.multi/multi-target-no-resumed.exp: inf_A=.: inf_B=.: send_gdb control C \(timeout\)"
)

kfail_factory=(
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

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29965
    "FAIL: gdb.threads/process-exit-status-is-leader-exit-status.exp: iteration=.*: continue \(the program exited\)"
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

kfail_powerpc64le=(
    # https://sourceware.org/bugzilla/show_bug.cgi?id=29420
    "FAIL: gdb.ada/convvar_comp.exp: print \\\$item.started"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29814
    "FAIL: gdb.base/msym-bp-shl.exp: debug=0: before run: info breakpoint"
    "FAIL: gdb.base/msym-bp-shl.exp: debug=1: before run: info breakpoint"

    # Commit a0eda3df5b7 ("PowerPC, fix support for printing the function
    # return value for non-trivial values").
    "FAIL: gdb.cp/non-trivial-retval.exp: finish from"
    "FAIL: gdb.ada/array_return.exp: value printed by finish of Create_Small_Float_Vector"
    "FAIL: gdb.base/gnu_vector.exp: call add_structvecs"

    # Commit f68eca29d3b ("PowerPC, fix gdb.base/retval-large-struct.exp").
    "FAIL: gdb.base/retval-large-struct.exp: finish from return_large_struct"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29793
    "FAIL: gdb.cp/gdb2495.exp: call a function that raises an exception without a handler."
    "FAIL: gdb.cp/gdb2495.exp: bt after returning from a popped frame"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29792
    "FAIL: gdb.opt/solib-intra-step.exp: second-hit"
    
    # Carl Love mentioned he's working on these.
    # https://sourceware.org/bugzilla/show_bug.cgi?id=29793#c2
    "FAIL: gdb.reverse/finish-precsave.exp"
    "FAIL: gdb.reverse/finish-reverse.exp"
    
    # Commit 29004660c94 ("PowerPC fix for gdb.server/sysroot.exp").
    "FAIL: gdb.server/sysroot.exp: sysroot=local: continue to printf"
    "FAIL: gdb.server/sysroot.exp: sysroot=remote: continue to printf"    

    # Known to run into timeouts.
    "FAIL: gdb.gdb/python-helper.exp"

    # Fedora test.  Fails because it doesn't handle ppc64le.
    "FAIL: gdb.arch/powerpc-bcl-prologue.exp: powerpc arch test"

    # Commit 301fe55e9c4 ("PowerPC: bp-permanent.exp, kill-after-signal fix").
    "FAIL: gdb.base/kill-after-signal.exp: stepi"
    "FAIL: gdb.base/bp-permanent.exp: always_inserted=off, sw_watchpoint=0: stepi signal with handler: mainline pc points at permanent breakpoint"
    "FAIL: gdb.base/bp-permanent.exp: always_inserted=off, sw_watchpoint=1: stepi signal with handler: mainline pc points at permanent breakpoint"
    "FAIL: gdb.base/bp-permanent.exp: always_inserted=on, sw_watchpoint=0: stepi signal with handler: mainline pc points at permanent breakpoint"
    "FAIL: gdb.base/bp-permanent.exp: always_inserted=on, sw_watchpoint=1: stepi signal with handler: mainline pc points at permanent breakpoint"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29813
    "FAIL: gdb.base/vla-optimized-out.exp: o1: printed size of optimized out vla"

    # Commit 4d88ae0c7b5 ("[gdb/testsuite] Fix gdb.base/maint.exp on powerpc64le").
    "FAIL: gdb.base/maint.exp: maint print objfiles: symtabs"

    # Commit e7d69e72bfd ("gdb: always add the default register groups").
    "FAIL: gdb.xml/tdesc-regs.exp: maintenance print reggroups"

    # Commit 91836f41e20 ("Powerpc fix for gdb.base/unwind-on-each-insn.exp").
    "FAIL: gdb.base/inline-frame-cycle-unwind.exp: cycle at level [0-9]*: backtrace when the unwind is broken at frame [0-9]*"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29815
    "FAIL: gdb.reverse/finish-reverse-bkpt.exp: reverse-finish from void_func trips breakpoint at entry"
    "FAIL: gdb.reverse/finish-reverse-bkpt.exp: no spurious proceed after breakpoint stop"
    "FAIL: gdb.reverse/next-reverse-bkpt-over-sr.exp: reverse-next over call trips user breakpoint at function entry"
    "FAIL: gdb.reverse/next-reverse-bkpt-over-sr.exp: stopped at the right callee call"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29816
    "FAIL: gdb.ada/float-bits.exp: print 16llf#4000921fb54442d18469898cc51701b8#"
    "FAIL: gdb.ada/float-bits.exp: print \\\$foo:=16llf#4000921fb54442d18469898cc51701b8#"
    "FAIL: gdb.ada/float-bits.exp: print internal long double variable after assignment"

    # Commit 8b272d7671f ("[gdb/testsuite] Fix gdb.guile/scm-symtab.exp for
    # ppc64le").
    "FAIL: gdb.guile/scm-symtab.exp: test find-pc-line with resume address"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29897
    "FAIL: gdb.base/run-control-while-bg-execution.exp: action1=.*: action2=start: start \(GDB internal error\)"
    "FAIL: gdb.base/run-control-while-bg-execution.exp: action1=.*: action2=run: run \(GDB internal error\)"
)

kfail_powerpc64le_sle12=(
    # Commit 85819864f7c ("[gdb/testsuite] Fix gdb.arch/altivec-regs.exp with
    # gcc 4.8.5").
    "FAIL: gdb.arch/altivec-regs.exp: down to vector_fun"
    "FAIL: gdb.arch/altivec-regs.exp: finish returned correct value"
    "FAIL: gdb.arch/altivec-regs.exp: print vector parameter a"
    "FAIL: gdb.arch/altivec-regs.exp: print vector parameter b"
)

kfail_s390x_s390=(
    # Commit 167f3beb655 ("[gdb/testsuite] Fix gdb.base/write_mem.exp for big
    # endian")
    "FAIL: gdb.base/write_mem.exp: x /xh main"
)

# Plain s390 or s390x/-m31.
kfail_s390=(
    "${kfail_s390x_s390[@]}"
    
    # https://sourceware.org/bugzilla/show_bug.cgi?id=29841
    "FAIL: gdb.reverse/.*.exp:"

    # Doesn't reproduce with trunk on SLE-12SP5.
    "FAIL: gdb.guile/scm-ports.exp: buffered: test byte at sp, before flush"
    
    # https://sourceware.org/bugzilla/show_bug.cgi?id=29867
    "FAIL: gdb.guile/scm-lazy-string.exp: ptr: lazy string length 2 value"
    "FAIL: gdb.guile/scm-lazy-string.exp: ptr: lazy string value"
    "FAIL: gdb.guile/scm-lazy-string.exp: ptr: print ptr"
    "FAIL: gdb.base/sym-file.exp: add-symbol-file sym-file-lib.so addr"
    "FAIL: gdb.base/sym-file.exp: continue to breakpoint: gdb_add_symbol_file"
    "FAIL: gdb.python/py-lazy-string.exp: ptr: lazy string length 2 value"
    "FAIL: gdb.python/py-lazy-string.exp: ptr: lazy string value"
    "FAIL: gdb.python/py-lazy-string.exp: ptr: print ptr"
    "FAIL: gdb.python/py-nested-maps.exp: headers=on: pretty=off: exp='\*mm': depth=1: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: headers=on: pretty=off: exp='\*mm': depth=2: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: headers=on: pretty=off: exp='\*mm': depth=3: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: headers=on: pretty=off: exp='\*mm': depth=unlimited: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: pretty=off: exp='\*mm': depth=1: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: pretty=off: exp='\*mm': depth=2: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: pretty=off: exp='\*mm': depth=3: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: pretty=off: exp='\*mm': depth=unlimited: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: pretty=on: exp='\*mm': depth=1: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: pretty=on: exp='\*mm': depth=2: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: pretty=on: exp='\*mm': depth=3: p \*mm"
    "FAIL: gdb.python/py-nested-maps.exp: pretty=on: exp='\*mm': depth=unlimited: p \*mm"
    "FAIL: gdb.base/info-shared.exp:"
    "FAIL: gdb.python/py-strfns.exp: p /d {char\[4\]} arg"
    "FAIL: gdb.python/py-strfns.exp: p arg"
)

# s390x/-m64.
kfail_s390x=(
    "${kfail_s390x_s390[@]}"
)

case $n in
    1)
	# 'FAIL: .* internal error' in gdb.sum.
	# Test fail due to internal error.
	#
	# Todo: apply kfail_factory/kfail_sle12 only when appropriate.
	kfail+=("${kfail_factory[@]}")
	kfail+=("${kfail_sle12[@]}")
	kfail+=("${kfail_s390[@]}")
	kfail+=("${kfail_powerpc64le[@]}")
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
	    ".i586.*i386-linux-nat.c:[0-9]*: internal-error: Got request for bad register number [0-9]*."
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

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=29783
	    "frame.c:[0-9]*: internal-error: get_selected_frame: Assertion \`selected_frame != NULL' failed."

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=29841
	    "regcache.c:[0-9]*: internal-error: raw_read: Assertion \`buf != NULL' failed."

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=29897
	    "displaced-stepping.c:[0-9]*: internal-error: prepare: Assertion \`buf.current_thread != thread' failed."
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

	(
	    kfail+=("${kfail_powerpc64le[@]}")

	    # Known clean config: SLE 15 / openSUSE 15.4 powerpc64le.
	    for config in SLE-15.ppc64le/gdb-testresults openSUSE_Leap_15.4.ppc64le/gdb-testresults; do
		sums=("$config/gdb-ppc64le-suse-linux-m64.-fno-PIE.-no-pie.sum"
		      "$config/gdb-ppc64le-suse-linux-m64.sum")
	    done
	    
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
	if [ "$librpm" != "" ]; then
	    grep -c "PASS: gdb.suse/zypper-hint.exp: zypper hint printed (librpm)" \
		 $librpm \
		| grep -E -v ":1"
	fi
	if [ "$nolibrpm" != "" ]; then
	    grep -c "PASS: gdb.suse/zypper-hint.exp: zypper hint printed (no librpm)" \
		 $nolibrpm \
		| grep -E -v ":1"
	fi
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
	if $have_sle11; then
	    kfail+=("${kfail_sle11[@]}")
	fi
	if $have_sle12; then
	    kfail+=("${kfail_sle12[@]}")
	fi
	if $have_aarch64; then
	    kfail+=("${kfail_aarch64[@]}")
	fi
	if $have_powerpc64le; then
	    kfail+=("${kfail_powerpc64le[@]}")
	fi
	if $have_powerpc64le && $have_sl12; then
	    kfail+=("${kfail_powerpc64le_sle12[@]}")
	fi
	if $have_s390; then
	    kfail+=("${kfail_s390[@]}")
	fi

	if $have_s390x; then
	    kfail+=("${kfail_s390x[@]}")
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
