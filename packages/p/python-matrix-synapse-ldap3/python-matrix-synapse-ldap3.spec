#
# spec file for package python-matrix-synapse-ldap3
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python3 1
%define         github_user matrix-org
%define         short_name matrix-synapse-ldap3
Name:           python-%{short_name}
Version:        0.1.3
Release:        0
Summary:        An LDAP3 auth provider for Synapse
License:        Apache-2.0
URL:            https://github.com/matrix-org/matrix-synapse-ldap3
Source:         https://github.com/%{github_user}/%{short_name}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/matrix-org/matrix-synapse-ldap3/issues/73
Patch0:         py3compat.patch
BuildRequires:  %{python_module Twisted >= 15.1}
BuildRequires:  %{python_module ldap3 >= 0.9.5}
BuildRequires:  %{python_module ldaptor}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pydenticon}
BuildRequires:  %{python_module service_identity}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted >= 15.1
Requires:       python-ldap3 >= 0.9.5
Requires:       python-pydenticon
Requires:       python-service_identity
BuildArch:      noarch
%python_subpackages

%description
Synapse LDAP Auth Provider

Allows synapse to use LDAP as a password provider.

%prep
%setup -q -n %{short_name}-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
