#
# spec file for package python-re-assert
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
Name:           python-re-assert
Version:        1.0.0
Release:        0
Summary:        Show Python regex match assertion failures
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/asottile/re-assert
Source:         https://files.pythonhosted.org/packages/source/r/re_assert/re_assert-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/asottile/re-assert/master/tests/re_assert_test.py
Source2:        https://raw.githubusercontent.com/asottile/re-assert/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-regex
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module regex}
# /SECTION
%python_subpackages

%description
Show where your regex match assertion failed.

%prep
%setup -q -n re_assert-%{version}
cp %{SOURCE1} %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
