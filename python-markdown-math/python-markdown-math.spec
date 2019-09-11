#
# spec file for package python-markdown-math
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
Name:           python-markdown-math
Version:        0.6
Release:        0
Summary:        Math extension for Python-Markdown
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mitya57/python-markdown-math
Source:         https://files.pythonhosted.org/packages/source/p/python-markdown-math/python-markdown-math-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Markdown
BuildArch:      noarch
# SECTION Required for tests in %%check
BuildRequires:  %{python_module Markdown}
# /SECTION
%python_subpackages

%description
This extension adds math formulas support to Python-Markdown.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.md changelog
%{python_sitelib}/*

%changelog
