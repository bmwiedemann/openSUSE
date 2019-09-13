#
# spec file for package python-atspi
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define _name   pyatspi
Name:           python-atspi
Version:        2.32.1
Release:        0
Summary:        Python bindings for the Assistive Technology Service Provider Interface
License:        LGPL-2.0-only
Group:          Development/Libraries/Python
URL:            http://www.gnome.org/
Source0:        https://download.gnome.org/sources/pyatspi/2.32/%{_name}-%{version}.tar.xz

BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module gobject >= 2.90.1}
BuildRequires:  %{python_module gobject-devel >= 2.90.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
# Needed to have typelib() Requires.
BuildRequires:  gobject-introspection
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
Requires:       python-gobject >= 2.90.1
# The bindings are really useful only if the at-spi registry is running. But
# it's not a strict runtime dependency.
Recommends:     at-spi2-core
# Old versions of at-spi 1.x provided the same files
Conflicts:      at-spi < 1.29.3
BuildArch:      noarch
%ifpython2
Requires:       dbus-1-python
%endif
%ifpython3
Requires:       dbus-1-python3
%endif
# Virtual package, so that apps can depend on it, without having to know which
# at-spi stack is used. Only the default at-spi stack should define it.
%ifpython2
Provides:       py2atspi
Provides:       pyatspi
%endif
%ifpython3
Provides:       py3atspi
%endif
%python_subpackages

%description
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

This package contains the python bindings for AT-SPI.

%prep
%setup -q -n %{_name}-%{version}

%build
# Configure for out-of-tree builds
%define _configure ../configure

%{python_expand mkdir build_%{$python_bin_suffix}
pushd build_%{$python_bin_suffix}
export PYTHON=$python
%configure
make %{?_smp_mflags}
popd
}

%install
%{python_expand pushd build_%{$python_bin_suffix}
%make_install
popd
}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc AUTHORS NEWS README
%{python_sitelib}/pyatspi/

%changelog
