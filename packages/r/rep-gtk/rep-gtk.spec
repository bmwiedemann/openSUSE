#
# spec file for package rep-gtk
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2007 Jan Nieuwenhuizen <jnieuwenhuizen@novell.com>
# Copyright (c) 2000 John Harper <john@dcs.warwick.ac.uk>
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


Name:           rep-gtk
Version:        0.90.8.2
Release:        0
Summary:        GTK+ binding for librep Lisp environment
License:        GPL-2.0+
Group:          Development/Libraries/GNOME
Url:            http://sawfish.wikia.com/wiki/Rep-GTK
Source:         http://download.tuxfamily.org/librep/rep-gtk/%{name}_%{version}.tar.xz
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.23.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires:  pkgconfig(librep) >= 0.92.1
%if 0%{?suse_version} <= 1210
BuildRequires:  xz
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


%description
This is a binding of GTK+ for the rep Lisp system. It is based on
Marius Vollmer's guile-gtk binding (initially version 0.15, updated to
0.17), with a new glue-code generator.

%package devel
Summary:        GTK+ binding for librep Lisp environment - Development Files
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       pkgconfig(gtk+-2.0) >= 2.24.0
Requires:       pkgconfig(librep) >= 0.92.1

%description devel
This is a binding of GTK+ for the rep Lisp system. It is based on
Marius Vollmer's guile-gtk binding (initially version 0.15, updated to
0.17), with a new glue-code generator.

%prep
%setup -q -n %{name}_%{version}
chmod -x examples/*.jl

%build
%configure
%__make %{_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name "*.la" -delete

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING examples/ NEWS README README.gtk-defs README.guile-gtk TODO *.defs
%{_libdir}/rep/gui/

%files devel
%defattr(-,root,root)
%{_includedir}/rep-gtk/
%{_libdir}/pkgconfig/rep-gtk.pc

%changelog
