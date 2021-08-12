#
# spec file for package python-djvulibre
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-djvulibre
Version:        0.8.6
Release:        0
Summary:        Python Support for the DjVu Image Format
License:        GPL-2.0-only
Group:          Development/Libraries/Python
URL:            http://jwilk.net/software/python-djvulibre
Source0:        https://files.pythonhosted.org/packages/source/p/python-djvulibre/%{name}-%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/p/python-djvulibre/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Patch1:         remove-all-dependencies-on-nose-in-the-code.patch
Patch2:         remove-nose-in-documentation.patch
# PATCH-FIX-UPSTREAM sphinx_4_compatibility.patch gh#sphinx-doc/sphinx#7747 mcepl@suse.com
# Sphinx doesn't stable API
Patch3:         sphinx_4_compatibility.patch
BuildRequires:  %{python_module Cython >= 0.19.1}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  djvulibre
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  graphviz-gnome
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(ddjvuapi) >= 3.5.21
Requires:       djvulibre >= 3.5.21

%python_subpackages

%description
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open source implementation of DjVu.

%package -n %{name}-doc
Summary:        Python Support for the DjVu Image Format (Documentation)
Group:          Documentation/HTML
BuildArch:      noarch

%description -n %{name}-doc
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open source implementation of DjVu.

This package contains technical documentation.

%prep
%autosetup -p1

chmod -x examples/*

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build
%python_build build_sphinx

%install
%python_install
rm build/sphinx/html/.buildinfo build/sphinx/html/objects.inv
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
cd tests/
%pyunittest_arch -v

%files %{python_files}
%license doc/COPYING
%doc doc/changelog doc/credits doc/todo
%{python_sitearch}/*

%files -n %{name}-doc
%doc build/sphinx/html/ examples/

%changelog
