#
# spec file for package python-pytest-codestyle
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
Name:           python-pytest-codestyle
Version:        1.4.0
Release:        0
Summary:        Pytest plugin to run pycodestyle
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/henry0312/pytest-codestyle
Source:         https://files.pythonhosted.org/packages/source/p/pytest-codestyle/pytest-codestyle-%{version}.tar.gz
Patch0:         fix-super.patch
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pytest-isort}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pycodestyle
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
pytest plugin to run pycodestyle in python tests

%prep
%setup -q -n pytest-codestyle-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
