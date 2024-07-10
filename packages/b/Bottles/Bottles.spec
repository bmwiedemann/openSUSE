#
# spec file for package Bottles
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


%global appid com.usebottles.bottles
Name:           Bottles
Version:        51.12
Release:        0
Summary:        Easily manage wineprefix using environments
License:        GPL-3.0-or-later
Group:          System/Emulators/Other
URL:            https://usebottles.com/
Source0:        https://github.com/bottlesdevs/Bottles/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         disable-core-preferences.patch
BuildRequires:  blueprint-compiler
BuildRequires:  fdupes
BuildRequires:  gtk4-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(python3)
Requires:       ImageMagick
Requires:       cabextract
Requires:       dconf
Requires:       gtk4
Requires:       libadwaita-1-0 >= 1.2
Requires:       p7zip
Requires:       patool
Requires:       python3-Markdown
Requires:       python3-PyYAML
Requires:       python3-chardet
Requires:       python3-fvs
Requires:       python3-gobject
Requires:       python3-icoextract
Requires:       python3-pathvalidate
Requires:       python3-pefile
Requires:       python3-pycurl
Requires:       python3-requests
Requires:       typelib-1_0-Adw-1 >= 1.2
Requires:       typelib-1_0-GtkSource-4
Requires:       typelib-1_0-GtkSource-5
Requires:       typelib-1_0-Handy-1_0
Requires:       typelib-1_0-WebKit2-4_0
Requires:       vkbasalt-cli
Requires:       xdpyinfo
Suggests:       wine
Suggests:       dxvk
Suggests:       gamemoded
Suggests:       libbsd
Suggests:       libcaca
Suggests:       libcapi20
Suggests:       libgamemode0
Suggests:       libgamemodeauto0
Suggests:       libpcap1
Suggests:       libvkd3d-shader1
Suggests:       libvkd3d1
Suggests:       samba-winbind
Suggests:       vkbasalt
BuildArch:      noarch
Obsoletes:      bottles >= 2022
Provides:       bottles = %{version}-%{release}
%lang_package

%description
Bottles is an application that allows you to easily manage windows prefixes on your favorite Linux distribution.

Windows prefixes are environments where it is possible to run Windows software using runners.
Runners are compatibility layers capable of running Windows applications on Linux systems.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file %{appid}
%find_lang bottles

%fdupes %{buildroot}

%files
%license COPYING.md
%doc README.md
%{_bindir}/bottles
%{_bindir}/bottles-cli
%{_datadir}/bottles
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}*.svg
%{_datadir}/icons/hicolor/*/apps/bottle-symbolic.svg
%{_datadir}/icons/hicolor/symbolic/apps/bottles-steam-symbolic.svg
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml

%files lang -f bottles.lang

%changelog
