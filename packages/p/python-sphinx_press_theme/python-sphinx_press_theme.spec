#
# spec file for package python-sphinx_press_theme
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021 LISA GmbH, Bingen, Germany.
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
Name:           python-sphinx_press_theme
Version:        0.8.0
Release:        0
Summary:        A Sphinx-doc theme based on Vuepress
License:        MIT
URL:            https://schettino72.github.io/sphinx_press_site/
Source:         https://files.pythonhosted.org/packages/source/s/sphinx_press_theme/sphinx_press_theme-%{version}.tar.gz
Source100:      LICENSE
BuildRequires:  %{python_module Sphinx >= 4.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 4.0.0
BuildArch:      noarch
%python_subpackages

%description
Sphinx Press is a modern responsive theme for python’s Sphinx docs.

This theme is based on VuePress. It uses Vue.js & Stylus managed by vite.

%prep
%setup -q -n sphinx_press_theme-%{version}
cp %{SOURCE100} .

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
