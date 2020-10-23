#
# spec file for package python-passlib
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
Name:           python-passlib
Version:        1.7.2
Release:        0
Summary:        Password hashing framework supporting over 20 schemes
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://bitbucket.org/ecollins/passlib
Source:         https://files.pythonhosted.org/packages/source/p/passlib/passlib-%{version}.tar.gz
BuildRequires:  %{python_module argon2_cffi}
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scrypt}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-argon2_cffi
Recommends:     python-bcrypt
Recommends:     python-cryptography
Recommends:     python-scrypt
BuildArch:      noarch
%python_subpackages

%description
Passlib is a password hashing library for Python 2 & 3. It provides
implementations of over 20 password hashing algorithms, as well as a
framework for managing existing password hashes. It can verify hashes
found in %{_sysconfdir}/shadow, and provide password hashing for
applications.

%prep
%setup -q -n passlib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README
%{python_sitelib}/passlib
%{python_sitelib}/passlib-%{version}-py%{python_version}.egg-info

%changelog
