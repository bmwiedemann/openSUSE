#
# spec file for package pcmanfm-qt
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


Name:           pcmanfm-qt
Version:        2.0.0
Release:        0
Summary:        File manager and desktop icon manager
License:        GPL-2.0-or-later
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/pcmanfm-qt
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
#bsc#1100208 - mvetter@suse.de - set default openSUSE wallpaper
Patch0:         %{name}-default-wallpaper.patch
BuildRequires:  cmake >= 3.18.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt6Svg6
BuildRequires:  pkgconfig
BuildRequires:  cmake(LayerShellQt) >= 6.0.0
BuildRequires:  cmake(Qt6DBus) >= 6.6.0
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(fm-qt6)
BuildRequires:  cmake(lxqt2-build-tools) >= 2.0.0
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libmenu-cache) >= 1.1.0
%requires_eq    libQt6Svg6
#bsc#1128570 - mvetter@suse.de
Requires:       menu-cache
#bsc#1100208 - mvetter@suse.de
Requires:       wallpaper-branding-openSUSE
Recommends:     %{name}-lang = %{version}-%{release}
Recommends:     gnome-keyring-pam

%description
PCManFM-Qt is the Qt port of the LXDE file manager PCManFM

%lang_package

%prep
%autosetup -p1

%build
%cmake_qt6
%qt6_build

%install
%qt6_install
%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name} --with-qt

%files
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lxqt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-desktop-pref.desktop
%{_mandir}/man?/%{name}.?%{?ext_man}
%config %{_sysconfdir}/xdg/autostart/lxqt-desktop.desktop
%{_datadir}/%{name}/lxqt/settings.conf
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%license LICENSE

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%if 0%{?sle_version}
%{_datadir}/%{name}/translations/%{name}_???.qm
%endif

%changelog
