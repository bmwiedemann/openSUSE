#
# spec file for package python-paramiko
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
Name:           python-paramiko
Version:        2.7.2
Release:        0
Summary:        SSH2 protocol library
License:        LGPL-2.1-or-later
Group:          Documentation/Other
URL:            http://www.paramiko.org/
Source0:        https://files.pythonhosted.org/packages/source/p/paramiko/paramiko-%{version}.tar.gz
Patch0:         paramiko-test_extend_timeout.patch
# PATCH-FIX-UPSTREAM paramiko-pr1655-remove-pytest-relaxed.patch gh#paramiko/paramiko#1655 -- pytest-relaxed is broken
Patch1:         paramiko-pr1655-remove-pytest-relaxed.patch
BuildRequires:  %{python_module PyNaCl >= 1.0.1}
BuildRequires:  %{python_module bcrypt >= 3.1.3}
BuildRequires:  %{python_module cryptography >= 2.5}
BuildRequires:  %{python_module gssapi}
BuildRequires:  %{python_module invocations}
BuildRequires:  %{python_module invoke}
BuildRequires:  %{python_module pyasn1 >= 0.1.7}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-gssapi
Recommends:     python-invoke
Requires:       python-PyNaCl >= 1.0.1
Requires:       python-bcrypt >= 3.1.3
Requires:       python-cryptography >= 2.5
Requires:       python-pyasn1 >= 0.1.7
BuildArch:      noarch
BuildRequires:  %{python_module mock}
%python_subpackages

%description
This is a library for making SSH2 connections (client or server).
Emphasis is on using SSH2 as an alternative to SSL for making secure
connections between python scripts.  All major ciphers and hash methods
are supported.  SFTP client and server mode are both supported too.

%package -n python-paramiko-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module paramiko-doc = %{version}}

%description -n python-paramiko-doc
This is a library for making SSH2 connections (client or server).
Emphasis is on using SSH2 as an alternative to SSL for making secure
connections between python scripts.  All major ciphers and hash methods
are supported.  SFTP client and server mode are both supported too.

This package contains the documentation.

%prep
%setup -q -n paramiko-%{version}
%autopatch -p1

# Fix non-executable script rpmlint issue:
find demos -name "*.py" -exec sed -i "/#\!\/usr\/bin\/.*/d" {} \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%files -n python-paramiko-doc
%license LICENSE
%doc demos/

%changelog
