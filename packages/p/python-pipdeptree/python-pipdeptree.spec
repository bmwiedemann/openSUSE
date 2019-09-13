#
# spec file for package python-pipdeptree
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
Name:           python-pipdeptree
Version:        0.13.2
Release:        0
Summary:        Command line utility to show dependency tree of packages
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/naiquevin/pipdeptree
Source:         https://github.com/naiquevin/pipdeptree/archive/%{version}.tar.gz#/pipdeptree-%{version}.tar.gz
# Generated following tests/virtualenvs/Makefile
Source1:        test-data.tgz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pip >= 6.0.0
Suggests:       python-graphviz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module pip >= 6.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  graphviz-gnome
# /SECTION
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
%python_subpackages

%description
Command line utility to show dependency tree of packages.

%prep
%setup -q -n pipdeptree-%{version}
tar -xzf %{SOURCE1}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pipdeptree

%check
# Two tests fail due to https://github.com/naiquevin/pipdeptree/issues/116
%python_exec -m pytest -k 'not test_render_tree_exclude and not test_render_tree_exclude_reverse'

%post
%{python_install_alternative pipdeptree}

%postun
%{python_uninstall_alternative pipdeptree}

%files %{python_files}
%doc CHANGES.md README.rst
%license LICENSE
%python_alternative %{_bindir}/pipdeptree
%{python_sitelib}/*

%changelog
