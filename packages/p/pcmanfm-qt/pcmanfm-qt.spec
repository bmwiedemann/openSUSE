#
# spec file for package pcmanfm-qt
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.2.1
Release:        0
Summary:        File manager and desktop icon manager
License:        GPL-2.0-or-later
Group:          System/GUI/LXQt
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
#bsc#1100208 - mvetter@suse.de - set default openSUSE wallpaper
Patch0:         pcmanfm-qt-default-wallpaper.patch
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools-devel >= 0.11.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  pkgconfig(Qt5Core) >= 5.15.0
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libfm-qt) >= 1.1.0
#bsc#1100208 - mvetter@suse.de
Requires:       wallpaper-branding-openSUSE
#bsc#1128570 - mvetter@suse.de
Requires:       menu-cache
Recommends:     %{name}-lang
Recommends:     gnome-keyring-pam

%description
PCManFM-Qt is the Qt port of the LXDE file manager PCManFM

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%cmake -DPULL_TRANSLATIONS=No

%install
%cmake_install
%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name} --with-qt

%files
%doc AUTHORS
%dir %{_datadir}/pcmanfm-qt
%dir %{_datadir}/pcmanfm-qt/lxqt
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man?/%{name}.?%{ext_man}
%config %{_sysconfdir}/xdg/autostart/lxqt-desktop.desktop
%{_datadir}/pcmanfm-qt/lxqt/settings.conf

%files lang -f %{name}.lang
%dir %{_datadir}/pcmanfm-qt
%{_datadir}/pcmanfm-qt/translations

%changelog
