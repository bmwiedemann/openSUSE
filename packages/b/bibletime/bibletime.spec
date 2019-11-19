#
# spec file for package bibletime
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.11.2
Release:        0
Summary:        A Bible study tool
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Other
Url:            http://www.bibletime.info/
Source0:        https://github.com/bibletime/bibletime/releases/download/v%{version}/bibletime-%{version}.tar.xz
Source1:        bibletime-rpmlintrc
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

%build
%cmake \
  -Wno-dev
%cmake_build

%install
%cmake_install
# move the icon to a valid place (/usr/share/icons is not valid... it has to be in a theme; hicolor as the usual falback)
# this is only a link pointing out of the icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/%{name}/icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
# then link back the icon into the app directory
ln -sf %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg %{buildroot}%{_datadir}/%{name}/icons/%{name}.svg
%fdupes -s %{buildroot}
sed -i "s|bibletime/handbook/index.html|bibletime/handbook/en/index.html|" %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file -r %{name} Education Humanities

%files
%{_bindir}/bibletime
%{_datadir}/icons/*
%{_datadir}/applications/bibletime.desktop
%dir %{_datadir}/bibletime
%{_datadir}/bibletime/*

%changelog
