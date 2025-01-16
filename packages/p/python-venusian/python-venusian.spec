#
# spec file for package python-venusian
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2013-2019 LISA GmbH, Bingen, Germany.
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


%{?sle15_python_module_pythons}
Name:           python-venusian
Version:        3.1.1
Release:        0
Summary:        A library for deferring decorator actions
License:        SUSE-Repoze AND ZPL-2.1
URL:            https://github.com/Pylons/venusian
Source:         https://files.pythonhosted.org/packages/source/v/venusian/venusian-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-copybutton}
# /SECTION
# SECTION documentation requirements
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pylons-sphinx-themes}
# /SECTION
%python_subpackages

%description
Venusian is a library which allows framework authors to defer
decorator actions.  Instead of taking actions when a function (or
class) decorator is executed at import time, you can defer the action
usually taken by the decorator until a separate "scan" phase.

See the "docs" directory of the package or the online documentation at
http://docs.pylonsproject.org/projects/venusian/dev/.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}

%description doc
This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n venusian-%{version}

rm -rf venusian.*-info
sed -i '/addopts/d' setup.cfg

%build
%pyproject_wheel
PYTHONPATH=src python%python_bin_suffix -msphinx docs build/sphinx/html \
    && rm -rv build/sphinx/html/{.buildinfo,objects.inv,.doctrees}

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{python_sitelib}/venusian
%{python_sitelib}/venusian-%{version}.dist-info

%files %{python_files doc}
%license LICENSE.txt
%doc build/sphinx/html/

%changelog
