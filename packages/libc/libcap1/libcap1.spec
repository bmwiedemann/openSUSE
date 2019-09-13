#
# spec file for package libcap1
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


BuildRequires:  xz
Name:           libcap1
Summary:        Library for Capabilities (linux-privs) Support
License:        BSD-3-Clause
Group:          System/Libraries
Version:        1.97
Release:        0
Source:         http://www.kernel.org/pub/linux/libs/security/linux-privs/libcap1/libcap-%{version}.tar.xz
Source1:        http://www.kernel.org/pub/linux/libs/security/linux-privs/libcap1/libcap-%{version}.tar.sign
Source2:        %name.keyring
Source3:        baselibs.conf
Patch1:         libcap-shlib-fix.diff
Patch2:         header.patch
Patch3:         libcap.eal3.diff
Patch6:         libcap-invalid-free-fix.diff
Patch7:         libcap-array-range-fix.diff
Patch8:         libcap-no-version-check.diff
Patch9:         feature-tests.patch
#URL:		http://www.kernel.org/
#Prefix:       /usr
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# bug437293
%ifarch ppc64
Obsoletes:      libcap-64bit
%endif
#
# 10.2 had libcap 1.92, 10.3 had libcap 1.10
Obsoletes:      libcap <= 1.92

%description
This package provides a compatible library for the old libcap-1.



%prep
%setup -q -n libcap-%{version}
%patch1
%patch2
%patch3 -p1
%patch6
%patch7
%patch8
%patch9 -p1

%build
lib=%{_lib} make %{?_smp_mflags} LDFLAGS= COPTFLAG="$RPM_OPT_FLAGS" CC="%{__cc}"

%install
make install FAKEROOT=$RPM_BUILD_ROOT LIBDIR=$RPM_BUILD_ROOT/%{_lib} MANDIR=$RPM_BUILD_ROOT%{_mandir}
# move *.so file to libdir and relink
rm -f $RPM_BUILD_ROOT/%{_lib}/*.so
# remove non-library files
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_mandir}
rm -rf $RPM_BUILD_ROOT/sbin

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%attr(755,root,root) /%{_lib}/libcap.so.*

%changelog
