#
# spec file for package python-djvulibre
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
Name:           python-djvulibre
Version:        0.8.4
Release:        0
Summary:        Python Support for the DjVu Image Format
License:        GPL-2.0-only
Group:          Development/Libraries/Python
URL:            http://jwilk.net/software/python-djvulibre
Source0:        https://files.pythonhosted.org/packages/source/p/python-djvulibre/%{name}-%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/p/python-djvulibre/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  %{python_module Cython >= 0.19}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
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
%setup -q
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
PYTHONPATH=%{buildroot}%{$python_sitearch}
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m nose --exclude='^test_export_ps$' --verbose

%files %{python_files}
%license doc/COPYING
%doc doc/changelog doc/credits doc/todo
%{python_sitearch}/*

%files -n %{name}-doc
%doc build/sphinx/html/ examples/

%changelog
