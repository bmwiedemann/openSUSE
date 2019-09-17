#
# spec file for package python-keyczar
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{!?license: %global license %doc}
%define pkgname keyczar
Name:           python-keyczar
Version:        0.716
Release:        0
Summary:        Python toolkit for cryptography
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://www.keyczar.org
Source0:        https://github.com/google/%{pkgname}/archive/Python_release_%{version}.tar.gz
Source1:        keyczart.1
Patch0:         0001-Fixes-output-value-changes-between-older-and-newer-p.patch
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module pycrypto >= 2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyasn1
Requires:       python-pycrypto >= 2.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Keyczar is a cryptographic toolkit that facilitates
using cryptography in applications.
Keyczar supports authentication and encryption with both symmetric and
asymmetric keys. Some features of Keyczar include:

 - Key rotation and versioning
 - Automated generation of initialization vectors and ciphertext signatures

%prep
%setup -q -n %{pkgname}-Python_release_%{version}/python
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -Dm644 %{SOURCE1} %{buildroot}%{_mandir}/man1/keyczart.1
%python_clone -a %{buildroot}%{_bindir}/keyczart
%python_clone -a %{buildroot}%{_mandir}/man1/keyczart.1

%post
%{python_install_alternative keyczart keyczart.1}

%postun
%{python_uninstall_alternative keyczart keyczart.1}

%if %{with test}
%check
export PYTHONPATH=$(pwd)/build/lib
pushd tests/keyczar_tests
%python_exec alltests.py
popd
%endif

%files %{python_files}
%doc README PKG-INFO doc/
%license LICENSE
%python_alternative %{_mandir}/man1/keyczart.1%{ext_man}
%{python_sitelib}/keyczar
%{python_sitelib}/python_keyczar-*.egg-info
%python_alternative %{_bindir}/keyczart

%changelog
