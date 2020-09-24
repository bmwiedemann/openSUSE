#
# spec file for package qclib
#
# Copyright (c) 2017-2020 SUSE LLC
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


Name:           qclib
Version:        2.2.0
Release:        0
Summary:        Query Capacity library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://public.dhe.ibm.com/software/dw/linux390/ht_src/%{name}-%{version}.tgz
Source:         %{name}-%{version}.tgz
Source1:        %{name}-rpmlintrc
Patch1:         qclib.fix.missing.makefile.if.statement.patch
Patch99:        qclib.makefile.libdir.patch
BuildRequires:  doxygen
BuildRequires:  gcc-c++
ExclusiveArch:  s390 s390x
%if 0%{?suse_version} > 1300
BuildRequires:  glibc-devel-static
%else
BuildRequires:  glibc-devel
%endif

%description
qclib provides a C API for extraction of system information for Linux on z
Systems.

For instance, it will provide the number of CPUs
  * on the machine (CEC, Central Electronic Complex) layer
  * on the PR/SM (Processor Resource/Systems Manager) layer, i.e. visible to
    LPARs
  * in z/VM hosts, guests and CPU pools
  * in KVM hosts and guests
This allows calculating the upper limit of CPU resources a highest level guest
can use.

E.g.: If an LPAR on a z13 provides 4 CPUs to a z/VM hypervisor, and the
hypervisor provides 8 virtual CPUs to a guest, qclib can be used to retrieve
all of these numbers, and it can be concluded that not more capacity than 4
CPUs can be used by the software running in the guest.

qclib uses various interfaces and provides this data through a common and
consistent API (Application Programming Interface), using information provided
by:
  * STSI (Store System Information) instruction - for more details, refer to
    the z/Architecture Principles of Operation (SA22-7832)
  * STHYI (Store Hypervisor Information) instruction as provided by a z/VM
    hypervisor - for more information, refer to z/VM: V6R3 CP Programming
    Service (SC24-6179), chapter 'Store Hypervisor Information (STHYI)
    Instruction'.
  * hypfs file system - for more information, refer to 'Device Drivers,
    Features, and Commands', chapter 'S/390 hypervisor file system'.

%package -n libqc2
Summary:        Query Capacity Library shared library
Group:          System/Libraries
Obsoletes:      libqc1
Provides:       libqc1

%description -n libqc2
qclib provides a C API for extraction of system information for Linux on z
Systems.

%package devel
Summary:        Development files for Query Capacity library
Group:          Development/Libraries/C and C++
Requires:       libqc2 = %{version}-%{release}

%description devel
qclib provides a C API for extraction of system information for Linux on z
Systems.

%package devel-static
Summary:        Development files for Query Capacity library
Group:          Development/Libraries/C and C++
Requires:       libqc2 = %{version}-%{release}
Requires:       qclib-devel = %{version}-%{release}

%description devel-static
qclib provides a C API for extraction of system information for Linux on z
Systems.

%prep
%autosetup -p 1

%build
MYCFLAGS=$(grep ^CFLAGS Makefile | cut -f2 -d=)
%make_build all CFLAGS="${MYCFLAGS} %{optflags}"
%make_build doc

%check
%make_build doc test
%make_build doc test-sh

%install
%make_install LIBDIR=%{_lib} V=1
gzip -9 %{buildroot}/%{_mandir}/man8/*
make installdoc DESTDIR=%{buildroot} V=1

%post -n libqc2 -p /sbin/ldconfig

%postun -n libqc2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir %{_docdir}/%{name}
%{_bindir}/zname
%{_bindir}/zhypinfo
%{_docdir}/%{name}/*
%{_mandir}/man8/zname.8%{?ext_man}
%{_mandir}/man8/zhypinfo.8%{?ext_man}

%files -n libqc2
%defattr(-,root,root)
%{_libdir}/libqc.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/libqc.so

%files devel-static
%defattr(-,root,root)
%{_libdir}/libqc.a

%changelog
