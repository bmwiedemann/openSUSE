#
# spec file for package python-pytest-reqs
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
Name:           python-pytest-reqs
Version:        0.2.1
Release:        0
Summary:        Pytest plugin to check pinned requirements
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/di/pytest-reqs
Source:         https://files.pythonhosted.org/packages/source/p/pytest-reqs/pytest-reqs-%{version}.tar.gz
BuildRequires:  %{python_module pip >= 6}
BuildRequires:  %{python_module pip-api >= 0.0.2}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest >= 2.4.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Setuptools and pip are both used at runtime
Requires:       python-pip >= 6
Requires:       python-pip-api >= 0.0.2
Requires:       python-pytest >= 2.4.2
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
This plugin checks the requirements files for specific versions, and
compares those versions with the installed libraries in the
environment, failing the test suite if any are invalid or out of
date.

This can be used to keep virtual environments up to date, and
ensuring that the test suite is always being passed with the
requirements that have been specified.

It also verifies that the requirements files are syntatically valid.

%prep
%setup -q -n pytest-reqs-%{version}
sed -i '/python_requires/d' setup.py

chmod a-x CHANGELOG LICENSE README.rst
rm -f tox.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
