#
# spec file for package python-pytest-subprocess
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname pytest_subprocess
Name:           python-pytest-subprocess
Version:        1.4.2
Release:        0
Summary:        A plugin to fake subprocess for pytest
License:        MIT
URL:            https://github.com/aklajnert/pytest-subprocess
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-subprocess/pytest-subprocess-%{version}.tar.gz
Source1:        tests.tar.xz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 4.0.0
Recommends:     python-Pygments >= 2.0
Recommends:     python-anyio
Recommends:     python-changelogd
Recommends:     python-coverage
Recommends:     python-docutils >= 0.12
Recommends:     python-furo
Recommends:     python-nox
Recommends:     python-pytest-asyncio >= 0.15.1
Recommends:     python-pytest-rerunfailures
Recommends:     python-sphinx
Recommends:     python-sphinx-autodoc-typehints
Recommends:     python-sphinxcontrib-napoleon
BuildArch:      noarch
# SECTION Test requirements
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A pytest plugin to fake subprocess for pytest.  The plugin adds the
``fake_process`` fixture (and ``fp`` as an alias).  It can be used it to
register subprocess results so you won't need to rely on the real processes.

%prep
%autosetup -p1 -a1 -n pytest-subprocess-%{version}

chmod -x LICENSE README.rst pytest_subprocess/py.typed pytest_subprocess.egg-info/*
sed -Ei "s/\r$//" README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Docs dir is missing from tarball
%pytest -k "not test_documentation"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
