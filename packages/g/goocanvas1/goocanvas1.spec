#
# spec file for package goocanvas1
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   goocanvas
Name:           goocanvas1
Version:        1.0.0
Release:        0
Summary:        A cairo-based canvas widget for GTK+
License:        LGPL-2.0-only
Group:          Development/Libraries/GNOME
URL:            http://sourceforge.net/projects/goocanvas
Source0:        %{_name}-%{version}.tar.bz2
BuildRequires:  cairo-devel
BuildRequires:  gtk2-devel
BuildRequires:  translation-update-upstream

%description
GooCanvas is similar in many ways to GnomeCanvas and FooCanvas. But it
uses cairo for rendering, has an optional model/view split, and uses
interfaces for items & models (so you can easily turn any application
object into a canvas item or model).

%package -n libgoocanvas3-devel
Summary:        A cairo-based canvas widget for GTK+
Group:          Development/Libraries/GNOME
Requires:       libgoocanvas3 = %{version}
Provides:       goocanvas-doc = %{version}
Obsoletes:      goocanvas-doc < %{version}

%description -n libgoocanvas3-devel
GooCanvas is similar in many ways to GnomeCanvas and FooCanvas. But it
uses cairo for rendering, has an optional model/view split, and uses
interfaces for items & models (so you can easily turn any application
object into a canvas item or model).

%package -n libgoocanvas3
Summary:        A cairo-based canvas widget for GTK+
Group:          System/Libraries
Recommends:     libgoocanvas3-lang
Provides:       goocanvas = %{version}
Obsoletes:      goocanvas < %{version}

%description -n libgoocanvas3
GooCanvas is similar in many ways to GnomeCanvas and FooCanvas. But it
uses cairo for rendering, has an optional model/view split, and uses
interfaces for items & models (so you can easily turn any application
object into a canvas item or model).

%lang_package -n libgoocanvas3

%prep
%setup -q -n %{_name}-%{version}
translation-update-upstream

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}/%{_libdir}/*.*a
%find_lang %{_name}

%post -n libgoocanvas3 -p /sbin/ldconfig
%postun -n libgoocanvas3 -p /sbin/ldconfig

%files -n libgoocanvas3
%doc AUTHORS NEWS README TODO
%{_libdir}/*.so.*

%files -n libgoocanvas3-devel
%{_includedir}/goocanvas-1.0/
%{_libdir}/pkgconfig/goocanvas.pc
%{_libdir}/*.so
%doc %{_datadir}/gtk-doc/html/goocanvas/

%files -n libgoocanvas3-lang -f %{_name}.lang

%changelog
