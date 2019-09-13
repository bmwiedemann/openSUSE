#
# spec file for package python-flake8-pep3101
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
Name:           python-flake8-pep3101
Version:        1.2.1
Release:        0
Summary:        Checks for old string formatting
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/gforcada/flake8-pep3101
Source:         https://files.pythonhosted.org/packages/source/f/flake8-pep3101/flake8-pep3101-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8 >= 3.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flake8 >= 3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testfixtures}
# /SECTION
%python_subpackages

%description
Checks for old string formatting.

%prep
%setup -q -n flake8-pep3101-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE LICENSE.rst
%{python_sitelib}/*

%changelog
