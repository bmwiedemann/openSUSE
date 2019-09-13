#
# spec file for package libgsf
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


Name:           libgsf
Version:        1.14.46
Release:        0
Summary:        I/O library for dealing with structured file formats
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://www.gnome.org
Source:         http://download.gnome.org/sources/libgsf/1.14/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  intltool
BuildRequires:  libbz2-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.26.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.0.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.16
Requires:       libgsf-1-114

%description
The libgsf library is an extensible I/O abstraction library for dealing
with structured file formats.

%package tools
Summary:        Tools from libgsf, a structured file formats handling library
Group:          Productivity/Office/Other
Recommends:     %{name}-lang

%description tools
The libgsf library is an extensible I/O abstraction library for dealing
with structured file formats.

%package -n gsf-office-thumbnailer
Summary:        Office files thumbnailer for the GNOME desktop
Group:          Productivity/Office/Other

%description -n gsf-office-thumbnailer
This package provides a thumbnailer for office files.

%package 1-114
Summary:        I/O library for dealing with structured file formats
Group:          System/Libraries
Recommends:     %{name}-lang
# To make lang package installable
Provides:       %{name} = %{version}
# With libgsf 1.14.22 (first in 12.2), gnome-vfs and bonobo support got dropped, so no more gnome package.
Obsoletes:      libgsf-gnome < 1.14.22
# With libgsf 1.14.23 (first in 12.2), we prefer to use introspection
Obsoletes:      python-gsf < 1.14.23
#

%description 1-114
The libgsf library is an extensible I/O abstraction library for dealing
with structured file formats.

%package -n typelib-1_0-Gsf-1
Summary:        Introspection bindings for the GNOME desktop Office files thumbnailer
Group:          System/Libraries

%description -n typelib-1_0-Gsf-1
The libgsf library is an extensible I/O abstraction library for dealing
with structured file formats.

%package devel
Summary:        Development files for libgsf, a structured file format handling library
Group:          Development/Libraries/GNOME
Requires:       libgsf-1-114 = %{version}
Requires:       typelib-1_0-Gsf-1 = %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}
#

%description devel
The libgsf library is an extensible I/O abstraction library for dealing
with structured file formats.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure --disable-static \
        --enable-introspection
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print

%post 1-114 -p /sbin/ldconfig
%postun 1-114 -p /sbin/ldconfig

%files tools
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/gsf
%{_bindir}/gsf-vba-dump
%{_mandir}/man1/gsf.1%{ext_man}
%{_mandir}/man1/gsf-vba-dump.1%{ext_man}

%files -n gsf-office-thumbnailer
%{_bindir}/gsf-office-thumbnailer
%{_mandir}/man1/gsf-office-thumbnailer.1%{ext_man}
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gsf-office.thumbnailer

%files 1-114
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgsf-1.so.*

%files -n typelib-1_0-Gsf-1
%{_libdir}/girepository-1.0/Gsf-1.typelib

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libgsf-1
%{_datadir}/gir-1.0/Gsf-1.gir
%{_datadir}/gtk-doc/html/gsf/

%files lang -f %{name}.lang

%changelog
