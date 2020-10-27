#
# spec file for package libconfini
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libconfini
Version:        1.16.0
Release:        0
Summary:        INI file parser libarary
License:        GPL-3.0-or-later
URL:            https://madmurphy.github.io/libconfini
Source:         https://github.com/madmurphy/libconfini/releases/download/%{version}/%{name}-%{version}-with-configure.tar.gz
BuildRequires:  pkgconfig

%description
libconfini is a INI file parser library written in C.

%package -n %{name}0
Summary:        INI file parser library

%description -n %{name}0
libconfini is a INI file parser library written in C.

%package devel
Summary:        INI file parser library - development files
Requires:       %{name}0 = %{version}

%description devel
libconfini is a INI file parser library written in C.
This package contains files required for development.

%prep
%setup -q -n %{name}-%{version}-with-configure

%build
%configure --disable-static --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n %{name}0 -p /sbin/ldconfig
%postun -n %{name}0 -p /sbin/ldconfig

%files -n %{name}0
%license COPYING
%{_libdir}/libconfini.so.*

%files devel
%license COPYING
%doc %{_docdir}/%{name}
%{_mandir}/man3/*.3%{?ext_man}
%{_libdir}/libconfini.so
%{_includedir}/*
%{_libdir}/pkgconfig/libconfini.pc

%changelog
