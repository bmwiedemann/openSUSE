#
# spec file for package python-vine
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-vine
Version:        5.1.0
Release:        0
Summary:        Python Promises
License:        BSD-3-Clause
URL:            https://github.com/celery/vine/
Source:         https://files.pythonhosted.org/packages/source/v/vine/vine-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#celery/vine#105
Patch0:         use-correct-test-method.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module case}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Promises implementation for python.

%prep
%autosetup -p1 -n vine-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc Changelog README.rst
%license LICENSE
%{python_sitelib}/vine
%{python_sitelib}/vine-%{version}.dist-info

%changelog
