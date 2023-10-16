#
# spec file for package fsverity-utils
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


Name:           fsverity-utils
Version:        1.5
Release:        0
Summary:        Userspace utilities for fs-verity
License:        MIT
Group:          System/Filesystems
URL:            https://www.kernel.org/doc/html/latest/filesystems/fsverity.html
Source0:        https://git.kernel.org/pub/scm/fs/fsverity/%{name}.git/snapshot/%{name}-%{version}.tar.gz
# manpage pregenerated from "make install-man" to avoid pandoc build
# dependency. pandoc is huge and unavailable on some architectures.
Source1:        fsverity.1
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libopenssl-devel

%description
fsverity is a userspace utility for fs-verity. fs-verity is a Linux
kernel filesystem feature that does transparent on-demand verification
of the contents of read-only files using Merkle trees.

fsverity can enable fs-verity on files, retrieve the digests of
fs-verity files, and sign files for use with fs-verity (among other
things). fsverity's functionality is divided among various subcommands.

%package -n libfsverity0
Summary:        Library package for fsverity-utils

%description -n libfsverity0
Shared-object dependencies for fsverity-utils.

%package devel
Summary:        Development package for fsverity-utils
Requires:       libfsverity0 = %{version}-%{release}

%description devel
Development package for fsverity-utils, including libfsverity header
and library files.

%prep
%setup -q

%build
%make_build USE_SHARED_LIB=1

%install
%make_install \
	USE_SHARED_LIB=1 \
	BINDIR=%{_bindir} \
	INCDIR=%{_includedir} \
	LIBDIR=%{_libdir} \
	MANDIR=%{_mandir}

# see Source note...
install -D -m 644 -t %{buildroot}/%{_mandir}/man1 %{SOURCE1}

rm %{buildroot}/%{_libdir}/libfsverity.a

%post -n libfsverity0 -p /sbin/ldconfig
%postun -n libfsverity0 -p /sbin/ldconfig

%files
%{_bindir}/fsverity
%{_mandir}/man1/fsverity.*

%files -n libfsverity0
%{_libdir}/libfsverity.so.0

%files devel
%license LICENSE
%{_libdir}/libfsverity.so
%{_libdir}/pkgconfig/libfsverity.pc
%{_includedir}/libfsverity.h

%changelog
