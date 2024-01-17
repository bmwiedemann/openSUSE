#
# spec file for package libmicrodns
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


%define libname libmicrodns1

Name:           libmicrodns
Version:        0.2.0+6
Release:        0
Summary:        Minimal mDNS resolver library
License:        LGPL-2.1-or-later
URL:            https://github.com/videolabs/libmicrodns
Source:         %{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  meson
BuildRequires:  pkgconfig

%description
Minimal mDNS resolver (and announcer) library.

%package -n     %{libname}
Summary:        Shared library files for %{name}

%description -n     %{libname}
Minimal mDNS resolver (and announcer) library.
The %{libname} package contains shared libraries files for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%{_libdir}/libmicrodns.so.*

%files devel
%doc AUTHORS NEWS README.md
%{_includedir}/microdns
%{_libdir}/libmicrodns.so
%{_libdir}/pkgconfig/microdns.pc

%changelog
