#
# spec file for package cosmic-ext-applet-tailscale
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


%define         appname com.github.bhh32.GUIScaleApplet
Name:           cosmic-ext-applet-tailscale
Version:        2.0.0+1
Release:        0
Summary:        Tailscale applet for the COSMIC Desktop
License:        BSD-3-Clause
URL:            https://github.com/cosmic-utils/gui-scale-applet
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Patch0:         fix-justfile.patch
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(xkbcommon)

%description
This is a COSMIC applet for Tailscale. It has SSH and Allow Routes
enable/disable and Tail Drop functionality.

%prep
%autosetup -a1

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%suse_update_desktop_file %{appname}

%files
%license LICENSE
%doc README.md
%{_bindir}/gui-scale-applet
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/status/%{appname}.png

%changelog
