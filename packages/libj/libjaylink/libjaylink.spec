#
# spec file for package libjaylink
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


Name:           libjaylink
Version:        0.5.0
Release:        0
Summary:        USB interface library for J-Link
License:        LGPL-2.1-or-later
URL:            https://gitlab.zapb.de/libjaylink/libjaylink.git
Source:         libjaylink-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.16
BuildRequires:  pkgconfig(udev)
Requires(post): udev
Requires(postun): udev
Provides:       libjaylink0:%{_udevrulesdir}/60-libjaylink.rules

%description
Library for accessing Segger J-Link USB devices.

%package -n libjaylink0
Summary:        USB interface library for J-Link
Recommends:     libjaylink

%description -n libjaylink0
Library for accessing Segger J-Link USB devices.

%package devel
Summary:        USB interface library for J-Link -- development files
Requires:       libjaylink0 = %{version}-%{release}

%description devel
Library for accessing Segger J-Link USB devices.

This sub-package contains the development files.

%prep
%setup -q

%build
%meson -Dusb=enabled
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_udevrulesdir}
sed -e 's/GROUP="plugdev"/GROUP="users"/' <contrib/60-libjaylink.rules >%{buildroot}%{_udevrulesdir}/60-libjaylink.rules

%post
%udev_rules_update

%postun
%udev_rules_update

%ldconfig_scriptlets -n libjaylink0

%files
%license COPYING
%{_udevrulesdir}/60-libjaylink.rules

%files -n libjaylink0
%{_libdir}/libjaylink.so.0*

%files devel
%{_includedir}/libjaylink/
%{_libdir}/libjaylink.so
%{_libdir}/pkgconfig/libjaylink.pc

%changelog
