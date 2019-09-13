#
# spec file for package python-hkdf
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-hkdf
Version:        0.0.3
Release:        0
Summary:        HMAC-based Extract-and-Expand Key Derivation Function (HKDF)
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/casebeer/python-hkdf
Source:         https://files.pythonhosted.org/packages/source/h/hkdf/hkdf-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
This module implements the HMAC Key Derivation function.

%prep
%setup -q -n hkdf-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*

%changelog
