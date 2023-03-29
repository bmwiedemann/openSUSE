#
# spec file for package python-gobject
#
# Copyright (c) 2023 SUSE LLC
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
%define skip_python2 1
# Define these before the call of python_subpackages
%define introspection_real_package  %(rpm -q --qf '%%{NAME}' -f $(readlink %{_libdir}/libgirepository-1.0.so -f))
%define cairo_real_package %(rpm -q --qf '%%{NAME}' --whatprovides cairo)
# Don't BuildRequire pkgconfig(gdk-3.0) to find the real package for libgdk-3!
# It produces a dependency cycle: avahi - gtk3-devel - python-dbus-python
#%%define gdk_real_package %%(rpm -q --qf '%%{NAME}' -f $(readlink %%{_libdir}/libgdk-3.so -f))
# This figures in an error message
%global __requires_exclude typelib\\(%%namespaces\\)
%global __requires_exclude_from ^%{_libdir}/python.*/site-packages/gi/__init__.py$
%define _name   pygobject
Name:           python-gobject
Version:        3.44.1
Release:        0
Summary:        Python bindings for GObject
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://wiki.gnome.org/Projects/PyGObject/
Source0:        https://download.gnome.org/sources/pygobject/3.44/%{_name}-%{version}.tar.xz

BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pycairo >= 1.16.0}
BuildRequires:  %{python_module pycairo-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gio-2.0) >= 2.38.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
# build cycle!
# BuildRequires:  pkgconfig(gdk-3.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.46.0
# Trigger an automatic installation of python(2|3.*)-gobject when python and libgirepository are installed.
Supplements:    (python and %{introspection_real_package})
%python_subpackages

%description
Pygobjects is an extension module for python that gives you access to
GLib's GObjects.

%package Gdk
Summary:        Python bindings for GObject/Gdk
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       %{name}-cairo = %{version}
# See above
#Supplements:    (python-gobject and %{gdk_real_package})

%description Gdk
Pygobjects is an extension module for python that gives you access to
GLib's GObjects.

This package contains the Python Gdk bindings for GObject.

%package cairo
Summary:        Python bindings for GObject/Cairo
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Supplements:    (python-gobject and %{cairo_real_package})
Requires:       python-cairo

%description cairo
Pygobjects is an extension module for python that gives you access to
GLib's GObjects.

This package contains the Python Cairo bindings for GObject.

%package devel
Summary:        Metapackage to pull in all of python-gobject's packages
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       %{name}-Gdk = %{version}
Requires:       %{name}-cairo = %{version}
Requires:       %{name}-common-devel = %{version}
Requires:       python-devel

%description devel
This package contains files required to build wrappers for gobject
addon libraries such as pygtk.

%package -n %{name}-common-devel
Summary:        Shared development files for GObject's Python bindings
Group:          Development/Languages/Python
Requires:       glib2-devel >= 2.56.0
Requires:       gobject-introspection-devel >= 1.56.0
Requires:       libffi-devel >= 3.0.0
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(cairo-gobject)
Provides:       %{python_module gobject-common-devel = %{version}}

%description -n %{name}-common-devel
This package contains common files required to build wrappers for gobject
addon libraries such as pygtk in both Python2 and Python3.

%prep
%setup -q -n %{_name}-%{version}
# Remove the executable bits from example scripts:
find examples -name '*.py' -exec chmod -R -x {} +

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
# Incorrectly installed by a python38-setuptools vendored distutils
# which does not play well with the distro patched python38.
# Later flavors installed the correct files into lib64 as well
if [ "%{_libdir}" != "%{_prefix}/lib" -a -d %{buildroot}%{_prefix}/lib/pkgconfig ]; then
  rm -r  %{buildroot}%{_prefix}/lib/pkgconfig
fi

%{python_expand # delete unwanted python scripts and their compiled cache files
# Drop pygtkcompat layer - It's useless and we lack other stuff for it to work
rm -v %{buildroot}%{$python_sitearch}/gi/pygtkcompat.py*
rm -vf %{buildroot}%{$python_sitearch}/gi/__pycache__/pygtkcompat*
rm -vr %{buildroot}%{$python_sitearch}/pygtkcompat/

# Drop GIMarshallingTests - It's test suite remainders that should not be installed
find %{buildroot}%{$python_sitearch} -name GIMarshallingTests* -delete -print
}

find %{buildroot} "(" -name '*.la' -or -name '*.a' ")" -delete

%{?python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license COPYING
%doc NEWS
%doc examples/
%{python_sitearch}/gi/
%{python_sitearch}/PyGObject-%{version}*-py*.egg-info
# Lives in cairo subpackage
%exclude %{python_sitearch}/gi/_gi_cairo*.so
# Lives in Gdk subpackage
%exclude %{python_sitearch}/gi/_gtktemplate.py
%exclude %{python_sitearch}/gi/overrides/Gdk.*
%exclude %{python_sitearch}/gi/overrides/GdkPixbuf.py
%exclude %{python_sitearch}/gi/overrides/Gtk.*
%exclude %{python_sitearch}/gi/overrides/keysyms.*
%exclude %{python_sitearch}/gi/overrides/Pango.*
%pycache_only %exclude %{python_sitearch}/gi/__pycache__/_gtktemplate*
%pycache_only %exclude %{python_sitearch}/gi/overrides/__pycache__/Gdk.*
%pycache_only %exclude %{python_sitearch}/gi/overrides/__pycache__/GdkPixbuf.*
%pycache_only %exclude %{python_sitearch}/gi/overrides/__pycache__/Gtk.*
%pycache_only %exclude %{python_sitearch}/gi/overrides/__pycache__/keysyms.*
%pycache_only %exclude %{python_sitearch}/gi/overrides/__pycache__/Pango.*

%files %{python_files Gdk}
%{python_sitearch}/gi/_gtktemplate.py
%{python_sitearch}/gi/overrides/Gdk.*
%{python_sitearch}/gi/overrides/GdkPixbuf.py
%{python_sitearch}/gi/overrides/Gtk.*
%{python_sitearch}/gi/overrides/keysyms.*
%{python_sitearch}/gi/overrides/Pango.*
%pycache_only %{python_sitearch}/gi/__pycache__/_gtktemplate*
%pycache_only %{python_sitearch}/gi/overrides/__pycache__/Gdk.*
%pycache_only %{python_sitearch}/gi/overrides/__pycache__/GdkPixbuf.*
%pycache_only %{python_sitearch}/gi/overrides/__pycache__/Gtk.*
%pycache_only %{python_sitearch}/gi/overrides/__pycache__/keysyms.*
%pycache_only %{python_sitearch}/gi/overrides/__pycache__/Pango.*

%files %{python_files cairo}
%{python_sitearch}/gi/_gi_cairo*.so

%files %{python_files devel}
%doc README.rst

%files -n %{name}-common-devel
%{_includedir}/pygobject-3.0/
%{_libdir}/pkgconfig/pygobject-3.0.pc

%changelog
