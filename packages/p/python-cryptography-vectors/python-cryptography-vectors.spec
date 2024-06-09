#
# spec file for package python-cryptography-vectors
#
# Copyright (c) 2024 SUSE LLC
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


# ALWAYS KEEP IN SYNC WITH python-cryptography!
%{?sle15_python_module_pythons}
Name:           python-cryptography-vectors
# ALWAYS KEEP IN SYNC WITH python-cryptography!
Version:        42.0.8
Release:        0
Summary:        Test vectors for the cryptography package
License:        Apache-2.0 OR BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pyca/cryptography
Source0:        https://files.pythonhosted.org/packages/source/c/cryptography_vectors/cryptography_vectors-%{version}.tar.gz
Source2:        %{name}.keyring
Source3:        python-cryptography-vectors-rpmlintrc
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Vectors for testing of the python cryptography package.

%prep
%setup -q -n cryptography_vectors-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# this is test data only package for tests with python-cryptography.

%files %{python_files}
%license LICENSE*
%{python_sitelib}/cryptography_vectors
%{python_sitelib}/cryptography_vectors-%{version}.dist-info

%changelog
