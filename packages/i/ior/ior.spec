#
# spec file for package ior
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.1.0
Release:        0
Summary:        Parallel filesystem I/O benchmark
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            https://github.com/hpc/ior
Source:         https://github.com/hpc/ior/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  libs3-devel
BuildRequires:  openmpi2-devel
Requires:       openmpi2

%description
Parallel filesystem I/O benchmark

%prep
%setup -q

%build
export MPICC="%{_libdir}/mpi/gcc/openmpi2/bin/mpicc"
%configure \
  --with-mpiio \
  --with-posix
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_datadir}/USER_GUIDE
chmod -x  {COPYRIGHT,ChangeLog,README,doc/USER_GUIDE}

%files
%doc COPYRIGHT ChangeLog README doc/USER_GUIDE
%{_bindir}/%{name}

%changelog
