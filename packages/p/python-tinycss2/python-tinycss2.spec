#
# spec file for package python-tinycss2
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-tinycss2
Version:        1.2.1
Release:        0
Summary:        A tiny CSS parser
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Kozea/tinycss2
Source:         https://files.pythonhosted.org/packages/source/t/tinycss2/tinycss2-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module webencodings >= 0.4}
# /SECTION
Requires:       python-webencodings >= 0.4
BuildArch:      noarch

%python_subpackages

%description
tinycss2 is a low-level CSS parser and generator written in Python:
it can parse strings, return objects representing tokens and blocks,
and generate CSS strings corresponding to these objects.

Based on the CSS Syntax Level 3 specification, tinycss2 knows the
grammar of CSS but doesn't know specific rules, properties or values
supported in various CSS modules.

%prep
%setup -q -n tinycss2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/tinycss2
%{python_sitelib}/tinycss2-%{version}*-info

%changelog
