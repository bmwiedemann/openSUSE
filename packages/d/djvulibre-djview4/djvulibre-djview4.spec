#
# spec file for package djvulibre-djview4
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


Name:           djvulibre-djview4
Version:        4.12.3
Release:        0
Summary:        Portable DjVu Qt4 Based Viewer and Browser Plugin
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://djvu.sourceforge.net/djview4.html
Source:         https://downloads.sourceforge.net/djvu/djview-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libtool
BuildRequires:  pkgconfig
%if 0%{suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
Requires:       djvulibre >= 3.5.18
%if 0%{?suse_version} < 1550
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%endif
Conflicts:      djvulibre-djview3

%description
DjView4 is a viewer and browser plugin for DjVu documents, based on the
DjVuLibre library and the Qt toolkit.

%prep
%autosetup -p1 -n djview-%{version}
sed -i 's|PLUGINSDIR|%{_libdir}/browser-plugins|g' nsdejavu/nsdejavu.1.in

%build
export QMAKE=%{_bindir}/qmake-qt5
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
%make_build

%install
%make_install pluginsdir=%{_libdir}/browser-plugins
rm -f %{buildroot}%{_libdir}/browser-plugins/*.la
install -m 0644 desktopfiles/djview.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/djvulibre-djview4.svg
rm -f %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/djvulibre-djview4.svgz
ln -s %{_bindir}/djview %{buildroot}%{_bindir}/djview4

%if 0%{?suse_version} < 1550
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license COPYING COPYRIGHT
%doc NEWS README README_translations
%{_mandir}/man1/*
%{_bindir}/djview4
%{_bindir}/djview
%{_libdir}/browser-plugins/nsdejavu.so
%dir %{_datadir}/djvu/
%{_datadir}/djvu/djview4/
%{_datadir}/applications/djvulibre-djview4.desktop
%{_datadir}/icons/hicolor/*/mimetypes/djvulibre-djview4.*

%changelog
