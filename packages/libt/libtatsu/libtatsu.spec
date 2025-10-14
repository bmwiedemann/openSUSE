#
# spec file for package libtatsu
#
# Copyright (c) 2025 SUSE LLC
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


%define libname libtatsu0
Name:           libtatsu
Version:        1.0.5+3git.20250922
Release:        0
Summary:        Apple's Tatsu Signing Server Communication Library
License:        LGPL-2.1-or-later
URL:            https://github.com/libimobiledevice/libtatsu
Source:         %{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl) >= 7.0
BuildRequires:  pkgconfig(libplist-2.0) >= 2.6.0

%description
Library handling the communication with Apple's Tatsu Signing Server (TSS).

%package -n %{libname}
Summary:        Apple's Tatsu Signing Server Communication Librar

%description -n %{libname}
Library handling the communication with Apple's Tatsu Signing Server (TSS).

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}
Requires:       pkgconfig(libplist-2.0)

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
autoreconf -fvi
%configure \
  --disable-silent-rules \
  --disable-static \
  PYTHON=%{_bindir}/python3 PACKAGE_VERSION=%{version}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

%changelog
