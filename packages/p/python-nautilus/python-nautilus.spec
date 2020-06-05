#
# spec file for package python-nautilus
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.2.3
Release:        0
Summary:        Python bindings for Nautilus
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://wiki.gnome.org/Projects/NautilusPython
Source:         http://download.gnome.org/sources/nautilus-python/1.2/%{_name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM python-nautilus-gcc10-buildfix.patch -- Fix build with gcc 10
Patch0:         python-nautilus-gcc10-buildfix.patch

BuildRequires:  %{python_module devel}
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libnautilus-extension)
BuildRequires:  pkgconfig(pygobject-3.0)

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
%define _configure ../configure
%{python_expand mkdir build_%{$python_bin_suffix}
pushd build_%{$python_bin_suffix}
export PYTHON=$python
%configure \
	--disable-static \
	--docdir=%{_docdir}/$python-nautilus \
	--enable-gtk-doc \
	%{nil}
%make_build
popd
}

%install
%{python_expand pushd build_%{$python_bin_suffix}
%make_install
popd
}
# New dir where python extensions get installed. It's not created by make
# install (bgo#638890).
test ! -d %{buildroot}%{_datadir}/nautilus-python/extensions
mkdir -p %{buildroot}%{_datadir}/nautilus-python/extensions
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -size 0 -delete

%files %{python_files}
%license COPYING
%doc NEWS
%doc %{_docdir}/%{python_flavor}-nautilus

%files -n %{name}-common-files
%{_libdir}/nautilus/extensions-3.0/libnautilus-python.so
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions

%files %{python_files devel}
%doc AUTHORS ChangeLog

%files -n %{name}-common-devel
%doc %{_datadir}/gtk-doc/html/nautilus-python
%{_libdir}/pkgconfig/nautilus-python.pc

%changelog
