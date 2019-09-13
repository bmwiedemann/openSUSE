#
# spec file for package albert
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           albert
Version:        0.16.1
Release:        0
Summary:        Desktop agnostic launcher
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://albertlauncher.github.io/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Charts) >= 5.9
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.9
BuildRequires:  pkgconfig(Qt5Core) >= 5.9
BuildRequires:  pkgconfig(Qt5DBus) >= 5.9
BuildRequires:  pkgconfig(Qt5Gui) >= 5.9
BuildRequires:  pkgconfig(Qt5Network) >= 5.9
BuildRequires:  pkgconfig(Qt5Qml) >= 5.9
BuildRequires:  pkgconfig(Qt5Sql) >= 5.9
BuildRequires:  pkgconfig(Qt5Svg) >= 5.9
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.9
BuildRequires:  pkgconfig(Qt5Xml) >= 5.9
BuildRequires:  pkgconfig(muparser)
BuildRequires:  pkgconfig(python3)

%description
Access everything with virtually zero effort. Run applications,
open files or their paths, open bookmarks in your browser, search
the web, calculate things and a lot more.

%prep
%setup -q

%build
%cmake \
  -DCMAKE_INSTALL_LIBDIR="%{_lib}" \
  -DCMAKE_SHARED_LINKER_FLAGS=""   \
  -DCMAKE_SKIP_RPATH=OFF           \
  -DBUILD_VIRTUALBOX=OFF
%cmake_build

%install
%cmake_install

%suse_update_desktop_file %{name} Utility DesktopUtility

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
