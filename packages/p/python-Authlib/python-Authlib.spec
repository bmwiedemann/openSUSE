#
# spec file for package authlib
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
%global modname Authlib
Name:           python-%{modname}
Version:        0.14.3
Release:        0
Summary:        Python library in building OAuth and OpenID Connect servers
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://authlib.org/
Source:         https://files.pythonhosted.org/packages/source/A/Authlib/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module tox}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
Suggests:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Python library in building OAuth and OpenID Connect servers.
JWS, JWK, JWA, JWT are included.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog