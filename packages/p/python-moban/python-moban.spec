#
# spec file for package python-moban
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
Name:           python-moban
Version:        0.5.0
Release:        0
Summary:        Yet another jinja2 CLI for static text generation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/moremoban/moban
Source:         https://files.pythonhosted.org/packages/source/m/moban/moban-%{version}.tar.gz
BuildRequires:  %{python_module GitPython >= 2.0.0}
BuildRequires:  %{python_module Jinja2 >= 2.7.1}
BuildRequires:  %{python_module appdirs >= 1.2.0}
BuildRequires:  %{python_module crayons >= 0.1.0}
BuildRequires:  %{python_module git-url-parse >= 1.2.2}
BuildRequires:  %{python_module jinja2-time}
BuildRequires:  %{python_module lml >= 0.0.9}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ruamel.yaml >= 0.15.98}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-GitPython >= 2.0.0
Requires:       python-Jinja2 >= 2.7.1
Requires:       python-appdirs >= 1.2.0
Requires:       python-crayons >= 0.1.0
Requires:       python-git-url-parse >= 1.2.2
Requires:       python-jinja2-time
Requires:       python-lml >= 0.0.9
Requires:       python-ruamel.yaml >= 0.15.98
BuildArch:      noarch
%python_subpackages

%description
moban (模板) is yet another jinja2 CLI for static text generation.

moban brings the template engine (JINJA2) for web into static text
generation. It is used in the pyexcel project to keep documentation
consistent across the documentations of individual libraries.

%prep
%setup -q -n moban-%{version}
# integration tests need network
rm -r tests/integration_tests

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_level_9 depends on package pypi-mobans-pkg
# test_level_10 depends on access to github.com
# test_level_11 depends on moban-handlebars
# test_handle_targets_sequence fails on wrong arg count
%python_exec %{_bindir}/nosetests --with-doctest --doctest-extension=.rst -e 'test_level_(9|10|11)|test_handle_targets_sequence' README.rst tests docs moban

%files %{python_files}
%{python_sitelib}/*
%license LICENSE
%doc README.rst CHANGELOG.rst
%python3_only %{_bindir}/moban

%changelog
