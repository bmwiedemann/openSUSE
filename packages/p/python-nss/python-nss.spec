#
# spec file for package python-nss
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


Name:           python-nss
Version:        1.0.1
Release:        0
Summary:        Python bindings for mozilla-nss and mozilla-nspr
License:        MPL-1.1+ OR GPL-2.0-or-later OR LGPL-2.0-or-later
Group:          Development/Languages/Python
URL:            http://www.mozilla.org/projects/security/pki/python-nss
Source:         https://files.pythonhosted.org/packages/source/p/python-nss/python-nss-%{version}.tar.bz2
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  mozilla-nspr-devel
BuildRequires:  mozilla-nss-devel
# Required for tests
BuildRequires:  mozilla-nss-tools
%python_subpackages

%description
python-nss is a Python binding for NSS (Network Security Services) and
NSPR (Netscape Portable Runtime). NSS provides cryptography services
supporting SSL, TLS, PKI, PKIX, X509, PKCS*, etc. NSS is an
alternative to OpenSSL and used extensively by major software
projects. NSS is FIPS-140 certified.

%prep
%setup -q -n python-nss-%{version}

%build
%python_build

%install
%python_install

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python test/run_tests -i
}

%files %{python_files}
%license LICENSE.mpl LICENSE.lgpl LICENSE.gpl
%doc README doc/ChangeLog
%{python_sitearch}/*

%changelog
