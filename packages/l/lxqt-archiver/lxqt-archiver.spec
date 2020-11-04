#
# spec file for package lxqt-archiver
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


Name:           lxqt-archiver
Version:        0.3.0
Release:        0
Summary:        LXQt File Archiver
License:        GPL-2.0-or-later
Group:          System/GUI/LXQt
URL:            http://www.lxqt.org
Source0:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  libexif-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.12.0
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libfm-qt) >= 0.16.0
Requires:       bsdtar
Requires(post): desktop-file-utils
Requires(pre):  desktop-file-utils

%description
LXQt file archiver.

%lang_package

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install

%find_lang %{name} --with-qt

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_bindir}/lxqt-archiver
%dir %{_libexecdir}/lxqt-archiver
%{_libexecdir}/lxqt-archiver/isoinfo.sh
%{_datadir}/applications/lxqt-archiver.desktop
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/scalable/apps/lxqt-archiver.svg

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt-archiver/
%dir %{_datadir}/lxqt-archiver/translations/
%{_datadir}/lxqt-archiver/translations/*.qm

%changelog
