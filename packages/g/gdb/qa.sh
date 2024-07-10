#!/bin/bash

usage ()
{
    echo "usage: $0 <1-5>"
    echo "       $0 -local [ -sle11 | -sle12 | -factory | -i586 | -x86_64 | -aarch64 | -powerpc64le | -s390 | -s390x ] <dir>"
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
have_arm=false
have_powerpc64le=false
have_s390=false
have_s390x=false
have_i586=false
have_x86_64=false
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
	    -arm)
		have_arm=true
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
	    -i586)
		have_i586=true
		;;
	    -x86_64)
		have_x86_64=true
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
    echo -n "ERROR COUNT: "
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

    # https://sourceware.org/bugzilla/show_bug.cgi?id=28617
    "FAIL: gdb.base/info-os.exp: get process list \(timeout\)"
    "FAIL: gdb.base/info-os.exp: get process list"
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

    # https://sourceware.org/bugzilla/show_bug.cgi?id=28478
    "FAIL: gdb.gdb/selftest.exp: backtrace through signal handler"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29781
    "FAIL: gdb.mi/mi-multi-commands.exp: args=.*: look for second command output, command length .* \(timeout\)"

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

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29040
    "FAIL: gdb.threads/next-fork-other-thread.exp:"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31810
    "FAIL: gdb.threads/next-fork-exec-other-thread.exp:"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30521
    "FAIL: gdb.base/printcmds.exp: print {unsigned char\[\]}{0xffffffff}"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30528
    # Fixed in 15.  Backportable to 14.
    "FAIL: gdb.dwarf2/per-bfd-sharing.exp: couldn't remove files in temporary cache dir"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30480
    "FAIL: gdb.ada/info_auto_lang.exp: language_choice=auto: frame=0, frame_lang=c: info functions proc_in_"
    "FAIL: gdb.ada/info_auto_lang.exp: language_choice=auto: frame=1, frame_lang=ada: info functions proc_in_"
    "FAIL: gdb.ada/info_auto_lang.exp: language_choice=ada: frame=0, frame_lang=c: info functions proc_in_"
    "FAIL: gdb.ada/info_auto_lang.exp: language_choice=ada: frame=1, frame_lang=ada: info functions proc_in_"
    "FAIL: gdb.ada/info_auto_lang.exp: language_choice=c: frame=0, frame_lang=c: info functions proc_in_"
    "FAIL: gdb.ada/info_auto_lang.exp: language_choice=c: frame=1, frame_lang=ada: info functions proc_in_"
    "FAIL: gdb.ada/info_exc.exp: info exceptions task"
    "FAIL: gdb.ada/info_exc.exp: info exceptions const.aint"
    "FAIL: gdb.ada/mi_exc_info.exp: -info-ada-exceptions task \(unexpected output\)"
    "FAIL: gdb.ada/mi_exc_info.exp: -info-ada-exceptions const.aint \(unexpected output\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31440
    "FAIL: gdb.python/py-progspace-events.exp: inferior 1 \(timeout\)"
    "FAIL: gdb.python/py-progspace-events.exp: step"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31809
    "FAIL: gdb.threads/attach-slow-waitpid.exp: attach to target \(timeout\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31806
    "FAIL: gdb.debuginfod/fetch_src_and_symbols.exp: local_url: file corefile"
    "FAIL: gdb.debuginfod/crc_mismatch.exp: local_debuginfod: debuginfod running, info downloaded, no CRC mismatch"

    # Fixed by commit 17f6581c36a ("gdb/testsuite: another attempt to fix
    # gdb.threads/thread-specific-bp.exp").
    "FAIL: gdb.threads/thread-specific-bp.exp: non_stop=on: continue to end \(timeout\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31811
    "FAIL: gdb.threads/threads-after-exec.exp:"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29253
    "FAIL: gdb.server/stop-reply-no-thread.exp: to_disable=threads: continue to main \(timeout\)"
    "FAIL: gdb.server/stop-reply-no-thread.exp: to_disable=threads: continue until exit \(timeout\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31831
    "FAIL: gdb.dap/log-message.exp: logging output \(checking body category\)"

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
    "FAIL: gdb.arch/amd64-init-x87-values.exp: check_x87_regs_around_init: runto: run to main"
    "FAIL: gdb.arch/amd64-init-x87-values.exp: check_setting_mxcsr_before_enable: runto: run to main"
    "FAIL: gdb.arch/amd64-init-x87-values.exp: check_setting_x87_regs_before_enable: runto: run to main"
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
    "FAIL: gdb.base/longjmp-until-in-main.exp: until \\\$line, in main"
    
    # Test-cases that use -static but may turn out to be PIE when using
    # unix/-fPIE/-fpie.
    # https://sourceware.org/bugzilla/show_bug.cgi?id=29244
    "FAIL: gdb.base/break-entry.exp: runto: run to *"
    "FAIL: gdb.base/catch-fork-static.exp: run to fork"
    "FAIL: gdb.threads/staticthreads.exp: runto: run to main"
    "FAIL: gdb.threads/staticthreads.exp: continue to main's call of sem_post"
    "FAIL: gdb.threads/staticthreads.exp: handle SIG32 helps"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step back into _start"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step back into foo"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step into bar"
    "FAIL: gdb.dwarf2/frame-inlined-in-outer-frame.exp: step into foo"

    # Fails on both i586 and s390x/-m31 for SLE-12-SP3, but does not reproduce
    # on s390x/-m31 for SLE-12-SP5 with trunk.
    "FAIL: gdb.guile/scm-disasm.exp: disassemble via memory port"
    "FAIL: gdb.guile/scm-disasm.exp: memory-port: disassemble"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30180
    "FAIL: gdb.fortran/module.exp: print var_d"
    "FAIL: gdb.fortran/module.exp: print var_x value 31"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30531
    "FAIL: gdb.threads/clone-thread_db.exp: continue to clone_fn \(the program exited\)"
    "FAIL: gdb.threads/clone-thread_db.exp: continue to end \(the program is no longer running\)"

) # kfail_sle12

kfail_sle11=(

    # FAILs for SLE-11 are not very interesting.  This is with on old compiler:
    # 4.3.4, and tests are likely to be broken.  We're really only interested in
    # segmentation faults and internal errors.
    "FAIL: "

)

kfail_factory=(

    # yama ptrace_scope == 1
    # https://sourceware.org/pipermail/gdb-patches/2024-April/208251.html
    "FAIL: .*attach.*"
    "FAIL: .*detach.*"
    "FAIL: gdb.base/gcore-excessive-memory.exp: verify we can get to main"
    "FAIL: gdb.base/gcore-excessive-memory.exp: verify we can get to main"
    "FAIL: gdb.base/gcore-excessive-memory.exp: Save the core file"
    "FAIL: gdb.base/gcorebg.exp: Core file generated by standard gcore"
    "FAIL: gdb.threads/check-libthread-db.exp: automated load-time check: libpthread.so fully initialized: check debug libthread-db output \(pattern 1\)"
    
    # https://sourceware.org/pipermail/gdb-patches/2021-October/182449.html
    "FAIL: gdb.threads/current-lwp-dead.exp: continue to breakpoint: fn_return"

    # Similar error message to the one above, see if fixing that one fixes this.
    "FAIL: gdb.threads/clone-new-thread-event.exp: catch SIGUSR1"

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

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29196
    "FAIL: gdb.base/gdb11531.exp: watchpoint variable triggers at next"
    "FAIL: gdb.base/gdb11531.exp: watchpoint variable triggers at continue"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29706
    "FAIL: gdb.base/eof-exit.exp: with non-dump terminal: with bracketed-paste-mode on: close GDB with eof \(missed the prompt\)"

    # Looks like a problem with modern debug info, where stepping out of a
    # function takes more one step.
    "FAIL: gdb.base/rtld-step.exp: finish out of foo 1"
    "FAIL: gdb.base/rtld-step.exp: next over baz in bar"
    "FAIL: gdb.base/rtld-step.exp: step into foo 2"
    "FAIL: gdb.base/rtld-step.exp: next over baz in foo"
    "FAIL: gdb.base/rtld-step.exp: step out of foo back into bar"
    "FAIL: gdb.base/rtld-step.exp: continue until exit"
    "FAIL: gdb.base/rtld-step.exp: next over foo 0"
    "FAIL: gdb.base/rtld-step.exp: step into bar"
    "FAIL: gdb.base/rtld-step.exp: step into foo 1"

    # Sets breakpoints in gdb build with lto.  This is known to be slow, and
    # likely to cause timeouts.
    gdb.gdb/python-helper.exp

    # Should be fixed by commit fe6356def67 ("PowerPC and aarch64: Fix reverse
    # stepping failure"), available in gdb 15.
    "FAIL: gdb.reverse/solib-precsave.exp: reverse-step into solib function one"
    "FAIL: gdb.reverse/solib-precsave.exp: reverse-step within solib function one"
    "FAIL: gdb.reverse/solib-precsave.exp: reverse-step back to main one"
    "FAIL: gdb.reverse/solib-precsave.exp: reverse-step into solib function two"
    "FAIL: gdb.reverse/solib-precsave.exp: reverse-step within solib function two"
    "FAIL: gdb.reverse/solib-precsave.exp: reverse-step back to main two"
    "FAIL: gdb.reverse/solib-precsave.exp: run until end part two"
    "FAIL: gdb.reverse/solib-precsave.exp: reverse-next over solib function one"
    "FAIL: gdb.reverse/solib-precsave.exp: reverse-next over solib function two"
    "FAIL: gdb.reverse/solib-reverse.exp: reverse-step into solib function one"
    "FAIL: gdb.reverse/solib-reverse.exp: reverse-step within solib function one"
    "FAIL: gdb.reverse/solib-reverse.exp: reverse-step back to main one"
    "FAIL: gdb.reverse/solib-reverse.exp: reverse-step into solib function two"
    "FAIL: gdb.reverse/solib-reverse.exp: reverse-step within solib function two"
    "FAIL: gdb.reverse/solib-reverse.exp: reverse-step back to main two"
    "FAIL: gdb.reverse/solib-reverse.exp: run until end part two"
    "FAIL: gdb.reverse/solib-reverse.exp: reverse-next over solib function one"
    "FAIL: gdb.reverse/solib-reverse.exp: reverse-next over solib function two"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31564
    "FAIL: gdb.base/rtld-step.exp: runto: run to main"

) # kfail_factory

kfail_aarch64=(

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29405
    "FAIL: gdb.base/step-over-syscall.exp: (fork|vfork): displaced=(on|off): pc after stepi matches insn addr after syscall"
    "FAIL: gdb.base/step-over-syscall.exp: (fork|vfork): displaced=(on|off): check_pc_after_cross_syscall: single step over fork final pc"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29423
    "FAIL: gdb.base/watchpoint-unaligned.exp: continue \(timeout\)"
    "FAIL: gdb.base/watchpoint-unaligned.exp: size8twice write"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31214
    "FAIL: gdb.base/watch-bitfields.exp: -location watch against bitfields: q\.e: 0->5: continue"
    "FAIL: gdb.base/watch-bitfields.exp: -location watch against bitfields: q\.a: 1->0: print expression before"
    "FAIL: gdb.base/watch-bitfields.exp: -location watch against bitfields: q\.a: 1->0: continue \(the program exited\)"
    "FAIL: gdb.base/watch-bitfields.exp: -location watch against bitfields: q\.e: 5->4: print expression before"
    "FAIL: gdb.base/watch-bitfields.exp: -location watch against bitfields: q\.e: 5->4: continue \(the program is no longer running\)"
    "FAIL: gdb.base/watch-bitfields.exp: -location watch against bitfields: q\.e: 5->4: print expression after"
    "FAIL: gdb.base/watch-bitfields.exp: -location watch against bitfields: continue until exit \(the program is no longer running\)"
    
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28561
    # "[gdb/testsuite] Error due to not reading \r\n at end of mi prompt"
    # We match pretty aggressively here.
    "FAIL: gdb.mi/.*.exp:"
    "FAIL: gdb.python/.*-mi.exp:"
    "FAIL: gdb.python/py-mi-.*.exp:"
    "FAIL: gdb.ada/mi.*.exp:"
    "FAIL: gdb.base/annota.*.exp:"
    "FAIL: gdb.dwarf2/dw2-opt-structptr.exp: mi"
    "FAIL: gdb.trace/mi-.*.exp:"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31826
    "FAIL: gdb.arch/aarch64-unwind-pc.exp:"

) # kfail_aarch64

kfail_powerpc64le=(

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29792
    "FAIL: gdb.opt/solib-intra-step.exp: second-hit"
    
    # Known to run into timeouts.
    "FAIL: gdb.gdb/python-helper.exp"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30548
    "FAIL: gdb.base/inline-frame-cycle-unwind.exp: cycle at level [0-9]*: backtrace when the unwind is broken at frame [0-9]*"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29815
    "FAIL: gdb.reverse/finish-reverse-bkpt.exp: reverse-finish from void_func trips breakpoint at entry"
    "FAIL: gdb.reverse/finish-reverse-bkpt.exp: no spurious proceed after breakpoint stop"
    "FAIL: gdb.reverse/next-reverse-bkpt-over-sr.exp: reverse-next over call trips user breakpoint at function entry"
    "FAIL: gdb.reverse/next-reverse-bkpt-over-sr.exp: stopped at the right callee call"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=29897
    "FAIL: gdb.base/run-control-while-bg-execution.exp: action1=.*: action2=start: start \(GDB internal error\)"
    "FAIL: gdb.base/run-control-while-bg-execution.exp: action1=.*: action2=run: run \(GDB internal error\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30021
    "FAIL: gdb.base/unwind-on-each-insn.exp: instruction 6: \\\$fba_value == \\\$main_fba"
    "FAIL: gdb.base/unwind-on-each-insn.exp: instruction 6: \[string equal \\\$fid \\\$main_fid\]"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30542
    "FAIL: gdb.base/watch-before-fork.exp: test: continue to catch fork"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30543
    "FAIL: gdb.python/py-send-packet.exp: call python run_auxv_send_packet_test function"

    # Cluster of fails related to hw watchpoint support.
    "FAIL: gdb.ada/scoped_watch.exp:"
    "FAIL: gdb.ada/task_watch.exp:"
    "FAIL: gdb.ada/watch_minus_l.exp:"
    "FAIL: gdb.base/watch-before-fork.exp:"
    "FAIL: gdb.base/watch-bitfields.exp:"
    "FAIL: gdb.base/watch-cond.exp:"
    "FAIL: gdb.base/watch-cond-infcall.exp:"
    "FAIL: gdb.base/watchpoint-during-step.exp:"
    "FAIL: gdb.base/watchpoint.exp:"
    "FAIL: gdb.base/watchpoint-hw-attach.exp:"
    "FAIL: gdb.base/watchpoint-hw-hit-once.exp:"
    "FAIL: gdb.base/watchpoints.exp:"
    "FAIL: gdb.base/watchpoint-solib.exp:"
    "FAIL: gdb.base/watchpoint-stops-at-right-insn.exp:"
    "FAIL: gdb.base/watchpoint-unaligned.exp:"
    "FAIL: gdb.base/watch-read.exp:"
    "FAIL: gdb.base/watch_thread_num.exp:"
    "FAIL: gdb.base/watch-vfork.exp:"
    "FAIL: gdb.cp/watch-cp.exp:"
    "FAIL: gdb.mi/mi-watch.exp:"
    "FAIL: gdb.threads/step-over-trips-on-watchpoint.exp:"
    "FAIL: gdb.threads/watchpoint-fork.exp:"
    "FAIL: gdb.threads/watchthreads2.exp:"
    "FAIL: gdb.threads/wp-replication.exp:"
    "FAIL: gdb.base/display.exp:"
    "FAIL: gdb.base/recurse.exp:"
    "FAIL: gdb.base/gdb11531.exp:"
    "FAIL: gdb.base/pr11022.exp:"
    "FAIL: gdb.base/value-double-free.exp: continue \(the program exited\)"
    "FAIL: gdb.base/value-double-free.exp: print empty\(\)"
    "FAIL: gdb.cp/annota2.exp: watch triggered on a.x \(timeout\)"
    "FAIL: gdb.cp/annota2.exp: annotate-quit"
    "FAIL: gdb.cp/annota3.exp: watch triggered on a.x \(timeout\)"
    "FAIL: gdb.cp/annota3.exp: annotate-quit \(pattern 1\)"
    "FAIL: gdb.mi/pr11022.exp:"
    "FAIL: gdb.python/py-breakpoint.exp: test_watchpoints: Test watchpoint write \(the program exited\)"
    "FAIL: gdb.python/py-breakpoint.exp: test_bkpt_internal: Test watchpoint write \(the program exited\)"
    "FAIL: gdb.python/py-breakpoint.exp: test_bkpt_eval_funcs: Test watchpoint write \(the program exited\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31004
    "FAIL: gdb.base/run-control-while-bg-execution.exp: action1=.*: action2=run: run"
    "FAIL: gdb.base/run-control-while-bg-execution.exp: action1=.*: action2=start: start"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31823
    "FAIL: gdb.base/nodebug.exp: p/c \(int\) array_index\(\"abcdef\",2\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31825
    "FAIL: gdb.base/break-interp.exp: ldprelink=NO: ldsepdebug=NO: binprelink=NO: binsepdebug=NO: binpie=YES: INNER: reach-\(_dl_debug_state|dl_main\)-2: reach"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31827
    "FAIL: gdb.base/gnu_vector.exp: call add_structvecs"

)

kfail_powerpc64le_sle12=(

    "FAIL: gdb.guile/scm-breakpoint.exp:.*"
    # Cluster of fails related to hw watchpoint support.
    "FAIL: gdb.guile/scm-breakpoint.exp: test_bkpt_eval_funcs: test watchpoint write \(the program exited\)"
    "FAIL: gdb.guile/scm-breakpoint.exp: test_bkpt_internal: test invisible watchpoint write \(the program exited\)"
    "FAIL: gdb.guile/scm-breakpoint.exp: test_watchpoints: test watchpoint write \(the program exited\)"

)

kfail_s390x_s390=(

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

kfail_i586=(

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30518
    "FAIL: gdb.python/py-disasm.exp: memory source api: disassemble test"
    "FAIL: gdb.python/py-disasm.exp: memory source api: python analyzing_disassembler.find_replacement_candidate\(\)"
    "FAIL: gdb.python/py-disasm.exp: memory source api: second disassembler pass"
    "FAIL: gdb.python/py-disasm.exp: memory source api: python analyzing_disassembler.check\(\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30519
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test default value"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test default value via gdb.parameter"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: {test set to -1}"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test value of -1"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test value of -1 via gdb.parameter"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test set to 1"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test value of 1"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test value of 1 via gdb.parameter"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: {test set to -5}"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test value of -5 via gdb.parameter"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test set to 5"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test value of 5 via gdb.parameter"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: {test set to None}"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test value of None"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test value of None via gdb.parameter"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test set to 0"
    "FAIL: gdb.python/py-parameter.exp: test_integer_parameter: kind=PARAM_UINTEGER: test value of 0 via gdb.parameter"

)

kfail_arm=(

    # https://sourceware.org/bugzilla/show_bug.cgi?id=30537
    "FAIL: gdb.fortran/intrinsics.exp: p cmplx \(4,4,16\) \(GDB internal error\)"
    "FAIL: gdb.fortran/intrinsics.exp: ptype cmplx \(4,4,16\) \(GDB internal error\)"

    # https://sourceware.org/bugzilla/show_bug.cgi?id=31061
    "FAIL: gdb.base/gdb-sigterm.exp: .*internal error"

)

case $n in
    1)
	# 'FAIL: .* internal error' in gdb.sum.
	# Test fail due to internal error.
	#
	# Todo: apply kfail_factory/kfail_sle12 only when appropriate.
	kfail+=("${kfail_factory[@]}")
	kfail+=("${kfail_sle12[@]}")
	kfail+=("${kfail_sle11[@]}")
	kfail+=("${kfail_s390[@]}")
	kfail+=("${kfail_powerpc64le[@]}")
	kfail+=("${kfail_arm[@]}")
	kfail+=("${kfail_aarch64[@]}")
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

	    # Gdb runs out of virtual memory, we can expect an internal error.
	    "UNRESOLVED: gdb.base/gcore-excessive-memory.exp: attach"
	    "UNRESOLVED: gdb.base/gcore-excessive-memory.exp: verify we can get to main"

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=31001
	    "UNRESOLVED: gdb.threads/async.exp: thread 1: current thread is 1"

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=31648
	    "SLE-11.*UNRESOLVED: gdb.ada/tick_length_array_enum_idx.exp: print vars'length"

	    # yama ptrace_scope == 1
	    # https://sourceware.org/pipermail/gdb-patches/2024-April/208251.html
	    "Factory.*UNRESOLVED: gdb.base/gstack.exp: spawn gstack"
	    "Factory.*UNRESOLVED: gdb.multi/multi-term-settings.exp: inf1_how=run: inf2_how=attach: inf2: flush inferior output"
	    "Factory.*UNRESOLVED: gdb.multi/multi-term-settings.exp: inf1_how=attach: inf2_how=run: inf1: flush inferior output"
	    "Factory.*UNRESOLVED: gdb.multi/multi-term-settings.exp: inf1_how=attach: inf2_how=attach: inf2: flush inferior output"
	    "Factory.*UNRESOLVED: gdb.multi/multi-term-settings.exp: inf1_how=attach: inf2_how=run: continue"
	    "Factory.*UNRESOLVED: gdb.multi/multi-term-settings.exp: inf1_how=attach: inf2_how=run: continue"
	    "Factory.*UNRESOLVED: gdb.multi/multi-term-settings.exp: inf1_how=run: inf2_how=attach: continue"

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=31671
	    "SLE-11.*UNRESOLVED: gdb.objc/basicclass.exp: call an Objective-C method with no arguments"
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

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=19675
	    # PR is fixed in gdb-15.
	    "linux-nat.c:[0-9]*: internal-error: wait returned unexpected status"
	    "linux-nat.c:[0-9]*: internal-error: wait returned unexpected PID"

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=28553
	    "infrun.c:[0-9]*: internal-error: thread .* needs a step-over, but not in step-over queue"

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

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=30537
	    "f-lang.c:[0-9]*: internal-error: eval_op_f_cmplx: Assertion \`kind_arg->code \(\) == TYPE_CODE_COMPLEX' failed."

	    # Test-case gdb.base/gcore-excessive-memory.exp.
	    "utils.c:[0-9]*: internal-error: virtual memory exhausted: can't allocate [0-9]* bytes."

	    # https://sourceware.org/bugzilla/show_bug.cgi?id=31061
	    "intrusive_list.h:[0-9]*: internal-error: erase_element: Assertion \`elem_node->prev != INTRUSIVE_LIST_UNLINKED_VALUE' failed\."
	)

	kfail_re=$(join "|" "${kfail[@]}")
	grep -a -H internal-error: binaries-testsuite.*/gdb-testresults/*.log \
	    | grep -a -v "maint.c:[0-9]" \
	    | grep -a -E -v "$kfail_re"
	;;

    4)
	for id in SLE-12 \
		      SLE-15 \
		      ALP \
		      openSUSE_Leap_15.3 \
		      openSUSE_Leap_15.4 \
		      openSUSE_Leap_15.5 \
		      openSUSE_Factory; \
	    do
		for arch in x86_64 \
				i586 \
				aarch64 \
				ppc64le \
				s390x; \
		    do

			config=$id.$arch
			case $config in
			    SLE-15.i586|SLE-12.i586|ALP.i586)
				# No such config.
				continue
				;;
			    ALP.ppc64le|openSUSE_Factory.ppc64le|*.s390x)
				# Not cleaned up yet.
				continue
				;;
			esac

			id2=$id
			case $id in
			    openSUSE_Factory)
				case $arch in
				    s390x)
					id2=openSUSE_Factory_zSystems
					;;
				    ppc64le)
					id2=openSUSE_Factory_PPC
					;;
				    i586)
					id2=openSUSE_Factory_LegacyX86
					;;
				    armv7l|aarch64)
					id2=openSUSE_Factory_ARM
					;;
				esac
			esac
			config=$id2.$arch

			config="$config/gdb-testresults"

			sums=()
			case $arch in
			    x86_64)
				case $id in
				    SLE-12|ALP)
					sums=("$config/gdb-$arch-suse-linux-m64.-fPIE.-pie.sum"
					      "$config/gdb-$arch-suse-linux-m64.sum"
					      "$config/gdb-$arch-suse-linux-m32.-fPIE.-pie.sum"
					      "$config/gdb-$arch-suse-linux-m32.sum")
				    ;;
				    *)
					sums=("$config/gdb-$arch-suse-linux-m64.-fno-PIE.-no-pie.sum"
					      "$config/gdb-$arch-suse-linux-m64.sum"
					      "$config/gdb-$arch-suse-linux-m32.-fno-PIE.-no-pie.sum"
					      "$config/gdb-$arch-suse-linux-m32.sum")
					;;
				esac
				;;
			    i586)
				sums=("$config/gdb-$arch-suse-linux-m32.-fno-PIE.-no-pie.sum"
				      "$config/gdb-$arch-suse-linux-m32.sum")
				;;
			    aarch64)
				case $id in
				    SLE-12|ALP)
					sums=("$config/gdb-$arch-suse-linux.-fPIE.-pie.sum"
					      "$config/gdb-$arch-suse-linux.sum")
					;;
				    *)
					sums=("$config/gdb-$arch-suse-linux.-fno-PIE.-no-pie.sum"
					      "$config/gdb-$arch-suse-linux.sum")
					;;
				esac
				;;
			    ppc64le|s390x)
				case $id in
				    SLE-12|ALP)
					sums=("$config/gdb-$arch-suse-linux-m64.-fPIE.-pie.sum"
					      "$config/gdb-$arch-suse-linux-m64.sum")
					;;
				    *)
					sums=("$config/gdb-$arch-suse-linux-m64.-fno-PIE.-no-pie.sum"
					      "$config/gdb-$arch-suse-linux-m64.sum")
					;;
				esac
				;;
			    *)
				echo "Don't know how to handle: $arch"
				exit 1
				;;
			esac

			(
			    case $arch in
				i586)
				    kfail+=("${kfail_i586[@]}")
				    ;;
				aarch64)
				    kfail+=("${kfail_aarch64[@]}")
				    ;;
				ppc64le)
				    kfail+=("${kfail_powerpc64le[@]}")
				    ;;
				*)
				    ;;
			    esac

			    case $id in
				SLE-12)
				    kfail+=("${kfail_sle12[@]}")
				    ;;
				ALP|openSUSE_Factory)
				    kfail+=("${kfail_factory[@]}")
				    ;;
				*)
				    ;;
			    esac

			    case $id.$arch in
				SLE-12.ppc64le)
				    kfail+=("${kfail_powerpc64le_sle12[@]}")
				    ;;
			    esac
			    
			    for sum in "${sums[@]}"; do
				sum=binaries-testsuite.$sum
				report_sum "$sum"
			    done
			)
		done
	done

	(
	    # Known cleanish config: Factory x86_64.
	    config=openSUSE_Factory.x86_64/gdb-testresults
	    sums=("$config/gdb-x86_64-suse-linux-m64.-fno-PIE.-no-pie.sum"
		  "$config/gdb-x86_64-suse-linux-m64.sum"
		  "$config/gdb-x86_64-suse-linux-m32.-fno-PIE.-no-pie.sum"
		  "$config/gdb-x86_64-suse-linux-m32.sum")	

	    kfail+=("${kfail_factory[@]}")

	    for sum in "${sums[@]}"; do
		sum=binaries-testsuite.$sum
		report_sum "$sum"
	    done
	)

	(
	    # Known clean config: Factory i586.
	    config=openSUSE_Factory_LegacyX86.i586/gdb-testresults
	    sums=("$config/gdb-i586-suse-linux-m32.-fno-PIE.-no-pie.sum"
		   "$config/gdb-i586-suse-linux-m32.sum")

	    kfail+=("${kfail_factory[@]}")
	    kfail+=("${kfail_i586[@]}")

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
	if $have_arm; then
	    kfail+=("${kfail_arm[@]}")
	fi
	if $have_powerpc64le; then
	    kfail+=("${kfail_powerpc64le[@]}")
	fi
	if $have_powerpc64le && $have_sle12; then
	    kfail+=("${kfail_powerpc64le_sle12[@]}")
	fi
	if $have_s390; then
	    kfail+=("${kfail_s390[@]}")
	fi
	if $have_s390x; then
	    kfail+=("${kfail_s390x[@]}")
	fi
	if $have_i586; then
	    kfail+=("${kfail_i586[@]}")
	fi
	if $have_x86_64; then
	    kfail+=("${kfail_x86_64[@]}")
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

true
