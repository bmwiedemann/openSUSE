#
# spec file for package python-pykerberos
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
Name:           python-pykerberos
Version:        1.2.1
Release:        0
Summary:        High-level interface to Kerberos
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/02strich/pykerberos/
Source:         https://pypi.io/packages/source/p/pykerberos/pykerberos-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(krb5)
# https://github.com/02strich/pykerberos/issues/17
Conflicts:      python-kerberos
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%python_subpackages

%description
This Python package is a high-level wrapper for Kerberos (GSSAPI) operations.
The goal is to avoid having to build a module that wraps the entire Kerberos.framework,
and instead offer a limited set of functions that do what is needed for client/server
Kerberos authentication based on <http://www.ietf.org/rfc/rfc4559.txt>.

%prep
%setup -q -n pykerberos-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc README.txt
%license LICENSE
%{python_sitearch}/*

%changelog
