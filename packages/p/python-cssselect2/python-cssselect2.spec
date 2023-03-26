#
# spec file for package python-cssselect2
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


%define skip_python2 1
Name:           python-cssselect2
Version:        0.7.0
Release:        0
Summary:        CSS selectors for Python ElementTree
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Kozea/cssselect2/
Source:         https://github.com/Kozea/cssselect2/archive/refs/tags/%{version}.tar.gz#/cssselect2-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tinycss2
Requires:       python-webencodings
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tinycss2}
BuildRequires:  %{python_module webencodings}
# /SECTION
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

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/cssselect2
%{python_sitelib}/cssselect2-%{version}*-info

%changelog
