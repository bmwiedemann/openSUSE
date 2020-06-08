#
# spec file for package python-IMAPClient
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-IMAPClient
Version:        2.1.0
Release:        0
Summary:        Easy-to-use, Pythonic and complete IMAP client library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mjs/imapclient/
Source0:        https://github.com/mjs/imapclient/archive/%{version}.tar.gz
BuildRequires:  %{python_module mock >= 1.3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 20.5}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
IMAPClient is an easy-to-use, Pythonic and complete IMAP client library.

Features:
    * Arguments and return values are natural Python types.
    * IMAP server responses are fully parsed and readily usable.
    * IMAP unique message IDs (UIDs) are handled transparently.
    * Internationalised mailbox names are transparently handled.
    * Time zones are correctly handled.
    * Convenience methods are provided for commonly used functionality.
    * Exceptions are raised when errors occur.

IMAPClient includes comprehensive units tests and automated
functional tests that can be run against a live IMAP server.

%prep
%setup -q -n imapclient-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_redacted_password fails on openSUSE 15.x only
%pytest -k 'not test_redacted_password'

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/*

%changelog
