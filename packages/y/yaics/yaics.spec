#
# spec file for package yaics
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           yaics
Version:        0.6
Release:        0
Summary:        A simple GNU social client written in C++/Qt
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://gitlab.com/stigatle/yaics
Source:         https://gitlab.com/stigatle/yaics/-/archive/%{version}-1/yaics-%{version}-1.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)

%description
Yaics is a simple GNU social client written in C++ and Qt and
licensed under the GNU GPL 3.0 (or later).

%prep
%setup -q -n %{name}-%{version}-1

%build
%qmake5 PREFIX=%{_prefix}
%make_build

%install
%qmake5_install

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
