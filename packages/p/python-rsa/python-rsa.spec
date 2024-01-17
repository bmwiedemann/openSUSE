#
# spec file for package python-rsa
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-rsa
Version:        4.9
Release:        0
Summary:        Pure-Python RSA Implementation
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://stuvel.eu/rsa
Source:         https://files.pythonhosted.org/packages/source/r/rsa/rsa-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-pyasn1 >= 0.1.3
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(preun):update-alternatives
%endif
Requires(pre):  coreutils
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pyasn1 >= 0.1.3}
BuildRequires:  %{python_module pytest}
# /SECTION
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

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pyrsa-priv2pub

%post
%{python_install_alternative pyrsa-priv2pub pyrsa-decrypt pyrsa-encrypt pyrsa-keygen pyrsa-sign pyrsa-verify}

%preun
%python_uninstall_alternative pyrsa-priv2pub

%check
# don't run the static type checker test -- mypy is only available for the default python3 flavor
# pytest --ignore tests/test_mypy.py

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/pyrsa-decrypt
%python_alternative %{_bindir}/pyrsa-encrypt
%python_alternative %{_bindir}/pyrsa-keygen
%python_alternative %{_bindir}/pyrsa-priv2pub
%python_alternative %{_bindir}/pyrsa-sign
%python_alternative %{_bindir}/pyrsa-verify
%{python_sitelib}/rsa
%{python_sitelib}/rsa-%{version}*-info

%changelog
