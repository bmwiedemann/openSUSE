#
# spec file for package python-case
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-case
Version:        1.5.3
Release:        0
Summary:        Python unittest Utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/celery/case
Source:         https://files.pythonhosted.org/packages/source/c/case/case-%{version}.tar.gz
Patch0:         remove_unittest2.patch
Patch1:         remove_coverage.patch
Patch2:         remove-nose.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
Requires:       python-setuptools
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Python unittest Utilities.

%prep
%setup -q -n case-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check no tests exist https://github.com/celery/case/issues/8

%files %{python_files}
%license LICENSE
%doc Changelog README.rst
%{python_sitelib}/case
%{python_sitelib}/case-%{version}*-info

%changelog
