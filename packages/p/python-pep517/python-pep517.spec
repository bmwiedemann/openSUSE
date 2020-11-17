#
# spec file for package python-pep517
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pep517
Version:        0.9.1
Release:        0
Summary:        Wrappers to build Python packages using PEP 517 hooks
License:        MIT
URL:            https://github.com/takluyver/pep517
Source:         https://files.pythonhosted.org/packages/source/p/pep517/pep517-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-toml
Recommends:     python-pip
Recommends:     python-wheel >= 0.25
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel >= 0.25}
BuildRequires:  python3-flit-core
# /SECTION
%python_subpackages

%description
Wrappers to build Python packages using PEP 517 hooks.

%prep
%setup -q -n pep517-%{version}
sed -i 's/--flake8//' pytest.ini

# Remove what appears to be overly cautious flag
# that causes tests to require internet, both here
# and the test suites of any dependencies. Tracking at:
# https://github.com/pypa/pep517/issues/101
sed -i "s/'--ignore-installed',//" pep517/envbuild.py

# Needed for test_meta to avoid pypi.org fetches
sed -i 's/"flit_core >=2,<3"/"flit_core"/' pyproject.toml

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
if [ $python = "%{_bindir}/python2" ]; then
  $python -m pytest -v -k "not test_meta"
else
  $python -m pytest -v
fi
}

%files %{python_files}
%doc README.rst doc/*.rst
%license LICENSE
%{python_sitelib}/*

%changelog
