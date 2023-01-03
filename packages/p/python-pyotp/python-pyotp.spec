#
# spec file for package python-pyotp
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
%define skip_python2 1
Name:           python-pyotp
Version:        2.8.0
Release:        0
Summary:        Python One Time Password Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pyauth/pyotp
Source:         https://files.pythonhosted.org/packages/source/p/pyotp/pyotp-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
PyOTP is a Python library for generating and verifying one-time passwords. It can be used to implement two-factor (2FA)
or multi-factor (MFA) authentication methods in web applications and in other systems that require users to log in.

%prep
%setup -q -n pyotp-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
