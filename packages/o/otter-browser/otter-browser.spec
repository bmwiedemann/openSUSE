#
# spec file for package otter-browser
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.0.03
Release:        0
Summary:        Web browser with aspects of Opera
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://otter-browser.org/
Source:         https://github.com/OtterBrowser/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.1
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  sonnet-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.6
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.9
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.9
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(hunspell) >= 1.5.1
Recommends:     %{name}-lang

%description
Otter Browser is a web browser that recreates some aspects of
the classic Opera web browser (version 12.x) using the Qt framework.

%lang_package

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install
%find_lang %{name} --with-qt

%files
%license COPYING
%doc CHANGELOG CONTRIBUTING.md README.md TODO
%{_bindir}/%{name}
%exclude %{_datadir}/%{name}/locale/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang
%{_datadir}/%{name}/locale/

%changelog
