#
# spec file for package python-pipdeptree
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


Name:           python-pipdeptree
Version:        2.23.0
Release:        0
Summary:        Command line utility to show dependency tree of packages
License:        MIT
URL:            https://github.com/naiquevin/pipdeptree
Source:         https://github.com/naiquevin/pipdeptree/archive/%{version}.tar.gz#/pipdeptree-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pip
Suggests:       python-graphviz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  graphviz-gnome
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Command line utility to show dependency tree of packages.

%prep
%setup -q -n pipdeptree-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pipdeptree

%check
%pytest -k 'not test_custom_interpreter and not test_console'

%post
%{python_install_alternative pipdeptree}

%postun
%{python_uninstall_alternative pipdeptree}

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pipdeptree
%{python_sitelib}/pipdeptree
%{python_sitelib}/pipdeptree-%{version}*-info

%changelog
