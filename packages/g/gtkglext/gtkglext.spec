#
# spec file for package gtkglext
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


%define git_commit 8c13cc48
%define git_date 20110529
Name:           gtkglext
Version:        1.2.0git%{git_date}
Release:        0
Summary:        OpenGL Extension to GTK
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://projects.gnome.org/gtkglext/
# git clone git://git.gnome.org/gtkglext
# git archive %{git_commit} --prefix=gtkglext-git%{git_date}/ | bzip2 > ../gtkglext-git%{git_date}.tar.bz2
Source:         %{name}-git%{git_date}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freeglut-devel
# For directory ownership:
BuildRequires:  gtk-doc
BuildRequires:  libdrm-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20

%description
GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
that support OpenGL rendering in GTK and GtkWidget API add-ons, to make
GTK+ widgets OpenGL-capable.

%package -n libgtkglext-x11-1_0-0
Summary:        OpenGL Extension to GTK
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libgtkglext-x11-1_0-0
GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
that support OpenGL rendering in GTK and GtkWidget API add-ons, to make
GTK+ widgets OpenGL-capable.

%package devel
Summary:        OpenGL Extension to GTK
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       Mesa-devel
Requires:       libgtkglext-x11-1_0-0 = %{version}
# Those are listed as Libs in gdkglext-1.0.pc, and therefore are not
# automatically added
Requires:       pkgconfig(gl)

%description devel
GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
which support OpenGL rendering in GTK, and GtkWidget API add-ons to
make GTK+ widgets OpenGL-capable.

%package doc
Summary:        Documentation of the OpenGL Extension to GTK
License:        LGPL-2.1-or-later
Group:          Documentation/HTML
Requires:       libgtkglext-x11-1_0-0 = %{version}

%description doc
This package contains additional documentation for gtkglext.

GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
which support OpenGL rendering in GTK, and GtkWidget API add-ons to
make GTK+ widgets OpenGL-capable.

%prep
%setup -q -n %{name}-git%{git_date}

%build
./bootstrap
# Required for gtkglext-1.2.0:
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgtkglext-x11-1_0-0 -p /sbin/ldconfig
%postun -n libgtkglext-x11-1_0-0 -p /sbin/ldconfig

%files -n libgtkglext-x11-1_0-0
# NEWS is empty
%license COPYING
%doc AUTHORS README TODO
%{_libdir}/libgdkglext-x11-1.0.so.*
%{_libdir}/libgtkglext-x11-1.0.so.*

%files devel
# %{_datadir}/aclocal/gtkglext-1.0.m4
%{_libdir}/gtkglext-1.0/
%{_libdir}/libgdkglext-x11-1.0.so
%{_libdir}/libgtkglext-x11-1.0.so
%{_libdir}/pkgconfig/gdkglext-1.0.pc
%{_libdir}/pkgconfig/gdkglext-x11-1.0.pc
%{_libdir}/pkgconfig/gtkglext-1.0.pc
%{_libdir}/pkgconfig/gtkglext-x11-1.0.pc
%{_includedir}/gtkglext-1.0/

%files doc
%doc %{_datadir}/gtk-doc/html/gtkglext/

%changelog
