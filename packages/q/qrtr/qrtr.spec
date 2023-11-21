#
# spec file for package qrtr
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
Name:          qrtr
Version:       1.0
Release:       0
Summary:       Qualcomm IPC Router shared library
License:       BSD-3-Clause
URL:           https://github.com/andersson/qrtr
Source0:       https://github.com/andersson/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:	       https://github.com/andersson/qrtr/commit/d0d471c96e7d112fac6f48bd11f9e8ce209c04d2.patch
Patch2:        https://github.com/andersson/qrtr/commit/a4398c8bf271f90338f95e1230373dde977d9cff.patch
ExclusiveArch: aarch64

%description
Userspace reference for net/qrtr in the Linux kernel 

%package -n libqrtr1
Summary:       Qualcomm IPC Router shared library

%description -n libqrtr1
Userspace shared library of Qualcomm IPC Router (QRTR)

%package devel
Summary:       The devel package of Qualcomm IPC Router
Requires:      libqrtr1 = %{version}

%description devel
A development pacakge that includes C header files of the qrtr shared library.

%prep
%autosetup -p1

%build
%make_build prefix="%{_prefix}" libdir="%{_libdir}" bindir="%{_sbindir}"

%install
%make_install prefix="%{_prefix}" libdir="%{_libdir}" bindir="%{_sbindir}"
# fix up spurious exec permission on libqrtr.h
chmod 644 %{buildroot}%{_includedir}/libqrtr.h

%preun
%service_del_preun qrtr-ns.service

%postun
%service_del_postun qrtr-ns.service

%pre
%service_add_pre qrtr-ns.service

%post
%service_add_post qrtr-ns.service

%ldconfig_scriptlets -n libqrtr1

%files
%{_sbindir}/qrtr-cfg
%{_sbindir}/qrtr-lookup
%{_sbindir}/qrtr-ns
%{_unitdir}/qrtr-ns.service

%files -n libqrtr1
%{_libdir}/libqrtr.so.*

%files devel
%{_includedir}/libqrtr.h
%{_libdir}/libqrtr.so

%changelog
