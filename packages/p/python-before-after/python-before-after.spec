#
# spec file for package python-before-after
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-before-after
Version:        1.0.1
Release:        0
Summary:        Python utilities for testing race conditions
License:        GPL-2.0-only
URL:            https://github.com/c-oreills/before_after
Source:         https://files.pythonhosted.org/packages/source/b/before_after/before_after-%{version}.tar.gz
# https://github.com/c-oreills/before_after/issues/8
Source1:        https://raw.githubusercontent.com/c-oreills/before_after/master/LICENSE
Patch0:         https://patch-diff.githubusercontent.com/raw/c-oreills/before_after/pull/6.patch#/pr_6.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mock >= 1.0.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock >= 1.0.1}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
before_after provides utilities for testing race conditions.

%prep
%setup -q -n before_after-%{version}
%patch0 -p1
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/before_after/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
