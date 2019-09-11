#
# spec file for package libgnomecanvas
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


Name:           libgnomecanvas
Version:        2.30.3
Release:        0
Summary:        An Add-On for the GNOME User Interface Libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://gitlab.gnome.org/Archive/libgnomecanvas
Source:         ftp://ftp.gnome.org/pub/GNOME/sources/libgnomecanvas/2.20/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf

BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(gail) >= 1.9.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.10.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.2.0
BuildRequires:  pkgconfig(libart-2.0) >= 2.3.8
BuildRequires:  pkgconfig(pango) >= 1.0.1
BuildRequires:  pkgconfig(pangoft2) >= 1.0.1

%description
Libgnomecanvas is a graphical add-on for the GNOME User Interface
libraries.

%package -n libgnomecanvas-2-0
Summary:        An Add-On for the GNOME User Interface Libraries
Group:          System/Libraries
Recommends:     %{name}-lang
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
#

%description -n libgnomecanvas-2-0
Libgnomecanvas is a graphical add-on for the GNOME User Interface
libraries.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/GNOME
Requires:       libgnomecanvas-2-0 = %{version}
Provides:       libgnomecanvas-doc = %{version}
Obsoletes:      libgnomecanvas-doc < %{version}
#

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%configure \
	--with-pic \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name}-2.0
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgnomecanvas-2-0 -p /sbin/ldconfig
%postun -n libgnomecanvas-2-0 -p /sbin/ldconfig

%files -n libgnomecanvas-2-0
%license COPYING.LIB
%doc AUTHORS README NEWS ChangeLog
%{_libdir}/libgnomecanvas-2.so.*

%files lang -f %{name}-2.0.lang

%files devel
%{_includedir}/libgnomecanvas-2.0/
%{_libdir}/libgnomecanvas-2.so
%{_libdir}/pkgconfig/libgnomecanvas-2.0.pc
%{_datadir}/gtk-doc/html/libgnomecanvas/
# Own these repositories to not depend on gtk-doc while building:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html

%changelog
