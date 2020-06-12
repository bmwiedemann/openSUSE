#
# spec file for package python-moban
#
# Copyright (c) 2020 SUSE LLC
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
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-moban
Version:        0.7.8
Release:        0
Summary:        Yet another jinja2 CLI for static text generation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/moremoban/moban
Source:         https://files.pythonhosted.org/packages/source/m/moban/moban-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2 >= 2.7.1}
BuildRequires:  %{python_module appdirs >= 1.4.3}
BuildRequires:  %{python_module crayons >= 0.1.0}
BuildRequires:  %{python_module fs >= 2.4.11}
BuildRequires:  %{python_module jinja2-fsloader >= 0.2.0}
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
Requires:       python-Jinja2 >= 2.7.1
Requires:       python-appdirs >= 1.4.3
Requires:       python-crayons >= 0.1.0
Requires:       python-fs >= 2.4.11
Requires:       python-jinja2-fsloader >= 0.2.0
Requires:       python-lml >= 0.0.9
Requires:       python-ruamel.yaml >= 0.15.98
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-gitfs2
Suggests:       python-pypifs
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
%python_clone -a %{buildroot}%{_bindir}/moban
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_level_9_deprecated needs pypi-mobans-pkg just for templates... too much effort
# test_level_9 needs pypifs, which is now optional
# test_level_10_deprecated depends on access to github.com
# test_level_10 needs gitfs, which is optional
# test_level_11 probably depends on moban-handlebars, which is needed only in tests
# test_handle_targets_sequence fails on wrong arg count
# test_overrides_fs_url needs gitfs2, which is optional
# test_level_24 needs httpfs, which is optional
%python_expand nosetests-%{$python_bin_suffix} -e 'test_level_(9|10|11|24)|test_handle_targets_sequence|test_overrides_fs_url'

%post
%python_install_alternative moban

%postun
%python_uninstall_alternative moban

%files %{python_files}
%{python_sitelib}/*
%license LICENSE
%doc README.rst CHANGELOG.rst
%python_alternative %{_bindir}/moban

%changelog
