#
# spec file
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2018–2019 Markus S. <kamikazow@opensuse.org>
# Copyright (c) 2016      Yuriy Gorodilin <yurg27@gmail.com>
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


%global flavor @BUILD_FLAVOR@%{nil}
%define name_suffix %{nil}
%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{flavor}" == "qt5"
#
# Qt5 Flavor
#
  %define pkg_name QGnomePlatform-qt5
  %define qt5 1
  %define qt_min_version 5.15.2
  %define _qt_plugindir %{_libqt5_plugindir}
  %define name_suffix -qt5
%endif
%if "%{flavor}" == "qt6"
#
# Qt6 Flavor
#
  %define pkg_name QGnomePlatform-qt6
  %define qt6 1
  %define qt_min_version 6.2.0
  %define _qt_plugindir %{_qt6_pluginsdir}
  %define name_suffix -qt6
%endif

%define adwaitaqt_version 1.4.2

Name:           QGnomePlatform%{?name_suffix}
Version:        0.9.0
Release:        0
Summary:        A better Qt application inclusion under GNOME
#
# Most code is LGPL-2.1 or any later version but qgtk3dialoghelpers files,
# forked from Qt 5, let's us choose beteween LGPL-3.0 and GPL-2.0 or even
# GPL-3.0 or still any later version approved by the KDE Free Qt Foundation.
# So we're better off using LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only on
# behalf of qgtk3dialoghelpers' source code rather the using *-or-later and
# risk getting screwed over by KDE Free Qt Foundation someday.
#
# This is what the license tag should look like:
#   LGPL-2.1-or-later AND (LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-only))
#
# But since we do not have support for such nested logic let us use:
#   LGPL-2.1-or-later AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only)
#
# NOTE: Keep an eye on it so that the bots don't mess up the logic, ordey is
#       important here.
#       You may have to append --noservice to 'osc build'/'osc checkin'.
#
License:        (GPL-2.0-only OR LGPL-3.0-only OR GPL-3.0-only) AND LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://github.com/FedoraQt/QGnomePlatform/
Source:         %{url}/archive/%{version}.tar.gz#/QGnomePlatform-%{version}.tar.gz
Patch0:         fix-XSetTransientForHint.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
# QGnomePlatform relies on glib's pkgconfig file to find gsettings files
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
%if 0%{?qt5}
#
# Qt5 Buildtime Dependencies
#
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-qtwayland-private-headers-devel
BuildRequires:  cmake(AdwaitaQt) >= %{adwaitaqt_version}
BuildRequires:  cmake(Qt5Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt_min_version}
BuildRequires:  cmake(Qt5ThemeSupport)
BuildRequires:  cmake(Qt5WaylandClient) >= %{qt_min_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt_min_version}
BuildRequires:  cmake(Qt5XkbCommonSupport)
Supplements:    (libQt5Gui5 and gnome-session)
Obsoletes:      QGnomePlatform =< 0.8.4
Provides:       QGnomePlatform = %{version}
%endif
%if 0%{?qt6}
#
# Qt6 Buildtime Dependencies
#
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-wayland-private-devel
# Use cmake() instead of pkgconfig() to make Leap 15.4's life easier.
BuildRequires:  cmake(AdwaitaQt6) >= %{adwaitaqt_version}
BuildRequires:  cmake(Qt6Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt_min_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt_min_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt_min_version}
Supplements:    (libQt6Gui6 and gnome-session)
%endif
#
# Runtime Dependencies
#
Requires:       adwaita-%{flavor}

%description
QGnomePlatform is a Qt Platform Theme designed to use as many of the GNOME
settings as possible in unmodified Qt applications. It allows Qt applications
to fit into the environment as well as possible.

%prep
%autosetup -p1 -n QGnomePlatform-%{version}

%build
%if 0%{?qt6}
%cmake_qt6                 \
%else
%cmake                     \
%endif
    %{?qt5:-D USE_QT6=OFF} \
    %{?qt6:-D USE_QT6=ON}  \
    %{nil}

%if 0%{?qt6}
%qt6_build
%else
%cmake_build
%endif

%install
%if 0%{?qt6}
%{qt6_install}
%else
%cmake_install
%endif

%files
%doc README.md
%license LICENSE
# Qt6 SONAME is libqgnomeplatform6.so so expand a "6" when appropriate.
%{_libdir}/libqgnomeplatform%{?qt6:6}.so
%dir %{_qt_plugindir}
%dir %{_qt_plugindir}/platformthemes
%{_qt_plugindir}/platformthemes/libqgnomeplatformtheme.so
%{_qt_plugindir}/wayland-decoration-client/libqgnomeplatformdecoration.so

%changelog
