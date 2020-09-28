#
# spec file for package python-ldap
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-ldap
Version:        3.3.1
Release:        0
Summary:        Python LDAP interface
License:        Python-2.0
Group:          Development/Libraries/Python
URL:            https://www.python-ldap.org/
Source0:        https://files.pythonhosted.org/packages/source/p/python-ldap/python-ldap-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyasn1 >= 0.3.7}
BuildRequires:  %{python_module pyasn1-modules >= 0.1.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cyrus-sasl-devel >= 2.1
BuildRequires:  fdupes
BuildRequires:  krb5-devel
BuildRequires:  libopenssl-devel >= 0.9.7
# needed for slapd binary in tests
BuildRequires:  openldap2
# needed for ldapadd binary in tests
BuildRequires:  openldap2-client
BuildRequires:  openldap2-devel >= 2.4.11
BuildRequires:  python-rpm-macros
Requires:       python-pyasn1 >= 0.3.7
Requires:       python-pyasn1-modules >= 0.1.5
%python_subpackages

%description
python-ldap provides an object-oriented API to access LDAP directory
servers from Python programs.  Mainly it wraps the OpenLDAP 2.x libs
for that purpose.  Additionally the package contains modules for other
LDAP-related stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 schema, etc.).

%prep
%setup -q
cp Build/setup.cfg.suse-linux setup.cfg

%build
CFLAGS="%{optflags}" %python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENCE
%doc README Demo CHANGES TODO
%{python_sitearch}/*

%changelog
