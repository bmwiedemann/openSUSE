#
# spec file for package gnome-directory-thumbnailer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gnome-directory-thumbnailer
Version:        0.1.10
Release:        0
Summary:        Directory Thumbnailer
License:        LGPL-2.1-or-later
Group:          Productivity/Office/Other
URL:            https://wiki.gnome.org/GnomeDirectoryThumbnailer
Source0:        http://download.gnome.org/sources/gnome-directory-thumbnailer/0.1/%{name}-%{version}.tar.xz
BuildRequires:  intltool >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.36.5
BuildRequires:  pkgconfig(gio-2.0) >= 2.22.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.35.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 2.2.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
Recommends:     %{name}-lang

%description
GNOME thumbnailer to generate thumbnails for directories.

%lang_package

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc ChangeLog NEWS README
%{_bindir}/gnome-directory-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gnome-directory-thumbnailer.thumbnailer

%files lang -f %{name}.lang

%changelog
