#
# spec file for package qlipper
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        5.1.1
Release:        0
Summary:        Clipboard history applet
License:        GPL-2.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://github.com/pvanek/qlipper
Source:         https://github.com/pvanek/qlipper/archive/%{version}.tar.gz
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  lxqt-build-tools-devel >= 0.5.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
A clipboard history applet.

%lang_package

%prep
%setup -q

%build
%cmake \
    -DENABLE_LXQT_AUTOSTART=ON
make %{?_smp_mflags}

%install
%cmake_install
%if 0%{?suse_version}
%suse_update_desktop_file -r -u %{name} Utility DesktopUtility
%endif

%find_lang %{name} --with-qt

%files
%license COPYING
%doc CHANGELOG README
%{_sysconfdir}/xdg/autostart/lxqt-%{name}-autostart.desktop
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations

%changelog
