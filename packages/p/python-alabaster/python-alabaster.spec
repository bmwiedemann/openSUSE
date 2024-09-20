#
# spec file for package python-alabaster
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-alabaster
Version:        1.0.0
Release:        0
Summary:        (c)lean, responsive, configurable theme for the Sphinx
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://alabaster.readthedocs.io/en/latest
Source:         https://github.com/sphinx-doc/alabaster/archive/refs/tags/%{version}.tar.gz#/alabaster-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Alabaster is a visually (c)lean, responsive, configurable theme for the Sphinx documentation system.
It requires Python 3.10 or newer and Sphinx 6.2 or newer.

%prep
%setup -q -n alabaster-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/alabaster
%{python_sitelib}/alabaster-%{version}.dist-info

%changelog
