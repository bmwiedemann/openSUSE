#
# spec file for package python-mechanize
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.4.8
Release:        0
Summary:        Stateful programmatic web browsing
License:        BSD-3-Clause AND (BSD-3-Clause OR ZPL-2.1)
URL:            https://github.com/python-mechanize/mechanize
Source:         https://files.pythonhosted.org/packages/source/m/mechanize/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-mechanize-setup.cfg.patch gh#python-mechanize/mechanize#73 -- setup.cfg: Move packages def to options section
Patch1:         %{name}-setup.cfg.patch
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-html5lib
BuildArch:      noarch
%python_subpackages

%description
Stateful programmatic web browsing in Python. Browse pages
programmatically with HTML form filling and clicking
of links.

%prep
%setup -q -n %{modname}-%{version}
%patch1 -p1
sed -i -e '1{/^#!\/usr\/bin\/env python/d}' %{modname}/{_entities,_equiv,_form_controls,polyglot}.py
sed -i -e '1{/^#!/d}' examples/forms/{echo.cgi,example.py,simple.py}
chmod -x examples/forms/{echo.cgi,example.py,simple.py}

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
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
