#
# spec file for package python-zope.testing
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-zope.testing
Version:        5.1
Release:        0
Summary:        Zope testing helpers
License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zope.testing
Source:         https://files.pythonhosted.org/packages/source/z/zope.testing/zope_testing-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
This package provides a number of testing frameworks.

cleanup
  Provides a mixin class for cleaning up after tests that
  make global changes.

formparser
  An HTML parser that extracts form information.

  **Python 2 only**

  This is intended to support functional tests that need to extract
  information from HTML forms returned by the publisher.

  See formparser.txt.

loggingsupport
  Support for testing logging code

  If you want to test that your code generates proper log output, you
  can create and install a handler that collects output.

loghandler
  Logging handler for tests that check logging output.

module
  Lets a doctest pretend to be a Python module.

  See module.txt.

renormalizing
  Regular expression pattern normalizing output checker.
  Useful for doctests.

server
  Provides a simple HTTP server compatible with the zope.app.testing
  functional testing API.  Lets you interactively play with the system
  under test.  Helpful in debugging functional doctest failures.

  **Python 2 only**

setupstack
  A simple framework for automating doctest set-up and tear-down.
  See setupstack.txt.

wait
  A small utility for dealing with timing non-determinism
  See wait.txt.

%prep
%setup -q -n zope_testing-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v zope.testing.tests.test_suite

%files %{python_files}
%license LICENSE.txt
%doc COPYRIGHT.txt README.rst
%dir %{python_sitelib}/zope
%{python_sitelib}/zope/testing
%{python_sitelib}/zope[_.]testing-%{version}.dist-info
%{python_sitelib}/zope.testing-%{version}*-nspkg.pth

%changelog
