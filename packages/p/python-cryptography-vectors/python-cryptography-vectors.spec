#
# spec file for package python-cryptography-vectors
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
# ALWAYS KEEP IN SYNC WITH python-cryptography!
%define skip_python2 1
Name:           python-cryptography-vectors
# ALWAYS KEEP IN SYNC WITH python-cryptography!
Version:        39.0.0
Release:        0
Summary:        Test vectors for the cryptography package
License:        Apache-2.0 OR BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pyca/cryptography
Source0:        https://files.pythonhosted.org/packages/source/c/cryptography_vectors/cryptography_vectors-%{version}.tar.gz
Source2:        %{name}.keyring
Source3:        python-cryptography-vectors-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Vectors for testing of the python cryptography package.

%prep
%setup -q -n cryptography_vectors-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# this is test data only package for tests with python-cryptography.

%files %{python_files}
%license LICENSE*
%{python_sitelib}/cryptography_vectors
%{python_sitelib}/cryptography_vectors-%{version}*-info

%changelog
