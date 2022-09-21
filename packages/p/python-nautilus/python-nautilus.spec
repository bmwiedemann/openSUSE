#
# spec file for package python-nautilus
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define _name nautilus-python
%define skip_python2 1

Name:           python-nautilus
Version:        4.0
Release:        0
Summary:        Python bindings for Nautilus
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://wiki.gnome.org/Projects/NautilusPython
Source:         https://download.gnome.org/sources/nautilus-python/4.0/%{_name}-%{version}.tar.xz

BuildRequires:  %{python_module devel}
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libnautilus-extension-4) >= 43.beta
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0.0

Requires:       %{name}-common-files = %{version}
Requires:       python-gobject
# we can't have automatic typelib() Requires here: it's C code: PyImport_ImportModule("gi.repository.Nautilus")
Requires:       typelib(Nautilus)
%python_subpackages

%description
This package contains bindings to write Nautilus extensions with Python.
It allows writing menu, property pages and column providers extensions,
so that Nautilus functionality can be easily extended.

%package -n %{name}-common-files
Summary:        Python nautilus files shared between python interpreter versions
Group:          Development/Libraries/Python
Provides:       %{python_module nautilus-common-files = %{version}}

%description -n %{name}-common-files
This package contains common files required to build wrappers for
python-nautilus in both Python2 and Python3.

%package devel
Summary:        Metapackage to pull in all of python-nautilus' packages
Group:          Development/Libraries/Python
Requires:       %{name} >= %{version}
Requires:       %{name}-common-devel = %{version}
Requires:       python-devel

%description devel
This package contains files required to build wrappers for python-nautilus.

%package -n %{name}-common-devel
Summary:        Shared development files for python-nautilus
Group:          Development/Libraries/Python
Requires:       python3-nautilus-devel = %{version}
Provides:       %{python_module nautilus-common-devel = %{version}}

%description -n %{name}-common-devel
This package contains common files required to build wrappers for
python-nautilus in both Python2 and Python3.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%{python_expand export PYTHON=$python
%define _vpath_builddir build_%{$python_bin_suffix}
sed -i "s|docdir =.*|docdir = '%{_docdir}/$python-nautilus'|g" meson.build
%meson
%meson_build
}

%install
%{python_expand export PYTHON=$python
%define _vpath_builddir build_%{$python_bin_suffix}
sed -i "s|docdir =.*|docdir = '%{_docdir}/$python-nautilus'|g" meson.build
%meson_install
}

# New dir where python extensions get installed. It's not created by make
# install (bgo#638890).
test ! -d %{buildroot}%{_datadir}/nautilus-python/extensions
mkdir -p %{buildroot}%{_datadir}/nautilus-python/extensions
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -size 0 -delete

%files %{python_files}
%license COPYING
%doc %{_docdir}/%{python_flavor}-nautilus/

%files -n %{name}-common-files
%doc NEWS.md
%{_libdir}/nautilus/extensions-4/libnautilus-python.so
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions

%files %{python_files devel}
%doc AUTHORS

%files -n %{name}-common-devel
%doc %{_datadir}/gtk-doc/html/nautilus-python
%{_datadir}/pkgconfig/nautilus-python.pc

%changelog
