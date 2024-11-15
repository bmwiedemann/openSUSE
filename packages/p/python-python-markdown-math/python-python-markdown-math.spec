#
# spec file for package python-python-markdown-math
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-python-markdown-math
Version:        0.8
Release:        0
Summary:        Math extension for Python-Markdown
License:        BSD-3-Clause
Provides:       python-markdown-math = %version-%release
Obsoletes:      python-markdown-math < %version-%release
URL:            https://github.com/mitya57/python-markdown-math
Source:         https://files.pythonhosted.org/packages/source/p/python-markdown-math/python-markdown-math-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Markdown
BuildArch:      noarch
# SECTION Required for tests in %%check
BuildRequires:  %{python_module Markdown}
# /SECTION
Provides:       python-markdown-math = %version
Obsoletes:      python-markdown-math < %version
%python_subpackages

%description
This extension adds math formulas support to Python-Markdown.

%prep
%autosetup -p1 -n python-markdown-math-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE
%doc README.md changelog
%{python_sitelib}/mdx_math.py
%pycache_only %{python_sitelib}/__pycache__/mdx_math*.pyc
%{python_sitelib}/python_markdown_math-%{version}*-info

%changelog
