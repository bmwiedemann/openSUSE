#
# spec file for package lagrange
#
# Copyright (c) 2024 SUSE LLC
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


%define gui_app_id fi.skyjake.Lagrange
%define tui_app_id fi.skyjake.clagrange

Name:           lagrange
Version:        1.18.4
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
BuildRequires:  pkgconfig(ncursesw) >= 6
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)

%description
Lagrange is a desktop GUI client for browsing Geminispace. It offers modern
conveniences familiar from web browsers, such as smooth scrolling, inline image
viewing, multiple tabs, visual themes, Unicode fonts, bookmarks, history, and
page outlines.

%package -n clagrange
Summary:        TUI client for browsing Geminispace

%description -n clagrange
Clagrange is a TUI client for browsing Geminispace.

%prep
%setup -q

%build
%cmake \
    -DTFDN_ENABLE_SSE41=NO \
    -DENABLE_TUI=YES
%cmake_build

%install
%cmake_install
%suse_update_desktop_file %{gui_app_id} WebBrowser
%suse_update_desktop_file %{tui_app_id} WebBrowser

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{gui_app_id}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/%{gui_app_id}.png
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{gui_app_id}.appdata.xml
%{_mandir}/man1/%{name}.1%{ext_man}

%files -n clagrange
%{_bindir}/clagrange
%{_datadir}/applications/%{tui_app_id}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/%{tui_app_id}.png

%changelog
