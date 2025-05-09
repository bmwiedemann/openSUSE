#
# spec file for package libquo
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2014-2016 Christoph Junghans <junghans@votca.org>
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


Name:           libquo
Version:        1.4
%global sover   8
Release:        0
Summary:        A library for run-time tuning of process binding policies
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://lanl.github.io/libquo/
Source:         https://lanl.github.io/libquo/dists/%{name}-%{version}.tar.gz
BuildRequires:  hwloc
BuildRequires:  numactl
BuildRequires:  openmpi-macros-devel
BuildRequires:  pkgconfig

%description
QUO is an API tailored for MPI/MPI+X codes that may benefit from
evolving process binding policies during their execution. QUO allows
for arbitrary process binding policies to be enacted and reverted
during the execution as different computational phases are entered
and exited, respectively.

%package -n libquo%{sover}
Summary:        A library for run-time tuning of process binding policies
Group:          System/Libraries

%description -n libquo%{sover}
QUO is an API tailored for MPI/MPI+X codes that may benefit from
evolving process binding policies during their execution. QUO allows
for arbitrary process binding policies to be enacted and reverted
during the execution as different computational phases are entered
and exited, respectively.

%package devel
Summary:        Development headers and libraries for libquo
Group:          Development/Libraries/C and C++
Requires:       libquo%{sover} = %{version}-%{release}

%description devel
QUO is an API tailored for MPI/MPI+X codes that may benefit from
evolving process binding policies during their execution. QUO allows
for arbitrary process binding policies to be enacted and reverted
during the execution as different computational phases are entered
and exited, respectively.

This package contains development headers and libraries for libquo.

%prep
%setup -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%setup_openmpi

DATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
%configure --disable-silent-rules --enable-shared CC=mpicc USER="Opensuse-builder" HOSTNAME="Opensuse" DATE="$DATE"
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libquo%{sover} -p /sbin/ldconfig
%postun -n libquo%{sover} -p /sbin/ldconfig

%files -n libquo%{sover}
%{_libdir}/libquo.so.%{sover}*

%files devel
%{_bindir}/quo-info
%{_includedir}/*.h
%{_libdir}/libquo.so
%{_libdir}/libquo.a
%{_libdir}/pkgconfig/libquo.pc

%changelog
