#
# spec file for package bibletime
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# Internal QML import
%global __requires_exclude qmlimport\\(BibleTime.*

Name:           bibletime
Version:        3.2.0
Release:        0
Summary:        A Bible study tool
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Other
URL:            http://www.bibletime.info/
Source0:        https://github.com/bibletime/bibletime/releases/download/v%{version}/bibletime-%{version}.tar.xz
Source1:        bibletime-rpmlintrc
BuildRequires:  cmake >= 3.25
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(libclucene-core) >= 2.0
BuildRequires:  pkgconfig(sword) >= 1.8.1
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
%autosetup -p1

%build
%cmake_qt6 \
  -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
  -DBT_DOCBOOK_XSL_HTML_CHUNK_XSL=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/html/chunk.xsl \
  -DBT_DOCBOOK_XSL_PDF_DOCBOOK_XSL=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/fo/docbook.xsl
%qt6_build

%install
%qt6_install

%fdupes -s %{buildroot}

%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/info.%{name}.BibleTime.desktop Education Humanities

%files
%doc README.md
%license LICENSE
%{_bindir}/bibletime
%{_datadir}/icons/*
%{_datadir}/applications/info.%{name}.BibleTime.desktop
%dir %{_datadir}/bibletime
%{_datadir}/bibletime/*
%dir %{_docdir}/bibletime
%{_docdir}/bibletime/*
%{_datadir}/metainfo/info.bibletime.BibleTime.metainfo.xml

%changelog
