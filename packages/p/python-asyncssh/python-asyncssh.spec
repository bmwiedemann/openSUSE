#
# spec file for package python-asyncssh
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-asyncssh
Version:        2.21.1
Release:        0
Summary:        Asynchronous SSHv2 client and server library
License:        EPL-2.0 OR GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ronf/asyncssh
Source:         https://files.pythonhosted.org/packages/source/a/asyncssh/asyncssh-%{version}.tar.gz
Patch0:         gss_test.patch
# PATCH-FIX-UPSTREAM fido2-compat.patch
Patch1:         fido2-compat.patch
# SECTION test requirements
BuildRequires:  %{python_module bcrypt >= 3.1.3}
BuildRequires:  %{python_module cryptography >= 39.0}
BuildRequires:  %{python_module fido2 >= 2}
BuildRequires:  %{python_module gssapi >= 1.2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL >= 17.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions >= 4.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  openssh
BuildRequires:  openssl
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 39.0
Requires:       python-typing_extensions >= 4.0.0
Recommends:     python-bcrypt >= 3.1.3
Recommends:     python-fido2 >= 2
Recommends:     python-gssapi >= 1.2.0
Recommends:     python-libnacl >= 1.4.2
Recommends:     python-pyOpenSSL >= 23.0.0
BuildArch:      noarch

%python_subpackages

%description
AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python asyncio framework.

%prep
%autosetup -p1 -n asyncssh-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not (test_connect_timeout_exceeded or test_forward_remote or test_enroll)'

%files %{python_files}
%license LICENSE COPYRIGHT
%doc README.rst
%{python_sitelib}/asyncssh
%{python_sitelib}/asyncssh-%{version}.dist-info

%changelog
