#
# spec file for package xdg-desktop-portal-cosmic
#
# Copyright (c) 2024 SUSE LLC
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


Name:           xdg-desktop-portal-cosmic
Version:        0.1.0+git20240717.813352e
Release:        0
Summary:        COSMIC xdg portal
License:        GPL-3.0-only
URL:            https://github.com/pop-os/xdg-desktop-portal-cosmic
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xdg-desktop-portal)
BuildRequires:  pkgconfig(xkbcommon)

%description
This package contains the xdg portal implementation for COSMIC DE.

%prep
%autosetup -a1

%build
%make_build

%install
%make_install prefix=%{_prefix}

%check
%{cargo_test}

%files
%license LICENSE
%{_libexecdir}/%{name}
%{_iconsdir}/hicolor/scalable/actions/*.svg
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.cosmic.service
%{_datadir}/xdg-desktop-portal/cosmic-portals.conf
%{_datadir}/xdg-desktop-portal/portals/cosmic.portal

%changelog
