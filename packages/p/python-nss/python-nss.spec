#
# spec file for package python-nss
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


Name:           python-nss
Version:        1.0.1
Release:        0
Summary:        Python bindings for mozilla-nss and mozilla-nspr
License:        MPL-1.1+ OR GPL-2.0-or-later OR LGPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/Python_binding_for_NSS
Source:         https://files.pythonhosted.org/packages/source/p/python-nss/python-nss-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM 0001-Rename-DSA-RSA-PublicKey-to-Py-DSA-RSA-PublicKey.patch bmo#1474274 mcepl@suse.com
# Incompatibility with NSS 3.58+
Patch0:         0001-Rename-DSA-RSA-PublicKey-to-Py-DSA-RSA-PublicKey.patch
# PATCH-FIX-UPSTREAM sphinx.patch bsc#[0-9]+ mcepl@suse.com
# this patch makes things totally awesome
Patch1:         sphinx.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
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

%package -n %{name}-doc
Summary:        Documentation files for %name
Group:          Documentation/Other

%description -n %{name}-doc
HTML Documentation and examples for %name.

%prep
%autosetup -p1 -n python-nss-%{version}

%build
%python_build build_doc
rm -rf build/sphinx/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python test/run_tests -i
}

%files %{python_files}
%license LICENSE.mpl LICENSE.lgpl LICENSE.gpl
%doc README doc/ChangeLog
%{python_sitearch}/*

%files -n %{name}-doc
%license LICENSE.mpl LICENSE.lgpl LICENSE.gpl
%doc build/sphinx/html

%changelog
