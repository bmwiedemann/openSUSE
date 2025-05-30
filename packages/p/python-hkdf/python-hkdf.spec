#
# spec file for package python-hkdf
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


Name:           python-hkdf
Version:        0.0.3
Release:        0
Summary:        HMAC-based Extract-and-Expand Key Derivation Function (HKDF)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/casebeer/python-hkdf
Source:         https://files.pythonhosted.org/packages/source/h/hkdf/hkdf-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module implements the HMAC Key Derivation function.

%prep
%setup -q -n hkdf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/hkdf.py
%{python_sitelib}/hkdf-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/hkdf*

%changelog
