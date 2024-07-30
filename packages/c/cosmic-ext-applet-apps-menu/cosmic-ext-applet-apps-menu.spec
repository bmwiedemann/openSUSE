#
# spec file for package cosmic-ext-applet-apps-menu
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


%define         appname dev.dominiccgeh.CosmicAppletAppsMenu
Name:           cosmic-ext-applet-apps-menu
Version:        0.1.6+git20240705.21c3063
Release:        0
Summary:        Category based menu for apps for COSMIC DE
License:        GPL-3.0-only
URL:            https://github.com/leb-kuchen/apps-menu-applet-for-cosmic_tm
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Patch0:         fix-binary-name.patch
Patch1:         fix-justfile.patch
BuildRequires:  cargo-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%suse_update_desktop_file %{appname}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{appname}.svg

%changelog
