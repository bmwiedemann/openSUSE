#
# spec file for package python-sigstore
#
# Copyright (c) 2024 SUSE LLC
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
Version:        3.6.1
Release:        0
Summary:        A tool for signing Python package distributions
License:        Apache-2.0
URL:            https://github.com/sigstore/sigstore-python
Source:         https://github.com/sigstore/sigstore-python/archive/v%{version}.tar.gz#/sigstore-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module rfc3161-client}
BuildRequires:  %{python_module cryptography >= 42}
BuildRequires:  %{python_module id >= 1.1.0}
BuildRequires:  %{python_module platformdirs >= 4.2}
BuildRequires:  %{python_module pyasn1 >= 0.6}
BuildRequires:  %{python_module pydantic >= 2}
BuildRequires:  %{python_module PyJWT >= 2.1}
BuildRequires:  %{python_module pyOpenSSL >= 23.0.0}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module rfc8785 >= 0.1.2}
BuildRequires:  %{python_module rich >= 13.0}
BuildRequires:  %{python_module sigstore-protobuf-specs == 0.3.2}
BuildRequires:  %{python_module sigstore-rekor-types == 0.0.18}
BuildRequires:  %{python_module tuf >= 5.0}

# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module importlib_resources if %python-base < 3.11}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cryptography >= 42
Requires:       python-id >= 1.1.0
Requires:       python-platformdirs >= 4.2
Requires:       python-pyasn1 >= 0.6
Requires:       python-pydantic >= 2
Requires:       python-PyJWT >= 2.1
Requires:       python-pyOpenSSL >= 23.0.0
Requires:       python-requests
Requires:       python-rfc8785 >= 0.1.2
Requires:       python-rich >= 13.0
Requires:       python-sigstore-protobuf-specs == 0.3.2
Requires:       python-sigstore-rekor-types == 0.0.18
Requires:       python-tuf >= 5.0
Requires:       (python-importlib_resources if python-base < 3.11)
Requires:       python-rfc3161-client
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
