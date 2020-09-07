#
# spec file for package bibletime
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012-2014 Lars Vogdt
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


Name:           bibletime
Version:        3.0
Release:        0
Summary:        A Bible study tool
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Other
URL:            http://www.bibletime.info/
Source0:        https://github.com/bibletime/bibletime/releases/download/v%{version}/bibletime-%{version}.tar.xz
Source1:        bibletime-rpmlintrc
# PATCH-FIX-UPSTREAM: Fix bug #260 Move DisplayView.qml to share/bibletime/qml
Patch0:         displayview.patch
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebKit)
BuildRequires:  cmake(Qt5WebKitWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(libclucene-core)
BuildRequires:  pkgconfig(sword) >= 1.7
# Dependencies for building documentation
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fop
BuildRequires:  libxslt-tools
BuildRequires:  po4a
Recommends:     sword-bible
Recommends:     sword-commentary
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
BibleTime is a Bible study program.

The software uses the SWORD programming library to work with over 200 free
Bible texts, commentaries, dictionaries and books provided by the Crosswire
Bible Society.

BibleTime provides easy handling of digitalized texts (Bibles, commentaries and
lexicons) and powerful features to work with these texts (search in texts,
write own notes, save, print etc.).

%prep
%setup -q
%patch0 -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DBT_DOCBOOK_XSL_HTML_CHUNK_XSL=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/html/chunk.xsl \
  -DBT_DOCBOOK_XSL_PDF_DOCBOOK_XSL=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/fo/docbook.xsl
%cmake_build

%install
%cmake_install

%fdupes -s %{buildroot}

%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/info.%{name}.BibleTime.desktop Education Humanities

%files
%doc ChangeLog README.md
%license LICENSE
%{_bindir}/bibletime
%{_datadir}/icons/*
%{_datadir}/applications/info.%{name}.BibleTime.desktop
%dir %{_datadir}/bibletime
%{_datadir}/bibletime/*
%dir %{_datadir}/doc/bibletime
%{_datadir}/doc/bibletime/*
%{_datadir}/metainfo/info.bibletime.BibleTime.metainfo.xml

%changelog
