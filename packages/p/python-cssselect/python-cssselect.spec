#
# spec file for package python-cssselect
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-cssselect
Version:        1.0.3
Release:        0
Summary:        CSS3 selectors for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://packages.python.org/cssselect/
Source:         https://pypi.io/packages/source/c/cssselect/cssselect-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
cssselect parses CSS3 Selectors and translates them to XPath 1.0
expressions. Such expressions can be used in lxml or another XPath engine to
find the matching elements in an XML or HTML document.

This module used to live inside of lxml as lxml.cssselect before it was
extracted as a stand-alone project.

%prep
%setup -q -n cssselect-%{version}

%build
%python_build

%install
%python_install

%files %python_files
%defattr(-,root,root,-)
%{python_sitelib}/*
%doc README.rst LICENSE CHANGES AUTHORS

%changelog
