#
# spec file for package python-flask-oidc
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2020 Neal Gompa <ngompa13@gmail.com>.
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


%global pypi_name flask-oidc
Name:           python-%{pypi_name}
Version:        2.4.0
Release:        0
Summary:        OpenID Connect support for Flask
License:        BSD-2-Clause
URL:            https://github.com/fedora-infra/%{pypi_name}
Source0:        https://pypi.io/packages/source/f/%{pypi_name}/flask_oidc-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Don't fail a test due to quoting
Patch0:         ignore-quoting-madness.patch
BuildRequires:  %{python_module Authlib >= 1.2}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.20}
BuildRequires:  %{python_module responses}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Authlib >= 1.2
Requires:       python-Flask
Requires:       python-blinker >= 1.4
Requires:       python-requests >= 2.20
BuildArch:      noarch
%python_subpackages

%description
This library should work with any standards compliant OpenID Connect provider.

It has been tested with:
* Ipsilon

%prep
%autosetup -p1 -n flask_oidc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSES/BSD-2-Clause.txt
%{python_sitelib}/flask_oidc/
%{python_sitelib}/flask_oidc-%{version}.dist-info

%changelog
