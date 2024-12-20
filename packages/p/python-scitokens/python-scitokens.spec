#
# spec file for package python-scitokens
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


%define bname scitokens

Name:           python-scitokens
Version:        1.8.1
Release:        0
Summary:        SciToken reference implementation library
License:        Apache-2.0
URL:            https://scitokens.org
Source:         https://github.com/scitokens/scitokens/archive/refs/tags/v%{version}.tar.gz#/%{bname}-%{version}.tar.gz
BuildRequires:  %{python_module PyJWT >= 2.2}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 2.2
Requires:       python-cryptography
Requires:       python-requests
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
SciTokens provide a token format for distributed authorization. The tokens are
self-describing, can be verified in a distributed fashion (no need to contact
the issuer to determine if the token is valid). This is convenient for a
federated environment where several otherwise-independent storage endpoints
want to delegate trust for an issuer for managing a storage allocation.

%prep
%autosetup -p1 -n scitokens-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/scitokens-admin-create-key
%python_clone -a %{buildroot}%{_bindir}/scitokens-admin-create-token
%python_clone -a %{buildroot}%{_bindir}/scitokens-verify-token
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not network'

%post
%python_install_alternative scitokens-admin-create-key
%python_install_alternative scitokens-admin-create-token
%python_install_alternative scitokens-verify-token

%postun
%python_uninstall_alternative scitokens-admin-create-key
%python_uninstall_alternative scitokens-admin-create-token
%python_uninstall_alternative scitokens-verify-token

%files %{python_files}
%{python_sitelib}/scitokens
%{python_sitelib}/scitokens-%{version}.dist-info
%python_alternative %{_bindir}/scitokens-admin-create-key
%python_alternative %{_bindir}/scitokens-admin-create-token
%python_alternative %{_bindir}/scitokens-verify-token

%changelog
