#
# spec file for package quiterss
#
# Copyright (c) 2019 SUSE LLC
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


Name:           quiterss
Version:        0.19.2
Release:        0
Summary:        RSS/Atom aggregator
License:        GPL-3.0-or-later
Group:          Productivity/Networking/News/Utilities
URL:            https://www.quiterss.org
Source:         https://quiterss.org/files/%{version}/QuiteRSS-%{version}-src.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(sqlite3)
Requires:       libQt5Sql5-sqlite
Recommends:     %{name}-lang = %{version}

%description
QuiteRSS is a RSS/Atom news feed reader.

%lang_package

%prep
%setup -q -c
dos2unix AUTHORS CHANGELOG README.md

%build
%qmake5 PREFIX=%{_prefix}
%make_jobs

%install
%qmake5_install
%find_lang %{name} --with-qt --without-mo
%suse_update_desktop_file %{name}
%fdupes %{buildroot}

%files
%doc AUTHORS CHANGELOG README.md
%license COPYING
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/sound
%{_datadir}/%{name}/style

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/lang

%changelog
