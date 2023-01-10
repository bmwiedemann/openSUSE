#
# spec file for package procps
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define somajor 8
%define libname libprocps%{somajor}
%if 0%{?suse_version} < 1550
%bcond_with     bin2usr
%else
%bcond_without  bin2usr
%endif
%bcond_without  pidof
%bcond_without  nls
Name:           procps
Version:        3.3.17
Release:        0
Summary:        The ps utilities for /proc
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Monitoring
URL:            https://sf.net/projects/procps-ng/
Source:         https://downloads.sourceforge.net/project/procps-ng/Production/procps-ng-%{version}.tar.xz
#Alternate:     https://gitlab.com/procps-ng/procps/-/archive/v%{version}/procps-v%{version}.tar.gz
Source1:        procps-rpmlintrc
Patch0:         procps-ng-3.3.9-watch.patch
Patch1:         procps-v3.3.3-ia64.diff
Patch3:         procps-ng-3.3.9-w-notruncate.diff
Patch7:         procps-ng-3.3.8-readeof.patch
Patch8:         procps-ng-3.3.10-slab.patch
Patch10:        procps-ng-3.3.8-accuracy.dif
Patch11:        procps-ng-3.3.10-xen.dif
Patch12:        procps-ng-3.3.10-fdleak.dif
Patch13:        procps-v3.3.3-columns.dif
Patch14:        procps-ng-3.3.10-integer-overflow.patch
Patch15:        procps-ng-3.3.10-bnc634071_procstat2.diff
Patch16:        procps-ng-3.3.8-bnc634840.patch
Patch17:        procps-v3.3.3-read-sysctls-also-from-boot-sysctl.conf-kernelversion.diff
Patch18:        procps-ng-3.3.8-petabytes.patch
Patch19:        procps-ng-3.3.10-large_pcpu.patch
Patch20:        procps-ng-3.3.8-tinfo.dif
Patch21:        procps-v3.3.3-pwdx.patch
# PATCH-FIX-OPENSUSE -- trifle rest of the old terabyte patch
Patch28:        procps-ng-3.3.8-vmstat-terabyte.dif
# PATCH-FIX-SUSE -- Ignore scan_unevictable_pages in sysctl
Patch31:        procps-ng-3.3.8-ignore-scan_unevictable_pages.patch
# PATCH-FIX-SUSE -- Avoid errno set by setlocale()
Patch32:        procps-ng-3.3.10-errno.patch
# PATCH-FEATURE-SUSE -- Let upstream pmap behave similar to old suse pmap
Patch33:        procps-ng-3.3.11-pmap4suse.patch
# PATCH-FIX-UPSTREAM -- bsc#1181976
Patch34:        procps-3.3.17-bsc1181976.patch
# PATCH-FIX-UPSTREAM -- bsc#1195468
Patch35:        bsc1195468-23da4f40.patch
# PATCH-BACKPORT-FROM-UPSTREAM -- bsc#1181475: 'free' command reports misleading "used" value
Patch42:        procps-3.3.17-library-bsc1181475.patch
Patch43:        procps-3.3.17-top-bsc1181475.patch
BuildRequires:  automake
BuildRequires:  dejagnu
BuildRequires:  diffutils
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  screen
BuildRequires:  xz
BuildRequires:  pkgconfig(libsystemd)
Provides:       ps = %{version}-%{release}
Obsoletes:      ps < %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
%ifarch ia64 x86_64 ppc64 ppc %{sparc}
BuildRequires:  libnuma-devel
%endif
%lang_package

%description
The procps package contains a set of system utilities that provide
system information. Procps includes ps, free, skill, snice, tload, top,
uptime, vmstat, w, and watch. The ps command displays a snapshot of
running processes. The top command provides a repetitive update of the
statuses of running processes. The free command displays the amounts of
free and used memory on your system. The skill command sends a
terminate command (or another specified signal) to a specified set of
processes. The snice command is used to change the scheduling priority
of specified processes. The tload command prints a graph of the current
system load average to a specified tty. The uptime command displays the
current time, how long the system has been running, how many users are
logged on, and system load averages for the past one, five, and fifteen
minutes. The w command displays a list of the users who are currently
logged on and what they are running. The watch program watches a
running program. The vmstat command displays virtual memory statistics
about processes, memory, paging, block I/O, traps, and CPU activity.

%package devel
Summary:        Development files for procps
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
The procps library can be used to read informations out from /proc
the process information pseudo-file system.

This subpackage contains the header files for libprocps.

%package -n %{libname}
Summary:        The procps library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libname}
The procps library can be used to read informations out from /proc
the process information pseudo-file system.

%prep
%setup -q
%patch0
%patch1
%patch3 -b .trcate
%patch7 -b .rof
%patch8 -b .cache
%patch10 -b .acc
%patch11
%patch12
%patch13 -b .column
%patch14 -b .ovrflw
%patch15
%patch16
%patch17 -b .sysctl
%patch18
%patch19
%patch20
%patch21
%patch28
%patch31 -p1
%patch32
%patch33 -b .pmap4us
%patch34
%patch35 -p1
%patch42
%patch43

%build
test -s .tarball-version || echo %{version} > .tarball-version
#./autogen.sh
autoreconf -fiv
major=$(sed -rn 's/^#define\s+NCURSES_VERSION_MAJOR\s+([0-9]+)/\1/p' %{_includedir}/ncurses.h)
export NCURSESW_CFLAGS="$(ncursesw${major}-config --cflags)"
export NCURSESW_LIBS="$(ncursesw${major}-config --libs)"
export LFS_CFLAGS="$(getconf LFS_CFLAGS)"
%global optflags	%{optflags} -D_GNU_SOURCE $LFS_CFLAGS -DCPU_ZEROTICS -DUSE_X_COLHDR -pipe
%configure		\
    --disable-static	\
%if !%{with nls}
    --disable-nls	\
%endif
    --disable-rpath	\
    --disable-kill	\
%if !%{with pidof}
    --disable-pidof	\
%endif
    --enable-watch8bit	\
    --enable-shared	\
    --enable-skill	\
    --enable-w-from	\
    --enable-sigwinch	\
    --enable-wide-percent \
    --enable-wide-memory \
    --enable-w-from	\
    --enable-libselinux	\
    --with-pic=yes	\
    --with-systemd	\
    --with-gnu-ld \
    --disable-modern-top
%make_build

LD_LIBRARY_PATH=$PWD/proc/.libs \
./pmap $$ || {
    uname -a
    echo /proc/$$/maps
    cat  /proc/$$/maps
    echo /proc/$$/smaps
    cat  /proc/$$/smaps
    exit 1
}

%install
%make_install
install -d %{buildroot}/bin
install -d %{buildroot}/sbin

# clean unwanted files (e.g. coreutils)
rm -f %{buildroot}%{_bindir}/kill
rm -f %{buildroot}%{_bindir}/uptime
rm -f %{buildroot}%{_mandir}/man1/kill.1
rm -f %{buildroot}%{_mandir}/*/man1/kill.1
rm -f %{buildroot}%{_mandir}/man1/uptime.1
rm -f %{buildroot}%{_mandir}/*/man1/uptime.1
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_datadir}/doc/procps-ng

if cmp -s %{buildroot}%{_mandir}/man1/procps.1 %{buildroot}%{_mandir}/man1/ps.1
then
    rm -vf %{buildroot}%{_mandir}/man1/procps.1
    (cat > %{buildroot}%{_mandir}/man1/procps.1)<<-'EOF'
	.so man1/ps.1
	EOF
fi

%if %{with bin2usr}
#
# Identical binaries
#
if cmp -s %{buildroot}/%{_bindir}/pgrep %{buildroot}/%{_bindir}/pkill
then
    rm -vf %{buildroot}/%{_bindir}/pkill
    pushd %{buildroot}/%{_bindir}
	ln pgrep pkill
    popd
fi
if cmp -s %{buildroot}/%{_bindir}/snice %{buildroot}/%{_bindir}/skill
then
    rm -vf %{buildroot}/%{_bindir}/skill
    pushd %{buildroot}/%{_bindir}
	ln snice skill
    popd
fi
%if 0%{?suse_version} < 1550
ln -s %{_bindir}/ps      %{buildroot}/bin/
ln -s %{_bindir}/pgrep   %{buildroot}/bin/
ln -s %{_bindir}/pkill   %{buildroot}/bin/
ln -s %{_sbindir}/sysctl %{buildroot}/sbin/
%endif
%else
mv %{buildroot}%{_bindir}/ps      %{buildroot}/bin/
mv %{buildroot}%{_bindir}/pgrep   %{buildroot}/bin/
mv %{buildroot}%{_bindir}/pkill   %{buildroot}/bin/
mv %{buildroot}%{_sbindir}/sysctl %{buildroot}/sbin/
#
# Identical binaries
#
if cmp -s %{buildroot}/bin/pgrep %{buildroot}/bin/pkill
then
    rm -vf %{buildroot}/bin/pkill
    pushd %{buildroot}/bin
	ln pgrep pkill
    popd
fi
if cmp -s %{buildroot}/%{_bindir}/snice %{buildroot}/%{_bindir}/skill
then
    rm -vf %{buildroot}/%{_bindir}/skill
    pushd %{buildroot}/%{_bindir}
	ln snice skill
    popd
fi
ln -s /bin/ps      %{buildroot}%{_bindir}/ps
ln -s /bin/pgrep   %{buildroot}%{_bindir}/pgrep
ln -s /bin/pkill   %{buildroot}%{_bindir}/pkill
ln -s /sbin/sysctl %{buildroot}%{_sbindir}/sysctl
%endif

%find_lang procps-ng --with-man --all-name

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%check
#
# Skip w test as there is no valid utmp
#
rm -rvf testsuite/w.test
#
# Provide a tty for testing
#
LANG=POSIX
LC_ALL=$LANG
unset LC_CTYPE
SCREENDIR=$(mktemp -d ${PWD}/screen.XXXXXX) || exit 1
SCREENRC=${SCREENDIR}/bash
export SCREENRC SCREENDIR
exec 0< /dev/null
SCREENLOG=${SCREENDIR}/log
cat > $SCREENRC<<-EOF
	deflogin off
	deflog on
	logfile $SCREENLOG
	logfile flush 1
	logtstamp off
	log on
	setsid on
	scrollback 0
	silence on
	utf8 on
	EOF
TMPDIR=$(mktemp -d /tmp/bash.XXXXXXXXXX) || exit 1
> $SCREENLOG
tail -q -s 0.5 -f $SCREENLOG & pid=$!
env HOME=$PWD TERM=$TERM TMPDIR=$TMPDIR SCREENRC=$SCREENRC SCREENDIR=$SCREENDIR \
  screen -D -m make check
kill -TERM $pid
error=no
for log in test-suite.log testsuite/*.log
do
    if grep -E '^(XFAIL|FAIL|ERROR):' $log
    then
	cat $log
	error=yes
    fi
done
%if 0%{?qemu_user_space_build}
if test -x /usr/bin/qemu-%_build_arch
then
    echo Do not fail as pgrep as well as ps will find unexpected qemu-%_build_arch on command lines
    exit 0
fi
%endif
test $error = no || exit 1

%files
%defattr (-,root,root,755)
%license COPYING COPYING.LIB
%doc NEWS Documentation/bugs.md Documentation/FAQ
%if %{with bin2usr}
%if 0%{?suse_version} < 1550
%verify(link) /bin/ps
%verify(link) /bin/pgrep
%verify(link) /bin/pkill
%verify(link) /sbin/sysctl
%endif
%{_bindir}/ps
%{_bindir}/pgrep
%{_bindir}/pkill
%{_sbindir}/sysctl
%else
/bin/ps
/bin/pgrep
/bin/pkill
/sbin/sysctl
%verify(link) %{_bindir}/ps
%verify(link) %{_bindir}/pgrep
%verify(link) %{_bindir}/pkill
%verify(link) %{_sbindir}/sysctl
%endif
%{_bindir}/free
%if %{with pidof}
%{_bindir}/pidof
%endif
%{_bindir}/pmap
%{_bindir}/pwait
%{_bindir}/pwdx
%{_bindir}/skill
%{_bindir}/slabtop
%{_bindir}/snice
%{_bindir}/tload
%{_bindir}/top
%{_bindir}/vmstat
%{_bindir}/w
%{_bindir}/watch
%{_mandir}/man1/free.1%{?ext_man}
%{_mandir}/man1/pgrep.1%{?ext_man}
%if %{with pidof}
%{_mandir}/man1/pidof.1%{?ext_man}
%endif
%{_mandir}/man1/pkill.1%{?ext_man}
%{_mandir}/man1/pmap.1%{?ext_man}
%{_mandir}/man1/procps.1%{?ext_man}
%{_mandir}/man1/ps.1%{?ext_man}
%{_mandir}/man1/pwait.1%{?ext_man}
%{_mandir}/man1/pwdx.1%{?ext_man}
%{_mandir}/man1/skill.1%{?ext_man}
%{_mandir}/man1/slabtop.1%{?ext_man}
%{_mandir}/man1/snice.1%{?ext_man}
%{_mandir}/man1/tload.1%{?ext_man}
%{_mandir}/man1/top.1%{?ext_man}
%{_mandir}/man1/w.1%{?ext_man}
%{_mandir}/man1/watch.1%{?ext_man}
%{_mandir}/man5/sysctl.conf.5%{?ext_man}
%{_mandir}/man8/vmstat.8%{?ext_man}
%{_mandir}/man8/sysctl.8%{?ext_man}

%files devel
%defattr (-,root,root,755)
%dir %{_includedir}/proc
%{_includedir}/proc/alloc.h
%{_includedir}/proc/devname.h
%{_includedir}/proc/escape.h
%{_includedir}/proc/numa.h
%{_includedir}/proc/procps.h
%{_includedir}/proc/pwcache.h
%{_includedir}/proc/readproc.h
%{_includedir}/proc/sig.h
%{_includedir}/proc/slab.h
%{_includedir}/proc/sysinfo.h
%{_includedir}/proc/version.h
%{_includedir}/proc/wchan.h
%{_includedir}/proc/whattime.h
%{_libdir}/libprocps.so
%{_libdir}/pkgconfig/libprocps.pc
%{_mandir}/man3/openproc.3%{?ext_man}
%{_mandir}/man3/readproc.3%{?ext_man}
%{_mandir}/man3/readproctab.3%{?ext_man}

%files -n %{libname}
%defattr (-,root,root,755)
%{_libdir}/libprocps.so.%{somajor}*

%files lang -f procps-ng.lang
%if 0%{?suse_version} < 1550
%dir %{_mandir}/uk/
%endif

%changelog
