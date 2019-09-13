#
# spec file for package python-cssselect2
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
Name:           python-cssselect2
Version:        0.2.1
Release:        0
Summary:        CSS selectors for Python ElementTree
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/Kozea/cssselect2/
Source:         https://files.pythonhosted.org/packages/source/c/cssselect2/cssselect2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tinycss2}
# /SECTION
Requires:       python-tinycss2
BuildArch:      noarch

%python_subpackages

%description
CSSselect2 is an implementation of CSS3 Selectors for markup
documents (HTML, XML, etc.) that can be read by ElementTree-like
parsers (including cElementTree, lxml, html5lib, etc.)

Unlike cssselect, it does not translate selectors to XPath and therefore does
not have all the correctness corner cases that are hard or impossible to fix in
cssselect.

%prep
%setup -q -n cssselect2-%{version}
sed -i '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec -m pytest cssselect2/tests

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
