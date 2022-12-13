#
# spec file for package aml
#
# Copyright (c) 2022 SUSE LLC
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


Name:           aml
Version:        0.2.2
Release:        0
Summary:        Another Main Loop
License:        ISC
URL:            https://github.com/any1/aml
Source0:        https://github.com/any1/aml/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig

%description
A main loop that is interoperable with other event loops and aims to be portable, utilitarian and simple.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libaml0 = %{version}

%description    devel
Development files and headers for %{name}.

%package -n     libaml0
Summary:        A VNC server library
Group:          System/Libraries

%description -n libaml0
A portable, uitlitarian and simple event loop library.

%prep
%setup -q

%build
%meson

%meson_build

%install
%meson_install

%post -n libaml0 -p /sbin/ldconfig
%postun -n libaml0 -p /sbin/ldconfig

%files devel
%license COPYING
%doc README.md

%{_includedir}/aml.h
%{_libdir}/libaml.so
%{_libdir}/pkgconfig/aml.pc

%files -n libaml0
%{_libdir}/libaml.so.0
%{_libdir}/libaml.so.0.0.0

%changelog
