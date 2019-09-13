#
# spec file for package sblim-indication_helper
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sblim-indication_helper
BuildRequires:  gcc-c++
BuildRequires:  sblim-cmpi-devel
Version:        0.5.0
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://sblim.wiki.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Summary:        Toolkit for CMPI Indication Providers
License:        EPL-1.0
Group:          System/Management

%description 
This package contains a developer library for helping out when writing
CMPI providers. This library polls the registered functions for data
and, if it changes, a CMPI indication is set with the values of the
indication class properties (also set by the developer).

%package devel
Summary:        Toolkit for CMPI indication providers (Development Files)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       sblim-cmpi-devel

%description devel
This package contain developer library for helping out when writing
CMPI providers. This library polls the registered functions for data
and if they change an CMPI indication is set with the values of the
indication class properties (also set by the developer).

This package holds the development files for sblim-indication_helper.

%prep
%setup -q

%build
%configure --disable-static --with-pic
%{__make}

%install
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README COPYING ChangeLog TODO
%{_libdir}/libind_helper.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/sblim
%{_libdir}/libind_helper.so
%exclude %{_libdir}/libind_helper.la

%changelog
