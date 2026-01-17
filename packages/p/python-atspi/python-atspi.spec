#
# spec file for package python-atspi
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
# the test suite builds platform specific libraries, failing on some
ExcludeArch:    %arm ppc64le
%define configureargs --enable-tests
%else
%define psuffix %{nil}
%bcond_with test
# the resulting python library is pure
BuildArch:      noarch
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define _name   pyatspi
Name:           python-atspi%{psuffix}
Version:        2.58.1
Release:        0
Summary:        Python bindings for the Assistive Technology Service Provider Interface
License:        LGPL-2.0-only
Group:          Development/Libraries/Python
URL:            https://gitlab.gnome.org/GNOME/pyatspi2
Source0:        https://download.gnome.org/sources/pyatspi/2.58/%{_name}-%{version}.tar.xz
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module gobject >= 2.90.1}
BuildRequires:  %{python_module gobject-devel >= 2.90.1}
BuildRequires:  %{python_module meson-python}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  meson
# Needed to have typelib() Requires.
BuildRequires:  gobject-introspection
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(gtk+-3.0)
%if %{with test}
BuildRequires:  at-spi2-core
BuildRequires:  glib2-devel
BuildRequires:  libxml2-devel
BuildRequires:  (at-spi2-atk-gtk2 if at-spi2-core < 2.45)
BuildRequires:  (atk-devel if at-spi2-core-devel < 2.45)
%endif
Requires:       python-dbus-python
Requires:       python-gobject >= 2.90.1
# The bindings are really useful only if the at-spi registry is running. But
# it's not a strict runtime dependency.
Recommends:     at-spi2-core
# Old versions of at-spi 1.x provided the same files
Conflicts:      at-spi < 1.29.3
# Virtual package, so that apps can depend on it, without having to know which
# at-spi stack is used. Only the default at-spi stack should define it.
# DEPRECATED: For python packages, use Requires: python-pyatspi and let the
# python_subpackages macro figure out the correct package.
%ifpython2
Provides:       py2atspi
Provides:       pyatspi
%endif
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       py3atspi
%endif
%python_subpackages

%description
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

This package contains the python bindings for AT-SPI.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%meson
%meson_build
%pyproject_wheel

%install
%if ! %{with test}
%meson_install
%pyproject_install
%endif

%if %{with test}
%check
%meson_test
%endif

%if ! %{with test}
%files %{python_files}
%license COPYING
%doc AUTHORS NEWS README.md
%{python_sitelib}/pyatspi/
%{python_sitelib}/pyatspi-%{version}.dist-info
%endif

%changelog
