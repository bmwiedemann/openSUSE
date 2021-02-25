#
# spec file for package python-asyncssh
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-asyncssh
Version:        2.5.0
Release:        0
Summary:        Asynchronous SSHv2 client and server library
License:        EPL-2.0 OR GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ronf/asyncssh
Source:         https://files.pythonhosted.org/packages/source/a/asyncssh/asyncssh-%{version}.tar.gz
Patch0:         gss_test.patch
# SECTION test requirements
BuildRequires:  %{python_module bcrypt >= 3.1.3}
BuildRequires:  %{python_module cryptography >= 2.8}
BuildRequires:  %{python_module fido2 >= 0.8.1}
BuildRequires:  %{python_module gssapi >= 1.2.0}
BuildRequires:  %{python_module pyOpenSSL >= 17.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module uvloop >= 0.9.1}
BuildRequires:  (libnettle8 if python38-base)
BuildRequires:  openssh
BuildRequires:  openssl
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bcrypt >= 3.1.3
Requires:       python-cryptography >= 2.8
Requires:       python-gssapi >= 1.2.0
Requires:       python-libnacl >= 1.4.2
Requires:       python-pyOpenSSL >= 17.0.0
Recommends:     python-fido2 >= 0.8.1
Recommends:     libnettle8
BuildArch:      noarch

%python_subpackages

%description
AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python asyncio framework.


%prep
%setup -q -n asyncssh-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover -v 

%files %{python_files}
%license LICENSE COPYRIGHT
%doc README.rst
%{python_sitelib}/*

%changelog
