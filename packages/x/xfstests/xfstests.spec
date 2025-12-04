#
# spec file for package xfstests
#
# Copyright (c) 2025 SUSE LLC
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


# We only want DMAPI for SLE11/12
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000
%define need_dmapi 1
%endif

%if 0%{?sles_version} == 11
%define need_dmapi 1
%endif

# the snapshot download from URL location below uses current version format
%define version_unconverted dev-2025.11.18
Name:           xfstests
Version:        1.1.1+git.20251118
Release:        0
Summary:        Filesystem regression test suite
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://git.kernel.org/pub/scm/fs/xfs/xfstests-dev.git/
Source:         xfstests-%{version_unconverted}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?need_dmapi}
BuildRequires:  dmapi-devel
%endif
BuildRequires:  e2fsprogs-devel
BuildRequires:  fdupes
BuildRequires:  gdbm-devel
BuildRequires:  libacl-devel
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  libbtrfs-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  xfsprogs-devel
BuildRequires:  xz
Requires:       acl
Requires:       attr
Requires:       bash
Requires:       bc
Requires:       bind-utils
Requires:       btrfsprogs
Requires:       coreutils
Requires:       device-mapper
Requires:       duperemove
Requires:       e2fsprogs
Requires:       keyutils
Requires:       libcap-progs
Requires:       lvm
Requires:       perl
Requires:       quota
Requires:       xfsdump
Requires:       xfsprogs
Requires:       xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The filesystem regression test suite. Contains around 1500+ specific tests for
userspace and kernelspace for several linux filesystems.

%prep
%setup -q -n %{name}-%{version_unconverted}

%build
export OPTIMIZER="-fPIC"
export CFLAGS="%{optflags} -Iinclude"
INSTALL_USER=`id -un`
INSTALL_GROUP=`id -gn`
export INSTALL_USER INSTALL_GROUP

# autoreconf doesn't pass -Im4 to aclocal on SLE11
make configure
libtoolize -i
%configure		\
  --disable-static	\
  --exec_prefix=%{_prefix}/lib
make %{?_smp_mflags} V=1

%install
DIST_ROOT=%{buildroot}
DIST_INSTALL=`pwd`/install.manifest
export DIST_ROOT DIST_INSTALL
make %{?_smp_mflags} DESTDIR=%{buildroot} install DIST_ROOT=%{buildroot} DIST_MANIFEST="$DIST_INSTALL"
make -C build/rpm rpmfiles DESTDIR=%{buildroot} DIST_MANIFEST="$DIST_INSTALL"
%fdupes %{buildroot}/%{_prefix}

%files
%defattr(-,root,root)
%{_prefix}/lib/xfstests

%changelog