#
# spec file for package geeqie
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


Name:           geeqie
Version:        1.7.3
Release:        0
Summary:        Lightweight Gtk+ based image viewer
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            http://www.geeqie.org
Source0:        https://github.com/BestImageViewer/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/BestImageViewer/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        geeqie.keyring

BuildRequires:  c++_compiler
BuildRequires:  docbook_4
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
# Needed to bootstrap the tarball
BuildRequires:  libtool
BuildRequires:  lirc-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-lxml
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  yelp-xsl
BuildRequires:  pkgconfig(champlain-0.12) >= 0.12
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.12
BuildRequires:  pkgconfig(clutter-1.0) >= 1.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.0
BuildRequires:  pkgconfig(ddjvuapi) >= 3.5.27
BuildRequires:  pkgconfig(exiv2) >= 0.11
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(lcms2) >= 2.0
BuildRequires:  pkgconfig(libarchive) >= 3.4.0
BuildRequires:  pkgconfig(libheif) >= 1.3.2
# Not yet in Factory:
#BuildRequires:  pkgconfig(libjxl) >= 0.3.7
# Not yet in Factory:
#BuildRequires:  pkgconfig(libffmpegthumbnailer) >= 2.1.0
BuildRequires:  pkgconfig(libopenjp2) >= 2.3.0
%if 0%{?suse_version} >= 1540
# Too old version in 15.3:
BuildRequires:  pkgconfig(libraw) >= 0.20
%endif
BuildRequires:  pkgconfig(libwebp) >= 0.6.1
BuildRequires:  pkgconfig(lua5.1)
BuildRequires:  pkgconfig(poppler-glib) >= 0.62
Requires(post): update-desktop-files
Requires(postun):update-desktop-files

%description
Geeqie is a lightweight image viewer for Linux, BSDs and compatibles.

%lang_package

%prep
%autosetup -p1

%build
# Needed to bootstrap
intltoolize --copy --force --automake
autoreconf -fvi
%configure \
        --enable-lirc \
        --with-readmedir=%{_defaultdocdir}/%{name} \
        --enable-map \
        %{nil}
%make_build CFLAGS="-Wno-deprecated-declarations"

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}
%fdupes %{buildroot}/%{_prefix}

# Already in the license directory
rm %{buildroot}%{_docdir}/%{name}/COPYING

%files
%license COPYING
%doc AUTHORS ChangeLog ChangeLog.html NEWS TODO README.md README.lirc
%doc %{_docdir}/geeqie/html
%{_bindir}/geeqie
%{_datadir}/applications/geeqie.desktop
%{_datadir}/geeqie/
%{_datadir}/pixmaps/geeqie.png
%{_datadir}/metainfo/org.geeqie.Geeqie.appdata.xml
%{_prefix}/lib/geeqie/
%{_mandir}/man1/geeqie.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
