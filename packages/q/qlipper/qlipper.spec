#
# spec file for package qlipper
#
# Copyright (c) 2025 SUSE LLC
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


Name:           qlipper
Version:        6.0.0
Release:        0
Summary:        Clipboard history applet
License:        GPL-2.0-or-later
URL:            https://github.com/pvanek/qlipper
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-translations.patch
BuildRequires:  cmake >= 3.5.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)

%description
Lightweight and cross-platform clipboard history applet.

%lang_package

%prep
%autosetup -p1

%build
%cmake_qt6 \
    -DENABLE_LXQT_AUTOSTART=ON \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%qt6_build

%install
%qt6_install

%find_lang %{name} --with-qt

%files
%license COPYING
%doc CHANGELOG README
%config %{_sysconfdir}/xdg/autostart/lxqt-%{name}-autostart.desktop
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations

%changelog
