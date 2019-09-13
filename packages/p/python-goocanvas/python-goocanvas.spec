#
# spec file for package python-goocanvas
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-goocanvas
#Does not work with python 3 so far...
%define         skip_python3 1
Version:        0.14.1
Release:        0
Summary:        Python bindings for goocanvas
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://github.com/GNOME/pygoocanvas
Source0:        pygoocanvas-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM python-goocanvas-revert-svn229.patch bgo576198 vuntz@novell.com -- This svn commit makes things crash on "import goocanvas"...
Patch1:         python-goocanvas-revert-svn229.patch
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(goocanvas)
BuildRequires:  pkgconfig(pycairo)
BuildRequires:  pkgconfig(pygobject-2.0)
BuildRequires:  pkgconfig(pygtk-2.0)
Requires:       python-cairo
Requires:       python-gobject2
Requires:       python-gtk

%python_subpackages

%description
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library
for drawing. 

This package provides python bindings for GooCanvas.

%package devel
Summary:        Python bindings for goocanvas - Development pack
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library
for drawing. 

This package provides development information for the python bindings
for GooCanvas.

%prep
%setup -q -n pygoocanvas-%{version}
%patch1 -p1

%build
autoreconf -fi
%configure --disable-docs
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{python_sitearch}/goocanvasmodule.la

%files %{python_files}
%doc AUTHORS NEWS
%{python_sitearch}/*.so

%files %{python_files devel}
%{_libdir}/pkgconfig/*.pc

%changelog
