#
# spec file for package python3-gobject2
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


%define build_for_python3 1
%if %{build_for_python3}
%define local_py_requires Requires: python(abi) = %{py3_ver}
%define local_py_sitedir  %{python3_sitearch}
%else
%define local_py_requires %{py_requires}
%define local_py_sitedir  %{python_sitearch}
%endif
%define _name   pygobject
Name:           python3-gobject2
Version:        2.28.7
Release:        0
Summary:        Python bindings for GObject
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
URL:            http://ftp.gnome.org/pub/GNOME/sources/pygobject/
Source:         http://download.gnome.org/sources/pygobject/2.28/%{_name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  glib2-devel
BuildRequires:  libffi-devel
%{local_py_requires}
%if %{build_for_python3}
BuildRequires:  python3-cairo-devel
BuildRequires:  python3-devel
%else
BuildRequires:  python-cairo-devel
BuildRequires:  python-devel
Provides:       python2-gobject2 = %{version}
%endif

%description
Pygobjects is an extension module for python that gives you access to
GLib's GObjects.

%package cairo
%define cairo_real_package %(rpm -q --qf '%%{NAME}' --whatprovides cairo)
Summary:        Python bindings for GObject -- Cairo bindings
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:%{cairo_real_package})

%description cairo
Pygobjects is an extension module for python that gives you access to
GLib's GObjects.

This package contains the Python Cairo bindings for GObject.

%package devel
Summary:        Python bindings for GObject
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
%if %{build_for_python3}
# Several files are conflicting between python2 and python3 builds
Conflicts:      python-gobject2-devel
%else
Provides:       python-gobject2-doc = %{version}
Obsoletes:      python-gobject2-doc < %{version}
Provides:       python2-gobject2-devel = %{version}
%endif

%description devel
This package contains files required to build wrappers for gobject
addon libraries such as pygtk.

%prep
%setup -q -n %{_name}-%{version}

%build
%if %{build_for_python3}
export PYTHON=python3
%endif
%configure --disable-static --disable-introspection
make %{?_smp_mflags} V=1

%install
%makeinstall
find %{buildroot} -name '*.la' -delete -print
rm examples/Makefile*
%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README ChangeLog examples
%{local_py_sitedir}/glib/
%{local_py_sitedir}/gobject/
%dir %{local_py_sitedir}/gtk-2.0
%{local_py_sitedir}/gtk-2.0/dsextras.py*
%{local_py_sitedir}/gtk-2.0/gio/
%{local_py_sitedir}/pygtk.*
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/pygtk-2.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/pygobject-2.0.pc
%if !%{build_for_python3}
## codegen
%{_bindir}/pygobject-codegen-2.0
%{_datadir}/%{_name}/2.0/codegen/
%endif
# we explicitly list the directories here to be sure we don't include something
# that should live in the main package
%dir %{_datadir}/%{_name}
%dir %{_datadir}/%{_name}/2.0
%{_datadir}/%{_name}/2.0/defs/
%{_datadir}/%{_name}/xsl/
## doc: we need the files there since building API docs for other python
## bindings require some files from here
# Own these repositories to not depend on gtk-doc while building:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/pygobject/

%changelog
