#
# spec file for package djvulibre-djview4
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        4.10.6
Release:        0
Summary:        Portable DjVu Qt4 Based Viewer and Browser Plugin
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
Url:            http://djvu.sourceforge.net/djview4.html
Source:         http://downloads.sourceforge.net/djvu/djview-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libqt5-linguist
BuildRequires:  pkg-config
%if 0%{suse_version} >= 1550
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  update-desktop-files
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
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Conflicts:      djvulibre-djview3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
DjView4 is a viewer and browser plugin for DjVu documents,based on the
DjVuLibre-3.5 library and the Qt4 toolkit.

%prep
%setup -q -n djview-%{version}
sed -i 's|PLUGINSDIR|%{_libdir}/browser-plugins|g' nsdejavu/nsdejavu.1.in 

%build
export QMAKE=/usr/bin/qmake-qt5
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} pluginsdir=%{_libdir}/browser-plugins install %{?_smp_mflags}
ln -s %{_bindir}/djview %{buildroot}%{_bindir}/djview4
%suse_update_desktop_file -i djvulibre-djview4 Qt Graphics Viewer

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc COPYING COPYRIGHT NEWS README README_translations
%doc %{_mandir}/man1/*
%{_bindir}/djview4
%{_bindir}/djview
%{_libdir}/browser-plugins
%{_datadir}/djvu/djview4/
%{_datadir}/applications/djvulibre-djview4.desktop
%{_datadir}/icons/hicolor
%dir %{_datadir}/djvu/

%changelog
