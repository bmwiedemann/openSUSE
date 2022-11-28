#
# spec file for package lagrange
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


%define app_id fi.skyjake.Lagrange
Name:           lagrange
Version:        1.14.1
Release:        0
Summary:        Desktop GUI client for browsing Geminispace
License:        BSD-2-Clause
URL:            https://gmi.skyjake.fi/lagrange
Source0:        https://git.skyjake.fi/skyjake/lagrange/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zip
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)

%description
Lagrange is a desktop GUI client for browsing Geminispace. It offers modern
conveniences familiar from web browsers, such as smooth scrolling, inline image
viewing, multiple tabs, visual themes, Unicode fonts, bookmarks, history, and
page outlines.

%prep
%setup -q

%build
%cmake -DTFDN_ENABLE_SSE41=NO
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -G "Gemini Client" %{app_id} WebBrowser

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/%{app_id}.png
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{app_id}.appdata.xml
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
