#
# spec file for package python-retry
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-retry
Version:        0.9.2
Release:        0
Summary:        Python retry decorator
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/invl/retry
Source:         https://files.pythonhosted.org/packages/source/r/retry/retry-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module decorator >= 3.4.2}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module py >= 1.4.26}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-decorator >= 3.4.2
Requires:       python-py >= 1.4.26
BuildArch:      noarch

%python_subpackages

%description
Easy to use retry decorator.

%prep
%setup -q -n retry-%{version}
sed -i '/tox/d;/wheel/d' test-requirements.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
