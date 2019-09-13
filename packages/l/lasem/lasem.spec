#
# spec file for package lasem
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


%define api 0.4
Name:           lasem
Version:        0.4.4
Release:        0
Summary:        MathML and SVG rendering library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://live.gnome.org/Lasem
Source:         http://download.gnome.org/sources/%{name}/%{api}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM lasem-cairo-avoid-integer-overflow.patch CVE-2013-7447 zaitor@opensuse.org -- cairo: Avoid integer overflow
Patch0:         lasem-cairo-avoid-integer-overflow.patch
BuildRequires:  bison
BuildRequires:  gobject-introspection >= 0.6.7
BuildRequires:  intltool >= 0.35.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.2
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.16
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo) >= 1.16.0

%description
Lasem is a library for rendering SVG and MathML, implementing a DOM like API.
It's based on GObject and uses Pango and Cairo for the rendering. Included in the package
is a simple application, lasemrender, which is able to convert a MathML, a Latex
math or an SVG file to either PNG, PDF or an SVG image.

%package -n liblasem-0_4-4
Summary:        MathML and SVG rendering library
Group:          System/Libraries
Recommends:     %{name}-lang

%description -n liblasem-0_4-4
Lasem is a library for rendering SVG and MathML, implementing a DOM like API.
It's based on GObject and uses Pango and Cairo for the rendering.

%package devel
Summary:        Development files for lasem, a MathML and SVG rendering library
Group:          Development/Languages/C and C++
Requires:       liblasem-0_4-4 = %{version}

%description devel
Lasem is a library for rendering SVG and MathML, implementing a DOM like API.
It's based on GObject and uses Pango and Cairo for the rendering.

%prep
%setup -q
%patch0 -p1

%build
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
# Those files do not belong there... we package them using %%doc
rm -rf %{buildroot}%{_prefix}/doc
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}-%{api}

%post -n liblasem-0_4-4 -p /sbin/ldconfig
%postun -n liblasem-0_4-4 -p /sbin/ldconfig

%files -f %{name}-%{api}.lang
%license COPYING
%doc README
%{_bindir}/%{name}-render-%{api}
%{_mandir}/man1/%{name}-render-%{api}.1%{?ext_man}

%files -n liblasem-0_4-4
%license COPYING

%{_libdir}/lib%{name}-%{api}.so.*

%files devel
%{_includedir}/%{name}-%{api}/
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_datadir}/gtk-doc/html/%{name}-%{api}/

%changelog
