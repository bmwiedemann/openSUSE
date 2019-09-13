#
# spec file for package python-cookies
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
Name:           python-cookies
Version:        2.2.1
Release:        0
Summary:        Friendlier RFC 6265-compliant cookie parser/renderer
License:        MIT
Group:          Development/Languages/Python
URL:            https://gitlab.com/sashahart/cookies
Source:         https://files.pythonhosted.org/packages/source/c/cookies/cookies-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/sashahart/cookies/master/LICENSE
# PATCH-FIX-OPENSUSE do-not-install-test_cookies.diff -- Do not install test files
Patch0:         do-not-install-test_cookies.diff
Patch1:         python37.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
cookies.py is a Python module for working with HTTP cookies: parsing and
rendering 'Cookie:' request headers and 'Set-Cookie:' response headers,
and exposing a convenient API for creating and modifying cookies. It can be
used as a replacement of Python's Cookie.py (aka http.cookies).

* Rendering according to RFC 6265. It uses URL encoding to represent
  non-ASCII by default, like many other languages' libraries.
* Liberal parsing, incorporating many complaints about Cookie.py
  barfing on common cookie formats which can be reliably parsed
* Documented code, with chapter and verse from RFCs
* A test suite with 100%% test coverage
* Unlike Cookie.py, it doesn't lock all implementation inside its own
  classes. You can suppress minor parse exceptions with parameters
  rather than subclass wrappers. You can plug in your own parsers,
  renderers and validators for new or existing cookie attributes. You
  can render the data out in a dict. You can use the underlying
  imperative API or even lift the parser's regexps for your own
  parser or project.

While this is intended to be a good module for handling cookies, it does not
even try to do any of the following:

* Backward compatibility with Cookie.py
* Implementation of RFC 2109 or 2965
* Handle every conceivable output from legacy applications
* Provide a means to store pickled Python objects in cookie values

This does not compete with the cookielib (http.cookiejar) module in the Python
standard library.

%prep
%setup -q -n cookies-%{version}
%autopatch -p1

cp %{SOURCE1} .

%build
%python_build

%install
%python_install

%check
%python_expand py.test-%{$python_version} test_cookies.py

%files %{python_files}
%license LICENSE
%doc README
%{python_sitelib}/*

%changelog
