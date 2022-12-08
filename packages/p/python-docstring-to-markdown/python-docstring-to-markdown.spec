#
# spec file for package python-docstring-to-markdown
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


Name:           python-docstring-to-markdown
Version:        0.11
Release:        0
Summary:        On the fly conversion of Python docstrings to markdown
License:        LGPL-2.1-only
URL:            https://github.com/python-lsp/docstring-to-markdown
Source:         https://github.com/python-lsp/docstring-to-markdown/archive/refs/tags/v%{version}.tar.gz#/docstring-to-markdown-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-docstring_to_markdown = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
On the fly conversion of Python docstrings to markdown
  - Python 3.6+
  - currently can recognise reStructuredText and convert
    multiple of its features to Markdown
  - in the future will be able to convert Google docstrings too

%prep
%setup -q -n docstring-to-markdown-%{version}
sed -i -e '/--cov/d' -e '/-flake8/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/docstring_to_markdown
%{python_sitelib}/docstring_to_markdown-%{version}*-info

%changelog
