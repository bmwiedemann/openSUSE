#
# spec file for package python-flit-core
#
# Copyright (c) 2019 SUSE LLC
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
Name:           python-flit-core
Version:        2.1.0
Release:        0
Summary:        Distribution-building parts of Flit
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/takluyver/flit
Source:         https://files.pythonhosted.org/packages/source/f/flit_core/flit_core-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytoml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testpath}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-dephell
Requires:       python-pytoml
BuildArch:      noarch
%python_subpackages

%description
Flit is a simple way to put Python packages and modules on PyPI.

%prep
%setup -q -n flit_core-%{version}
dephell convert --from-format pyproject --from-path pyproject.toml --to setup.py

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/flit_core/tests
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%{python_sitelib}/*

%changelog
