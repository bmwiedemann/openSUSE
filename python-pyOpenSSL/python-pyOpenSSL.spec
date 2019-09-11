#
# spec file for package python-pyOpenSSL
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
Name:           python-pyOpenSSL
Version:        19.0.0
Release:        0
Summary:        Python wrapper module around the OpenSSL library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pyca/pyopenssl
Source:         https://files.pythonhosted.org/packages/source/p/pyOpenSSL/pyOpenSSL-%{version}.tar.gz
Patch1:         skip-networked-test.patch
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module cryptography >= 2.3.0}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest >= 3.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
Requires:       python-cffi
Requires:       python-cryptography >= 2.3.0
Requires:       python-six >= 1.5.2
Provides:       pyOpenSSL = %{version}
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-openssl < %{version}
Provides:       %{oldpython}-openssl = %{version}
%endif
%python_subpackages

%description
pyOpenSSL is a set of Python bindings for OpenSSL.  It includes some low-level
cryptography APIs but is primarily focused on providing an API for using the
TLS protocol from Python.

pyOpenSSL is now a pure-Python project with a dependency on a new project,
cryptography (<https://github.com/pyca/cryptography>), which provides (among
other things) a cffi-based interface to OpenSSL.

%prep
%setup -q -n pyOpenSSL-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=en_US.UTF-8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix} -m "not network"
}

%files %{python_files}
%license LICENSE
%doc *.rst
%{python_sitelib}/OpenSSL/
%{python_sitelib}/pyOpenSSL-%{version}-py*.egg-info

%changelog
