#
# spec file for package python-pytest-runner
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
Name:           python-pytest-runner
Version:        5.2
Release:        0
Summary:        Testing with Python
License:        MIT
URL:            https://github.com/pytest-dev/pytest-runner
Source:         https://files.pythonhosted.org/packages/source/p/pytest-runner/pytest-runner-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3}
BuildRequires:  %{python_module pytest-virtualenv}
BuildRequires:  %{python_module setuptools >= 30.4}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3
Requires:       python-setuptools >= 30.4
BuildArch:      noarch
%python_subpackages

%description
Invoke py.test as distutils command with dependency resolution.

%prep
%setup -q -n pytest-runner-%{version}
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Uses Virtualenv and then tries to download everything from pip
#%%pytest

%files %{python_files}
%license LICENSE
%doc README.rst CHANGES.rst docs/*
%{python_sitelib}/*

%changelog
