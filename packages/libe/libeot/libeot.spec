#
# spec file for package libeot
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define libname libeot0
%define srcver  0.0.4
Name:           libeot
Version:        0.04
Release:        0
Summary:        A library for parsing Embedded OpenType font files
License:        MPL-2.0
Group:          Productivity/Publishing/Word
URL:            https://github.com/umanwizard/libeot
Source:         https://github.com/umanwizard/libeot/releases/download/v%{srcver}/libeot-%{srcver}.tar.xz
BuildRequires:  pkgconfig

%description
%{name} is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package -n %{libname}
Summary:        A library for parsing Embedded OpenType font files
Group:          System/Libraries

%description -n %{libname}
%{name} is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package devel
Summary:        A library for parsing Embedded OpenType font files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
%{name} is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package tools
Summary:        Tools to transform EOT font files into other formats
Group:          Productivity/Publishing/Word

%description tools
Tools to transform EOT font files into other formats. Only TTF is
supported currently.

%prep
%autosetup -p1 -n %{name}-%{srcver}

%build
%configure \
    --disable-silent-rules \
    --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# 0.0.4 sorts below the previous release, 0.01, for both rpm and pkg-config,
# which breaks consumers checking for "libeot >= 0.01" (LibreOffice). Publish
# the package version (0.04) in the .pc file instead.
sed -i 's/^Version: .*/Version: %{version}/' %{buildroot}%{_libdir}/pkgconfig/libeot.pc

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE
%{_libdir}/libeot.so.*

%files devel
%{_libdir}/libeot.so
%{_libdir}/pkgconfig/libe*.pc
%{_includedir}/libeot

%files tools
%doc PATENTS
%{_bindir}/*

%changelog
