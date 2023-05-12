#
# spec file for package python-timeout-decorator
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-timeout-decorator
Version:        0.5.0
Release:        0
Summary:        Python timeout decorator
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pnpnpn/timeout-decorator
Source:         https://files.pythonhosted.org/packages/source/t/timeout-decorator/timeout-decorator-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/pnpnpn/timeout-decorator/master/tests/test_timeout_decorator.py
# https://github.com/pnpnpn/timeout-decorator/issues/68
Source2:        https://raw.githubusercontent.com/pnpnpn/timeout-decorator/master/LICENSE.txt
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python timeout decorator.

%prep
%setup -q -n timeout-decorator-%{version}
cp %{SOURCE1} %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
