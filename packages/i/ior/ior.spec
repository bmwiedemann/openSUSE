#
# spec file for package ior
#
# Copyright (c) 2021 SUSE LLC
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
Version:        3.3.0
Release:        0
Summary:        Parallel filesystem I/O benchmark
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            https://github.com/hpc/ior
Source:         https://github.com/hpc/ior/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  hdf5-openmpi2-devel
%ifarch  x86_64 aarch64 ppc64le s390x
BuildRequires:  librbd-devel
%endif
BuildRequires:  libs3-devel
BuildRequires:  openmpi2-devel
BuildRequires:  zlib-devel
Requires:       openmpi2
Provides:       mdtest = %{version}
Obsoletes:      mdtest < %{version}

%description
Parallel filesystem I/O benchmark

%prep
%autosetup
chmod -x README.md doc/USER_GUIDE COPYRIGHT

%build
export MPICC="%{_libdir}/mpi/gcc/openmpi2/bin/mpicc"
%configure \
  --with-mpiio \
  --with-posix \
  --with-hdf5 \
%ifarch  x86_64 aarch64 ppc64le s390x
  --with-rados
%endif
  %nil
%make_build

%install
%make_install
rm %{buildroot}%{_datadir}/USER_GUIDE
rm %{buildroot}%{_libdir}/libaiori.a

%files
%doc NEWS README.md doc/USER_GUIDE
%license COPYRIGHT
%{_bindir}/%{name}
%{_bindir}/mdtest
%{_mandir}/man1/mdtest.1%{?ext_man}

%changelog
