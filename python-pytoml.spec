#
# spec file for package python-pytoml
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
Name:           python-pytoml
Version:        0.1.21
Release:        0
Summary:        TOML-0.4.0 parser/writer for Python
License:        MIT
URL:            https://github.com/avakar/pytoml
Source0:        https://files.pythonhosted.org/packages/source/p/pytoml/pytoml-%{version}.tar.gz
# toml-test for tests from author's fork with specific commit
Source1:        https://github.com/avakar/toml-test/archive/b212790.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
BuildArch:      noarch
%python_subpackages

%description
A specs-conforming and strict parser and writer for TOML files.
The library currently supports version 0.4.0 of the specs.

The pytoml project is no longer being actively maintained.
Consider using the toml package instead.

%prep
%setup -q -n pytoml-%{version}
tar -C test -xzf%{SOURCE1}
cd test
mv toml-test-b212790a6b7367489f389411bda009e5ff765f20 toml-test

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test/test.py

%files %{python_files}
%license LICENSE
%{python_sitelib}/pytoml/
%{python_sitelib}/pytoml-%{version}-py*.egg-info/

%changelog
