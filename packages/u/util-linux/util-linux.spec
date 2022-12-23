#
# spec file for package util-linux
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


%global flavor @BUILD_FLAVOR@%{nil}

# Parts description:
# core: libraries, all binaries except those dependent on libsystemd
# systemd: binaries dependent on systemd, man pages (generator is dependent on ruby)
# python: Python bindings

%if "%{flavor}" == ""
%define psuffix -core
%define ulbuild base
%define ulsubset core
%endif

%if "%{flavor}" == "systemd"
%define ulbuild base
%define ulsubset systemd
%endif

# All python flavors are build separately. No module can be built together with base.
# This is a limitation of %%python_subpackages.
%if "%{flavor}" == "python"
%define ulbuild python
%endif

%if !0%{?usrmerged}
%define ul_extra_bin_sbin 1
%else
%define ul_extra_bin_sbin 0
%endif
%define ul_suid 4755

%define _name   util-linux

%if ! %{defined _distconfdir}
%define _distconfdir %{_sysconfdir}
%else
%define no_config 1
%endif

%define ulprefix %{_prefix}
%define ulexecprefix %{_exec_prefix}
%define ulbindir %{_bindir}
%define ullibdir %{_libdir}
%define ullibexecdir %{_libexecdir}
%define ulincludedir %{_includedir}
%define ulsbindir %{_sbindir}
%define uldatadir %{_datadir}
%define ulmandir %{_mandir}
%define ulinfodir %{_infodir}
%define uldocdir %{_docdir}
%define uldistconfdir %{_distconfdir}
%define ulsysconfdir %{_sysconfdir}
%define ulpamdir %{_pam_vendordir}

%if "%ulbuild" == "base"
%if "%ulsubset" == "core"
Name:           util-linux
Summary:        A collection of basic system utilities (core part)
%else
Name:           util-linux-systemd
Summary:        A collection of basic system utilities (systemd dependent part)
%endif
Group:          System/Base
%else
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-libmount
Summary:        Python bindings for the libmount library
Group:          Development/Languages/Python
%endif
Version:        2.38.1
Release:        0
License:        GPL-2.0-or-later
URL:            https://www.kernel.org/pub/linux/utils/util-linux/
Source:         https://www.kernel.org/pub/linux/utils/util-linux/v2.38/util-linux-%{version}.tar.xz
Source2:        util-linux-login_defs-check.sh
Source3:        util-linux-rpmlintrc
Source6:        etc_filesystems
Source7:        baselibs.conf
Source8:        login.pamd
Source9:        remote.pamd
Source10:       su.pamd
Source11:       su.default
Source12:       https://www.kernel.org/pub/linux/utils/util-linux/v2.38/util-linux-%{version}.tar.sign
Source13:       %{_name}.keyring
Source14:       runuser.pamd
Source15:       runuser-l.pamd
Source16:       su-l.pamd
Source51:       blkid.conf
# PATCH-EXTEND-UPSTREAM: Let `su' handle /sbin and /usr/sbin in path
Patch0:         make-sure-sbin-resp-usr-sbin-are-in-PATH.diff
Patch1:         libmount-print-a-blacklist-hint-for-unknown-filesyst.patch
Patch2:         Add-documentation-on-blacklisted-modules-to-mount-8-.patch
# PATCH-FIX-SUSE util-linux-bash-completion-su-chsh-l.patch bsc1172427 -- Fix "su -s" bash completion.
Patch4:         util-linux-bash-completion-su-chsh-l.patch
# PATCH-FIX-SUSE util-linux-fix-tests-when-@-in-path.patch bsc#1194038 -- rpmbuild %checks fail when @ in the directory path
Patch5:         util-linux-fix-tests-when-at-symbol-in-path.patch
BuildRequires:  audit-devel
BuildRequires:  bc
BuildRequires:  binutils-devel
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  gettext-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libeconf-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
BuildRequires:  utempter-devel
BuildRequires:  zlib-devel
# util-linux is part of VMInstall, but we can well build without it
# Helps shorten a cycle and eliminate a bootstrap issue
#!BuildIgnore:  util-linux
%ifarch ppc ppc64 ppc64le
BuildRequires:  librtas-devel
%endif
%if "%ulsubset" == "systemd"
BuildRequires:  bash-completion
BuildRequires:  libudev-devel
BuildRequires:  socat
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  rubygem(asciidoctor)
PreReq:         permissions
Requires:       adjtimex
Requires:       time
Requires:       which
PreReq:         %install_info_prereq
# man pages were moved to -systemd subpackage with 2.38.x (SLE15 SP6, Leap 15.6)
Conflicts:      util-linux < 2.38
%systemd_requires
%endif
%if "%ulbuild" == "base"
%if "%ulsubset" == "core"
Provides:       fsck-with-dev-lock = %{version}
# bnc#651598:
Provides:       util-linux(fake+no-canonicalize)
Provides:       eject = 2.1.0
Provides:       login = 4.0
Provides:       rfkill = 0.5
# File conflict of eject (up to 12.3 and SLE11).
Obsoletes:      eject <= 2.1.0
# File conflict of login (up to 12.1 and SLE11).
Obsoletes:      login <= 4.0
# File conflict (man page) of rfkill (up to Leap 15 and SLE 15).
Obsoletes:      rfkill <= 0.5
# util-linux-2.34 integrates hardlink (up to Leap 15.1 and SLE15 SP1).
# The last version was 1.0+git.e66999f.
Provides:       hardlink = 1.1
Obsoletes:      hardlink < 1.1
# bnc#805684:
%ifarch s390x
Obsoletes:      s390-32
Provides:       s390-32
%endif
Supplements:    filesystem(minix)
# All login.defs variables require support from shadow side.
# Upgrade this symbol version only if new variables appear!
# Verify by shadow-login_defs-check.sh from shadow source package.
Recommends:     login_defs-support-for-util-linux >= 2.37
%endif
Requires(pre):  group(tty)
# The problem with inconsistent /proc/self/mountinfo read is fixed in kernel 5.8.
# util-linux >= 2.37 no more contain work-around.
Conflicts:      kernel < 5.8
%endif
%if "%ulbuild" == "python"
BuildRequires:  %{python_module devel}
BuildRequires:  rubygem(asciidoctor)
%python_subpackages
%endif

%if "%ulbuild" == "base"
%description
This package contains a large variety of low-level system utilities
that are necessary for a Linux system to function. It contains the
mount program, the fdisk configuration tool, and more.

%if "%ulsubset" == "core"
%package -n libblkid1
Summary:        Filesystem detection library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libblkid1
Library for filesystem detection.

%package -n libblkid-devel
Summary:        Development files for the filesystem detection library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libblkid1 = %{version}

%description -n libblkid-devel
Files needed to develop applications using the library for filesystem
detection.

%package -n libblkid-devel-static
Summary:        Development files for the filesystem detection library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libblkid-devel = %{version}

%description -n libblkid-devel-static
Files needed to develop applications using the library for filesystem
detection.

%package -n libfdisk1
Summary:        Filesystem detection library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libfdisk1
Library for filesystem detection.

%package -n libfdisk-devel
Summary:        Development files for the filesystem detection library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libfdisk1 = %{version}

%description -n libfdisk-devel
Files needed to develop applications using the library for filesystem
detection.

%package -n libfdisk-devel-static
Summary:        Development files for the filesystem detection library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libfdisk-devel = %{version}

%description -n libfdisk-devel-static
Files needed to develop applications using the library for filesystem
detection.

%package -n libmount1
Summary:        Device mount library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libmount1
Library designed to be used in low-level utils like
mount(8) and /usr/sbin/mount.<type> helpers.

%package -n libmount-devel
Summary:        Development files for libmount
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libmount1 = %{version}

%description -n libmount-devel
Files to develop applications using the libmount library.

%package -n libmount-devel-static
Summary:        Development files for libmount
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libmount-devel = %{version}

%description -n libmount-devel-static
Files to develop applications using the libmount library.

%package -n libsmartcols1
Summary:        Column-based text sort engine
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libsmartcols1
Library to sort human readable column-based text output.

%package -n libsmartcols-devel
Summary:        Development files for libsmartcols
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libsmartcols1 = %{version}

%description -n libsmartcols-devel
Files to develop applications using the libsmartcols library.

%package -n libsmartcols-devel-static
Summary:        Development files for libsmartcols
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libsmartcols-devel = %{version}

%description -n libsmartcols-devel-static
Files to develop applications using the libsmartcols library.

%package -n libuuid1
Summary:        Library to generate UUIDs
License:        BSD-3-Clause
Group:          System/Libraries
# declare presence of the new ABI call __uuid_generate_time_cont
# Required for seamless update from older versions (SLE15 SP4, Leap 15.4 and older).
Provides:       libuuid__uuid_generate_time_cont

%description -n libuuid1
A library to generate universally unique IDs (UUIDs).

%package -n libuuid-devel
Summary:        Development files for libuuid
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       libuuid1 = %{version}

%description -n libuuid-devel
Files to develop applications using the library to generate universally
unique IDs (UUIDs).

%package -n libuuid-devel-static
Summary:        Development files for libuuid
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       libuuid-devel = %{version}

%description -n libuuid-devel-static
Files to develop applications using the library to generate universally
unique IDs (UUIDs).

%lang_package
%endif
%if "%ulsubset" == "systemd"
%package -n uuidd
Summary:        Helper daemon to guarantee uniqueness of time-based UUIDs
License:        GPL-2.0-or-later
Group:          System/Filesystems
Requires(pre):  group(uuidd)
# uuidd restart requires the ABI of the new libuuid
# Required for seamless update from older versions (SLE15 SP4, Leap 15.4 and older).
Requires(post): libuuid__uuid_generate_time_cont
# uuidd bash-completion moved to a correct package
Conflicts:      util-linux < 2.25
# uuid-runtime appeared in SLE11 SP1 to SLE11 SP3
Provides:       uuid-runtime = %{version}
Obsoletes:      uuid-runtime <= 2.19.1
%systemd_requires

%description -n uuidd
The uuidd package contains a userspace daemon (uuidd) which guarantees
uniqueness of time-based UUID generation even at very high rates on
SMP systems.

%endif
%endif

%if "%ulbuild" == "python"
%description
This package contains the Python bindings for util-linux libmount
library.
%endif

%prep
%setup -q -n %{_name}-%{version}
cp -a %{S:2} .
%autopatch -p1
# This test randomly fails or keeps hanging task inside build chroot (tested on 2.38).
rm tests/ts/lsns/ioctl_ns

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export SUID_CFLAGS="-fpie"
export SUID_LDFLAGS="-pie"
export LDFLAGS="-Wl,-z,relro,-z,now"
export CFLAGS="%{optflags} -D_GNU_SOURCE"
export CXXFLAGS="%{optflags} -D_GNU_SOURCE"
# Here we define a build function. For the base build, we use it as it
# is. For python build, we use it repeatedly for all flavors.
function configure_and_build() {
%if "%ulbuild" == "python"
%define _configure ../configure
%endif
#
#AUTOPOINT=true GTKDOCIZE=true autoreconf -vfi
# All dirs needs to be specified, as %%configure does not derive them
# from %%_prefix, and bootstrap build will fall back to /usr.
%configure\
	--prefix=%{ulprefix}\
	--exec-prefix=%{ulexecprefix}\
	--disable-silent-rules\
	--bindir=%{ulbindir}\
	--sbindir=%{ulsbindir}\
	--sysconfdir=%{ulsysconfdir}\
	--datadir=%{uldatadir}\
	--includedir=%{ulincludedir}\
	--libdir=%{ullibdir}\
	--libexecdir=%{ullibexecdir}\
	--mandir=%{ulmandir}\
	--infodir=%{ulinfodir}\
	--docdir=%{uldocdir}/%{name}\
	--disable-makeinstall-chown\
	--disable-makeinstall-setuid\
	--with-audit\
	--with-btrfs\
	--with-gnu-ld\
	--with-ncursesw\
	--with-readline\
	--with-selinux\
	--with-utempter\
	--with-bashcompletiondir=%{uldatadir}/bash-completion/completions\
	--with-systemdsystemunitdir=%{_unitdir}\
	--enable-libuuid-force-uuidd\
	--enable-sulogin-emergency-mount\
	--disable-use-tty-group\
	--disable-rpath\
	--disable-chfn-chsh\
	--disable-newgrp\
	--disable-vipw\
	--disable-pg\
	--enable-fs-paths-default="/sbin:/usr/sbin"\
	--enable-static\
%if "%ulbuild" == "python"
	--disable-all-programs\
	--with-python\
	--enable-pylibmount\
	--enable-libmount\
	--enable-libblkid\
%else
	--enable-all-programs\
%if "%ulsubset" == "core"
	--without-systemd\
%else
	--with-systemd\
%endif
	--without-python\
%endif
	--with-vendordir=%{uldistconfdir}
make %{?_smp_mflags}
}
%if "%ulbuild" == "base"
configure_and_build
%if "%ulsubset" == "core"
bash ./util-linux-login_defs-check.sh
#BEGIN SYSTEMD SAFETY CHECK
# With systemd, some utilities are built differently. Keep track of these
# sources to prevent building of systemd-less versions.
#
# WARNING: Never edit following line without doing all suggested in the echo below!
UTIL_LINUX_KNOWN_SYSTEMD_DEPS='./login-utils/lslogins.c ./misc-utils/findmnt.c ./misc-utils/logger.c ./misc-utils/lsblk-properties.c ./misc-utils/uuidd.c '
UTIL_LINUX_FOUND_SYSTEMD_DEPS=$(grep -rl 'HAVE_LIB\(SYSTEMD\|UDEV\)' . | fgrep '.c' | LC_ALL=C sort | tr '\n' ' ')
if test "$UTIL_LINUX_KNOWN_SYSTEMD_DEPS" != "$UTIL_LINUX_FOUND_SYSTEMD_DEPS" ; then
	echo "List of utilities depending on systemd have changed.
Please check the new util-linux-systemd file list, file removal and update of Conflicts for safe update!
Then update configure options to build what needed.
Only then you can safely update following spec file line:
UTIL_LINUX_KNOWN_SYSTEMD_DEPS='$UTIL_LINUX_FOUND_SYSTEMD_DEPS'"
	exit 1
fi
#END SYSTEMD SAFETY CHECK
%endif
%endif
%if "%ulbuild" == "python"
%{python_expand export PYTHON=$python
mkdir -p build.$python
cd build.$python
configure_and_build
cd ..
}
%endif

%install
%if "%ulbuild" == "base"
%make_install
mkdir -p %{buildroot}{%{uldistconfdir}/default,%{ulpamdir},%{ulsysconfdir}/issue.d}
install -m 644 %{SOURCE51} %{buildroot}%{ulsysconfdir}/blkid.conf
install -m 644 %{SOURCE8} %{buildroot}%{ulpamdir}/login
install -m 644 %{SOURCE9} %{buildroot}%{ulpamdir}/remote
install -m 644 %{SOURCE14} %{buildroot}%{ulpamdir}/runuser
install -m 644 %{SOURCE15} %{buildroot}%{ulpamdir}/runuser-l
install -m 644 %{SOURCE10} %{buildroot}%{ulpamdir}/su
install -m 644 %{SOURCE16} %{buildroot}%{ulpamdir}/su-l
install -m 644 %{SOURCE11} %{buildroot}%{uldistconfdir}/default/su
sed 's/\bsu\b/runuser/g' <%{SOURCE11} >runuser.default
install -m 644 runuser.default %{buildroot}%{uldistconfdir}/default/runuser
rm -fv "%{buildroot}/%{ulsbindir}/raw" "%{buildroot}/sbin/raw" \
	"%{buildroot}/%{ulmandir}/man8/raw.8"*
install -m 644 %{SOURCE6} %{buildroot}%{ulsysconfdir}/filesystems
echo -e "#!/bin/sh\n/sbin/blockdev --flushbufs \$1" > %{buildroot}%{ulsbindir}/flushb
chmod 755 %{buildroot}%{ulsbindir}/flushb
# arch dependent
%ifarch s390 s390x
rm -f %{buildroot}%{ulsysconfdir}/fdprm
rm -f %{buildroot}%{ulbindir}/setterm
rm -f %{buildroot}%{ulsbindir}/fdformat
rm -f %{buildroot}%{ulsbindir}/hwclock
rm -f %{buildroot}%{ulsbindir}/tunelp
rm -f %{buildroot}%{ulmandir}/man8/fdformat.8*
rm -f %{buildroot}%{ulmandir}/man8/hwclock.8*
rm -f %{buildroot}%{ulmandir}/man8/tunelp.8*
%endif
%ifarch ia64 %sparc m68k
rm -f %{buildroot}%{ulmandir}/man8/cfdisk.8*
rm -f %{buildroot}%{ulmandir}/man8/sfdisk.8*
rm -f %{buildroot}%{ulsbindir}/cfdisk
rm -f %{buildroot}%{ulsbindir}/sfdisk
%endif
%ifarch ia64 m68k
rm -f %{buildroot}%{ulsbindir}/fdisk
rm -f %{buildroot}%{ulmandir}/man8/fdisk.8*
%endif
# create list of setarch(8) symlinks
find  %{buildroot}%{ulmandir}/man8 -regextype posix-egrep  \
  -regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64|parisc|parisc32|parisc64)\.8.*" \
  -printf "%{ulmandir}/man8/%f*\n" >> %{name}.files
find  %{buildroot}%{ulbindir}/ -regextype posix-egrep -type l \
  -regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64|parisc|parisc32|parisc64)$" \
  -printf "%{ulbindir}/%f\n" >> %{name}.files
mkdir -p %{buildroot}%{_sharedstatedir}/libuuid
mkdir -p %{buildroot}/run/uuidd
# clock.txt from uuidd is a ghost file
touch %{buildroot}%{_sharedstatedir}/libuuid/clock.txt
%if %{ul_extra_bin_sbin}
mkdir -p %{buildroot}{/bin,/sbin}
for i in dmesg findmnt kill logger lsblk more mount su umount; do
	if test -f "%{buildroot}%{ulbindir}/$i" ; then
		ln -s "%{ulbindir}/$i" "%{buildroot}/bin/"
	fi
done
for i in agetty blockdev cfdisk ctrlaltdel fdisk fsck.minix fsck.cramfs\
 hwclock losetup mkfs mkfs.bfs mkfs.minix mkfs.cramfs mkswap nologin\
 pivot_root raw sfdisk swapoff swapon blkid findfs fsck switch_root\
 wipefs fsfreeze swaplabel fstrim chcpu; do
	if test -f "%{buildroot}%{ulsbindir}/$i" ; then
		ln -s "%{ulsbindir}/$i" "%{buildroot}/sbin/"
	fi
done
# login is always and only in /bin
mv %{buildroot}%{ulbindir}/login %{buildroot}/bin/
%endif
%if "%ulsubset" == "core"
%find_lang %{_name} %{name}.lang
%else
echo -n "" >%{name}.lang
ln -sf /sbin/service %{buildroot}%{ulsbindir}/rcuuidd
ln -sf /sbin/service %{buildroot}%{ulsbindir}/rcfstrim
%endif
%endif
%if "%ulbuild" == "python"
%{python_expand cd build.$python
%make_install
rm %{buildroot}%{$python_sitearch}/libmount/*.*a
cd ..
}
# There is a limitation: python module needs to build much more, and install even more. Delete it.
rm -r %{buildroot}{%{ulbindir},%{ulmandir},%{uldatadir},%{ulincludedir},%{ullibdir}/{lib,pkg}*}
%endif
# Link duplicate manpages or python bindings.
%fdupes -s %{buildroot}%{ulprefix}

%if "%ulbuild" == "base"
%if "%ulbuild" != "python"
%check
# Perform testsuite with the standard build only.
# mark some tests "known_fail"
#
%if 0%{?qemu_user_space_build}
export TS_OPT_fdisk_gpt_known_fail="yes"
export TS_OPT_fdisk_oddinput_known_fail="yes"
export TS_OPT_fdisk_sunlabel_known_fail="yes"
export TS_OPT_fincore_count_known_fail="yes"
export TS_OPT_libfdisk_gpt_known_fail="yes"
export TS_OPT_misc_flock_known_fail="yes"
export TS_OPT_misc_ionice_known_fail="yes"
export TS_OPT_misc_swaplabel_known_fail="yes"
export TS_OPT_kill_name_to_number_known_fail="yes"
export TS_OPT_kill_print_pid_known_fail="yes"
export TS_OPT_kill_queue_known_fail="yes"
export TS_OPT_uuid_uuidd_known_fail="yes"
# unsupported syscall in script(1) ... might be fixed in qemu
export TS_OPT_script_known_fail="yes"
# may segfault on qemu-user-space
export TS_OPT_misc_setarch_known_fail="yes"
%endif
# Succeeds in local build, fails in OBS.
export TS_OPT_hardlink_options_known_fail="yes"
export TS_OPT_lsfd_mkfds_rw_character_device_known_fail="yes"
export TS_OPT_lsfd_mkfds_symlink_known_fail="yes"
# This does not work with a chroot build: / is not a mountpoint
export TS_OPT_misc_mountpoint_known_fail="yes"
#
# hacks
export PATH="$PATH:/sbin:/usr/sbin"
#
# do the check but don't abort yet
result="0"
make %{?_smp_mflags} check || result="1"
#
# always show test diffs (inclusive known_fail) and exit result
diffs_files="$(find tests/diff -type f | sort)"
echo "$diffs_files" | xargs -r cat
exit "$result"

%if "%ulsubset" == "core"
%verifyscript
%verify_permissions -e %{ulbindir}/wall -e %{ulbindir}/write -e %{ulbindir}/mount -e %{ulbindir}/umount
%verify_permissions -e %{ulbindir}/su

%endif

%pre
%if "%ulsubset" == "core"
# move outdated pam.d/*.rpmsave files away
for i in login remote runuser runuser-l su su-l ; do
    test -f /etc/pam.d/${i}.rpmsave && mv -v /etc/pam.d/${i}.rpmsave /etc/pam.d/${i}.rpmsave.old ||:
done
%endif
%if "%ulsubset" == "systemd"
%service_add_pre fstrim.service fstrim.timer
%endif

%post
%if "%ulsubset" == "core"
%set_permissions %{ulbindir}/wall %{ulbindir}/write %{ulbindir}/mount %{ulbindir}/umount
%set_permissions %{ulbindir}/su
%if ! %{defined no_config}
#
# If outdated PAM file is detected, issue a warning.
for PAM_FILE in login remote runuser runuser-l su su-l ; do
	if test -f %{ulpamdir}/$PAM_FILE.rpmnew ; then
		echo "Your %{ulpamdir}/$PAM_FILE is outdated. Please check %{ulpamdir}/$PAM_FILE.rpmnew!" >&2
	fi
done
#
# /etc/default/su is tagged as noreplace.
# But we want to migrate variables to /etc/login.defs (bsc#1121197).
# Perform one-time config replace.
# Applies for: Update from SLE11, online update for SLE15 SP1, Leap15.1.
# Not needed for /etc/default/runuser. It was first packaged after the change.
if ! grep -q "^# /etc/default/su is an override" %{ulsysconfdir}/default/su ; then
	if test -f %{ulsysconfdir}/default/su.rpmnew ; then
		if ! test -f %{ulsysconfdir}/default/su.rpmorig ; then
			cp -a %{ulsysconfdir}/default/su %{ulsysconfdir}/default/su.rpmorig
		fi
		mv %{ulsysconfdir}/default/su.rpmnew %{ulsysconfdir}/default/su
		echo "One time clean-up of %{ulsysconfdir}/default/su was performed." >&2
		echo "Original contents was saved to %{ulsysconfdir}/default/su.rpmorig." >&2
		echo "Please edit %{ulsysconfdir}/login.defs or %{ulsysconfdir}/default/su to restore your customization." >&2
	fi
fi
%endif
%if "%ulsubset" == "systemd"
%service_add_post fstrim.service fstrim.timer

%preun
%service_del_preun fstrim.service fstrim.timer

%postun
%service_del_postun fstrim.service fstrim.timer
%endif

%if "%ulsubset" == "core"
%if %{defined no_config}
%posttrans
# Migration to /usr/etc.
for i in  login remote runuser runuser-l su su-l; do
  test -f /etc/pam.d/${i}.rpmsave && mv -v /etc/pam.d/${i}.rpmsave /etc/pam.d/${i} ||:
done
%endif

%post -n libblkid1 -p /sbin/ldconfig

%postun -n libblkid1 -p /sbin/ldconfig

%post -n libmount1 -p /sbin/ldconfig

%postun -n libmount1 -p /sbin/ldconfig

%post -n libsmartcols1 -p /sbin/ldconfig

%postun -n libsmartcols1 -p /sbin/ldconfig

%post -n libuuid1 -p /sbin/ldconfig

%postun -n libuuid1 -p /sbin/ldconfig

%post -n libfdisk1 -p /sbin/ldconfig

%postun -n libfdisk1 -p /sbin/ldconfig

%endif
%if "%ulsubset" == "systemd"
%if 0%{?suse_version} >= 1330
%pre -n uuidd
%else

%pre -n uuidd
getent group uuidd >/dev/null || /usr/sbin/groupadd -r uuidd
getent passwd uuidd >/dev/null || \
	/usr/sbin/useradd -r -g uuidd -c "User for uuidd" \
	-d %{_localstatedir}/run/uuidd uuidd
%endif
%{service_add_pre uuidd.socket uuidd.service}

%post -n uuidd
# Fix running instance paths during live upgrade from
# Leap = 15, SLE = 15 (boo#1113188).
# Useful for Tumbleweed or zypper dup only.
mv /run/run/uuidd /run/uuidd >/dev/null 2>&1 || :
rmdir --ignore-fail-on-non-empty /run/run >/dev/null 2>&1 || :
%{service_add_post uuidd.socket uuidd.service}

%preun -n uuidd
%{service_del_preun uuidd.socket uuidd.service}

%postun -n uuidd
%{service_del_postun uuidd.socket uuidd.service}
%endif

%endif

%files -n %{name} -f %{name}.files
%defattr(-,root,root)
#
%if "%ulsubset" == "core"
# Common files for all archs
%doc AUTHORS ChangeLog README NEWS
%license README.licensing
%license COPYING
%license Documentation/licenses/*
%attr(-,uuidd,uuidd) %dir %{_sharedstatedir}/libuuid
%attr(-,uuidd,uuidd) %ghost %{_sharedstatedir}/libuuid/clock.txt
%config(noreplace) %{ulsysconfdir}/filesystems
%config(noreplace) %{ulsysconfdir}/blkid.conf
%endif
%if %{defined no_config}
%{ulpamdir}/login
%{ulpamdir}/remote
%{ulpamdir}/runuser
%{ulpamdir}/runuser-l
%{ulpamdir}/su
%{ulpamdir}/su-l
%if 0%{?suse_version} <= 1520
%dir %{uldistconfdir}/default
%endif
%{uldistconfdir}/default/runuser
%{uldistconfdir}/default/su
%else
%config(noreplace) %{ulpamdir}/login
%config(noreplace) %{ulpamdir}/remote
%config(noreplace) %{ulpamdir}/runuser
%config(noreplace) %{ulpamdir}/runuser-l
%config(noreplace) %{ulpamdir}/su
%config(noreplace) %{ulpamdir}/su-l
%config(noreplace) %{ulsysconfdir}/default/runuser
%config(noreplace) %{ulsysconfdir}/default/su
%endif
%config %dir %{ulsysconfdir}/issue.d
%if %{ul_extra_bin_sbin}
%exclude /bin/findmnt
/bin/kill
%verify(not mode) %attr(%ul_suid,root,root) /bin/su
/bin/dmesg
/bin/more
%verify(not mode) %attr(%ul_suid,root,root) /bin/mount
%verify(not mode) %attr(%ul_suid,root,root) /bin/umount
/bin/login
%exclude /bin/logger
%exclude /bin/lsblk
/sbin/agetty
/sbin/blockdev
/sbin/ctrlaltdel
/sbin/fsck.minix
/sbin/fsck.cramfs
/sbin/losetup
/sbin/mkfs
/sbin/mkfs.bfs
/sbin/mkfs.minix
/sbin/mkfs.cramfs
/sbin/mkswap
/sbin/nologin
/sbin/pivot_root
/sbin/swapoff
/sbin/swapon
/sbin/blkid
/sbin/findfs
/sbin/fsck
/sbin/switch_root
/sbin/wipefs
/sbin/fsfreeze
/sbin/swaplabel
/sbin/fstrim
/sbin/chcpu
%endif
%{ulbindir}/kill
%verify(not mode) %attr(%ul_suid,root,root) %{ulbindir}/su
%{ulbindir}/eject
%{ulbindir}/cal
%{ulbindir}/chmem
%{ulbindir}/choom
%{ulbindir}/chrt
%{ulbindir}/col
%{ulbindir}/colcrt
%{ulbindir}/colrm
%{ulbindir}/column
%{ulbindir}/dmesg
%{ulbindir}/fallocate
%{ulbindir}/fincore
%if "%ulsubset" == "core"
%exclude %{ulbindir}/findmnt
%exclude %{ulbindir}/logger
%exclude %{ulbindir}/lsblk
%exclude %{ulbindir}/lslogins
%endif
%{ulbindir}/flock
%{ulbindir}/getopt
%{ulbindir}/hardlink
%{ulbindir}/hexdump
%{ulbindir}/ionice
%{ulbindir}/ipcmk
%{ulbindir}/ipcrm
%{ulbindir}/ipcs
%{ulbindir}/irqtop
%{ulbindir}/isosize
%{ulbindir}/last
%{ulbindir}/lastb
%{ulbindir}/line
%{ulbindir}/look
%if !%{ul_extra_bin_sbin}
%{ulbindir}/login
%endif
%{ulbindir}/lscpu
%{ulbindir}/lsfd
%{ulbindir}/lsipc
%{ulbindir}/lsirq
%{ulbindir}/lslocks
%{ulbindir}/lsmem
%{ulbindir}/lsns
%{ulbindir}/mcookie
%{ulbindir}/mesg
%{ulbindir}/more
%verify(not mode) %attr(%ul_suid,root,root) %{ulbindir}/mount
%{ulbindir}/namei
%{ulbindir}/nsenter
%{ulbindir}/prlimit
%{ulbindir}/rename
%{ulbindir}/renice
%{ulbindir}/rev
%{ulbindir}/script
%{ulbindir}/scriptlive
%{ulbindir}/scriptreplay
%{ulbindir}/setarch
%{ulbindir}/setpriv
%{ulbindir}/setsid
%{ulbindir}/taskset
%{ulbindir}/uclampset
%{ulbindir}/ul
%verify(not mode)%attr(%ul_suid,root,root)  %{ulbindir}/umount
%{ulbindir}/unshare
%{ulbindir}/mountpoint
%{ulbindir}/utmpdump
%{ulbindir}/uuidgen
%{ulbindir}/uuidparse
%{ulbindir}/uname26
%{ulbindir}/wdctl
%{ulsbindir}/addpart
%{ulsbindir}/agetty
%{ulsbindir}/blkid
%{ulsbindir}/blkdiscard
# blkzone depends on linux/blkzoned.h
%if 0%{?suse_version} >= 1330
%{ulsbindir}/blkzone
%endif
%{ulsbindir}/blockdev
%{ulsbindir}/chcpu
%{ulsbindir}/ctrlaltdel
%{ulsbindir}/delpart
%{ulsbindir}/findfs
%{ulsbindir}/fsck
%{ulsbindir}/fsck.minix
%{ulsbindir}/fsck.cramfs
%{ulsbindir}/fsfreeze
%{ulsbindir}/fstrim
%{ulsbindir}/ldattach
%{ulsbindir}/losetup
%{ulsbindir}/mkfs
%{ulsbindir}/mkfs.bfs
%{ulsbindir}/mkfs.minix
%{ulsbindir}/mkfs.cramfs
%{ulsbindir}/mkswap
%{ulsbindir}/nologin
%{ulsbindir}/partx
%{ulsbindir}/pivot_root
%{ulsbindir}/resizepart
%{ulsbindir}/rfkill
%{ulsbindir}/rtcwake
%{ulsbindir}/runuser
%{ulsbindir}/sulogin
%{ulsbindir}/swaplabel
%{ulsbindir}/swapoff
%{ulsbindir}/swapon
%{ulsbindir}/switch_root
%{ulsbindir}/wipefs
%verify(not mode) %attr(0755,root,tty) %{ulbindir}/wall
%{ulbindir}/whereis
%verify(not mode) %attr(0755,root,tty) %{ulbindir}/write
%{ulsbindir}/zramctl
%{ulsbindir}/flushb
%{ulsbindir}/readprofile
# These directories should be owned by bash-completion. But we don't want to
# install them on build, so own these two directories:
%dir %{uldatadir}/bash-completion
%dir %{uldatadir}/bash-completion/completions
%{uldatadir}/bash-completion/completions/*
#
%exclude %{uldatadir}/bash-completion/completions/uuidd
# util-linux documentation files
%doc Documentation/blkid.txt
%doc Documentation/cal.txt
%doc Documentation/col.txt
%doc Documentation/deprecated.txt
%doc Documentation/getopt.txt
%doc Documentation/howto-debug.txt
%doc Documentation/hwclock.txt
%doc Documentation/modems-with-agetty.txt
%doc Documentation/mount.txt
%doc Documentation/pg.txt
%{uldocdir}/%{name}/getopt-example.*
%exclude %{ulmandir}/man*/*
%exclude %{ulsbindir}/uuidd
%endif
%if "%ulsubset" == "systemd"
%exclude %attr(-,uuidd,uuidd) %dir %{_sharedstatedir}/libuuid
%exclude %attr(-,uuidd,uuidd) %ghost %{_sharedstatedir}/libuuid/clock.txt
%exclude %config(noreplace) %{ulsysconfdir}/filesystems
%exclude %config(noreplace) %{ulsysconfdir}/blkid.conf
%if %{defined no_config}
%exclude %{ulpamdir}/login
%exclude %{ulpamdir}/remote
%exclude %{ulpamdir}/runuser
%exclude %{ulpamdir}/runuser-l
%exclude %{ulpamdir}/su
%exclude %{ulpamdir}/su-l
%if 0%{?suse_version} <= 1520
%exclude %dir %{uldistconfdir}/default
%endif
%exclude %{uldistconfdir}/default/runuser
%exclude %{uldistconfdir}/default/su
%else
%exclude %config(noreplace) %{ulpamdir}/login
%exclude %config(noreplace) %{ulpamdir}/remote
%exclude %config(noreplace) %{ulpamdir}/runuser
%exclude %config(noreplace) %{ulpamdir}/runuser-l
%exclude %config(noreplace) %{ulpamdir}/su
%exclude %config(noreplace) %{ulpamdir}/su-l
%exclude %config(noreplace) %{ulsysconfdir}/default/runuser
%exclude %config(noreplace) %{ulsysconfdir}/default/su
%endif
%exclude %config %dir %{ulsysconfdir}/issue.d
%if %{ul_extra_bin_sbin}
%exclude /bin/findmnt
%exclude /bin/kill
%exclude %verify(not mode) %attr(%ul_suid,root,root) /bin/su
%exclude /bin/dmesg
%exclude /bin/more
%exclude %verify(not mode) %attr(%ul_suid,root,root) /bin/mount
%exclude %verify(not mode) %attr(%ul_suid,root,root) /bin/umount
%exclude /bin/login
/bin/logger
/bin/lsblk
%exclude /sbin/agetty
%exclude /sbin/blockdev
%exclude /sbin/ctrlaltdel
%exclude /sbin/fsck.minix
%exclude /sbin/fsck.cramfs
%exclude /sbin/losetup
%exclude /sbin/mkfs
%exclude /sbin/mkfs.bfs
%exclude /sbin/mkfs.minix
%exclude /sbin/mkfs.cramfs
%exclude /sbin/mkswap
%exclude /sbin/nologin
%exclude /sbin/pivot_root
%exclude /sbin/swapoff
%exclude /sbin/swapon
%exclude /sbin/blkid
%exclude /sbin/findfs
%exclude /sbin/fsck
%exclude /sbin/switch_root
%exclude /sbin/wipefs
%exclude /sbin/fsfreeze
%exclude /sbin/swaplabel
%exclude /sbin/fstrim
%exclude /sbin/chcpu
%endif
%exclude %{ulbindir}/kill
%exclude %verify(not mode) %attr(%ul_suid,root,root) %{ulbindir}/su
%exclude %{ulbindir}/eject
%exclude %{ulbindir}/cal
%exclude %{ulbindir}/chmem
%exclude %{ulbindir}/choom
%exclude %{ulbindir}/chrt
%exclude %{ulbindir}/col
%exclude %{ulbindir}/colcrt
%exclude %{ulbindir}/colrm
%exclude %{ulbindir}/column
%exclude %{ulbindir}/dmesg
%exclude %{ulbindir}/fallocate
%exclude %{ulbindir}/fincore
%{ulbindir}/findmnt
%exclude %{ulbindir}/flock
%exclude %{ulbindir}/getopt
%exclude %{ulbindir}/hardlink
%exclude %{ulbindir}/hexdump
%exclude %{ulbindir}/ionice
%exclude %{ulbindir}/ipcmk
%exclude %{ulbindir}/ipcrm
%exclude %{ulbindir}/ipcs
%exclude %{ulbindir}/irqtop
%exclude %{ulbindir}/isosize
%exclude %{ulbindir}/last
%exclude %{ulbindir}/lastb
%exclude %{ulbindir}/line
%{ulbindir}/logger
%exclude %{ulbindir}/look
%if !%{ul_extra_bin_sbin}
%exclude %{ulbindir}/login
%endif
%{ulbindir}/lsblk
%exclude %{ulbindir}/lscpu
%exclude %{ulbindir}/lsfd
%exclude %{ulbindir}/lsipc
%exclude %{ulbindir}/lsirq
%{ulbindir}/lslocks
%{ulbindir}/lslogins
%exclude %{ulbindir}/lsmem
%exclude %{ulbindir}/lsns
%exclude %{ulbindir}/mcookie
%exclude %{ulbindir}/mesg
%exclude %{ulbindir}/more
%exclude %verify(not mode) %attr(%ul_suid,root,root) %{ulbindir}/mount
%exclude %{ulbindir}/namei
%exclude %{ulbindir}/nsenter
%exclude %{ulbindir}/prlimit
%exclude %{ulbindir}/rename
%exclude %{ulbindir}/renice
%exclude %{ulbindir}/rev
%exclude %{ulbindir}/script
%exclude %{ulbindir}/scriptlive
%exclude %{ulbindir}/scriptreplay
%exclude %{ulbindir}/setarch
%exclude %{ulbindir}/setpriv
%exclude %{ulbindir}/setsid
%exclude %{ulbindir}/taskset
%exclude %{ulbindir}/uclampset
%exclude %{ulbindir}/ul
%exclude %verify(not mode)%attr(%ul_suid,root,root)  %{ulbindir}/umount
%exclude %{ulbindir}/unshare
%exclude %{ulbindir}/mountpoint
%exclude %{ulbindir}/utmpdump
%exclude %{ulbindir}/uuidgen
%exclude %{ulbindir}/uuidparse
%exclude %{ulbindir}/uname26
%exclude %{ulbindir}/wdctl
%exclude %{ulsbindir}/addpart
%exclude %{ulsbindir}/agetty
%exclude %{ulsbindir}/blkid
%exclude %{ulsbindir}/blkdiscard
# blkzone depends on linux/blkzoned.h
%if 0%{?suse_version} >= 1330
%exclude %{ulsbindir}/blkzone
%endif
%exclude %{ulsbindir}/blockdev
%exclude %{ulsbindir}/chcpu
%exclude %{ulsbindir}/ctrlaltdel
%exclude %{ulsbindir}/delpart
%exclude %{ulsbindir}/findfs
%exclude %{ulsbindir}/fsck
%exclude %{ulsbindir}/fsck.minix
%exclude %{ulsbindir}/fsck.cramfs
%exclude %{ulsbindir}/fsfreeze
%exclude %{ulsbindir}/fstrim
%exclude %{ulsbindir}/ldattach
%exclude %{ulsbindir}/losetup
%exclude %{ulsbindir}/mkfs
%exclude %{ulsbindir}/mkfs.bfs
%exclude %{ulsbindir}/mkfs.minix
%exclude %{ulsbindir}/mkfs.cramfs
%exclude %{ulsbindir}/mkswap
%exclude %{ulsbindir}/nologin
%exclude %{ulsbindir}/partx
%exclude %{ulsbindir}/pivot_root
%exclude %{ulsbindir}/resizepart
%exclude %{ulsbindir}/rfkill
%exclude %{ulsbindir}/rtcwake
%exclude %{ulsbindir}/runuser
%exclude %{ulsbindir}/sulogin
%exclude %{ulsbindir}/swaplabel
%exclude %{ulsbindir}/swapoff
%exclude %{ulsbindir}/swapon
%exclude %{ulsbindir}/switch_root
%exclude %{ulsbindir}/wipefs
%verify(not mode) %attr(0755,root,tty) %{ulbindir}/wall
%exclude %{ulbindir}/whereis
%verify(not mode) %attr(0755,root,tty) %{ulbindir}/write
%exclude %{ulsbindir}/zramctl
%exclude %{ulsbindir}/flushb
%exclude %{ulsbindir}/readprofile
# These directories should be owned by bash-completion. But we don't want to
# install them on build, so own these two directories:
%exclude %dir %{uldatadir}/bash-completion
%exclude %dir %{uldatadir}/bash-completion/completions
%exclude %{uldatadir}/bash-completion/completions/*
#
%exclude %{ulsbindir}/uuidd
%exclude %{uldatadir}/bash-completion/completions/uuidd
%exclude %{uldatadir}/locale
%exclude %{ulincludedir}/*
%exclude %{ullibdir}/lib*.*
%exclude %{ullibdir}/pkgconfig/*.pc
%exclude %{uldocdir}/%{name}/getopt-example.*
%{ulmandir}/man1/kill.1.gz
%{ulmandir}/man1/su.1.gz
%{ulmandir}/man1/cal.1.gz
%{ulmandir}/man1/choom.1.gz
%{ulmandir}/man1/chrt.1.gz
%{ulmandir}/man1/col.1.gz
%{ulmandir}/man1/colcrt.1.gz
%{ulmandir}/man1/colrm.1.gz
%{ulmandir}/man1/column.1.gz
%{ulmandir}/man1/dmesg.1.gz
%{ulmandir}/man1/eject.1.gz
%{ulmandir}/man1/fallocate.1.gz
%{ulmandir}/man1/fincore.1.gz
%{ulmandir}/man1/flock.1.gz
%{ulmandir}/man1/getopt.1.gz
%{ulmandir}/man1/hardlink.1.gz
%{ulmandir}/man1/hexdump.1.gz
%{ulmandir}/man1/ipcrm.1.gz
%{ulmandir}/man1/ipcs.1.gz
%{ulmandir}/man1/last.1.gz
%{ulmandir}/man1/lastb.1.gz
%{ulmandir}/man1/line.1.gz
%{ulmandir}/man1/login.1.gz
%{ulmandir}/man1/look.1.gz
%{ulmandir}/man1/logger.1.gz
%{ulmandir}/man1/lscpu.1.gz
%{ulmandir}/man1/lsfd.1.gz
%{ulmandir}/man1/lsipc.1.gz
%{ulmandir}/man1/lsirq.1.gz
%{ulmandir}/man1/lslogins.1.gz
%{ulmandir}/man8/lsblk.8.gz
%{ulmandir}/man1/lsmem.1.gz
%{ulmandir}/man1/mcookie.1.gz
%{ulmandir}/man1/mesg.1.gz
%{ulmandir}/man1/more.1.gz
%{ulmandir}/man1/namei.1.gz
%{ulmandir}/man1/nsenter.1.gz
%{ulmandir}/man1/ionice.1.gz
%{ulmandir}/man1/irqtop.1.gz
%{ulmandir}/man1/prlimit.1.gz
%{ulmandir}/man1/rename.1.gz
%{ulmandir}/man1/rev.1.gz
%{ulmandir}/man1/renice.1.gz
%{ulmandir}/man1/setpriv.1.gz
%{ulmandir}/man1/setsid.1.gz
%{ulmandir}/man1/script.1.gz
%{ulmandir}/man1/scriptlive.1.gz
%{ulmandir}/man1/scriptreplay.1.gz
%{ulmandir}/man1/setterm.1.gz
%{ulmandir}/man1/taskset.1.gz
%{ulmandir}/man1/ul.1.gz
%{ulmandir}/man1/unshare.1.gz
%{ulmandir}/man1/wall.1.gz
%{ulmandir}/man1/whereis.1.gz
%{ulmandir}/man1/write.1.gz
%{ulmandir}/man1/ipcmk.1.gz
%{ulmandir}/man1/mountpoint.1.gz
%{ulmandir}/man1/runuser.1.gz
%{ulmandir}/man1/uclampset.1.gz
%{ulmandir}/man1/utmpdump.1.gz
%{ulmandir}/man1/uuidgen.1.gz
%{ulmandir}/man1/uuidparse.1.gz
%{ulmandir}/man5/adjtime_config.5.gz
%{ulmandir}/man5/fstab.5.gz
%{ulmandir}/man5/terminal-colors.d.5.gz
%{ulmandir}/man8/addpart.8.gz
%{ulmandir}/man8/agetty.8.gz
%if 0%{?suse_version} >= 1330
%{ulmandir}/man8/blkzone.8.gz
%endif
%{ulmandir}/man8/blockdev.8.gz
%{ulmandir}/man8/chmem.8.gz
%{ulmandir}/man8/ctrlaltdel.8.gz
%{ulmandir}/man8/delpart.8.gz
%{ulmandir}/man8/blkid.8.gz
%{ulmandir}/man8/blkdiscard.8.gz
%{ulmandir}/man8/switch_root.8.gz
%{ulmandir}/man8/mkfs.bfs.8.gz
%{ulmandir}/man8/mkfs.minix.8.gz
%{ulmandir}/man8/findfs.8.gz
%{ulmandir}/man8/fsck.8.gz
%{ulmandir}/man8/fsck.cramfs.8.gz
%{ulmandir}/man8/fsck.minix.8.gz
%{ulmandir}/man8/isosize.8.gz
%{ulmandir}/man8/ldattach.8.gz
%{ulmandir}/man8/losetup.8.gz
%{ulmandir}/man8/lslocks.8.gz
%{ulmandir}/man8/lsns.8.gz
%{ulmandir}/man8/mkfs.8.gz
%{ulmandir}/man8/mkfs.cramfs.8.gz
%{ulmandir}/man8/mkswap.8.gz
%{ulmandir}/man8/mount.8.gz
%{ulmandir}/man8/nologin.8.gz
%{ulmandir}/man8/fsfreeze.8.gz
%{ulmandir}/man8/swaplabel.8.gz
%{ulmandir}/man8/readprofile.8.gz
%{ulmandir}/man8/rfkill.8.gz
%{ulmandir}/man8/chcpu.8.gz
%{ulmandir}/man8/partx.8.gz
%{ulmandir}/man8/pivot_root.8.gz
%{ulmandir}/man8/rtcwake.8.gz
%{ulmandir}/man8/setarch.8.gz
%{ulmandir}/man8/swapoff.8.gz
%{ulmandir}/man8/swapon.8.gz
%{ulmandir}/man8/umount.8.gz
%{ulmandir}/man8/uname26.8.gz
%{ulmandir}/man8/wipefs.8.gz
%{ulmandir}/man8/zramctl.8.gz
%{ulmandir}/man8/findmnt.8.gz
%{ulmandir}/man8/fstrim.8.gz
%{ulmandir}/man8/resizepart.8.gz
%{ulmandir}/man8/sulogin.8.gz
%{ulmandir}/man8/wdctl.8.gz
%{ulsbindir}/rcfstrim
%{_unitdir}/fstrim.service
%{_unitdir}/fstrim.timer
%endif
#
# Files not common for all architectures
%ifnarch ia64 m68k
%if %{ul_extra_bin_sbin}
/sbin/fdisk
%endif
%{ulsbindir}/fdisk
%{ulmandir}/man8/fdisk.8.gz
%endif
%ifnarch %sparc ia64 m68k
%{ulmandir}/man8/cfdisk.8.gz
%{ulmandir}/man8/sfdisk.8.gz
%if %{ul_extra_bin_sbin}
/sbin/cfdisk
/sbin/sfdisk
%endif
%{ulsbindir}/cfdisk
%{ulsbindir}/sfdisk
%endif
%ifnarch s390 s390x
%{ulsbindir}/fdformat
%if %{ul_extra_bin_sbin}
/sbin/hwclock
%endif
%{ulsbindir}/hwclock
%{ulbindir}/setterm
%{ulsbindir}/tunelp
%{ulmandir}/man8/fdformat.8.gz
%{ulmandir}/man8/hwclock.8.gz
%{ulmandir}/man8/tunelp.8.gz
%endif

%if "%ulsubset" == "core"
%files -n libblkid1
%defattr(-, root, root)
%{ullibdir}/libblkid.so.1
%{ullibdir}/libblkid.so.1.*

%files -n libfdisk1
%defattr(-, root, root)
%{ullibdir}/libfdisk.so.1
%{ullibdir}/libfdisk.so.1.*

%files -n libmount1
%defattr(-, root, root)
%{ullibdir}/libmount.so.1
%{ullibdir}/libmount.so.1.*

%files -n libsmartcols1
%defattr(-, root, root)
%{ullibdir}/libsmartcols.so.1
%{ullibdir}/libsmartcols.so.1.*

%files -n libuuid1
%defattr(-, root, root)
%{ullibdir}/libuuid.so.1
%{ullibdir}/libuuid.so.1.*

#
# devel, lang and uuidd files are not packaged in staging mode
# and packaged separately in full mode
# FIXME: Is it needed?
# HACK: We have to use "%%files -n" here, otherwise python lua code will
# issue an error, even if it is inside a false condition.
%if "%ulsubset" == "core"
%files -n %{name}-lang -f %{name}.lang
%endif

%files -n libblkid-devel
%defattr(-, root, root)
%{ullibdir}/libblkid.so
%dir %{ulincludedir}/blkid
%{ulincludedir}/blkid/blkid.h
%{ullibdir}/pkgconfig/blkid.pc
%{ulmandir}/man3/libblkid.3.gz

%files -n libblkid-devel-static
%defattr(-, root, root)
%{ullibdir}/libblkid.*a

%files -n libfdisk-devel
%defattr(-, root, root)
%{ullibdir}/libfdisk.so
%dir %{ulincludedir}/libfdisk
%{ulincludedir}/libfdisk/libfdisk.h
%{ullibdir}/pkgconfig/fdisk.pc

%files -n libfdisk-devel-static
%defattr(-, root, root)
%{ullibdir}/libfdisk.*a

%files -n libmount-devel
%defattr(-, root, root)
%{ullibdir}/libmount.so
%dir %{ulincludedir}/libmount
%{ulincludedir}/libmount/libmount.h
%{ullibdir}/pkgconfig/mount.pc

%files -n libmount-devel-static
%defattr(-, root, root)
%{ullibdir}/libmount.*a

%files -n libsmartcols-devel
%defattr(-, root, root)
%{ullibdir}/libsmartcols.so
%dir %{ulincludedir}/libsmartcols
%{ulincludedir}/libsmartcols/libsmartcols.h
%{ullibdir}/pkgconfig/smartcols.pc

%files -n libsmartcols-devel-static
%defattr(-, root, root)
%{ullibdir}/libsmartcols.*a

%files -n libuuid-devel
%defattr(-, root, root)
%{ullibdir}/libuuid.so
%dir %{ulincludedir}/uuid
%{ulincludedir}/uuid/uuid.h
%{ullibdir}/pkgconfig/uuid.pc
%{ulmandir}/man3/uuid*

%files -n libuuid-devel-static
%defattr(-, root, root)
%{ullibdir}/libuuid.*a
%endif

%if "%ulsubset" == "systemd"
%files -n uuidd
%defattr(-, root, root)
%{ulsbindir}/uuidd
%attr(-,uuidd,uuidd) %dir %{_sharedstatedir}/libuuid
%attr(-,uuidd,uuidd) %ghost %{_sharedstatedir}/libuuid/clock.txt
%attr(-,uuidd,uuidd) %ghost %dir /run/uuidd
%{uldatadir}/bash-completion/completions/uuidd
%{ulmandir}/man8/uuidd.8.gz
%{ulsbindir}/rcuuidd
%{_unitdir}/uuidd.service
%{_unitdir}/uuidd.socket
%endif
%endif

%if "%ulbuild" == "python"
%files %{python_files}
%defattr(-, root, root)
%{python_sitearch}/libmount
%endif

%changelog
