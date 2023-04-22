#
# spec file for package python-mkdocs-material
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


Name:           python-mkdocs-material
Version:        9.1.7
Release:        0
Summary:        Material theme for mkdocs
License:        MIT
URL:            https://squidfunk.github.io/mkdocs-material/
Source:         https://files.pythonhosted.org/packages/source/m/mkdocs_material/mkdocs_material-%{version}.tar.gz
# PATCH-FIX-OPENSUSE no-hatchling-requirements_txt.patch mcepl@suse.com
# Manually create project.dependencies in pyproject.toml instead of using
# hatch_requirements_txt module
# This is a brutal hack, but otherwise (see sr#1072844 for
# details) we need python-hatch_requirements_txt which pulls in
# excessive number of packages (starting with python-conincidence,
# python-whey, python-domdf-python-tools, and many others). Until
# we have these in openSUSE, we should stay with this
# hand-managed patch.
Patch0:         no-hatchling-requirements_txt.patch
BuildRequires:  %{python_module Markdown >= 3.2}
BuildRequires:  %{python_module hatch_nodejs_version}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module jinja2 >= 3.0}
BuildRequires:  %{python_module mkdocs >= 1.4.2}
BuildRequires:  %{python_module mkdocs-material-extensions >= 1.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pygments >= 2.12}
BuildRequires:  %{python_module pymdown-extensions >= 9.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Requirements for core
# https://github.com/squidfunk/mkdocs-material/blob/master/requirements.txt#L21
Requires:       python-Markdown >= 3.2
Requires:       python-jinja2 >= 3.0
Requires:       python-mkdocs >= 1.4.2
Requires:       python-mkdocs-material-extensions >= 1.1
Requires:       python-pygments >= 2.14
Requires:       python-pymdown-extensions >= 9.9.1
# Requirements for plugins
# https://github.com/squidfunk/mkdocs-material/blob/master/requirements.txt#L29
Requires:       python-colorama >= 0.4
Requires:       python-regex => 2022.4.24
Requires:       python-requests >= 2.26

BuildArch:      noarch
%python_subpackages

%description
Material theme for mkdocs

%prep
%autosetup -p1 -n mkdocs_material-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no tests available upstream

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/material/
%{python_sitelib}/mkdocs_material-%{version}.dist-info/

%changelog
