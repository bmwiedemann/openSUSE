#
# spec file for package ior
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


Name:           ior
Version:        4.0.0
Release:        0
Summary:        Parallel filesystem I/O benchmark
License:        GPL-2.0-only
URL:            https://github.com/hpc/ior
Source:         https://github.com/hpc/ior/releases/download/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ior-4.0.0-option-c23-fp.patch -- fix function-pointer call rejected under C23 (gcc 15); fixed in upstream git
Patch0:         ior-4.0.0-option-c23-fp.patch
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  hdf5-openmpi5-devel
BuildRequires:  make
BuildRequires:  openmpi-macros-devel
BuildRequires:  zlib-devel
Provides:       mdtest = %{version}
Obsoletes:      mdtest < %{version}

%description
Parallel filesystem I/O benchmark

%prep
%autosetup -p1
chmod -x README.md doc/USER_GUIDE COPYRIGHT

%build
%{setup_openmpi}
# The RADOS backend is broken in the 4.0.0 release: src/aiori-RADOS.c was not
# ported to the new AIORI API and fails to compile (fixed in upstream git,
# expected to return in the next release). S3 backends stay disabled as before.
%configure \
  --with-mpiio \
  --with-posix \
  --with-hdf5 \
  %{nil}
%make_build

%install
%make_install
rm %{buildroot}%{_datadir}/USER_GUIDE
rm %{buildroot}%{_libdir}/libaiori.a
# strip bogus relative RUNPATH (check/lib64, the bundled test framework)
# that rpmlint rejects as binary-or-shlib-defines-rpath
chrpath -d %{buildroot}%{_bindir}/ior %{buildroot}%{_bindir}/mdtest %{buildroot}%{_bindir}/md-workbench

%files
%doc NEWS README.md doc/USER_GUIDE
%license COPYRIGHT
%{_bindir}/%{name}
%{_bindir}/mdtest
%{_bindir}/md-workbench
%{_mandir}/man1/mdtest.1%{?ext_man}

%changelog
