#
# spec file for package python-cryptography
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
%bcond_without python2
Name:           python-cryptography
Version:        3.2.1
Release:        0
Summary:        Python library which exposes cryptographic recipes and primitives
License:        Apache-2.0 OR BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://cryptography.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/c/cryptography/cryptography-%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/c/cryptography/cryptography-%{version}.tar.gz.asc
Source2:        %{name}.keyring
# PATCH-FIX-SLE disable-uneven-sizes-tests.patch bnc#944204
Patch1:         disable-uneven-sizes-tests.patch
Patch2:         skip_openssl_memleak_test.patch
BuildRequires:  %{python_module asn1crypto >= 0.21.0}
BuildRequires:  %{python_module cffi >= 1.7}
BuildRequires:  %{python_module cryptography-vectors = %{version}}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module idna >= 2.1}
BuildRequires:  %{python_module pyasn1-modules}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools >= 11.3}
BuildRequires:  %{python_module six >= 1.4.1}
BuildRequires:  fdupes
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libffi)
Requires:       python-asn1crypto >= 0.21.0
Recommends:     python-idna >= 2.1
Requires:       python-packaging
Requires:       python-pyasn1 >= 0.1.8
Requires:       python-setuptools >= 11.3
Requires:       python-six >= 1.4.1
%requires_eq    python-cffi
%if %{with python2}
BuildRequires:  python2-enum34
BuildRequires:  python2-ipaddress
%endif
# SECTION Test requirements
BuildRequires:  %{python_module hypothesis >= 1.11.4}
BuildRequires:  %{python_module iso8601}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pyasn1 >= 0.1.8}
BuildRequires:  %{python_module pytest > 3.3.0}
BuildRequires:  %{python_module virtualenv}
# /SECTION
# python-base is not enough, we need the _ssl module
%ifpython2
Requires:       python-enum34
Requires:       python-ipaddress
Requires:       python2
%endif
%ifpython3
Requires:       python3
%endif
%python_subpackages

%description
cryptography is a package designed to expose cryptographic
recipes and primitives to Python developers.  Our goal is
for it to be your "cryptographic standard library". It
supports Python 2.7, Python 3.4+, and PyPy-5.3+.

cryptography includes both high level recipes, and low
level interfaces to common cryptographic algorithms such as
symmetric ciphers, message digests and key derivation
functions.

%prep
%setup -q -n cryptography-%{version}
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
# Actually other *.c and *.h are appropriate
# see https://github.com/pyca/cryptography/issues/1463
find . -name .keep -print -delete

%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc AUTHORS.rst CONTRIBUTING.rst CHANGELOG.rst README.rst
%{python_sitearch}/*

%changelog
