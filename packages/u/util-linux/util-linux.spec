#
# spec file for package util-linux
#
# Copyright (c) 2023 SUSE LLC
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

%if 0%{?suse_version} < 1550
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
	--prefix=%{_prefix}\
	--exec-prefix=%{_exec_prefix}\
	--disable-silent-rules\
	--bindir=%{_bindir}\
	--sbindir=%{_sbindir}\
	--sysconfdir=%{_sysconfdir}\
	--datadir=%{_datadir}\
	--includedir=%{_includedir}\
	--libdir=%{_libdir}\
	--libexecdir=%{_libexecdir}\
	--mandir=%{_mandir}\
	--infodir=%{_infodir}\
	--docdir=%{_docdir}/%{name}\
	--disable-makeinstall-chown\
	--disable-makeinstall-setuid\
	--with-audit\
	--with-btrfs\
	--with-gnu-ld\
	--with-ncursesw\
	--with-readline\
	--with-selinux\
	--with-utempter\
	--with-bashcompletiondir=%{_datadir}/bash-completion/completions\
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
	--with-vendordir=%{_distconfdir}
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
mkdir -p %{buildroot}{%{_distconfdir}/default,%{_pam_vendordir},%{_sysconfdir}/issue.d}
install -m 644 %{SOURCE51} %{buildroot}%{_sysconfdir}/blkid.conf
install -m 644 %{SOURCE8} %{buildroot}%{_pam_vendordir}/login
install -m 644 %{SOURCE9} %{buildroot}%{_pam_vendordir}/remote
install -m 644 %{SOURCE14} %{buildroot}%{_pam_vendordir}/runuser
install -m 644 %{SOURCE15} %{buildroot}%{_pam_vendordir}/runuser-l
install -m 644 %{SOURCE10} %{buildroot}%{_pam_vendordir}/su
install -m 644 %{SOURCE16} %{buildroot}%{_pam_vendordir}/su-l
install -m 644 %{SOURCE11} %{buildroot}%{_distconfdir}/default/su
sed 's/\bsu\b/runuser/g' <%{SOURCE11} >runuser.default
install -m 644 runuser.default %{buildroot}%{_distconfdir}/default/runuser
rm -fv "%{buildroot}/%{_sbindir}/raw" "%{buildroot}/sbin/raw" \
	"%{buildroot}/%{_mandir}/man8/raw.8"*
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/filesystems
echo -e "#!/bin/sh\n/sbin/blockdev --flushbufs \$1" > %{buildroot}%{_sbindir}/flushb
chmod 755 %{buildroot}%{_sbindir}/flushb
# arch dependent
%ifarch s390 s390x
rm -f %{buildroot}%{_sysconfdir}/fdprm
rm -f %{buildroot}%{_bindir}/setterm
rm -f %{buildroot}%{_sbindir}/fdformat
rm -f %{buildroot}%{_sbindir}/hwclock
rm -f %{buildroot}%{_sbindir}/tunelp
rm -f %{buildroot}%{_mandir}/man8/fdformat.8*
rm -f %{buildroot}%{_mandir}/man8/hwclock.8*
rm -f %{buildroot}%{_mandir}/man8/tunelp.8*
%endif
%ifarch ia64 %sparc m68k
rm -f %{buildroot}%{_mandir}/man8/cfdisk.8*
rm -f %{buildroot}%{_mandir}/man8/sfdisk.8*
rm -f %{buildroot}%{_sbindir}/cfdisk
rm -f %{buildroot}%{_sbindir}/sfdisk
%endif
%ifarch ia64 m68k
rm -f %{buildroot}%{_sbindir}/fdisk
rm -f %{buildroot}%{_mandir}/man8/fdisk.8*
%endif
# create list of setarch(8) symlinks
find  %{buildroot}%{_mandir}/man8 -regextype posix-egrep  \
  -regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64|parisc|parisc32|parisc64)\.8.*" \
  -printf "%{_mandir}/man8/%f*\n" >> %{name}.files
find  %{buildroot}%{_bindir}/ -regextype posix-egrep -type l \
  -regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64|parisc|parisc32|parisc64)$" \
  -printf "%{_bindir}/%f\n" >> %{name}.files
mkdir -p %{buildroot}/run/uuidd
%if "%ulsubset" == "systemd"
# clock.txt from uuidd is a ghost file
# FIXME: This could also be used by libuuid, but for now we only
# create it for uuidd. See boo#1206690.
mkdir -p %{buildroot}%{_sharedstatedir}/libuuid/
touch %{buildroot}%{_sharedstatedir}/libuuid/clock.txt
%endif
%if %{ul_extra_bin_sbin}
mkdir -p %{buildroot}{/bin,/sbin}
for i in dmesg findmnt kill logger lsblk more mount su umount; do
	if test -f "%{buildroot}%{_bindir}/$i" ; then
		ln -s "%{_bindir}/$i" "%{buildroot}/bin/"
	fi
done
for i in agetty blockdev cfdisk ctrlaltdel fdisk fsck.minix fsck.cramfs\
 hwclock losetup mkfs mkfs.bfs mkfs.minix mkfs.cramfs mkswap nologin\
 pivot_root raw sfdisk swapoff swapon blkid findfs fsck switch_root\
 wipefs fsfreeze swaplabel fstrim chcpu; do
	if test -f "%{buildroot}%{_sbindir}/$i" ; then
		ln -s "%{_sbindir}/$i" "%{buildroot}/sbin/"
	fi
done
# login is always and only in /bin
mv %{buildroot}%{_bindir}/login %{buildroot}/bin/
%endif
%if "%ulsubset" == "core"
%find_lang %{_name} %{name}.lang
%else
echo -n "" >%{name}.lang
ln -sf /sbin/service %{buildroot}%{_sbindir}/rcuuidd
ln -sf /sbin/service %{buildroot}%{_sbindir}/rcfstrim
%endif
%endif
%if "%ulbuild" == "python"
%{python_expand cd build.$python
%make_install
rm %{buildroot}%{$python_sitearch}/libmount/*.*a
cd ..
}
# There is a limitation: python module needs to build much more, and install even more. Delete it.
rm -r %{buildroot}{%{_bindir},%{_mandir},%{_datadir},%{_includedir},%{_libdir}/{lib,pkg}*}
%endif
# Link duplicate manpages or python bindings.
%fdupes -s %{buildroot}%{_prefix}

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
%verify_permissions -e %{_bindir}/wall -e %{_bindir}/write -e %{_bindir}/mount -e %{_bindir}/umount
%verify_permissions -e %{_bindir}/su

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
%set_permissions %{_bindir}/wall %{_bindir}/write %{_bindir}/mount %{_bindir}/umount
%set_permissions %{_bindir}/su
%if ! %{defined no_config}
#
# If outdated PAM file is detected, issue a warning.
for PAM_FILE in login remote runuser runuser-l su su-l ; do
	if test -f %{_pam_vendordir}/$PAM_FILE.rpmnew ; then
		echo "Your %{_pam_vendordir}/$PAM_FILE is outdated. Please check %{_pam_vendordir}/$PAM_FILE.rpmnew!" >&2
	fi
done
#
# /etc/default/su is tagged as noreplace.
# But we want to migrate variables to /etc/login.defs (bsc#1121197).
# Perform one-time config replace.
# Applies for: Update from SLE11, online update for SLE15 SP1, Leap15.1.
# Not needed for /etc/default/runuser. It was first packaged after the change.
if ! grep -q "^# /etc/default/su is an override" %{_sysconfdir}/default/su ; then
	if test -f %{_sysconfdir}/default/su.rpmnew ; then
		if ! test -f %{_sysconfdir}/default/su.rpmorig ; then
			cp -a %{_sysconfdir}/default/su %{_sysconfdir}/default/su.rpmorig
		fi
		mv %{_sysconfdir}/default/su.rpmnew %{_sysconfdir}/default/su
		echo "One time clean-up of %{_sysconfdir}/default/su was performed." >&2
		echo "Original contents was saved to %{_sysconfdir}/default/su.rpmorig." >&2
		echo "Please edit %{_sysconfdir}/login.defs or %{_sysconfdir}/default/su to restore your customization." >&2
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
%pre -n uuidd
%if 0%{?suse_version} < 1330
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
%config(noreplace) %{_sysconfdir}/filesystems
%config(noreplace) %{_sysconfdir}/blkid.conf
%endif
%if %{defined no_config}
%{_pam_vendordir}/login
%{_pam_vendordir}/remote
%{_pam_vendordir}/runuser
%{_pam_vendordir}/runuser-l
%{_pam_vendordir}/su
%{_pam_vendordir}/su-l
%if 0%{?suse_version} <= 1520
%dir %{_distconfdir}/default
%endif
%{_distconfdir}/default/runuser
%{_distconfdir}/default/su
%else
%config(noreplace) %{_pam_vendordir}/login
%config(noreplace) %{_pam_vendordir}/remote
%config(noreplace) %{_pam_vendordir}/runuser
%config(noreplace) %{_pam_vendordir}/runuser-l
%config(noreplace) %{_pam_vendordir}/su
%config(noreplace) %{_pam_vendordir}/su-l
%config(noreplace) %{_sysconfdir}/default/runuser
%config(noreplace) %{_sysconfdir}/default/su
%endif
%config %dir %{_sysconfdir}/issue.d
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
%{_bindir}/kill
%verify(not mode) %attr(%ul_suid,root,root) %{_bindir}/su
%{_bindir}/eject
%{_bindir}/cal
%{_bindir}/chmem
%{_bindir}/choom
%{_bindir}/chrt
%{_bindir}/col
%{_bindir}/colcrt
%{_bindir}/colrm
%{_bindir}/column
%{_bindir}/dmesg
%{_bindir}/fallocate
%{_bindir}/fincore
%if "%ulsubset" == "core"
%exclude %{_bindir}/findmnt
%exclude %{_bindir}/logger
%exclude %{_bindir}/lsblk
%exclude %{_bindir}/lslogins
%exclude %{_mandir}/man*/*
%endif
%{_bindir}/flock
%{_bindir}/getopt
%{_bindir}/hardlink
%{_bindir}/hexdump
%{_bindir}/ionice
%{_bindir}/ipcmk
%{_bindir}/ipcrm
%{_bindir}/ipcs
%{_bindir}/irqtop
%{_bindir}/isosize
%{_bindir}/last
%{_bindir}/lastb
%{_bindir}/line
%{_bindir}/look
%if !%{ul_extra_bin_sbin}
%{_bindir}/login
%endif
%{_bindir}/lscpu
%{_bindir}/lsfd
%{_bindir}/lsipc
%{_bindir}/lsirq
%{_bindir}/lslocks
%{_bindir}/lsmem
%{_bindir}/lsns
%{_bindir}/mcookie
%{_bindir}/mesg
%{_bindir}/more
%verify(not mode) %attr(%ul_suid,root,root) %{_bindir}/mount
%{_bindir}/namei
%{_bindir}/nsenter
%{_bindir}/prlimit
%{_bindir}/rename
%{_bindir}/renice
%{_bindir}/rev
%{_bindir}/script
%{_bindir}/scriptlive
%{_bindir}/scriptreplay
%{_bindir}/setarch
%{_bindir}/setpriv
%{_bindir}/setsid
%{_bindir}/taskset
%{_bindir}/uclampset
%{_bindir}/ul
%verify(not mode)%attr(%ul_suid,root,root)  %{_bindir}/umount
%{_bindir}/unshare
%{_bindir}/mountpoint
%{_bindir}/utmpdump
%{_bindir}/uuidgen
%{_bindir}/uuidparse
%{_bindir}/uname26
%{_bindir}/wdctl
%{_sbindir}/addpart
%{_sbindir}/agetty
%{_sbindir}/blkid
%{_sbindir}/blkdiscard
# blkzone depends on linux/blkzoned.h
%if 0%{?suse_version} >= 1330
%{_sbindir}/blkzone
%endif
%{_sbindir}/blockdev
%{_sbindir}/chcpu
%{_sbindir}/ctrlaltdel
%{_sbindir}/delpart
%{_sbindir}/findfs
%{_sbindir}/fsck
%{_sbindir}/fsck.minix
%{_sbindir}/fsck.cramfs
%{_sbindir}/fsfreeze
%{_sbindir}/fstrim
%{_sbindir}/ldattach
%{_sbindir}/losetup
%{_sbindir}/mkfs
%{_sbindir}/mkfs.bfs
%{_sbindir}/mkfs.minix
%{_sbindir}/mkfs.cramfs
%{_sbindir}/mkswap
%{_sbindir}/nologin
%{_sbindir}/partx
%{_sbindir}/pivot_root
%{_sbindir}/resizepart
%{_sbindir}/rfkill
%{_sbindir}/rtcwake
%{_sbindir}/runuser
%{_sbindir}/sulogin
%{_sbindir}/swaplabel
%{_sbindir}/swapoff
%{_sbindir}/swapon
%{_sbindir}/switch_root
%{_sbindir}/wipefs
%verify(not mode) %attr(0755,root,tty) %{_bindir}/wall
%{_bindir}/whereis
%verify(not mode) %attr(0755,root,tty) %{_bindir}/write
%{_sbindir}/zramctl
%{_sbindir}/flushb
%{_sbindir}/readprofile
# These directories should be owned by bash-completion. But we don't want to
# install them on build, so own these two directories:
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/*
#
%exclude %{_datadir}/bash-completion/completions/uuidd
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
%{_docdir}/%{name}/getopt-example.*
%exclude %{_sbindir}/uuidd
%endif
%if "%ulsubset" == "systemd"
%exclude %config(noreplace) %{_sysconfdir}/filesystems
%exclude %config(noreplace) %{_sysconfdir}/blkid.conf
%if %{defined no_config}
%exclude %{_pam_vendordir}/login
%exclude %{_pam_vendordir}/remote
%exclude %{_pam_vendordir}/runuser
%exclude %{_pam_vendordir}/runuser-l
%exclude %{_pam_vendordir}/su
%exclude %{_pam_vendordir}/su-l
%if 0%{?suse_version} <= 1520
%exclude %dir %{_distconfdir}/default
%endif
%exclude %{_distconfdir}/default/runuser
%exclude %{_distconfdir}/default/su
%else
%exclude %config(noreplace) %{_pam_vendordir}/login
%exclude %config(noreplace) %{_pam_vendordir}/remote
%exclude %config(noreplace) %{_pam_vendordir}/runuser
%exclude %config(noreplace) %{_pam_vendordir}/runuser-l
%exclude %config(noreplace) %{_pam_vendordir}/su
%exclude %config(noreplace) %{_pam_vendordir}/su-l
%exclude %config(noreplace) %{_sysconfdir}/default/runuser
%exclude %config(noreplace) %{_sysconfdir}/default/su
%endif
%exclude %config %dir %{_sysconfdir}/issue.d
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
%exclude %{_bindir}/kill
%exclude %verify(not mode) %attr(%ul_suid,root,root) %{_bindir}/su
%exclude %{_bindir}/eject
%exclude %{_bindir}/cal
%exclude %{_bindir}/chmem
%exclude %{_bindir}/choom
%exclude %{_bindir}/chrt
%exclude %{_bindir}/col
%exclude %{_bindir}/colcrt
%exclude %{_bindir}/colrm
%exclude %{_bindir}/column
%exclude %{_bindir}/dmesg
%exclude %{_bindir}/fallocate
%exclude %{_bindir}/fincore
%{_bindir}/findmnt
%exclude %{_bindir}/flock
%exclude %{_bindir}/getopt
%exclude %{_bindir}/hardlink
%exclude %{_bindir}/hexdump
%exclude %{_bindir}/ionice
%exclude %{_bindir}/ipcmk
%exclude %{_bindir}/ipcrm
%exclude %{_bindir}/ipcs
%exclude %{_bindir}/irqtop
%exclude %{_bindir}/isosize
%exclude %{_bindir}/last
%exclude %{_bindir}/lastb
%exclude %{_bindir}/line
%{_bindir}/logger
%exclude %{_bindir}/look
%if !%{ul_extra_bin_sbin}
%exclude %{_bindir}/login
%endif
%{_bindir}/lsblk
%exclude %{_bindir}/lscpu
%exclude %{_bindir}/lsfd
%exclude %{_bindir}/lsipc
%exclude %{_bindir}/lsirq
%{_bindir}/lslocks
%{_bindir}/lslogins
%exclude %{_bindir}/lsmem
%exclude %{_bindir}/lsns
%exclude %{_bindir}/mcookie
%exclude %{_bindir}/mesg
%exclude %{_bindir}/more
%exclude %verify(not mode) %attr(%ul_suid,root,root) %{_bindir}/mount
%exclude %{_bindir}/namei
%exclude %{_bindir}/nsenter
%exclude %{_bindir}/prlimit
%exclude %{_bindir}/rename
%exclude %{_bindir}/renice
%exclude %{_bindir}/rev
%exclude %{_bindir}/script
%exclude %{_bindir}/scriptlive
%exclude %{_bindir}/scriptreplay
%exclude %{_bindir}/setarch
%exclude %{_bindir}/setpriv
%exclude %{_bindir}/setsid
%exclude %{_bindir}/taskset
%exclude %{_bindir}/uclampset
%exclude %{_bindir}/ul
%exclude %verify(not mode)%attr(%ul_suid,root,root)  %{_bindir}/umount
%exclude %{_bindir}/unshare
%exclude %{_bindir}/mountpoint
%exclude %{_bindir}/utmpdump
%exclude %{_bindir}/uuidgen
%exclude %{_bindir}/uuidparse
%exclude %{_bindir}/uname26
%exclude %{_bindir}/wdctl
%exclude %{_sbindir}/addpart
%exclude %{_sbindir}/agetty
%exclude %{_sbindir}/blkid
%exclude %{_sbindir}/blkdiscard
# blkzone depends on linux/blkzoned.h
%if 0%{?suse_version} >= 1330
%exclude %{_sbindir}/blkzone
%endif
%exclude %{_sbindir}/blockdev
%exclude %{_sbindir}/chcpu
%exclude %{_sbindir}/ctrlaltdel
%exclude %{_sbindir}/delpart
%exclude %{_sbindir}/findfs
%exclude %{_sbindir}/fsck
%exclude %{_sbindir}/fsck.minix
%exclude %{_sbindir}/fsck.cramfs
%exclude %{_sbindir}/fsfreeze
%exclude %{_sbindir}/fstrim
%exclude %{_sbindir}/ldattach
%exclude %{_sbindir}/losetup
%exclude %{_sbindir}/mkfs
%exclude %{_sbindir}/mkfs.bfs
%exclude %{_sbindir}/mkfs.minix
%exclude %{_sbindir}/mkfs.cramfs
%exclude %{_sbindir}/mkswap
%exclude %{_sbindir}/nologin
%exclude %{_sbindir}/partx
%exclude %{_sbindir}/pivot_root
%exclude %{_sbindir}/resizepart
%exclude %{_sbindir}/rfkill
%exclude %{_sbindir}/rtcwake
%exclude %{_sbindir}/runuser
%exclude %{_sbindir}/sulogin
%exclude %{_sbindir}/swaplabel
%exclude %{_sbindir}/swapoff
%exclude %{_sbindir}/swapon
%exclude %{_sbindir}/switch_root
%exclude %{_sbindir}/wipefs
%verify(not mode) %attr(0755,root,tty) %{_bindir}/wall
%exclude %{_bindir}/whereis
%verify(not mode) %attr(0755,root,tty) %{_bindir}/write
%exclude %{_sbindir}/zramctl
%exclude %{_sbindir}/flushb
%exclude %{_sbindir}/readprofile
# These directories should be owned by bash-completion. But we don't want to
# install them on build, so own these two directories:
%exclude %dir %{_datadir}/bash-completion
%exclude %dir %{_datadir}/bash-completion/completions
%exclude %{_datadir}/bash-completion/completions/*
#
%exclude %{_sbindir}/uuidd
%exclude %{_datadir}/bash-completion/completions/uuidd
%exclude %{_datadir}/locale
%exclude %{_includedir}/*
%exclude %{_libdir}/lib*.*
%exclude %{_libdir}/pkgconfig/*.pc
%exclude %{_docdir}/%{name}/getopt-example.*
# packaged in core step
%exclude %{_mandir}/man3/libblkid.3.gz
%exclude %{_mandir}/man3/uuid.3.gz
%exclude %{_mandir}/man3/uuid_*.3.gz
%{_mandir}/man1/kill.1.gz
%{_mandir}/man1/su.1.gz
%{_mandir}/man1/cal.1.gz
%{_mandir}/man1/choom.1.gz
%{_mandir}/man1/chrt.1.gz
%{_mandir}/man1/col.1.gz
%{_mandir}/man1/colcrt.1.gz
%{_mandir}/man1/colrm.1.gz
%{_mandir}/man1/column.1.gz
%{_mandir}/man1/dmesg.1.gz
%{_mandir}/man1/eject.1.gz
%{_mandir}/man1/fallocate.1.gz
%{_mandir}/man1/fincore.1.gz
%{_mandir}/man1/flock.1.gz
%{_mandir}/man1/getopt.1.gz
%{_mandir}/man1/hardlink.1.gz
%{_mandir}/man1/hexdump.1.gz
%{_mandir}/man1/ipcrm.1.gz
%{_mandir}/man1/ipcs.1.gz
%{_mandir}/man1/last.1.gz
%{_mandir}/man1/lastb.1.gz
%{_mandir}/man1/line.1.gz
%{_mandir}/man1/login.1.gz
%{_mandir}/man1/look.1.gz
%{_mandir}/man1/logger.1.gz
%{_mandir}/man1/lscpu.1.gz
%{_mandir}/man1/lsfd.1.gz
%{_mandir}/man1/lsipc.1.gz
%{_mandir}/man1/lsirq.1.gz
%{_mandir}/man1/lslogins.1.gz
%{_mandir}/man8/lsblk.8.gz
%{_mandir}/man1/lsmem.1.gz
%{_mandir}/man1/mcookie.1.gz
%{_mandir}/man1/mesg.1.gz
%{_mandir}/man1/more.1.gz
%{_mandir}/man1/namei.1.gz
%{_mandir}/man1/nsenter.1.gz
%{_mandir}/man1/ionice.1.gz
%{_mandir}/man1/irqtop.1.gz
%{_mandir}/man1/prlimit.1.gz
%{_mandir}/man1/rename.1.gz
%{_mandir}/man1/rev.1.gz
%{_mandir}/man1/renice.1.gz
%{_mandir}/man1/setpriv.1.gz
%{_mandir}/man1/setsid.1.gz
%{_mandir}/man1/script.1.gz
%{_mandir}/man1/scriptlive.1.gz
%{_mandir}/man1/scriptreplay.1.gz
%{_mandir}/man1/setterm.1.gz
%{_mandir}/man1/taskset.1.gz
%{_mandir}/man1/ul.1.gz
%{_mandir}/man1/unshare.1.gz
%{_mandir}/man1/wall.1.gz
%{_mandir}/man1/whereis.1.gz
%{_mandir}/man1/write.1.gz
%{_mandir}/man1/ipcmk.1.gz
%{_mandir}/man1/mountpoint.1.gz
%{_mandir}/man1/runuser.1.gz
%{_mandir}/man1/uclampset.1.gz
%{_mandir}/man1/utmpdump.1.gz
%{_mandir}/man1/uuidgen.1.gz
%{_mandir}/man1/uuidparse.1.gz
%{_mandir}/man5/adjtime_config.5.gz
%{_mandir}/man5/fstab.5.gz
%{_mandir}/man5/terminal-colors.d.5.gz
%{_mandir}/man8/addpart.8.gz
%{_mandir}/man8/agetty.8.gz
%if 0%{?suse_version} >= 1330
%{_mandir}/man8/blkzone.8.gz
%endif
%{_mandir}/man8/blockdev.8.gz
%{_mandir}/man8/chmem.8.gz
%{_mandir}/man8/ctrlaltdel.8.gz
%{_mandir}/man8/delpart.8.gz
%{_mandir}/man8/blkid.8.gz
%{_mandir}/man8/blkdiscard.8.gz
%{_mandir}/man8/switch_root.8.gz
%{_mandir}/man8/mkfs.bfs.8.gz
%{_mandir}/man8/mkfs.minix.8.gz
%{_mandir}/man8/findfs.8.gz
%{_mandir}/man8/fsck.8.gz
%{_mandir}/man8/fsck.cramfs.8.gz
%{_mandir}/man8/fsck.minix.8.gz
%{_mandir}/man8/isosize.8.gz
%{_mandir}/man8/ldattach.8.gz
%{_mandir}/man8/losetup.8.gz
%{_mandir}/man8/lslocks.8.gz
%{_mandir}/man8/lsns.8.gz
%{_mandir}/man8/mkfs.8.gz
%{_mandir}/man8/mkfs.cramfs.8.gz
%{_mandir}/man8/mkswap.8.gz
%{_mandir}/man8/mount.8.gz
%{_mandir}/man8/nologin.8.gz
%{_mandir}/man8/fsfreeze.8.gz
%{_mandir}/man8/swaplabel.8.gz
%{_mandir}/man8/readprofile.8.gz
%{_mandir}/man8/rfkill.8.gz
%{_mandir}/man8/chcpu.8.gz
%{_mandir}/man8/partx.8.gz
%{_mandir}/man8/pivot_root.8.gz
%{_mandir}/man8/rtcwake.8.gz
%{_mandir}/man8/setarch.8.gz
%{_mandir}/man8/swapoff.8.gz
%{_mandir}/man8/swapon.8.gz
%{_mandir}/man8/umount.8.gz
%{_mandir}/man8/uname26.8.gz
%{_mandir}/man8/wipefs.8.gz
%{_mandir}/man8/zramctl.8.gz
%{_mandir}/man8/findmnt.8.gz
%{_mandir}/man8/fstrim.8.gz
%{_mandir}/man8/resizepart.8.gz
%{_mandir}/man8/sulogin.8.gz
%{_mandir}/man8/wdctl.8.gz
%{_sbindir}/rcfstrim
%{_unitdir}/fstrim.service
%{_unitdir}/fstrim.timer
%endif
#
# Files not common for all architectures
%ifnarch ia64 m68k
%if %{ul_extra_bin_sbin}
/sbin/fdisk
%endif
%{_sbindir}/fdisk
%{_mandir}/man8/fdisk.8.gz
%endif
%ifnarch %sparc ia64 m68k
%{_mandir}/man8/cfdisk.8.gz
%{_mandir}/man8/sfdisk.8.gz
%if %{ul_extra_bin_sbin}
/sbin/cfdisk
/sbin/sfdisk
%endif
%{_sbindir}/cfdisk
%{_sbindir}/sfdisk
%endif
%ifnarch s390 s390x
%{_sbindir}/fdformat
%if %{ul_extra_bin_sbin}
/sbin/hwclock
%endif
%{_sbindir}/hwclock
%{_bindir}/setterm
%{_sbindir}/tunelp
%{_mandir}/man8/fdformat.8.gz
%{_mandir}/man8/hwclock.8.gz
%{_mandir}/man8/tunelp.8.gz
%endif

%if "%ulsubset" == "core"
%files -n libblkid1
%{_libdir}/libblkid.so.1
%{_libdir}/libblkid.so.1.*

%files -n libfdisk1
%{_libdir}/libfdisk.so.1
%{_libdir}/libfdisk.so.1.*

%files -n libmount1
%{_libdir}/libmount.so.1
%{_libdir}/libmount.so.1.*

%files -n libsmartcols1
%{_libdir}/libsmartcols.so.1
%{_libdir}/libsmartcols.so.1.*

%files -n libuuid1
%{_libdir}/libuuid.so.1
%{_libdir}/libuuid.so.1.*

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
%{_libdir}/libblkid.so
%dir %{_includedir}/blkid
%{_includedir}/blkid/blkid.h
%{_libdir}/pkgconfig/blkid.pc
%{_mandir}/man3/libblkid.3.gz

%files -n libblkid-devel-static
%{_libdir}/libblkid.*a

%files -n libfdisk-devel
%{_libdir}/libfdisk.so
%dir %{_includedir}/libfdisk
%{_includedir}/libfdisk/libfdisk.h
%{_libdir}/pkgconfig/fdisk.pc

%files -n libfdisk-devel-static
%{_libdir}/libfdisk.*a

%files -n libmount-devel
%{_libdir}/libmount.so
%dir %{_includedir}/libmount
%{_includedir}/libmount/libmount.h
%{_libdir}/pkgconfig/mount.pc

%files -n libmount-devel-static
%{_libdir}/libmount.*a

%files -n libsmartcols-devel
%{_libdir}/libsmartcols.so
%dir %{_includedir}/libsmartcols
%{_includedir}/libsmartcols/libsmartcols.h
%{_libdir}/pkgconfig/smartcols.pc

%files -n libsmartcols-devel-static
%{_libdir}/libsmartcols.*a

%files -n libuuid-devel
%{_libdir}/libuuid.so
%dir %{_includedir}/uuid
%{_includedir}/uuid/uuid.h
%{_libdir}/pkgconfig/uuid.pc
%{_mandir}/man3/uuid*

%files -n libuuid-devel-static
%{_libdir}/libuuid.*a
%endif

%if "%ulsubset" == "systemd"
%files -n uuidd
%{_sbindir}/uuidd
%attr(-,uuidd,uuidd) %dir %{_sharedstatedir}/libuuid
%attr(-,uuidd,uuidd) %ghost %{_sharedstatedir}/libuuid/clock.txt
%attr(-,uuidd,uuidd) %ghost %dir /run/uuidd
%{_datadir}/bash-completion/completions/uuidd
%{_mandir}/man8/uuidd.8.gz
%{_sbindir}/rcuuidd
%{_unitdir}/uuidd.service
%{_unitdir}/uuidd.socket
%endif
%endif

%if "%ulbuild" == "python"
%files %{python_files}
%{python_sitearch}/libmount
%endif

%changelog
