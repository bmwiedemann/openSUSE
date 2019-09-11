#
# spec file for package python-matrix-synapse-ldap3
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}

%define         github_user matrix-org
%define         short_name matrix-synapse-ldap3
Name:           python-%{short_name}
Version:        0.1.2
Release:        0
License:        Apache-2.0
Summary:        An LDAP3 auth provider for Synapse
Url:            https://github.com/%{github_user}/%{short_name}
Group:          Development/Languages/Python
Source:         https://github.com/%{github_user}/%{short_name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module ldap3}
BuildRequires:  %{python_module pydenticon}
Requires:       python-Twisted
Requires:       python-ldap3
Requires:       python-pydenticon
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
Synapse LDAP Auth Provider

Allows synapse to use LDAP as a password provider.

%prep
%setup -q -n %{short_name}-%{version}

%build
%python_build

%install
%python_install
%fdupes %{buildroot}%{_prefix}

%files %{python_files}
%defattr(-,root,root,-)
%doc LICENSE README.rst
%{python_sitelib}/*

%changelog
