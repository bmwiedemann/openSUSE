#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{pypi_name}
Version:        1.4.0
Release:        0
Summary:        OpenID Connect support for Flask
Group:          Development/Libraries/Python
License:        BSD-2-Clause
URL:            https://github.com/fedora-infra/%{pypi_name}
Source0:        https://pypi.io/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE authlib.patch -- gh#puiterwijk/flask-oidc#138
Patch0:         authlib.patch

BuildArch:      noarch

BuildRequires:  %{python_module Authlib}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module itsdangerous}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

Requires:       python-Flask
Requires:       python-itsdangerous
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-six
Requires(post): update-alternatives
Requires(postun):update-alternatives

%python_subpackages

%description
This library should work with any standards compliant OpenID Connect provider.

It has been tested with:
* Ipsilon

%prep
%autosetup -p2 -n %{pypi_name}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/oidc-register

%post
%python_install_alternative oidc-register

%postun
%python_uninstall_alternative oidc-register

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/flask_oidc/
%{python_sitelib}/*.egg-info/
%python_alternative %{_bindir}/oidc-register

%changelog
