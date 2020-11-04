#
# spec file for package otter-browser
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


Name:           otter-browser
Version:        1.0.01
Release:        0
Summary:        Web browser with aspects of Opera
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
Url:            https://otter-browser.org/
Source:         https://github.com/OtterBrowser/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  sonnet-devel
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.4
BuildRequires:  pkgconfig(Qt5Core) >= 5.4
BuildRequires:  pkgconfig(Qt5DBus) >= 5.4
BuildRequires:  pkgconfig(Qt5Gui) >= 5.4
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.4
BuildRequires:  pkgconfig(Qt5Network) >= 5.4
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.4
BuildRequires:  pkgconfig(Qt5Script) >= 5.4
BuildRequires:  pkgconfig(Qt5Sql) >= 5.4
BuildRequires:  pkgconfig(Qt5Svg) >= 5.4
BuildRequires:  pkgconfig(Qt5WebKit) >= 5.4
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.4
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4
BuildRequires:  pkgconfig(Qt5XmlPatterns) >= 5.4
BuildRequires:  pkgconfig(hunspell) >= 1.3.0
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.9
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.9
%else
BuildRequires:  update-desktop-files
%endif

%description
Otter Browser is a web browser that recreates some aspects of
the classic Opera web browser (version 12.x) using the Qt framework.

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install
%find_lang %{name} --with-qt

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc CHANGELOG CONTRIBUTING.md README.md TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man?/%{name}.?%{?ext_man}

%changelog
