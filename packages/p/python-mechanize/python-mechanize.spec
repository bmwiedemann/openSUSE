#
# spec file for package python-mechanize
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


%define modname mechanize
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-mechanize
Version:        0.4.3
Release:        0
Summary:        Stateful programmatic web browsing
License:        (BSD-3-Clause OR ZPL-2.1) AND BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-mechanize/mechanize
Source:         https://files.pythonhosted.org/packages/source/m/mechanize/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
BuildRequires:  python
BuildRequires:  python-rpm-macros
Requires:       python-Twisted
Requires:       python-html5lib
Requires:       python-zope.interface
BuildArch:      noarch
%python_subpackages

%description
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

The library is layered: mechanize.Browser (stateful web browser),
mechanize.UserAgent (configurable URL opener), plus urllib2 handlers.

Features include: ftp:, http: and file: URL schemes, browser history,
high-level hyperlink and HTML form support, HTTP cookies, HTTP-EQUIV and
Refresh, Referer [sic] header, robots.txt, redirections, proxies, and Basic and
Digest HTTP authentication. mechanize's response objects are (lazily-)
.seek()able and still work after .close().

Much of the code originally derived from Perl code by Gisle Aas (libwww-perl),
Johnny Lee (MSIE Cookie support) and last but not least Andy Lester
(WWW::Mechanize). urllib2 was written by Jeremy Hylton.

%prep
%setup -q -n %{modname}-%{version}
sed -i -e '/^#!\/usr\/bin\/env python/d' %{modname}/_{entities,equiv,form_controls}.py
sed -i "1d" examples/forms/{echo.cgi,example.py,simple.py} # Fix doc-file-dependency

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python ./run_tests.py -v

%files %{python_files}
%license LICENSE
%doc examples README.rst
%{python_sitelib}/%{modname}*

%changelog
