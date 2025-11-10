#
# spec file for package python-sigstore
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%{?sle15_python_module_pythons}
Name:           python-sigstore
Version:        4.1.0
Release:        0
Summary:        A tool for signing Python package distributions
License:        Apache-2.0
URL:            https://github.com/sigstore/sigstore-python
Source0:        https://github.com/sigstore/sigstore-python/archive/v%{version}.tar.gz#/sigstore-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-ecparam-testing.patch gh#sigstore/sigstore-python#1603 mcepl@suse.com
# Update supported public key algorithms
Patch0:         fix-ecparam-testing.patch
# PATCH-FIX-UPSTREAM nofail-neg-test.patch gh#sigstore/sigstore-python!1605 mcepl@suse.com
# Try to not fail negative key tests if support is not there
Patch1:         nofail-neg-test.patch
BuildRequires:  %{python_module PyJWT >= 2.1}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module cryptography >= 42}
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module id >= 1.1.0}
BuildRequires:  %{python_module importlib-resources >= 5.7 if %python-base < 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs >= 4.2}
BuildRequires:  %{python_module pyOpenSSL >= 23.0.0}
BuildRequires:  %{python_module pyasn1 >= 0.6}
BuildRequires:  %{python_module pydantic >= 2}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module rfc3161-client >= 1.0.3}
BuildRequires:  %{python_module rfc8785 >= 0.1.2}
BuildRequires:  %{python_module rich >= 13.0}
BuildRequires:  %{python_module sigstore-models}
BuildRequires:  %{python_module sigstore-rekor-types == 0.0.18}
BuildRequires:  %{python_module tuf >= 6.0}
BuildRequires:  python-rpm-macros

# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module importlib_resources if %python-base < 3.11}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyJWT >= 2.1
Requires:       python-cryptography >= 42
Requires:       python-id >= 1.1.0
Requires:       python-platformdirs >= 4.2
Requires:       python-pyOpenSSL >= 23.0.0
Requires:       python-pyasn1 >= 0.6
Requires:       python-pydantic >= 2
Requires:       python-requests
Requires:       python-rfc3161-client
Requires:       python-rfc8785 >= 0.1.2
Requires:       python-rich >= 13.0
Requires:       python-sigstore-models
Requires:       python-sigstore-rekor-types == 0.0.18
Requires:       python-tuf >= 6.0
Requires:       (python-importlib_resources if python-base < 3.11)
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
sigstore is a Python tool for generating and verifying Sigstore
signatures. You can use it to sign and verify Python package
distributions, or anything else!

%prep
%autosetup -p1 -n sigstore-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/sigstore
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Fails with https://github.com/sigstore/sigstore-python/issues/1603
%pytest --skip-online test/unit

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative sigstore

%post
%python_install_alternative sigstore

%postun
%python_uninstall_alternative sigstore

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/sigstore
%{python_sitelib}/sigstore
%{python_sitelib}/sigstore-%{version}.dist-info

%changelog
