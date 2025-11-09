#
# spec file for package python-pypi-attestations
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


%define upname  pypi_attestations
Name:           python-pypi-attestations
Version:        0.0.28
Release:        0
Summary:        A library to convert between Sigstore Bundles and PEP-740 Attestation objects
License:        Apache-2.0
URL:            https://pypi.org/project/pypi-attestations
Source:         https://files.pythonhosted.org/packages/source/p/pypi-attestations/%{upname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove_setuptools-scm.patch bsc#[0-9]+ mcepl@suse.com
# Don't use setuptools-scm
Patch0:         remove_setuptools-scm.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pyasn1 >= 0.6}
BuildRequires:  %{python_module pydantic >= 2.10.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module rfc3986}
BuildRequires:  %{python_module sigstore >= 4.0}
BuildRequires:  %{python_module sigstore-models}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cryptography
Requires:       python-packaging
Requires:       python-pyasn1 >= 0.6
Requires:       python-pydantic >= 2.10.0
Requires:       python-requests
Requires:       python-rfc3986
Requires:       python-sigstore >= 4.0
Requires:       python-sigstore-models
Suggests:       python-pdoc
Suggests:       python-ruff >= 0.9
Suggests:       python-mypy >= 1.0
Suggests:       python-types-html5lib
Suggests:       python-types-requests
Suggests:       python-types-toml
Suggests:       python-interrogate
Suggests:       python-pypi-attestations
Suggests:       python-pypi-attestations
Suggests:       python-build
BuildArch:      noarch
%python_subpackages

%description
A library to convert between Sigstore Bundles and PEP-740 Attestation objects

%prep
%autosetup -p1 -n %{upname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pypi-attestations
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pypi-attestations

%postun
%python_uninstall_alternative pypi-attestations

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/pypi-attestations
%{python_sitelib}/%{upname}
%{python_sitelib}/%{upname}-%{version}.dist-info

%changelog
