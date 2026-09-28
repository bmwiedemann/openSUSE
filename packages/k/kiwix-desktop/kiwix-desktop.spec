#
# spec file for package kiwix-desktop
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define app_id org.kiwix.desktop
Name:           kiwix-desktop
Version:        2.5.1
Release:        0
Summary:        Offline reader for Web content
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL-3.0-or-later
URL:            https://github.com/kiwix/kiwix-desktop
Source0:        https://mirror.download.kiwix.org/release/kiwix-desktop/kiwix-desktop-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6WebChannel)
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(libkiwix)
Requires:       aria2

%description
Kiwix is an offline reader for Web content, primarily designed to make
Wikipedia available offline. It reads archives in the ZIM file format, a highly
compressed open format with additional metadata.

%prep
%autosetup -p1

%build
export CXXFLAGS="%{optflags} -Wno-sfinae-incomplete"
%qmake6 PREFIX=%{_prefix}
%qmake6_build

%install
%qmake6_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/metainfo/%{app_id}.appdata.xml
%{_datadir}/mime/packages/%{app_id}-mime.xml
%{_iconsdir}/hicolor/

%changelog

