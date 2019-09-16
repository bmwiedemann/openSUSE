#
# spec file for package python-asyncssh
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
%define skip_python2 1
Name:           python-asyncssh
Version:        1.18.0
Release:        0
Summary:        Asynchronous SSHv2 client and server library
License:        EPL-2.0 OR GPL-2.0-or-later
Group:          Development/Languages/Python
Url:            http://asyncssh.timeheart.net
Source:         https://files.pythonhosted.org/packages/source/a/asyncssh/asyncssh-%{version}.tar.gz
BuildRequires:  %{python_module bcrypt >= 3.1.3}
BuildRequires:  %{python_module cryptography >= 2.7}
BuildRequires:  %{python_module gssapi >= 1.2.0}
BuildRequires:  %{python_module pyOpenSSL >= 17.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  openssh
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
Requires:       python-bcrypt >= 3.1.3
Requires:       python-cryptography >= 2.7
Requires:       python-gssapi >= 1.2.0
Requires:       python-libnacl >= 1.4.2
Requires:       python-pyOpenSSL >= 17.0.0
BuildArch:      noarch

%python_subpackages

%description
AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python 3.4+
asyncio framework.


%prep
%setup -q -n asyncssh-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover -s tests_py35
%python_exec setup.py test

%files %{python_files}
%license LICENSE COPYRIGHT
%doc README.rst
%{python_sitelib}/*

%changelog
