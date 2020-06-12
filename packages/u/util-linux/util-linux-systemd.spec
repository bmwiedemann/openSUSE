#
# spec file for package util-linux-systemd
#
# Copyright (c) 2020 SUSE LLC
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


%if 0%{?suse_version} >= 1330
%bcond_without  enable_last
%else
%bcond_with     enable_last
%endif

%if ! %{defined _distconfdir}
%define _distconfdir %{_sysconfdir}
%else
%define no_config 1
%endif

Name:           util-linux-systemd
%define _name   util-linux
# WARNING: Never edit this file!!! Edit util-linux.spec and call pre_checkin.sh to update spec files:
%define _name util-linux
# To prevent dependency loop in automatic build systems, we want to
# build util-linux in parts.  To build all at once, set build_all to 1.
#
# build_util_linux: First stage build builds all except:
# build_util_linux_systemd: Builds util-linux-systemd and uuidd.
# build_python_libmount: Builds python-libmount.
%define build_all 0
# definitions for the main packages
# This two level indirect definition of Summary and Group is needed to
# simplify parsing of spec file by format_spec_file,
# source_validator and check-in QA scripts).
%define         summary_ul  A collection of basic system utilities
%define         summary_uls A collection of basic system utilities
%define         summary_pl  Python bindings for the libmount library
%define         group_ul    System/Base
%define         group_uls   System/Base
%define         group_pl    Development/Languages/Python
%if "%{name}" == "python3-libmount"
%define         build_util_linux 0
%define         build_util_linux_systemd 0
%define         build_python_libmount 1
# To prevent dependency loops, verify signature only in third stage.
%define         main_summary %summary_pl
%define         main_group   %group_pl
%else
%if "%{name}" == "util-linux-systemd"
%define         build_util_linux 0
%define         build_util_linux_systemd 1
%define         build_python_libmount 0
%define         main_summary %summary_uls
%define         main_group   %group_uls
%else
%define         main_summary %summary_ul
%define         main_group   %group_ul
%if %build_all
%define         build_util_linux 1
%define         build_util_linux_systemd 1
%define         build_python_libmount 1
%else
%define         build_util_linux 1
%define         build_util_linux_systemd 0
%define         build_python_libmount 0
%endif
%endif
%endif
Summary:        %main_summary
License:        GPL-2.0-or-later
Group:          %main_group
BuildRequires:  audit-devel
BuildRequires:  binutils-devel
BuildRequires:  fdupes
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
%if %build_util_linux_systemd
BuildRequires:  socat
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
%endif
%if %build_python_libmount
BuildRequires:  python3-devel
%endif
#BEGIN SECOND STAGE DEPENDENCIES
%if !%build_util_linux
%if %build_util_linux_systemd
BuildRequires:  libblkid-devel
BuildRequires:  libmount-devel
BuildRequires:  libsmartcols-devel
BuildRequires:  libuuid-devel
%endif
%if %build_python_libmount
BuildRequires:  libmount-devel
%endif
%endif
#END SECOND STAGE DEPENDENCIES
Version:        2.35.1
Release:        0
URL:            https://www.kernel.org/pub/linux/utils/util-linux/
Source:         https://www.kernel.org/pub/linux/utils/util-linux/v2.35/util-linux-%{version}.tar.xz
Source1:        util-linux-rpmlintrc
Source2:        util-linux-login_defs-check.sh
Source4:        raw.service
Source5:        etc.raw
Source6:        etc_filesystems
Source7:        baselibs.conf
Source8:        login.pamd
Source9:        remote.pamd
Source10:       su.pamd
Source11:       su.default
Source12:       https://www.kernel.org/pub/linux/utils/util-linux/v2.35/util-linux-%{version}.tar.sign
Source13:       %{_name}.keyring
Source14:       runuser.pamd
Source15:       runuser-l.pamd
Source16:       su-l.pamd
Source51:       blkid.conf
# PATCH-EXTEND-UPSTREAM: Let `su' handle /sbin and /usr/sbin in path
Patch0:         make-sure-sbin-resp-usr-sbin-are-in-PATH.diff
Patch1:         libmount-print-a-blacklist-hint-for-unknown-filesyst.patch
Patch2:         Add-documentation-on-blacklisted-modules-to-mount-8-.patch
Patch3:         libeconf.patch
Patch4:         libmount-Avoid-triggering-autofs-in-lookup_umount_fs.patch
Patch5:         libfdisk-script-accept-sector-size.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#
%if %build_util_linux
Supplements:    filesystem(minix)
%if 0%{?suse_version} >= 1330
Requires(pre):  group(tty)
%endif
Provides:       fsck-with-dev-lock = %{version}
# bnc#651598:
Provides:       util-linux(fake+no-canonicalize)
PreReq:         %install_info_prereq permissions
Provides:       eject = 2.1.0
Provides:       login = 4.0
Provides:       rfkill = 0.5
# File conflict of eject (up to 12.3 and SLE11).
Obsoletes:      eject <= 2.1.0
# File conflict of login (up to 12.1 and SLE11).
Obsoletes:      login <= 4.0
# File conflict (man page) of rfkill (up to Leap 15 and SLE 15).
Obsoletes:      rfkill <= 0.5
# util-linux-2.34 integrates hardlink (up to Leap 15.1 and SLE 15.1).
# The last version was 1.0+git.e66999f.
Provides:       hardlink = 1.1
Obsoletes:      hardlink < 1.1
# bnc#805684:
%ifarch s390x
Obsoletes:      s390-32
Provides:       s390-32
%endif
# uuid-runtime appeared in SLE11 SP1 to SLE11 SP3
Provides:       uuid-runtime = %{version}-%{release}
Obsoletes:      uuid-runtime <= 2.19.1
# All login.defs variables require support from shadow side.
# Upgrade this symbol version only if new variables appear!
# Verify by shadow-login_defs-check.sh from shadow source package.
Requires:       login_defs-support-for-util-linux >= 2.33.1
#
# Using "Requires" here would lend itself to help upgrading, but since
# util-linux is in the initial bootstrap, that is not a good thing to do:
#
Recommends:     adjtimex
Recommends:     time
Recommends:     which
#
%else
%if %build_python_libmount
%else
%if %build_util_linux_systemd
Supplements:    packageand(util-linux:systemd)
# Split-provides for upgrade from SLE < 12 and openSUSE <= 13.1
Provides:       util-linux:/bin/logger
# Service files are being migrated during the update from SLE < 12 and openSUSE <= 13.1
Conflicts:      util-linux < 2.25
%systemd_requires
%else
# ERROR: No build_* variables are set.
%endif
%endif
%endif

%if %build_util_linux
%description
This package contains a large variety of low-level system utilities
that are necessary for a Linux system to function. It contains the
mount program, the fdisk configuration tool, and more.

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

%package -n libuuid1
Summary:        Library to generate UUIDs
License:        BSD-3-Clause
Group:          System/Libraries

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

%lang_package
%endif
%if %build_util_linux_systemd
%if %build_util_linux
%package systemd
Summary:        %summary_uls
License:        GPL-2.0-or-later
Group:          %group_uls
Supplements:    packageand(util-linux:systemd)
# Split-provides for upgrade from SLE < 12 and openSUSE <= 13.1
Provides:       util-linux:/usr/lib/systemd/system/fstrim.service
# Service files are being migrated during the update from SLE < 12 and openSUSE <= 13.1
Conflicts:      util-linux < 2.25

%description systemd
%else
%description
%endif
This package contains low-level util-linux utilities that use systemd.

%package -n uuidd
Summary:        Helper daemon to guarantee uniqueness of time-based UUIDs
License:        GPL-2.0-or-later
Group:          System/Filesystems
%if 0%{?suse_version} >= 1330
Requires(pre):  group(uuidd)
%else
Requires(pre):  /usr/sbin/groupadd
Requires(pre):  /usr/sbin/useradd
%endif
# uuidd bash-completion moved to a correct package
Conflicts:      util-linux < 2.25
%systemd_requires

%description -n uuidd
The uuidd package contains a userspace daemon (uuidd) which guarantees
uniqueness of time-based UUID generation even at very high rates on
SMP systems.

%endif
%if %build_python_libmount
%if %build_util_linux
%package -n python3-libmount
Summary:        %summary_pl
License:        GPL-2.0-or-later
Group:          %group_pl

%description -n python3-libmount
%else
%description
%endif
This package contains the Python bindings for util-linux libmount
library.

%endif
%prep
%setup -q -n %{_name}-%{version}
cp -a %{S:2} .
%autopatch -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
bash ./util-linux-login_defs-check.sh
%if %build_util_linux
#BEGIN SYSTEMD SAFETY CHECK
# With systemd, some utilities are built differently. Keep track of these
# sources to prevent building of systemd-less versions.
#
# WARNING: Never edit following line without doing all suggested in the echo below!
UTIL_LINUX_KNOWN_SYSTEMD_DEPS='./login-utils/lslogins.c ./misc-utils/logger.c ./misc-utils/uuidd.c '
UTIL_LINUX_FOUND_SYSTEMD_DEPS=$(grep -rl 'HAVE_LIBSYSTEMD' . | fgrep '.c' | LC_ALL=C sort | tr '\n' ' ')
if test "$UTIL_LINUX_KNOWN_SYSTEMD_DEPS" != "$UTIL_LINUX_FOUND_SYSTEMD_DEPS" ; then
	echo "List of utilities depending on systemd have changed.
Please check the new util-linux-systemd file list, file removal and update of Conflicts for safe update!
Then update configure options to build what needed.
Only then you can safely update following spec file line:
UTIL_LINUX_KNOWN_SYSTEMD_DEPS='$UTIL_LINUX_FOUND_SYSTEMD_DEPS'"
	exit 1
fi
#END SYSTEMD SAFETY CHECK
%else
#BEGIN SECOND STAGE MODIFICATIONS
# delete all make modules except wanted ones
sed -i '/^include/{
%if %build_python_libmount
		/libmount\/Makemodule.am/b 1
%endif
%if %build_util_linux_systemd
# for lslogins
		/login-utils/b 1
# for logger and uuidd
		/misc-utils/b 1
# for fstrim.service and fstrim.timer
		/sys-utils/b 1
# for uninstalled libcommon required by uuidd
		/ lib\//b 1
# for bash completions
		/bash-completion/b 1
# we always want tests (they are smart enough to skip irrelevant parts)
		/tests/b 1
%endif
%if %build_python_libmount
		/libmount\/python/b 1
%endif
		d
		:1
		}' Makefile.am libmount/Makemodule.am
%if %build_python_libmount
# trick: we do not want to build libmount, but include subdirs
# We close prefious if FALSE and open new pairing with endif
sed -i '/^if BUILD_LIBMOUNT/d
/^if ENABLE_GTK_DOC/i \
if BUILD_LIBMOUNT
' libmount/Makemodule.am
# Do not install terminal-colors.d.5
sed -i '/dist_man_MANS/d' lib/Makemodule.am
%endif
# disable all make modules except wanted ones
sed -i '/^if BUILD_/{
%if %build_util_linux_systemd
		/LSLOGINS/b 1
		/LOGGER/b 1
		/UUIDD/b 1
		/BASH_COMPLETION/b 1
%endif
		s/BUILD_.*/FALSE/
	:1
	}
	' libmount/Makemodule.am misc-utils/Makemodule.am login-utils/Makemodule.am sys-utils/Makemodule.am bash-completion/Makemodule.am
%if %build_util_linux_systemd
# trick: we do not want to build fstrim, but we want to install fstrim systemd connectors
# We close prefious if FALSE and open new pairing with endif
sed -i '/^if HAVE_SYSTEMD/i \
endif\
if TRUE
' sys-utils/Makemodule.am
# Do not install terminal-colors.d.5
sed -i '/dist_man_MANS/d' lib/Makemodule.am
%endif
# Use installed first stage libraries
sed -i '
# extra space to not replace pylibmount.la
	s/ libmount\.la/ -lmount/g
	s/libuuid\.la/-luuid/g
	s/libblkid\.la/-lblkid/g
	s/libsmartcols\.la/-lsmartcols/g
	' libmount/python/Makemodule.am misc-utils/Makemodule.am login-utils/Makemodule.am tests/helpers/Makemodule.am
# Ignore dependencies on optional (and not built in second stage) libraries
sed -i '
	s/UL_REQUIRES_BUILD(\[.*\], \[libuuid\])/dnl &/
	s/UL_REQUIRES_BUILD(\[.*\], \[libsmartcols\])/dnl &/
	' configure.ac
sed -i '
	/SUBDIRS =/s/ po//
	' Makefile.am
#END SECOND STAGE MODIFICATIONS
%endif
#
# util-linux itself
#
# Version check for libutempter
#
uhead=$(find %_includedir -name utempter.h 2>/dev/null)
if test -n "$uhead" && grep -q utempter_add_record "$uhead"
then
    uhead=--with-utempter
else
    uhead=--without-utempter
fi
export SUID_CFLAGS="-fpie"
export SUID_LDFLAGS="-pie"
export LDFLAGS="-Wl,-z,relro,-z,now"
export CFLAGS="%{optflags} -D_GNU_SOURCE"
export CXXFLAGS="%{optflags} -D_GNU_SOURCE"
#
# SUSE now supports only systemd based system. We do not build
# sysvinit-only versions of UTIL_LINUX_SYSTEMD_SOURCES utilities.
AUTOPOINT=true autoreconf -vfi
%configure \
  --disable-silent-rules \
  --docdir=%{_docdir}/%{_name} \
  --disable-makeinstall-chown \
  --disable-makeinstall-setuid \
  --with-audit \
  --with-btrfs \
  --with-gnu-ld \
  --with-ncursesw \
  --with-readline \
  --with-selinux \
  $uhead \
  --with-bashcompletiondir=%{_datadir}/bash-completion/completions \
  --with-systemdsystemunitdir=%{_unitdir} \
  --enable-libuuid-force-uuidd \
  --enable-sulogin-emergency-mount \
  --disable-use-tty-group \
  --enable-static \
  --disable-rpath \
  --enable-all-programs \
  --disable-reset \
  --disable-chfn-chsh \
  --disable-newgrp \
  --disable-vipw \
  --disable-pg \
%if %{without enable_last}
  --disable-last \
%endif
%if %build_util_linux_systemd
  --with-systemd \
  --enable-logger \
  --enable-lslogins \
  --enable-uuidd \
%else
  --without-systemd \
  --disable-logger \
  --disable-lslogins \
  --disable-uuidd \
%endif
%if %build_python_libmount
  --with-python \
%else
  --without-python \
%endif
  --enable-vendordir=%{_distconfdir}

#
# Safety check: HAVE_UUIDD should be always 1:
grep -q 'HAVE_UUIDD 1' config.h
make %{?_smp_mflags}

%check
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

%install
%if %build_util_linux
mkdir -p %{buildroot}{%{_distconfdir}/{pam.d,default},%{_mandir}/man{1,8},/bin,/sbin,%{_bindir},%{_sbindir},%{_infodir},%{_sysconfdir}/issue.d}
install -m 644 %{SOURCE51} %{buildroot}%{_sysconfdir}/blkid.conf
install -m 644 %{SOURCE8} %{buildroot}%{_distconfdir}/pam.d/login
install -m 644 %{SOURCE9} %{buildroot}%{_distconfdir}/pam.d/remote
install -m 644 %{SOURCE14} %{buildroot}%{_distconfdir}/pam.d/runuser
install -m 644 %{SOURCE15} %{buildroot}%{_distconfdir}/pam.d/runuser-l
install -m 644 %{SOURCE10} %{buildroot}%{_distconfdir}/pam.d/su
install -m 644 %{SOURCE16} %{buildroot}%{_distconfdir}/pam.d/su-l
install -m 644 %{SOURCE11} %{buildroot}%{_distconfdir}/default/su
sed 's/\bsu\b/runuser/g' <%{SOURCE11} >runuser.default
install -m 644 runuser.default %{buildroot}%{_distconfdir}/default/runuser
%endif
#
# util-linux install
#
%make_install
rm -f %{buildroot}%{python3_sitearch}/libmount/*.*a
%if %build_util_linux
#UsrMerge
ln -s %{_bindir}/kill %{buildroot}/bin
ln -s %{_bindir}/su %{buildroot}/bin
ln -s %{_bindir}/dmesg %{buildroot}/bin
ln -s %{_bindir}/more %{buildroot}/bin
ln -s %{_bindir}/mount %{buildroot}/bin
ln -s %{_bindir}/umount %{buildroot}/bin
ln -s %{_bindir}/findmnt %{buildroot}/bin
ln -s %{_bindir}/lsblk %{buildroot}/bin
ln -s %{_sbindir}/agetty %{buildroot}/sbin
ln -s %{_sbindir}/blockdev %{buildroot}/sbin
ln -s %{_sbindir}/cfdisk %{buildroot}/sbin
ln -s %{_sbindir}/ctrlaltdel %{buildroot}/sbin
ln -s %{_sbindir}/fdisk %{buildroot}/sbin
ln -s %{_sbindir}/fsck.minix %{buildroot}/sbin
ln -s %{_sbindir}/fsck.cramfs %{buildroot}/sbin
ln -s %{_sbindir}/hwclock %{buildroot}/sbin
ln -s %{_sbindir}/losetup %{buildroot}/sbin
ln -s %{_sbindir}/mkfs %{buildroot}/sbin
ln -s %{_sbindir}/mkfs.bfs %{buildroot}/sbin
ln -s %{_sbindir}/mkfs.minix %{buildroot}/sbin
ln -s %{_sbindir}/mkfs.cramfs %{buildroot}/sbin
ln -s %{_sbindir}/mkswap %{buildroot}/sbin
ln -s %{_sbindir}/nologin %{buildroot}/sbin
ln -s %{_sbindir}/pivot_root %{buildroot}/sbin
ln -s %{_sbindir}/raw %{buildroot}/sbin
ln -s %{_sbindir}/sfdisk %{buildroot}/sbin
ln -s %{_sbindir}/swapoff %{buildroot}/sbin
ln -s %{_sbindir}/swapon %{buildroot}/sbin
ln -s %{_sbindir}/blkid %{buildroot}/sbin
ln -s %{_sbindir}/findfs %{buildroot}/sbin
ln -s %{_sbindir}/fsck %{buildroot}/sbin
ln -s %{_sbindir}/switch_root %{buildroot}/sbin
ln -s %{_sbindir}/wipefs %{buildroot}/sbin
ln -s %{_sbindir}/fsfreeze %{buildroot}/sbin
ln -s %{_sbindir}/swaplabel %{buildroot}/sbin
ln -s %{_sbindir}/fstrim %{buildroot}/sbin
ln -s %{_sbindir}/chcpu %{buildroot}/sbin
#EndUsrMerge
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/filesystems
echo -e "#! /bin/bash\n/sbin/blockdev --flushbufs \$1" > %{buildroot}%{_sbindir}/flushb
chmod 755 %{buildroot}%{_sbindir}/flushb
# Install scripts to configure raw devices at boot time
install -m 644 $RPM_SOURCE_DIR%{_sysconfdir}.raw   %{buildroot}%{_sysconfdir}/raw
install -m 644 $RPM_SOURCE_DIR/raw.service %{buildroot}%{_unitdir}
ln -sf service %{buildroot}%{_sbindir}/rcraw
# upstream moved getopt examples from datadir to docdir but we keep
# the old location because we would need to fix the manpage first
mv %{buildroot}%{_docdir}/%{_name}/getopt %{buildroot}%{_datadir}/
# Stupid hack so we don't have a tcsh dependency
chmod 644 %{buildroot}%{_datadir}/getopt/getopt*.tcsh
# login is always and only in /bin
mv %{buildroot}%{_bindir}/login %{buildroot}/bin/
# arch dependent
%ifarch s390 s390x
rm -f %{buildroot}%{_sysconfdir}/fdprm
rm -f %{buildroot}%{_sbindir}/fdformat
rm -f %{buildroot}%{_sbindir}/hwclock
#UsrMerge
rm -f %{buildroot}/sbin/hwclock
#EndUsrMerge
rm -f %{buildroot}%{_bindir}/setterm
rm -f %{buildroot}%{_sbindir}/tunelp
rm -f %{buildroot}%{_mandir}/man8/fdformat.8*
rm -f %{buildroot}%{_mandir}/man8/hwclock.8*
rm -f %{buildroot}%{_mandir}/man8/tunelp.8*
%endif
%ifarch ia64 %sparc m68k
rm -f %{buildroot}%{_mandir}/man8/cfdisk.8*
rm -f %{buildroot}%{_mandir}/man8/sfdisk.8*
rm -f %{buildroot}%{_sbindir}/cfdisk
#UsrMerge
rm -f %{buildroot}/sbin/cfdisk
#EndUsrMerge
rm -f %{buildroot}%{_sbindir}/sfdisk
#UsrMerge
rm -f %{buildroot}/sbin/sfdisk
#EndUsrMerge
%endif
%ifarch ia64 m68k
rm -f %{buildroot}%{_sbindir}/fdisk
#UsrMerge
rm -f %{buildroot}/sbin/fdisk
#EndUsrMerge
rm -f %{buildroot}%{_mandir}/man8/fdisk.8*
%endif
%find_lang %{name} %{name}.lang
# create list of setarch(8) symlinks
find  %{buildroot}%{_bindir}/ -regextype posix-egrep -type l \
  -regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64|parisc|parisc32|parisc64)$" \
  -printf "%{_bindir}/%f\n" >> %{name}.files
find  %{buildroot}%{_mandir}/man8 -regextype posix-egrep  \
  -regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64|parisc|parisc32|parisc64)\.8.*" \
  -printf "%{_mandir}/man8/%f*\n" >> %{name}.files
%else
# install systemd files manually, don't use Makefile that expect build of utilities and its dependencies.
%endif
%if %build_util_linux_systemd
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_localstatedir}/lib/libuuid
mkdir -p %{buildroot}/run/uuidd
ln -s %{_bindir}/logger %{buildroot}/bin
# clock.txt from uuidd is a ghost file
touch %{buildroot}%{_localstatedir}/lib/libuuid/clock.txt
ln -sf /sbin/service %{buildroot}/usr/sbin/rcuuidd
ln -sf /sbin/service %{buildroot}/usr/sbin/rcfstrim
%if !%build_util_linux
%make_install
%endif
%endif
# link duplicate manpages and python bindings
%fdupes -s %{buildroot}%{_prefix}

%if %build_util_linux
%pre
%service_add_pre raw.service
# move outdated pam.d/*.rpmsave files away
for i in login remote runuser runuser-l su su-l ; do
    test -f /etc/pam.d/${i}.rpmsave && mv -v /etc/pam.d/${i}.rpmsave /etc/pam.d/${i}.rpmsave.old ||:
done

%post
%service_add_post raw.service
%set_permissions %{_bindir}/wall %{_bindir}/write %{_bindir}/mount %{_bindir}/umount
%set_permissions %{_bindir}/su
#
# If outdated PAM file is detected, issue a warning.
for PAM_FILE in login remote runuser runuser-l su su-l ; do
	if test -f %{_sysconfdir}/pam.d/$PAM_FILE.rpmnew ; then
		echo "Your %{_sysconfdir}/pam.d/$PAM_FILE is outdated. Please check %{_sysconfdir}/pam.d/$PAM_FILE.rpmnew!" >&2
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

%posttrans
# Migration to /usr/etc.
for i in  login remote runuser runuser-l su su-l; do
  test -f /etc/pam.d/${i}.rpmsave && mv -v /etc/pam.d/${i}.rpmsave /etc/pam.d/${i} ||:
done

%preun
%service_del_preun raw.service

%postun
%service_del_postun raw.service

%verifyscript
%verify_permissions -e %{_bindir}/wall -e %{_bindir}/write -e %{_bindir}/mount -e %{_bindir}/umount
%verify_permissions -e %{_bindir}/su

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

%files lang -f %{name}.lang
%endif

%if %build_util_linux_systemd
# fstrim(8) and fstrim.service are from different packages. But it's a oneshot
# service (timer), no restart needed on binary updates (unless path is changed).
%pre -n util-linux-systemd
%service_add_pre fstrim.service fstrim.timer

%post -n util-linux-systemd
%service_add_post fstrim.service fstrim.timer

%preun -n util-linux-systemd
%service_del_preun fstrim.service fstrim.timer

%postun -n util-linux-systemd
%service_del_postun fstrim.service fstrim.timer

%if 0%{?suse_version} >= 1330
%pre -n uuidd
%else
%pre -n uuidd
getent group uuidd >/dev/null || /usr/sbin/groupadd -r uuidd
getent passwd uuidd >/dev/null || \
	/usr/sbin/useradd -r -g uuidd -c "User for uuidd" \
	-d /var/run/uuidd uuidd
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

%if %build_util_linux
%files -f %{name}.files
# Common files for all archs
%defattr(-,root,root)
# util-linux documentation files
%doc AUTHORS ChangeLog README NEWS
%license README.licensing
%license COPYING
%license Documentation/licenses/*
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
%{_unitdir}/raw.service
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/raw
%config(noreplace) %{_sysconfdir}/filesystems
%config(noreplace) %{_sysconfdir}/blkid.conf
%if %{defined no_config}
%{_distconfdir}/pam.d/login
%{_distconfdir}/pam.d/remote
%{_distconfdir}/pam.d/runuser
%{_distconfdir}/pam.d/runuser-l
%{_distconfdir}/pam.d/su
%{_distconfdir}/pam.d/su-l
%{_distconfdir}/default
%{_distconfdir}/default/runuser
%{_distconfdir}/default/su
%else
%config(noreplace) %{_sysconfdir}/pam.d/login
%config(noreplace) %{_sysconfdir}/pam.d/remote
%config(noreplace) %{_sysconfdir}/pam.d/runuser
%config(noreplace) %{_sysconfdir}/pam.d/runuser-l
%config(noreplace) %{_sysconfdir}/pam.d/su
%config(noreplace) %{_sysconfdir}/pam.d/su-l
%config(noreplace) %{_sysconfdir}/default/runuser
%config(noreplace) %{_sysconfdir}/default/su
%endif
%config %dir %{_sysconfdir}/issue.d
#UsrMerge
/bin/kill
/bin/su
/bin/dmesg
/bin/more
/bin/mount
/bin/umount
/bin/findmnt
/bin/login
/bin/lsblk
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
/sbin/raw
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
#EndUsrMerge
%{_bindir}/kill
%verify(not mode) %{_bindir}/su
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
%{_bindir}/findmnt
%{_bindir}/flock
%{_bindir}/getopt
%{_bindir}/hardlink
%{_bindir}/hexdump
%{_bindir}/ionice
%{_bindir}/ipcmk
%{_bindir}/ipcrm
%{_bindir}/ipcs
%{_bindir}/isosize
%if %{with enable_last}
%{_bindir}/last
%{_bindir}/lastb
%endif
%{_bindir}/line
%{_bindir}/look
%{_bindir}/lsblk
%{_bindir}/lscpu
%{_bindir}/lsipc
%{_bindir}/lslocks
%{_bindir}/lsmem
%{_bindir}/lsns
%{_bindir}/mcookie
%{_bindir}/mesg
%{_bindir}/more
%verify(not mode) %{_bindir}/mount
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
%{_bindir}/ul
%verify(not mode) %{_bindir}/umount
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
%{_sbindir}/raw
%{_sbindir}/rcraw
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
%if %{with enable_last}
%{_mandir}/man1/last.1.gz
%{_mandir}/man1/lastb.1.gz
%endif
%{_mandir}/man1/line.1.gz
%{_mandir}/man1/login.1.gz
%{_mandir}/man1/look.1.gz
%{_mandir}/man1/lscpu.1.gz
%{_mandir}/man1/lsipc.1.gz
%{_mandir}/man1/lsmem.1.gz
%{_mandir}/man1/mcookie.1.gz
%{_mandir}/man1/mesg.1.gz
%{_mandir}/man1/more.1.gz
%{_mandir}/man1/namei.1.gz
%{_mandir}/man1/nsenter.1.gz
%{_mandir}/man1/ionice.1.gz
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
%{_mandir}/man1/utmpdump.1.gz
%{_mandir}/man1/runuser.1.gz
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
%{_mandir}/man8/findmnt.8.gz
%{_mandir}/man8/fsfreeze.8.gz
%{_mandir}/man8/swaplabel.8.gz
%{_mandir}/man8/readprofile.8.gz
%{_mandir}/man8/rfkill.8.gz
%{_mandir}/man8/chcpu.8.gz
%{_mandir}/man8/partx.8.gz
%{_mandir}/man8/pivot_root.8.gz
%{_mandir}/man8/raw.8.gz
%{_mandir}/man8/rtcwake.8.gz
%{_mandir}/man8/setarch.8.gz
%{_mandir}/man8/swapoff.8.gz
%{_mandir}/man8/swapon.8.gz
%{_mandir}/man8/umount.8.gz
%{_mandir}/man8/uname26.8.gz
%{_mandir}/man8/wipefs.8.gz
%{_mandir}/man8/zramctl.8.gz
%{_mandir}/man8/fstrim.8.gz
%{_mandir}/man8/lsblk.8.gz
%{_mandir}/man8/resizepart.8.gz
%{_mandir}/man8/sulogin.8.gz
%{_mandir}/man8/wdctl.8.gz
%{_sbindir}/flushb
%{_sbindir}/readprofile
%dir %{_datadir}/getopt
%attr (755,root,root) %{_datadir}/getopt/getopt-parse.bash
%attr (755,root,root) %{_datadir}/getopt/getopt-parse.tcsh
# These directories should be owned by bash-completion. But we don't want to
# install them on build, so own these two directories:
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/*
%if %build_util_linux_systemd
%exclude %{_datadir}/bash-completion/completions/logger
%exclude %{_datadir}/bash-completion/completions/lslogins
%exclude %{_datadir}/bash-completion/completions/uuidd
%endif
%ifnarch ia64 m68k
#XXX: post our patches upstream
#XXX: call fdupes on /usr/share/man
#UsrMerge
/sbin/fdisk
#EndUsrMerge
%{_sbindir}/fdisk
%{_mandir}/man8/fdisk.8.gz
%endif
%ifnarch %sparc ia64 m68k
%{_mandir}/man8/cfdisk.8.gz
%{_mandir}/man8/sfdisk.8.gz
#UsrMerge
/sbin/cfdisk
/sbin/sfdisk
#EndUsrMerge
%{_sbindir}/cfdisk
%{_sbindir}/sfdisk
%endif
%ifnarch s390 s390x
%{_sbindir}/fdformat
#UsrMerge
/sbin/hwclock
#EndUsrMerge
%{_sbindir}/hwclock
%{_bindir}/setterm
%{_sbindir}/tunelp
%{_mandir}/man8/fdformat.8.gz
%{_mandir}/man8/hwclock.8.gz
%{_mandir}/man8/tunelp.8.gz
%endif

%files -n libblkid1
%defattr(-, root, root)
%{_libdir}/libblkid.so.1
%{_libdir}/libblkid.so.1.*

%files -n libblkid-devel
%defattr(-, root, root)
%{_libdir}/libblkid.so
%dir %{_includedir}/blkid
%{_includedir}/blkid/blkid.h
%{_libdir}/pkgconfig/blkid.pc
%{_mandir}/man3/libblkid.3.gz

%files -n libblkid-devel-static
%defattr(-, root, root)
%{_libdir}/libblkid.*a

%files -n libmount1
%defattr(-, root, root)
%{_libdir}/libmount.so.1
%{_libdir}/libmount.so.1.*

%files -n libmount-devel
%defattr(-, root, root)
%{_libdir}/libmount.so
%dir %{_includedir}/libmount
%{_includedir}/libmount/libmount.h
%{_libdir}/pkgconfig/mount.pc

%files -n libmount-devel-static
%defattr(-, root, root)
%{_libdir}/libmount.*a

%files -n libsmartcols1
%defattr(-, root, root)
%{_libdir}/libsmartcols.so.1
%{_libdir}/libsmartcols.so.1.*

%files -n libsmartcols-devel
%defattr(-, root, root)
%{_libdir}/libsmartcols.so
%dir %{_includedir}/libsmartcols
%{_includedir}/libsmartcols/libsmartcols.h
%{_libdir}/pkgconfig/smartcols.pc

%files -n libsmartcols-devel-static
%defattr(-, root, root)
%{_libdir}/libsmartcols.*a

%files -n libuuid1
%defattr(-, root, root)
%{_libdir}/libuuid.so.1
%{_libdir}/libuuid.so.1.*

%files -n libuuid-devel
%defattr(-, root, root)
%{_libdir}/libuuid.so
%dir %{_includedir}/uuid
%{_includedir}/uuid/uuid.h
%{_libdir}/pkgconfig/uuid.pc
%{_mandir}/man3/uuid*

%files -n libuuid-devel-static
%defattr(-, root, root)
%{_libdir}/libuuid.*a

%files -n libfdisk1
%defattr(-, root, root)
%{_libdir}/libfdisk.so.1
%{_libdir}/libfdisk.so.1.*

%files -n libfdisk-devel
%defattr(-, root, root)
%{_libdir}/libfdisk.so
%dir %{_includedir}/libfdisk
%{_includedir}/libfdisk/libfdisk.h
%{_libdir}/pkgconfig/fdisk.pc

%files -n libfdisk-devel-static
%defattr(-, root, root)
%{_libdir}/libfdisk.*a
%endif

%if %build_util_linux_systemd
%if %build_util_linux
%files systemd
%else
%files
%endif
%defattr(-, root, root)
/bin/logger
%{_bindir}/logger
%{_bindir}/lslogins
#BEGIN bootstrap_hack
%if 0%{?suse_version} < 1330
# Build images of some products use util-linux that does not come from this
# spec and does not own bash-completion dir. So we have to own own these two
# directories in util-linux-systemd as well:
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%endif
#END bootstrap_hack
%{_datadir}/bash-completion/completions/logger
%{_datadir}/bash-completion/completions/lslogins
%{_mandir}/man1/logger.1.gz
%{_mandir}/man1/lslogins.1.gz
%{_sbindir}/rcfstrim
%{_unitdir}/fstrim.service
%{_unitdir}/fstrim.timer

%files -n uuidd
%defattr(-, root, root)
%{_sbindir}/uuidd
%attr(-,uuidd,uuidd) %dir %{_localstatedir}/lib/libuuid
%ghost %{_localstatedir}/lib/libuuid/clock.txt
%attr(-,uuidd,uuidd) %ghost %dir /run/uuidd
%{_datadir}/bash-completion/completions/uuidd
%{_mandir}/man8/uuidd.8.gz
%{_sbindir}/rcuuidd
%{_unitdir}/uuidd.service
%{_unitdir}/uuidd.socket
%endif

%if %build_python_libmount
%if %build_util_linux
%files -n python3-libmount
%else
%files
%endif
%defattr(-, root, root)
%{python3_sitearch}/libmount
%endif

%changelog
