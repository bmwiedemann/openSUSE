#
# spec file for package python-sphinx-markdown-builder
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-sphinx-markdown-builder
Version:        0.6.10
Release:        0
Summary:        A Sphinx extension to add markdown generation support
License:        MIT
URL:            https://github.com/liran-funaro/sphinx-markdown-builder
Source:         https://github.com/liran-funaro/sphinx-markdown-builder/archive/refs/tags/%{version}.tar.gz#/sphinx_markdown_builder-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module Sphinx >= 5.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinxcontrib-httpdomain}
BuildRequires:  %{python_module tabulate}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Sphinx >= 5.1.0
Requires:       python-docutils
Requires:       python-tabulate
Suggests:       python-sphinxcontrib-httpdomain
BuildArch:      noarch
%python_subpackages

%description
A Sphinx extension to add markdown generation support.

%prep
%autosetup -p1 -n sphinx-markdown-builder-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/sphinx_markdown_builder
%{python_sitelib}/sphinx_markdown_builder-%{version}.dist-info

%changelog
