#
# spec file for package python-sphinx_mdinclude
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


%define modname sphinx_mdinclude
Name:           python-sphinx_mdinclude
Version:        0.5.3
Release:        0
Summary:        Markdown extension for Sphinx
License:        MIT
URL:            https://github.com/omnilib/sphinx-mdinclude
Source:         https://files.pythonhosted.org/packages/source/s/sphinx_mdinclude/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module mistune}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Sphinx extension for including or writing pages in Markdown
format.

sphinx-mdinclude is a simple Sphinx extension that enables
including Markdown documents from within reStructuredText. It
provides the .. mdinclude:: directive, and automatically converts
the content of Markdown documents to reStructuredText format.

%prep
%autosetup -p1 -n %{modname}-%{version}

sed -i -e '1{\,^#!%{_bindir}/env python,d}' %{modname}/__init__.py \
    %{modname}/tests/test_renderer.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/sphinx_mdinclude
%{python_sitelib}/sphinx_mdinclude-%{version}*-info

%changelog
