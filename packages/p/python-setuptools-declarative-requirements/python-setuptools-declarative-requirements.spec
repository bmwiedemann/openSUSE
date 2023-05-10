#
# spec file for package python-setuptools-declarative-requirements
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-setuptools-declarative-requirements
Version:        1.2.0
Release:        0
Summary:        File support for setuptools declarative setup.cfg
License:        Apache-2.0
URL:            https://github.com/s0undt3ch/setuptools-declarative-requirements
Source:         https://files.pythonhosted.org/packages/source/s/setuptools-declarative-requirements/setuptools-declarative-requirements-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pypiserver}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  %{python_module wheel}
# /SECTION
BuildRequires:  fdupes
Requires:       python-setuptools
Requires:       python-toml
Requires:       python-wheel
BuildArch:      noarch
%python_subpackages

%description
File support for setuptools declarative setup.cfg.

%prep
%setup -q -n setuptools-declarative-requirements-%{version}
sed -i 's/"setuptools>=[0-9]*"/"setuptools"/g' tests/conftest.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# sdist test tries to contact pypi.org
%pytest -k 'not sdist'

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
