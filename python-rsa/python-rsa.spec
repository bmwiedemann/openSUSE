#
# spec file for package python-rsa
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
%bcond_without tests
Name:           python-rsa
Version:        4.0
Release:        0
Summary:        Pure-Python RSA Implementation
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://stuvel.eu/rsa
Source:         https://files.pythonhosted.org/packages/source/r/rsa/rsa-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyasn1 >= 0.1.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyasn1 >= 0.1.3
Requires(post): update-alternatives
Requires(pre):  coreutils
Requires(preun): update-alternatives
BuildArch:      noarch
%if %{with tests}
BuildRequires:  %{python_module nose}
%endif
%python_subpackages

%description
Python-RSA is a pure-Python RSA implementation. It supports encryption and
decryption, signing and verifying signatures, and key generation according to
PKCS#1 version 1.5.

%prep
%setup -q -n rsa-%{version}

%build
export LC_ALL=en_US.utf8
%python_build

%install
export LC_ALL=en_US.utf8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/pyrsa-priv2pub
%python_clone -a %{buildroot}%{_bindir}/pyrsa-decrypt
%python_clone -a %{buildroot}%{_bindir}/pyrsa-encrypt
%python_clone -a %{buildroot}%{_bindir}/pyrsa-keygen
%python_clone -a %{buildroot}%{_bindir}/pyrsa-sign
%python_clone -a %{buildroot}%{_bindir}/pyrsa-verify

%post
%{python_install_alternative pyrsa-priv2pub pyrsa-decrypt pyrsa-encrypt pyrsa-keygen pyrsa-sign pyrsa-verify}

%preun
%python_uninstall_alternative pyrsa-priv2pub

%if %{with tests}
%check
export LC_ALL=en_US.utf8
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%doc CHANGELOG.txt README.md
%python_alternative %{_bindir}/pyrsa-decrypt
%python_alternative %{_bindir}/pyrsa-encrypt
%python_alternative %{_bindir}/pyrsa-keygen
%python_alternative %{_bindir}/pyrsa-priv2pub
%python_alternative %{_bindir}/pyrsa-sign
%python_alternative %{_bindir}/pyrsa-verify
%{python_sitelib}/*

%changelog
