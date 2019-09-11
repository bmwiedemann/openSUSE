#
# spec file for package python-pytest-repeat
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-repeat
Version:        0.8.0
Release:        0
License:        MPL-2.0
Summary:        Pytest plugin for repeating tests
Url:            https://github.com/pytest-dev/pytest-repeat
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pytest-repeat/pytest-repeat-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.6}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 3.6
BuildArch:      noarch

%python_subpackages

%description
Pytest plugin for repeating tests.

%prep
%setup -q -n pytest-repeat-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
