#
# spec file for package wob
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


Name:           wob
Version:        0.14.2
Release:        0
Summary:        A lightweight overlay volume/backlight/progress/anything bar for Wayland
License:        ISC
Group:          System/X11/Utilities
URL:            https://github.com/francma/wob
Source0:        https://github.com/francma/wob/releases/download/%{version}/wob-%{version}.tar.gz
Source1:        https://github.com/francma/wob/releases/download/%{version}/wob-%{version}.tar.gz.sig
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/5C6DA024DDE27178073EA103F4B432D5D67990E3#/%{name}.keyring
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)

%description
A lightweight overlay volume/backlight/progress/anything bar for Wayland

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}.ini.5%{?ext_man}

%changelog
