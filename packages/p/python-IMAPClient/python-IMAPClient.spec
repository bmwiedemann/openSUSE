#
# spec file for package python-IMAPClient
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2016-2019 LISA GmbH, Bingen, Germany.
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


Name:           python-IMAPClient
Version:        3.0.1
Release:        0
Summary:        Pythonic IMAP client library
License:        BSD-3-Clause
URL:            https://github.com/mjs/imapclient/
Source0:        https://github.com/mjs/imapclient/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 20.5}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
IMAPClient is a Pythonic IMAP client library.

Features:
    * Arguments and return values are natural Python types.
    * IMAP server responses are parsed and readily usable.
    * IMAP unique message IDs (UIDs) and internationalised
      mailbox names are handled transparently.
    * Time zones are handled.
    * Convenience methods are provided for commonly used functionality.
    * Exceptions are raised when errors occur.

IMAPClient includes comprehensive units tests and automated
functional tests that can be run against a live IMAP server.

%prep
%setup -q -n imapclient-%{version}

%build
sed -i 's:#!::' imapclient/interact.py
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_redacted_password fails on openSUSE 15.x only
%pytest -k 'not test_redacted_password'

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/imapclient
%{python_sitelib}/[Ii][Mm][Aa][Pp][Cc]lient-%{version}.dist-info

%changelog
