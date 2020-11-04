#
# spec file for package lxqt-qtplugin
#
# Copyright (c) 2020 SUSE LLC
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


Name:           lxqt-qtplugin
Version:        0.16.0
Release:        0
Summary:        LXQt platform integration plugin for Qt 5
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libexif-devel
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  pkgconfig(Qt5Gui) >= 5.12.0
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xdg) >= 3.6.0
BuildRequires:  pkgconfig(Qt5XdgIconLoader)
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(libfm-qt) >= %{version}
BuildRequires:  pkgconfig(lxqt) >= %{version}
%if 0%{?fedora_version}
%requires_eq    qt5-qtbase-gui
%else
%requires_eq    libQt5Gui5
%endif

%description
With this plugin, all Qt-based programs can adopt settings of
LXQt, such as the icon theme.

To use the plugin in Qt5, we have to export the environment
variable QT_QPA_PLATFORMTHEME=lxqt. Then every Qt5 program
can load the theme plugin.
If, for some unknown reasons, the plugin is not loaded, we can
debug the plugin by exporting QT_DEBUG_PLUGINS=1.
Then, Qt5 will print detailed information and error messages
about all plugins in the console when running any Qt5 programs.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%files
%license LICENSE
%doc AUTHORS README.md
%dir %{_libdir}/qt5/plugins
%dir %{_libdir}/qt5/plugins/platformthemes
%{_libdir}/qt5/plugins/platformthemes/libqtlxqt.so

%changelog
