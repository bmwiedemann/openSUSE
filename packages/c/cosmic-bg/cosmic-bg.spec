#
# spec file for package cosmic-bg
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


%define         appname com.system76.CosmicBackground
Name:           cosmic-bg
Version:        1.0.0~alpha4+0
Release:        0
Summary:        COSMIC service for backgrounds
License:        MPL-2.0
URL:            https://github.com/pop-os/cosmic-bg
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  mold
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
COSMIC session service which applies backgrounds to displays.
Supports the following features:

    Supports common image formats supported by image-rs
    8 and 10-bit background surface layers
    Use of colors and gradients for backgrounds
    Per-display background application
    Wallpaper slideshows that alternate between backgrounds periodically

%prep
%autosetup -a1

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%check
%{cargo_test}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/cosmic
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appname}-symbolic.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
