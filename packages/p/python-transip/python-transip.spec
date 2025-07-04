#
# spec file for package python-transip
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-transip
Version:        2.1.2
Release:        0
Summary:        TransIP API Connector
License:        MIT
URL:            https://github.com/benkonrath/transip-api
Source:         https://github.com/benkonrath/transip-api/archive/%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module suds}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
Requires:       python-requests
Requires:       python-suds
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This library implements part of the TransIP API in Python.

%prep
%setup -q -n transip-api-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/transip-api
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# testConstructor needs network connection
%pytest -k 'not (test_constructor or testConstructor)'

%post
%python_install_alternative transip-api

%postun
%python_uninstall_alternative transip-api

%files %{python_files}
%license LICENSE
%{python_sitelib}/transip
%{python_sitelib}/transip-%{version}.dist-info
%python_alternative %{_bindir}/transip-api

%changelog
