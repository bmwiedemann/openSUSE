#
# spec file for package python-bcrypt
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%{?sle15_python_module_pythons}
Name:           python-bcrypt
Version:        4.2.1
Release:        0
Summary:        BSD type 2a and 2b password hashing
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pyca/bcrypt/
Source0:        https://files.pythonhosted.org/packages/source/b/bcrypt/bcrypt-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 3.2.1}
BuildRequires:  %{python_module setuptools-rust >= 1.7.0}
BuildRequires:  %{python_module wheel}
# setuptools 40.8.0 is required by upstream only for a pip issue that doesn't
# affect us, so we relax the requirement to build in SLE/Leap 15.2 with 40.5.0
BuildRequires:  %{python_module setuptools >= 40.5.0}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-py-bcrypt = %{version}
Obsoletes:      python-py-bcrypt < %{version}

%python_subpackages

%description
This Python module supports creating (and verifying) password hashes
using the BSD-originating hashing methods known as "2a" and "2b".

%prep
%autosetup -p1 -a1 -n bcrypt-%{version}
rm -v src/_bcrypt/Cargo.lock

%build
export RUSTFLAGS=%{rustflags}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitearch}

%check
%pytest_arch tests/

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/bcrypt
%{python_sitearch}/bcrypt-%{version}*-info

%changelog
