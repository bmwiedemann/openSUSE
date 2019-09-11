#
# spec file for package geeqie
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


Name:           geeqie
Version:        1.5.1
Release:        0
Summary:        Lightweight Gtk+ based image viewer
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            http://www.geeqie.org/
Source0:        http://www.geeqie.org/%{name}-%{version}.tar.xz
Source1:        http://www.geeqie.org/%{name}-%{version}.tar.xz.asc
Source2:        geeqie.keyring
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
# Needed to bootstrap the tarball
BuildRequires:  libtool
BuildRequires:  lirc-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(champlain-0.12) >= 0.12
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.12
BuildRequires:  pkgconfig(clutter-1.0) >= 1.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.0
BuildRequires:  pkgconfig(exiv2) >= 0.11
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2)
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
Recommends:     %{name}-lang
%if 0%{?suse_version} >= 1330
BuildRequires:  pkgconfig(lua5.1)
%endif

%description
Geeqie is a lightweight image viewer for Linux, BSDs and compatibles.

%lang_package

%prep
%setup -q

%build
# Needed to bootstrap
intltoolize --copy --force --automake
autoreconf -fvi
%configure \
        --enable-lirc \
        --with-readmedir=%{_defaultdocdir}/%{name} \
        --enable-map \
        %{nil}
make %{?_smp_mflags} CFLAGS="-Wno-deprecated-declarations"

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}
%fdupes %{buildroot}

# Already in the license directory
rm %{buildroot}%{_docdir}/%{name}/COPYING

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS ChangeLog ChangeLog.html NEWS TODO README.md README.lirc
%{_bindir}/geeqie
%{_datadir}/applications/geeqie.desktop
%{_datadir}/geeqie/
%{_datadir}/pixmaps/geeqie.png
%{_libexecdir}/geeqie/
%{_mandir}/man1/geeqie.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
