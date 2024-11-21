#
# spec file for package python-paramiko
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


%{?sle15_python_module_pythons}
Name:           python-paramiko
Version:        3.5.0
Release:        0
Summary:        SSH2 protocol library
License:        LGPL-2.1-or-later
URL:            https://www.paramiko.org/
Source0:        https://files.pythonhosted.org/packages/source/p/paramiko/paramiko-%{version}.tar.gz
Patch0:         paramiko-test_extend_timeout.patch
# PATCH-FIX-OPENSUSE remove-icecream-dep.patch to do not depend on python-icecream and unvendor lexicon
Patch1:         remove-icecream-dep.patch
BuildRequires:  %{python_module PyNaCl >= 1.0.1}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module bcrypt >= 3.2}
BuildRequires:  %{python_module cryptography >= 3.3}
BuildRequires:  %{python_module gssapi}
BuildRequires:  %{python_module invocations}
BuildRequires:  %{python_module invoke >= 2.0}
BuildRequires:  %{python_module lexicon}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module pytest-relaxed}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-gssapi
Recommends:     python-invoke
Recommends:     python-pyasn1 >= 0.1.7
Requires:       python-PyNaCl >= 1.5
Requires:       python-bcrypt >= 3.2
Requires:       python-cryptography >= 3.3
BuildArch:      noarch
%python_subpackages

%description
This is a library for making SSH2 connections (client or server).
Emphasis is on using SSH2 as an alternative to SSL for making secure
connections between python scripts.  All major ciphers and hash methods
are supported.  SFTP client and server mode are both supported too.

%package -n python-paramiko-doc
Summary:        Documentation for %{name}
Provides:       %{python_module paramiko-doc = %{version}}

%description -n python-paramiko-doc
This is a library for making SSH2 connections (client or server).
Emphasis is on using SSH2 as an alternative to SSL for making secure
connections between python scripts.  All major ciphers and hash methods
are supported.  SFTP client and server mode are both supported too.

This package contains the documentation.

%prep
%autosetup -p1 -n paramiko-%{version}
# Fix non-executable script rpmlint issue:
find demos -name "*.py" -exec sed -i "/#\!\/usr\/bin\/.*/d" {} \; -exec chmod -x {} \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# Do not test k5shell to avoid dependency
donttest="k5shell"
%pytest tests/test_*.py  -k "not $donttest"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/paramiko
%{python_sitelib}/paramiko-%{version}*-info

%files -n python-paramiko-doc
%license LICENSE
%doc demos/

%changelog
