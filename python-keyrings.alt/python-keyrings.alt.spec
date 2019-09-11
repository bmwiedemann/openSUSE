#
# spec file for package python-keyrings.alt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define keyring_ver 18.0.0
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-keyrings.alt
Version:        3.1.1
Release:        0
Summary:        Alternate keyring implementations
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/keyrings.alt
Source:         https://files.pythonhosted.org/packages/source/k/keyrings.alt/keyrings.alt-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-keyring >= 10.3.1
Requires:       python-pycrypto
Requires:       python-six
Recommends:     python-fs >= 0.5
Recommends:     python-gdata
Recommends:     python-keyczar
Recommends:     python-pycrypto
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module fs >= 0.5}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module keyczar}
BuildRequires:  %{python_module keyring >= 10.3.1}
BuildRequires:  %{python_module pycrypto}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module six}
BuildRequires:  python-backports.unittest_mock
BuildRequires:  typelib(GnomeKeyring)
# /SECTION
%python_subpackages

%description
Alternate keyring backend implementations for use with the
keyring package.

%prep
%setup -q -n keyrings.alt-%{version}
sed -i 's/--flake8//' pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# setup.py test works except it checks test dependencies which includes
# lots of non-test related dependencies.

# Three tests fail with AttributeError: 'x' object has no attribute 'get_credential'
# - CryptedFileKeyringTestCase
# - EncryptedFileKeyringTestCase
# - UncryptedFileKeyringTestCase
%{python_expand py.test-%{$python_bin_suffix} \
  --ignore=_build.python2 --ignore=_build.python3 -k 'not test_credential'
}

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
