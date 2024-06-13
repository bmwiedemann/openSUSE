#
# spec file for package util-linux
#
# Copyright (c) 2024 SUSE LLC
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
# systemd: binaries dependent on systemd or sqlite3, man pages (generator is dependent on ruby)
# python: Python bindings

%if "%{flavor}" == ""
%define psuffix -core
%define ulbuild base
%define ulsubset core
%define core %nil
%endif
# flavor == ""

%if "%{flavor}" == "systemd"
%define ulbuild base
%define ulsubset systemd
%define core %exclude
%endif
# flavor == systemd

# All python flavors are built separately. No module can be built together with base.
# This is a limitation of %%python_subpackages.
%if "%{flavor}" == "python"
%define ulbuild python
%endif
# flavor == python

%if 0%{?suse_version} < 1550
%define ul_extra_bin_sbin 1
%else
%define ul_extra_bin_sbin 0
%endif
# suse_version < 1550

%define ul_suid 4755

%define _name   util-linux

%if ! %{defined _distconfdir}
%define _distconfdir %{_sysconfdir}
%else
%define no_config 1
%endif
# ! _distconfdir

%if "%ulsubset" == "core"
Name:           util-linux
Summary:        A collection of basic system utilities (core part)
Group:          System/Base
%endif
# ulsubset == core

%if "%ulsubset" == "systemd"
Name:           util-linux-systemd
Summary:        A collection of basic system utilities (systemd dependent part)
Group:          System/Base
%endif
# ulsubset == systemd

%if "%ulbuild" == "python"
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-libmount
Summary:        Python bindings for the libmount library
Group:          Development/Languages/Python
%endif
# ulbuild == python

Version:        2.40.1
Release:        0
License:        GPL-2.0-or-later
URL:            https://www.kernel.org/pub/linux/utils/util-linux/
Source:         https://www.kernel.org/pub/linux/utils/util-linux/v2.40/util-linux-%{version}.tar.xz
Source2:        util-linux-login_defs-check.sh
Source3:        util-linux-rpmlintrc
Source7:        baselibs.conf
Source8:        login.pamd
Source9:        remote.pamd
Source10:       su.pamd
Source11:       su.default
Source12:       https://www.kernel.org/pub/linux/utils/util-linux/v2.39/util-linux-%{version}.tar.sign
Source13:       %{_name}.keyring
Source14:       runuser.pamd
Source15:       runuser-l.pamd
Source16:       su-l.pamd
Source17:       tmpfiles.lastlog2.conf
Source51:       blkid.conf
# PATCH-EXTEND-UPSTREAM: Let `su' handle /sbin and /usr/sbin in path
Patch0:         make-sure-sbin-resp-usr-sbin-are-in-PATH.diff
Patch1:         libmount-print-a-blacklist-hint-for-unknown-filesyst.patch
Patch2:         Add-documentation-on-blacklisted-modules-to-mount-8-.patch
# PATCH-FIX-SUSE util-linux-bash-completion-su-chsh-l.patch bsc1172427 -- Fix "su -s" bash completion.
Patch3:         util-linux-bash-completion-su-chsh-l.patch
Patch5:         static_lib.patch
Patch6:         0001-include-Include-unistd.h-in-pidfd-utils.h-for-syscal.patch
Patch7:         0002-lsfd-Refactor-the-pidfd-logic-into-lsfd-pidfd.c.patch
Patch8:         0003-lsfd-Support-pidfs.patch
Patch9:         0004-lsfd-test-Adapt-test-cases-for-pidfs.patch
BuildRequires:  audit-devel
BuildRequires:  bc
BuildRequires:  binutils-devel
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libeconf-devel-static
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
%if 0%{?suse_version} < 1600
BuildRequires:  utempter-devel
%endif
BuildRequires:  zlib-devel
Requires(post): permissions
Requires(verify): permissions
# util-linux is part of VMInstall, but we can well build without it
# Helps shorten a cycle and eliminate a bootstrap issue
#!BuildIgnore:  util-linux

%ifarch ppc ppc64 ppc64le
BuildRequires:  librtas-devel
%endif
#arch ppc

%if "%ulsubset" == "systemd"
BuildRequires:  bash-completion
BuildRequires:  libudev-devel
BuildRequires:  socat
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  rubygem(asciidoctor)
Supplements:    (util-linux and systemd)
# Split-provides for upgrade from SLE < 12 and openSUSE <= 13.1
Provides:       util-linux:/bin/logger
# man pages were moved to -systemd subpackage with 2.38.x (SLE15 SP6, Leap 15.6)
Conflicts:      util-linux < 2.38
%systemd_requires
%endif
# ulsubset == systemd

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
# arch s390x

Supplements:    filesystem(minix)
# All login.defs variables require support from shadow side.
# Upgrade this symbol version only if new variables appear!
# Verify by shadow-login_defs-check.sh from shadow source package.
Recommends:     login_defs-support-for-util-linux >= 2.37
%endif
# ulsubset == core

%if "%ulbuild" == "base"
# The problem with inconsistent /proc/self/mountinfo read is fixed in kernel 5.8.
# util-linux >= 2.37 no more contain work-around.
Conflicts:      kernel < 5.8
%endif
# ulbuild == base

%if "%ulbuild" == "python"
BuildRequires:  %{python_module devel}
BuildRequires:  rubygem(asciidoctor)
%python_subpackages
%endif
# ulbuild == python

%if "%ulbuild" == "python"
%description
This package contains the Python bindings for util-linux libmount
library.
%endif
# ulbuild == python

%if "%ulbuild" == "base"
%description
This package contains a large variety of low-level system utilities
that are necessary for a Linux system to function. It contains the
mount program, the fdisk configuration tool, and more.
%endif
# ulbuild == base

#################
# Core packages #
#################
%if "%ulsubset" == "core"
%ifarch s390 s390x ia64 m68k sparc
%package -n util-linux-extra
Summary:        A collection of basic system utilities - extra utilities
License:        GPL-2.0-or-later
Group:          System/Base

%description -n util-linux-extra
This package contains an util-linux tools that have no real use on a
particular platform. It contains programs that are not well usable for the
platform, but they can be required by scripts or third party tools.
%endif

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
Requires:       libeconf-devel-static

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
# ulsubset == core

%if "%ulsubset" == "systemd"

%package -n lastlog2
Summary:        Reports most recent login of users
License:        BSD-2-Clause
Group:          System/Base
Requires(pre):  pam-config >= 2.4
Requires(post): pam-config >= 2.4

%description -n lastlog2
pam_lastlog2 and lastlog2 are Y2038 safe versions of the old lastlog utility. pam_lastlog2 collects all data in a sqlite3 database and lastlog2 formats and prints the contents. The username, port, and last login time will be printed.

%package -n liblastlog2-2
Summary:        Library to report most recent login of users
License:        BSD-2-Clause
Group:          System/Libraries

%description -n liblastlog2-2
The liblastlog2 library provides various interfaces to read, write or modify the lastlog 2 database.

%package -n liblastlog2-devel
Summary:        Development files for the lastlog2 library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Requires:       liblastlog2-2 = %{version}
Provides:       lastlog2-devel = %{version}-%{release}
Obsoletes:      lastlog2-devel <= 1.3.1

%description -n liblastlog2-devel
Files to develop applications using the liblastlog2 library.

%endif
# ulsubset == systemd

####################
# Systemd packages #
####################
%if "%ulsubset" == "systemd"
%package -n util-linux-tty-tools
Summary:        Tools for writing to TTYs
License:        BSD-3-Clause
Requires(pre):  group(tty)
Requires(post): permissions
Requires(verify): permissions
Provides:       util-linux:%{_bindir}/mesg
Provides:       util-linux:%{_bindir}/wall
Provides:       util-linux:%{_bindir}/write
# File conflict: /usr/bin/mesg /usr/bin/wall
Conflicts:      busybox-util-linux

%description -n util-linux-tty-tools
Tools that write to TTYs that the current user does not own.

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
Requires:       group(uuidd)
Requires:       user(uuidd)
%systemd_requires

%description -n uuidd
The uuidd package contains a userspace daemon (uuidd) which guarantees
uniqueness of time-based UUID generation even at very high rates on
SMP systems.
%endif
# ulsubset == systemd

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

# configure options depending on ulbuild and ulsubset values
configure_options=""
# libmagic is only used for determining in more(1) whether or not a file
# is binary. but it has builtin code that is doing the same with a simpler
# check and the libmagic database dependency is rather large (9MB+)
configure_options+="--without-libmagic "

%if "%ulbuild" == "python"
%define _configure ../configure
configure_options+="--disable-all-programs "
configure_options+="--with-python "
configure_options+="--enable-pylibmount "
configure_options+="--enable-libmount "
configure_options+="--enable-libblkid "
%endif
# ulbuild == python

%if "%ulbuild" == "base"
configure_options+="--enable-all-programs "
configure_options+="--without-python "
%endif
# ulbuild == base

%if "%ulsubset" == "core"
configure_options+="--without-systemd --disable-liblastlog2"
%endif
# ulsubset == core

%if "%ulsubset" == "systemd"
configure_options+="--with-systemd "
%endif
# ulsubset == systemd

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
%if 0%{?suse_version} < 1600
	--with-utempter\
%endif
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
	--with-vendordir=%{_distconfdir} \
	--disable-libmount-mountfd-support \
	$configure_options
make %{?_smp_mflags}
}

################
# Python build #
################
%if "%ulbuild" == "python"
%{python_expand export PYTHON=$python
mkdir -p build.$python
cd build.$python
configure_and_build
cd ..
}
%endif
# ulbuild == python

##############
# Base build #
##############
%if "%ulbuild" == "base"
configure_and_build
%endif
# ulbuild == base

%if "%ulsubset" == "core"
bash ./util-linux-login_defs-check.sh
#BEGIN SYSTEMD SAFETY CHECK
# With systemd, some utilities are built differently. Keep track of these
# sources to prevent building of systemd-less versions.
#
# WARNING: Never edit following line without doing all suggested in the echo below!
UTIL_LINUX_KNOWN_SYSTEMD_DEPS='./login-utils/lslogins.c ./misc-utils/findmnt.c ./misc-utils/logger.c ./misc-utils/lsblk-properties.c ./misc-utils/uuidd.c '
UTIL_LINUX_FOUND_SYSTEMD_DEPS=$(find . -type f -name "*.c" -exec grep -l '#.*if.*HAVE_LIB\(SYSTEMD\|\UDEV\)' '{}' '+' | LC_ALL=C sort | tr '\n' ' ')
if test "$UTIL_LINUX_KNOWN_SYSTEMD_DEPS" != "$UTIL_LINUX_FOUND_SYSTEMD_DEPS" ; then
	echo "List of utilities depending on systemd have changed.
Please check the new util-linux-systemd file list, file removal and update of Conflicts for safe update!
Then update %%core and/or %%exclude in the file list to build what is needed.
Only then you can safely update following spec file line:
UTIL_LINUX_KNOWN_SYSTEMD_DEPS='$UTIL_LINUX_FOUND_SYSTEMD_DEPS'"
	exit 1
fi
#END SYSTEMD SAFETY CHECK
%endif
# ulsubset == core

%install
################
# Base install #
################
%if "%ulbuild" == "base"
%make_install
mkdir -p %{buildroot}{%{_distconfdir}/default,%{_pam_vendordir},%{_sysconfdir}/issue.d}
install -m 644 %{SOURCE51} %{buildroot}%{_sysconfdir}/blkid.conf
install -m 644 %{SOURCE8} %{buildroot}%{_pam_vendordir}/login
install -m 644 %{SOURCE9} %{buildroot}%{_pam_vendordir}/remote
%if 0%{?suse_version} <= 1500
sed -i '/^session/s/common-session-nonlogin/common-session/g' %{SOURCE14}
%endif
install -m 644 %{SOURCE14} %{buildroot}%{_pam_vendordir}/runuser
install -m 644 %{SOURCE15} %{buildroot}%{_pam_vendordir}/runuser-l
%if 0%{?suse_version} <= 1500
sed -i '/^session/s/common-session-nonlogin/common-session/g' %{SOURCE10}
%endif
install -m 644 %{SOURCE10} %{buildroot}%{_pam_vendordir}/su
install -m 644 %{SOURCE16} %{buildroot}%{_pam_vendordir}/su-l
install -m 644 %{SOURCE11} %{buildroot}%{_distconfdir}/default/su
sed 's/\bsu\b/runuser/g' <%{SOURCE11} >runuser.default
install -m 644 runuser.default %{buildroot}%{_distconfdir}/default/runuser
rm -fv "%{buildroot}/%{_sbindir}/raw" "%{buildroot}/sbin/raw" \
	"%{buildroot}/%{_mandir}/man8/raw.8"*
echo -e "#!/bin/sh\n/sbin/blockdev --flushbufs \$1" > %{buildroot}%{_sbindir}/flushb
chmod 755 %{buildroot}%{_sbindir}/flushb

# arch dependent

%if "%ulsubset" != "core"
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
# arch s390

%ifarch ia64 %sparc m68k
rm -f %{buildroot}%{_mandir}/man8/cfdisk.8*
rm -f %{buildroot}%{_mandir}/man8/sfdisk.8*
rm -f %{buildroot}%{_sbindir}/cfdisk
rm -f %{buildroot}%{_sbindir}/sfdisk
%endif
# arch ia64 sparc m68k

%ifarch ia64 m68k
rm -f %{buildroot}%{_sbindir}/fdisk
rm -f %{buildroot}%{_mandir}/man8/fdisk.8*
%endif
# arch ia64 m68k
%endif
# ulsubset != core

# create list of setarch(8) symlinks
find  %{buildroot}%{_mandir}/man8 -regextype posix-egrep  \
  -regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64|parisc|parisc32|parisc64|uname26)\.8.*" \
  -printf "%{_mandir}/man8/%f*\n" >> %{name}.files
find  %{buildroot}%{_bindir}/ -regextype posix-egrep -type l \
  -regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64|parisc|parisc32|parisc64|uname26)$" \
  -printf "%{_bindir}/%f\n" >> %{name}.files
mkdir -p %{buildroot}/run/uuidd

%if "%ulsubset" == "systemd"
# clock.txt from uuidd is a ghost file
# FIXME: This could also be used by libuuid, but for now we only
# create it for uuidd. See boo#1206690.
mkdir -p %{buildroot}%{_sharedstatedir}/libuuid/
touch %{buildroot}%{_sharedstatedir}/libuuid/clock.txt
# Install systemd-tmpfile for lastlog database
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE17} %{buildroot}%{_tmpfilesdir}/lastlog2.conf
%endif
# ulsubset == systemd, ulbuild == base

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
# ul_extra_bin_sbin, ulbuild == base

%if "%ulsubset" == "core"
%find_lang %{_name} %{name}.lang
%else
# ulsubset != core, ulbuild == base
echo -n "" >%{name}.lang
ln -sf /sbin/service %{buildroot}%{_sbindir}/rcuuidd
ln -sf /sbin/service %{buildroot}%{_sbindir}/rcfstrim
%endif
# ulsubset == core, ulbuild == base

%if "%ulsubset" == "systemd"
# No *.la packages
rm -r %{buildroot}%{_pam_moduledir}/*.la
%endif
# ulsubset == systemd

%endif
# ulbuild == base

##################
# Python install #
##################
%if "%ulbuild" == "python"
%{python_expand cd build.$python
%make_install
rm %{buildroot}%{$python_sitearch}/libmount/*.*a
cd ..
}
# There is a limitation: python module needs to build much more, and install even more. Delete it.
rm -r %{buildroot}{%{_bindir},%{_mandir},%{_datadir},%{_includedir},%{_libdir}/{lib,pkg}*}
%endif
# ulbuild == python

# fdupes for all multibuild flavors
# Link duplicate manpages or python bindings.
%fdupes %{buildroot}%{_prefix}

##############
# Base check #
##############
%if "%ulbuild" == "base"
%check
# Perform testsuite with the standard build only.
# mark some tests "known_fail"
#
%if 0%{?qemu_user_space_build}
# skip tests marked as ts_skip_qemu_user
export QEMU_USER=1
# unsupported syscall in script(1) ... might be fixed in qemu
export TS_OPT_script_known_fail="yes"
# may segfault on qemu-user-space
export TS_OPT_misc_setarch_known_fail="yes"
%endif
# qemu_user_space_build

# Succeeds in local build, fails in OBS.
export TS_OPT_hardlink_options_known_fail="yes"
# This does not work with a chroot build: / is not a mountpoint
export TS_OPT_misc_mountpoint_known_fail="yes"
# This test appears to be racy
export TS_OPT_lslocks_lslocks_known_fail=yes
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
%verify_permissions -e %{_bindir}/mount -e %{_bindir}/umount
%verify_permissions -e %{_bindir}/su
%endif
%dnl # ulsubset == core, ulbuild == base

%if "%ulsubset" == "systemd"
%verifyscript -n util-linux-tty-tools
%verify_permissions -e %{_bindir}/wall -e %{_bindir}/write
%endif
%dnl # ulsubset == systemd, ulbuild == base

%endif
%dnl # ulbuild == base

%dnl ###################
%dnl # Core pre & post #
%dnl ###################
%if "%ulsubset" == "core"
%pre
# move outdated pam.d/*.rpmsave files away
for i in login remote runuser runuser-l su su-l ; do
    test -f /etc/pam.d/${i}.rpmsave && mv -v /etc/pam.d/${i}.rpmsave /etc/pam.d/${i}.rpmsave.old ||:
done

%post
%set_permissions %{_bindir}/mount %{_bindir}/umount
%set_permissions %{_bindir}/su

%if ! %{defined no_config}
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
if ! grep -qs "^# /etc/default/su is an override" %{_sysconfdir}/default/su ; then
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
%dnl # !defined no_config

%if %{defined no_config}
%posttrans
# Migration to /usr/etc.
for i in  login remote runuser runuser-l su su-l; do
  test -f /etc/pam.d/${i}.rpmsave && mv -v /etc/pam.d/${i}.rpmsave /etc/pam.d/${i} ||:
done
%endif
%dnl # defined no_config

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
%dnl # ulsubset == core, pre & post
%dnl
%dnl ######################
%dnl # Systemd pre & post #
%dnl ######################
%if "%ulsubset" == "systemd"
%pre
%service_add_pre fstrim.service fstrim.timer

%post
%service_add_post fstrim.service fstrim.timer

%preun
%service_del_preun fstrim.service fstrim.timer

%postun
%service_del_postun fstrim.service fstrim.timer

%pre -n lastlog2
%service_add_pre lastlog2-import.service

%post -n lastlog2
%tmpfiles_create lastlog2.conf
%service_add_post lastlog2-import.service
%{_sbindir}/pam-config -a --lastlog2 --lastlog2-silent_if=gdm,gdm-password,lxdm,lightdm,mdm,sddm

%preun -n lastlog2
%service_del_preun lastlog2-import.service

%postun -n lastlog2
if [ "$1" -eq 0 ]; then
    %{_sbindir}/pam-config -d --lastlog2
fi
%service_del_postun lastlog2-import.service

%pre -n uuidd

%if 0%{?suse_version} < 1330
getent group uuidd >/dev/null || /usr/sbin/groupadd -r uuidd
getent passwd uuidd >/dev/null || \
	/usr/sbin/useradd -r -g uuidd -c "User for uuidd" \
	-d %{_localstatedir}/run/uuidd uuidd
%endif
%dnl # suse_version < 1330

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

%post -n util-linux-tty-tools
%set_permissions %{_bindir}/wall %{_bindir}/write

%post -n liblastlog2-2 -p /sbin/ldconfig

%postun -n liblastlog2-2 -p /sbin/ldconfig

%endif
%dnl # ulsubset == systemd, pre & post
%dnl
%dnl ##############
%dnl # Base files #
%dnl ##############
%if "%ulbuild" == "base"
%files -n %{name} -f %{name}.files
%defattr(-,root,root)

%if %{defined no_config}
%core %{_pam_vendordir}/login
%core %{_pam_vendordir}/remote
%core %{_pam_vendordir}/runuser
%core %{_pam_vendordir}/runuser-l
%core %{_pam_vendordir}/su
%core %{_pam_vendordir}/su-l

%if 0%{?suse_version} <= 1520
%core %dir %{_distconfdir}/default
%endif
# suse_version <= 1520

%core %{_distconfdir}/default/runuser
%core %{_distconfdir}/default/su

%else
# ! defined no_config

%core %config(noreplace) %{_pam_vendordir}/login
%core %config(noreplace) %{_pam_vendordir}/remote
%core %config(noreplace) %{_pam_vendordir}/runuser
%core %config(noreplace) %{_pam_vendordir}/runuser-l
%core %config(noreplace) %{_pam_vendordir}/su
%core %config(noreplace) %{_pam_vendordir}/su-l
%core %config(noreplace) %{_sysconfdir}/default/runuser
%core %config(noreplace) %{_sysconfdir}/default/su
%endif
# defined no_config

%config %dir %{_sysconfdir}/issue.d

%if %{ul_extra_bin_sbin}
%core /bin/kill
%core %verify(not mode) %attr(%ul_suid,root,root) /bin/su
%core /bin/dmesg
%core /bin/more
%core %verify(not mode) %attr(%ul_suid,root,root) /bin/mount
%core %verify(not mode) %attr(%ul_suid,root,root) /bin/umount
%core /bin/login
%core /sbin/agetty
%core /sbin/blockdev
%core /sbin/ctrlaltdel
%core /sbin/fsck.minix
%core /sbin/fsck.cramfs
%core /sbin/losetup
%core /sbin/mkfs
%core /sbin/mkfs.bfs
%core /sbin/mkfs.minix
%core /sbin/mkfs.cramfs
%core /sbin/mkswap
%core /sbin/nologin
%core /sbin/pivot_root
%core /sbin/swapoff
%core /sbin/swapon
%core /sbin/blkid
%core /sbin/findfs
%core /sbin/fsck
%core /sbin/switch_root
%core /sbin/wipefs
%core /sbin/fsfreeze
%core /sbin/swaplabel
%core /sbin/fstrim
%core /sbin/chcpu
%if "%ulsubset" != "systemd"
%exclude /bin/findmnt
%exclude /bin/logger
%exclude /bin/lsblk
%endif
%endif
# ul_extra_bin_sbin

%core %{_bindir}/kill
%core %verify(not mode) %attr(%ul_suid,root,root) %{_bindir}/su
%core %{_bindir}/eject
%core %{_bindir}/cal
%core %{_bindir}/chmem
%core %{_bindir}/choom
%core %{_bindir}/chrt
%core %{_bindir}/col
%core %{_bindir}/colcrt
%core %{_bindir}/colrm
%core %{_bindir}/column
%core %{_bindir}/dmesg
%core %{_bindir}/enosys
%core %{_bindir}/exch
%core %{_bindir}/fadvise
%core %{_bindir}/fallocate
%core %{_bindir}/fincore

%core %{_bindir}/flock
%core %{_bindir}/getopt
%core %{_bindir}/hardlink
%core %{_bindir}/hexdump
%core %{_bindir}/ionice
%core %{_bindir}/ipcmk
%core %{_bindir}/ipcrm
%core %{_bindir}/ipcs
%core %{_bindir}/irqtop
%core %{_bindir}/isosize

%if 0%{?suse_version} >= 1600
# last provided by wtmpdb, btmp support dropped
%exclude %{_bindir}/last
%exclude %{_bindir}/lastb
%else
%core %{_bindir}/last
%core %{_bindir}/lastb
%endif

%core %{_bindir}/line
%core %{_bindir}/look

%if !%{ul_extra_bin_sbin}
%core %{_bindir}/login
%endif
# ul_extra_bin_sbin

%core %{_bindir}/lsclocks
%core %{_bindir}/lscpu
%core %{_bindir}/lsfd
%core %{_bindir}/lsipc
%core %{_bindir}/lsirq
%core %{_bindir}/lslocks
%core %{_bindir}/lsmem
%core %{_bindir}/lsns
%core %{_bindir}/mcookie
%core %{_bindir}/more
%core %verify(not mode) %attr(%ul_suid,root,root) %{_bindir}/mount
%core %{_bindir}/namei
%core %{_bindir}/nsenter
%core %{_bindir}/pipesz
%core %{_bindir}/prlimit
%core %{_bindir}/rename
%core %{_bindir}/renice
%core %{_bindir}/rev
%core %{_bindir}/script
%core %{_bindir}/scriptlive
%core %{_bindir}/scriptreplay
%core %{_bindir}/setarch
%core %{_bindir}/setpgid
%core %{_bindir}/setpriv
%core %{_bindir}/setsid
%core %{_bindir}/taskset
%core %{_bindir}/uclampset
%core %{_bindir}/ul
%core %verify(not mode)%attr(%ul_suid,root,root)  %{_bindir}/umount
%core %{_bindir}/unshare
%core %{_bindir}/mountpoint
%core %{_bindir}/utmpdump
%core %{_bindir}/uuidgen
%core %{_bindir}/uuidparse
%core %{_bindir}/uname26
%core %{_bindir}/waitpid
%core %{_bindir}/wdctl
%core %{_sbindir}/addpart
%core %{_sbindir}/agetty
%core %{_sbindir}/blkid
%core %{_sbindir}/blkdiscard
%core %{_sbindir}/blkpr

# blkzone depends on linux/blkzoned.h
%if 0%{?suse_version} >= 1330
%core %{_sbindir}/blkzone
%endif
# suse_version >= 1330

%core %{_sbindir}/blockdev
%core %{_sbindir}/chcpu
%core %{_sbindir}/ctrlaltdel
%core %{_sbindir}/delpart
%core %{_sbindir}/findfs
%core %{_sbindir}/fsck
%core %{_sbindir}/fsck.minix
%core %{_sbindir}/fsck.cramfs
%core %{_sbindir}/fsfreeze
%core %{_sbindir}/fstrim
%core %{_sbindir}/ldattach
%core %{_sbindir}/losetup
%core %{_sbindir}/mkfs
%core %{_sbindir}/mkfs.bfs
%core %{_sbindir}/mkfs.minix
%core %{_sbindir}/mkfs.cramfs
%core %{_sbindir}/mkswap
%core %{_sbindir}/nologin
%core %{_sbindir}/partx
%core %{_sbindir}/pivot_root
%core %{_sbindir}/resizepart
%core %{_sbindir}/rfkill
%core %{_sbindir}/rtcwake
%core %{_sbindir}/runuser
%core %{_sbindir}/sulogin
%core %{_sbindir}/swaplabel
%core %{_sbindir}/swapoff
%core %{_sbindir}/swapon
%core %{_sbindir}/switch_root
%core %{_sbindir}/wipefs
%core %{_bindir}/whereis
%core %{_sbindir}/zramctl
%core %{_sbindir}/flushb
%core %{_sbindir}/readprofile
# These directories should be owned by bash-completion. But we don't want to
# install them on build, so own these two directories:
%core %dir %{_datadir}/bash-completion
%core %dir %{_datadir}/bash-completion/completions

%exclude %{_datadir}/bash-completion/completions/uuidd

# wtmpdb
%if 0%{?suse_version} >= 1600
%exclude %{_datadir}/bash-completion/completions/last
%exclude %{_datadir}/bash-completion/completions/lastb
%endif

# tty-tools package
%exclude %{_datadir}/bash-completion/completions/wall
%exclude %{_datadir}/bash-completion/completions/write
%exclude %{_datadir}/bash-completion/completions/mesg
%exclude %{_mandir}/man1/mesg.1.gz
%exclude %{_mandir}/man1/wall.1.gz
%exclude %{_mandir}/man1/write.1.gz
%exclude %{_bindir}/mesg
%exclude %{_bindir}/wall
%exclude %{_bindir}/write

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

#
# Files not common for all architectures
%ifnarch ia64 m68k

%if %{ul_extra_bin_sbin}
%core /sbin/fdisk
%endif
# ul_extra_bin_sbin

%core %{_sbindir}/fdisk
%core %{_mandir}/man8/fdisk.8.gz
%endif
# narch ia64 m68k

%ifnarch %sparc ia64 m68k
%core %{_mandir}/man8/cfdisk.8.gz
%core %{_mandir}/man8/sfdisk.8.gz

%if %{ul_extra_bin_sbin}
%core /sbin/cfdisk
%core /sbin/sfdisk
%endif
# ul_extra_bin_sbin

%core %{_sbindir}/cfdisk
%core %{_sbindir}/sfdisk
%endif
# narch sparc ia64 m68k

%ifnarch s390 s390x
%core %{_sbindir}/fdformat

%if %{ul_extra_bin_sbin}
%core /sbin/hwclock
%endif
# ul_extra_bin_sbin

%core %{_sbindir}/hwclock
%core %{_bindir}/setterm
%core %{_sbindir}/tunelp
%core %{_mandir}/man8/fdformat.8.gz
%core %{_mandir}/man8/hwclock.8.gz
%core %{_mandir}/man8/tunelp.8.gz
%endif
# narch s390

%core %{_mandir}/man1/kill.1.gz
%core %{_mandir}/man1/su.1.gz
%core %{_mandir}/man1/cal.1.gz
%core %{_mandir}/man1/choom.1.gz
%core %{_mandir}/man1/chrt.1.gz
%core %{_mandir}/man1/col.1.gz
%core %{_mandir}/man1/colcrt.1.gz
%core %{_mandir}/man1/colrm.1.gz
%core %{_mandir}/man1/column.1.gz
%core %{_mandir}/man1/dmesg.1.gz
%core %{_mandir}/man1/enosys.1.gz
%core %{_mandir}/man1/eject.1.gz
%core %{_mandir}/man1/exch.1.gz
%core %{_mandir}/man1/fadvise.1.gz
%core %{_mandir}/man1/fallocate.1.gz
%core %{_mandir}/man1/fincore.1.gz
%core %{_mandir}/man1/flock.1.gz
%core %{_mandir}/man1/getopt.1.gz
%core %{_mandir}/man1/hardlink.1.gz
%core %{_mandir}/man1/hexdump.1.gz
%core %{_mandir}/man1/ipcrm.1.gz
%core %{_mandir}/man1/ipcs.1.gz

%if 0%{?suse_version} >= 1600
%exclude %{_mandir}/man1/last.1.gz
%exclude %{_mandir}/man1/lastb.1.gz
%else
%core %{_mandir}/man1/last.1.gz
%core %{_mandir}/man1/lastb.1.gz
%endif

%core %{_mandir}/man1/line.1.gz
%core %{_mandir}/man1/login.1.gz
%core %{_mandir}/man1/look.1.gz
%core %{_mandir}/man1/lscpu.1.gz
%core %{_mandir}/man1/lsclocks.1.gz
%core %{_mandir}/man1/lsfd.1.gz
%core %{_mandir}/man1/lsipc.1.gz
%core %{_mandir}/man1/lsirq.1.gz
%core %{_mandir}/man1/lsmem.1.gz
%core %{_mandir}/man1/mcookie.1.gz
%core %{_mandir}/man1/more.1.gz
%core %{_mandir}/man1/namei.1.gz
%core %{_mandir}/man1/nsenter.1.gz
%core %{_mandir}/man1/ionice.1.gz
%core %{_mandir}/man1/irqtop.1.gz
%core %{_mandir}/man1/pipesz.1.gz
%core %{_mandir}/man1/prlimit.1.gz
%core %{_mandir}/man1/rename.1.gz
%core %{_mandir}/man1/rev.1.gz
%core %{_mandir}/man1/renice.1.gz
%core %{_mandir}/man1/setpriv.1.gz
%core %{_mandir}/man1/setsid.1.gz
%core %{_mandir}/man1/script.1.gz
%core %{_mandir}/man1/scriptlive.1.gz
%core %{_mandir}/man1/scriptreplay.1.gz
%core %{_mandir}/man1/setpgid.1.gz
%core %{_mandir}/man1/setterm.1.gz
%core %{_mandir}/man1/taskset.1.gz
%core %{_mandir}/man1/ul.1.gz
%core %{_mandir}/man1/unshare.1.gz
%core %{_mandir}/man1/whereis.1.gz
%core %{_mandir}/man1/ipcmk.1.gz
%core %{_mandir}/man1/mountpoint.1.gz
%core %{_mandir}/man1/runuser.1.gz
%core %{_mandir}/man1/uclampset.1.gz
%core %{_mandir}/man1/utmpdump.1.gz
%core %{_mandir}/man1/uuidgen.1.gz
%core %{_mandir}/man1/uuidparse.1.gz
%core %{_mandir}/man1/waitpid.1.gz
%core %{_mandir}/man5/adjtime_config.5.gz
%core %{_mandir}/man5/fstab.5.gz
%core %{_mandir}/man5/scols-filter.5.gz
%core %{_mandir}/man5/terminal-colors.d.5.gz
%core %{_mandir}/man8/addpart.8.gz
%core %{_mandir}/man8/agetty.8.gz

%if 0%{?suse_version} >= 1330
%core %{_mandir}/man8/blkzone.8.gz
%endif
# suse_version >= 1330

%core %{_mandir}/man8/blockdev.8.gz
%core %{_mandir}/man8/blkpr.8.gz
%core %{_mandir}/man8/chmem.8.gz
%core %{_mandir}/man8/ctrlaltdel.8.gz
%core %{_mandir}/man8/delpart.8.gz
%core %{_mandir}/man8/blkid.8.gz
%core %{_mandir}/man8/blkdiscard.8.gz
%core %{_mandir}/man8/switch_root.8.gz
%core %{_mandir}/man8/mkfs.bfs.8.gz
%core %{_mandir}/man8/mkfs.minix.8.gz
%core %{_mandir}/man8/findfs.8.gz
%core %{_mandir}/man8/fsck.8.gz
%core %{_mandir}/man8/fsck.cramfs.8.gz
%core %{_mandir}/man8/fsck.minix.8.gz
%core %{_mandir}/man8/isosize.8.gz
%core %{_mandir}/man8/ldattach.8.gz
%core %{_mandir}/man8/losetup.8.gz
%core %{_mandir}/man8/lslocks.8.gz
%core %{_mandir}/man8/lsns.8.gz
%core %{_mandir}/man8/mkfs.8.gz
%core %{_mandir}/man8/mkfs.cramfs.8.gz
%core %{_mandir}/man8/mkswap.8.gz
%core %{_mandir}/man8/mount.8.gz
%core %{_mandir}/man8/nologin.8.gz
%core %{_mandir}/man8/fsfreeze.8.gz
%core %{_mandir}/man8/swaplabel.8.gz
%core %{_mandir}/man8/readprofile.8.gz
%core %{_mandir}/man8/rfkill.8.gz
%core %{_mandir}/man8/chcpu.8.gz
%core %{_mandir}/man8/partx.8.gz
%core %{_mandir}/man8/pivot_root.8.gz
%core %{_mandir}/man8/rtcwake.8.gz
%core %{_mandir}/man8/setarch.8.gz
%core %{_mandir}/man8/swapoff.8.gz
%core %{_mandir}/man8/swapon.8.gz
%core %{_mandir}/man8/umount.8.gz
%core %{_mandir}/man8/wipefs.8.gz
%core %{_mandir}/man8/zramctl.8.gz
%core %{_mandir}/man8/fstrim.8.gz
%core %{_mandir}/man8/resizepart.8.gz
%core %{_mandir}/man8/sulogin.8.gz
%core %{_mandir}/man8/wdctl.8.gz

##############
# Core files #
##############

%if "%ulsubset" == "core"
# Common files for all archs
%doc AUTHORS ChangeLog README NEWS
%license README.licensing
%license COPYING
%license Documentation/licenses/*
%config(noreplace) %{_sysconfdir}/blkid.conf

%{_datadir}/bash-completion/completions/*
%exclude %{_datadir}/bash-completion/completions/findmnt
%exclude %{_datadir}/bash-completion/completions/logger
%exclude %{_datadir}/bash-completion/completions/lsblk
%exclude %{_datadir}/bash-completion/completions/lslogins

%exclude %{_bindir}/findmnt
%exclude %{_bindir}/logger
%exclude %{_bindir}/lsblk
%exclude %{_bindir}/lslogins

%exclude %{_mandir}/man8/findmnt.8.gz
%exclude %{_mandir}/man1/logger.1.gz
%exclude %{_mandir}/man8/lsblk.8.gz
%exclude %{_mandir}/man1/lslogins.1.gz

%exclude %{_mandir}/man8/uuidd.8.gz
%endif
# ulsubset == core, ulbuild == base

#################
# Systemd files #
#################
%if "%ulsubset" == "systemd"
%exclude %config(noreplace) %{_sysconfdir}/blkid.conf

%exclude %config %dir %{_sysconfdir}/issue.d

%if %{ul_extra_bin_sbin}
/bin/findmnt
/bin/logger
/bin/lsblk
%endif
# ul_extra_bin_sbin

%{_bindir}/findmnt
%{_bindir}/logger
%{_bindir}/lsblk
%{_bindir}/lslogins

%{_mandir}/man8/findmnt.8.gz
%{_mandir}/man1/logger.1.gz
%{_mandir}/man8/lsblk.8.gz
%{_mandir}/man1/lslogins.1.gz

# Exclude core binaries bash-completion
%exclude %{_datadir}/bash-completion/completions/addpart
%exclude %{_datadir}/bash-completion/completions/blkdiscard
%exclude %{_datadir}/bash-completion/completions/blkid
%exclude %{_datadir}/bash-completion/completions/blkzone
%exclude %{_datadir}/bash-completion/completions/blockdev
%exclude %{_datadir}/bash-completion/completions/cal
%exclude %{_datadir}/bash-completion/completions/cfdisk
%exclude %{_datadir}/bash-completion/completions/chcpu
%exclude %{_datadir}/bash-completion/completions/chmem
%exclude %{_datadir}/bash-completion/completions/chrt
%exclude %{_datadir}/bash-completion/completions/col
%exclude %{_datadir}/bash-completion/completions/colcrt
%exclude %{_datadir}/bash-completion/completions/colrm
%exclude %{_datadir}/bash-completion/completions/column
%exclude %{_datadir}/bash-completion/completions/ctrlaltdel
%exclude %{_datadir}/bash-completion/completions/delpart
%exclude %{_datadir}/bash-completion/completions/dmesg
%exclude %{_datadir}/bash-completion/completions/eject
%exclude %{_datadir}/bash-completion/completions/enosys
%exclude %{_datadir}/bash-completion/completions/exch
%exclude %{_datadir}/bash-completion/completions/fallocate
%exclude %{_datadir}/bash-completion/completions/fadvise
%exclude %{_datadir}/bash-completion/completions/fdformat
%exclude %{_datadir}/bash-completion/completions/fdisk
%exclude %{_datadir}/bash-completion/completions/fincore
%exclude %{_datadir}/bash-completion/completions/findfs
%exclude %{_datadir}/bash-completion/completions/flock
%exclude %{_datadir}/bash-completion/completions/fsck
%exclude %{_datadir}/bash-completion/completions/fsck.cramfs
%exclude %{_datadir}/bash-completion/completions/fsck.minix
%exclude %{_datadir}/bash-completion/completions/fsfreeze
%exclude %{_datadir}/bash-completion/completions/fstrim
%exclude %{_datadir}/bash-completion/completions/getopt
%exclude %{_datadir}/bash-completion/completions/hardlink
%exclude %{_datadir}/bash-completion/completions/hexdump
%exclude %{_datadir}/bash-completion/completions/hwclock
%exclude %{_datadir}/bash-completion/completions/ionice
%exclude %{_datadir}/bash-completion/completions/ipcmk
%exclude %{_datadir}/bash-completion/completions/ipcrm
%exclude %{_datadir}/bash-completion/completions/ipcs
%exclude %{_datadir}/bash-completion/completions/irqtop
%exclude %{_datadir}/bash-completion/completions/isosize
%exclude %{_datadir}/bash-completion/completions/last
%exclude %{_datadir}/bash-completion/completions/lastb
%exclude %{_datadir}/bash-completion/completions/ldattach
%exclude %{_datadir}/bash-completion/completions/look
%exclude %{_datadir}/bash-completion/completions/losetup
%exclude %{_datadir}/bash-completion/completions/lsclocks
%exclude %{_datadir}/bash-completion/completions/lscpu
%exclude %{_datadir}/bash-completion/completions/lsipc
%exclude %{_datadir}/bash-completion/completions/lsirq
%exclude %{_datadir}/bash-completion/completions/lslocks
%exclude %{_datadir}/bash-completion/completions/lsmem
%exclude %{_datadir}/bash-completion/completions/lsns
%exclude %{_datadir}/bash-completion/completions/mcookie
%exclude %{_datadir}/bash-completion/completions/mkfs
%exclude %{_datadir}/bash-completion/completions/mkfs.bfs
%exclude %{_datadir}/bash-completion/completions/mkfs.cramfs
%exclude %{_datadir}/bash-completion/completions/mkfs.minix
%exclude %{_datadir}/bash-completion/completions/mkswap
%exclude %{_datadir}/bash-completion/completions/more
%exclude %{_datadir}/bash-completion/completions/mount
%exclude %{_datadir}/bash-completion/completions/mountpoint
%exclude %{_datadir}/bash-completion/completions/namei
%exclude %{_datadir}/bash-completion/completions/nsenter
%exclude %{_datadir}/bash-completion/completions/partx
%exclude %{_datadir}/bash-completion/completions/pipesz
%exclude %{_datadir}/bash-completion/completions/pivot_root
%exclude %{_datadir}/bash-completion/completions/prlimit
%exclude %{_datadir}/bash-completion/completions/readprofile
%exclude %{_datadir}/bash-completion/completions/rename
%exclude %{_datadir}/bash-completion/completions/renice
%exclude %{_datadir}/bash-completion/completions/resizepart
%exclude %{_datadir}/bash-completion/completions/rev
%exclude %{_datadir}/bash-completion/completions/rfkill
%exclude %{_datadir}/bash-completion/completions/rtcwake
%exclude %{_datadir}/bash-completion/completions/runuser
%exclude %{_datadir}/bash-completion/completions/script
%exclude %{_datadir}/bash-completion/completions/scriptlive
%exclude %{_datadir}/bash-completion/completions/scriptreplay
%exclude %{_datadir}/bash-completion/completions/setarch
%exclude %{_datadir}/bash-completion/completions/setpgid
%exclude %{_datadir}/bash-completion/completions/setpriv
%exclude %{_datadir}/bash-completion/completions/setsid
%exclude %{_datadir}/bash-completion/completions/setterm
%exclude %{_datadir}/bash-completion/completions/sfdisk
%exclude %{_datadir}/bash-completion/completions/su
%exclude %{_datadir}/bash-completion/completions/swaplabel
%exclude %{_datadir}/bash-completion/completions/swapoff
%exclude %{_datadir}/bash-completion/completions/swapon
%exclude %{_datadir}/bash-completion/completions/taskset
%exclude %{_datadir}/bash-completion/completions/tunelp
%exclude %{_datadir}/bash-completion/completions/uclampset
%exclude %{_datadir}/bash-completion/completions/ul
%exclude %{_datadir}/bash-completion/completions/umount
%exclude %{_datadir}/bash-completion/completions/unshare
%exclude %{_datadir}/bash-completion/completions/utmpdump
%exclude %{_datadir}/bash-completion/completions/uuidgen
%exclude %{_datadir}/bash-completion/completions/uuidparse
%exclude %{_datadir}/bash-completion/completions/waitpid
%exclude %{_datadir}/bash-completion/completions/wdctl
%exclude %{_datadir}/bash-completion/completions/whereis
%exclude %{_datadir}/bash-completion/completions/wipefs
%exclude %{_datadir}/bash-completion/completions/zramctl

%{_datadir}/bash-completion/completions/findmnt
%{_datadir}/bash-completion/completions/logger
%{_datadir}/bash-completion/completions/lsblk
%{_datadir}/bash-completion/completions/lslogins

# uuidd sub-package
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

# exclude setarch from systemd package
%exclude %{_bindir}/linux32
%exclude %{_bindir}/linux64
%exclude %{_bindir}/s390
%exclude %{_bindir}/s390x
%exclude %{_bindir}/i386
%exclude %{_bindir}/ppc
%exclude %{_bindir}/ppc64
%exclude %{_bindir}/ppc32
%exclude %{_bindir}/sparc
%exclude %{_bindir}/sparc64
%exclude %{_bindir}/sparc32
%exclude %{_bindir}/sparc32bash
%exclude %{_bindir}/mips
%exclude %{_bindir}/mips64
%exclude %{_bindir}/mips32
%exclude %{_bindir}/ia64
%exclude %{_bindir}/x86_64
%exclude %{_bindir}/parisc
%exclude %{_bindir}/parisc32
%exclude %{_bindir}/parisc64
%exclude %{_bindir}/uname26

%exclude %{_mandir}/man8/linux32.8.gz
%exclude %{_mandir}/man8/linux64.8.gz
%exclude %{_mandir}/man8/s390.8.gz
%exclude %{_mandir}/man8/s390x.8.gz
%exclude %{_mandir}/man8/i386.8.gz
%exclude %{_mandir}/man8/ppc.8.gz
%exclude %{_mandir}/man8/ppc64.8.gz
%exclude %{_mandir}/man8/ppc32.8.gz
%exclude %{_mandir}/man8/sparc.8.gz
%exclude %{_mandir}/man8/sparc64.8.gz
%exclude %{_mandir}/man8/sparc32.8.gz
%exclude %{_mandir}/man8/sparc32bash.8.gz
%exclude %{_mandir}/man8/mips.8.gz
%exclude %{_mandir}/man8/mips64.8.gz
%exclude %{_mandir}/man8/mips32.8.gz
%exclude %{_mandir}/man8/ia64.8.gz
%exclude %{_mandir}/man8/x86_64.8.gz
%exclude %{_mandir}/man8/parisc.8.gz
%exclude %{_mandir}/man8/parisc32.8.gz
%exclude %{_mandir}/man8/parisc64.8.gz
%exclude %{_mandir}/man8/uname26.8.gz

%{_sbindir}/rcfstrim
%{_unitdir}/fstrim.service
%{_unitdir}/fstrim.timer
%endif
# ulsubset systemd

#######################
# Core packages files #
#######################
%if "%ulsubset" == "core"
%ifarch s390 s390x ia64 m68k sparc
%files -n util-linux-extra
#
# Files not common for all architectures
%ifarch ia64 m68k

%if %{ul_extra_bin_sbin}
%core /sbin/fdisk
%endif
# ul_extra_bin_sbin

%core %{_sbindir}/fdisk
%core %{_mandir}/man8/fdisk.8.gz
%endif
# arch ia64 m68k

%ifarch %sparc ia64 m68k
%core %{_mandir}/man8/cfdisk.8.gz
%core %{_mandir}/man8/sfdisk.8.gz

%if %{ul_extra_bin_sbin}
%core /sbin/cfdisk
%core /sbin/sfdisk
%endif
# ul_extra_bin_sbin

%core %{_sbindir}/cfdisk
%core %{_sbindir}/sfdisk
%endif
# arch sparc ia64 m68k

%ifarch s390 s390x
%core %{_sbindir}/fdformat

%if %{ul_extra_bin_sbin}
%core /sbin/hwclock
%endif
# ul_extra_bin_sbin

%core %{_sbindir}/hwclock
%core %{_bindir}/setterm
%core %{_sbindir}/tunelp
%core %{_mandir}/man8/fdformat.8.gz
%core %{_mandir}/man8/hwclock.8.gz
%core %{_mandir}/man8/tunelp.8.gz
%endif
# arch s390
%endif
# arch s390 s390x ia64 m68k sparc

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

# devel, lang and uuidd files are not packaged in staging mode
# and packaged separately in full mode
# FIXME: Is it needed?
# HACK: We have to use "%%files -n" here, otherwise python lua code will
# issue an error, even if it is inside a false condition.
%files -n %{name}-lang -f %{name}.lang

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
# ulsubset == core

##########################
# Systemd packages files #
##########################
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

%files -n util-linux-tty-tools
%{_bindir}/mesg
%verify(not mode) %attr(0755,root,tty) %{_bindir}/wall
%verify(not mode) %attr(0755,root,tty) %{_bindir}/write
%{_mandir}/man1/mesg.1.gz
%{_mandir}/man1/wall.1.gz
%{_mandir}/man1/write.1.gz

%{_datadir}/bash-completion/completions/wall
%{_datadir}/bash-completion/completions/write
%{_datadir}/bash-completion/completions/mesg

%files -n lastlog2
%{_bindir}/lastlog2
%{_pam_moduledir}/pam_lastlog2.so
%{_mandir}/man8/lastlog2.8.gz
%{_mandir}/man8/pam_lastlog2.8.gz
%{_unitdir}/lastlog2-import.service
%{_tmpfilesdir}/lastlog2.conf
%{_datadir}/bash-completion/completions/lastlog2

%files -n liblastlog2-2
%{_libdir}/liblastlog2.so.2
%{_libdir}/liblastlog2.so.2.*

%files -n liblastlog2-devel
%{_libdir}/liblastlog2.so
%dir %{_includedir}/liblastlog2
%{_includedir}/liblastlog2/lastlog2.h
%{_mandir}/man3/lastlog2.3.gz
%{_mandir}/man3/ll2_*

%endif
# ulsubset == systemd

%endif
# ulbuild == base

################
# Python files #
################
%if "%ulbuild" == "python"
%files %{python_files}
%{python_sitearch}/libmount
%endif
# ulbuild == python

%changelog
