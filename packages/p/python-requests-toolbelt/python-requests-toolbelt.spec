#
# spec file for package python-requests-toolbelt
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


%{?sle15_python_module_pythons}
Name:           python-requests-toolbelt
Version:        1.0.0
Release:        0
Summary:        A utility belt for advanced users of python3-requests
License:        Apache-2.0
URL:            https://github.com/requests/toolbelt
Source:         https://files.pythonhosted.org/packages/source/r/requests-toolbelt/requests-toolbelt-%{version}.tar.gz
# Replace expired test certificate
Source1:        test_cert.p12
# PATCH-FIX-OPENSUSE Stop using PyOpenSSLCompat, it generates widespread
# DeprecationWarnings
Patch0:         stop-using-pyopenssl-compat.patch
# PATCH-FIX-UPSTREAM 356-add-missing-casette-files.patch gh#requests/toolbelt!356 mcepl@suse.com
# add missing casette files
Patch1:         356-add-missing-casette-files.patch
BuildRequires:  %{python_module requests >= 2.12.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.12.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module betamax >= 0.5.0}
# gh#pyca/cryptography#5606
BuildRequires:  %{python_module pyOpenSSL >= 19.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trustme}
%if 0%{?suse_version} <= 1500
BuildRequires:  python-mock
%endif
# /SECTION
%python_subpackages

%description
This is just a collection of utilities for `python-requests`_, but don't
really belong in ``requests`` proper. The minimum tested requests version is
``2.1.0``. In reality, the toolbelt should work with ``2.0.1`` as well, but
some idiosyncracies prevent effective or sane testing on that version.

%prep
%autosetup -p1 -n requests-toolbelt-%{version}
cp %{SOURCE1} tests/certs

rm -rf requests_toolbelt.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Relax the crypto policies for the test-suite
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE=xyz_nonexistent_file
export OPENSSL_CONF=''

# Requires network access
%pytest
# -k 'not network'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/requests_toolbelt
%{python_sitelib}/requests_toolbelt-%{version}*-info

%changelog
