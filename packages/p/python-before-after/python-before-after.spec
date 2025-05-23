#
# spec file for package python-before-after
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
Name:           python-before-after
Version:        1.0.1
Release:        0
Summary:        Python utilities for testing race conditions
License:        GPL-2.0-only
URL:            https://github.com/c-oreills/before_after
Source:         https://files.pythonhosted.org/packages/source/b/before_after/before_after-%{version}.tar.gz
# https://github.com/c-oreills/before_after/issues/8
Source1:        https://raw.githubusercontent.com/c-oreills/before_after/master/LICENSE
# the 2nd patch download attempt is blocked - we can't have links in here
Patch0:         pr_6.patch
Patch1:         pr_10.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
before_after provides utilities for testing race conditions.

%prep
%autosetup -p1 -n before_after-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/before_after/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/before[-_]after
%{python_sitelib}/before[-_]after-%{version}*-info

%changelog
