#
# spec file for package python-aiosmtpd
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
Name:           python-aiosmtpd
Version:        1.4.6
Release:        0
Summary:        SMTP server based on asyncio
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://aiosmtpd.readthedocs.io/
Source:         https://github.com/aio-libs/aiosmtpd/archive/v%{version}.tar.gz#/aiosmtpd-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       python-atpublic
Requires:       python-attrs
Requires:       (python-typing_extensions if python-base < 3.8)
Requires:       user(nobody)
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions if %python-base < 3.8}
BuildRequires:  user(nobody)
# /SECTION
%python_subpackages

%description
The Python standard library includes a basic SMTP server in the smtpd module,
based on the old asynchronous libraries asyncore and asynchat. These modules
are quite old and are definitely showing their age; asyncore and asynchat are
difficult APIs to work with, understand, extend, and fix.

With the introduction of the asyncio module in Python 3.4, a much better way of
doing asynchronous I/O is now available. It seems obvious that an asyncio-based
version of the SMTP and related protocols are needed for Python 3. This project
brings together several highly experienced Python developers collaborating on
this reimplementation.

This package provides such an implementation of both the SMTP and LMTP protocols.

%prep
%autosetup -p1 -n aiosmtpd-%{version}

# Don't bother with the code coverage while packaging
sed -i '/--cov=/d' pytest.ini

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/aiosmtpd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
ignore=""

%if 0%{?sle_version}
# One of the tests in this file breaks the tests client state for
# Leap, so it's ignored for now.
ignore="--ignore aiosmtpd/tests/test_server.py"
%endif

%pytest $ignore

%post
%python_install_alternative aiosmtpd

%postun
%python_uninstall_alternative aiosmtpd

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/aiosmtpd
%{python_sitelib}/aiosmtpd
%{python_sitelib}/aiosmtpd-%{version}*-info
%exclude %{python_sitelib}/aiosmtpd/docs

%changelog
