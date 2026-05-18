#
# spec file for package python-pipdeptree
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-pipdeptree
Version:        2.35.3
Release:        0
Summary:        Command line utility to show dependency tree of packages
License:        MIT
URL:            https://github.com/tox-dev/pipdeptree
Source:         https://github.com/tox-dev/pipdeptree/archive/%{version}.tar.gz#/pipdeptree-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatch-vcs >= 0.5}
BuildRequires:  %{python_module hatchling >= 1.27}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 26
Requires:       python-pip >= 25.2
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
Suggests:       python-graphviz >= 0.21
Suggests:       python-rich >= 14.3.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module graphviz >= 0.21}
BuildRequires:  %{python_module packaging >= 26}
BuildRequires:  %{python_module pip >= 25.2}
BuildRequires:  %{python_module pytest >= 8.4.2}
BuildRequires:  %{python_module pytest-mock >= 3.15.1}
BuildRequires:  %{python_module pytest-subprocess}
BuildRequires:  %{python_module virtualenv >= 20.34}
BuildRequires:  graphviz-gnome
# /SECTION
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

%pre
%python_libalternatives_reset_alternative pipdeptree

%post
%python_install_alternative pipdeptree

%postun
%python_uninstall_alternative pipdeptree

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pipdeptree
%{python_sitelib}/pipdeptree
%{python_sitelib}/pipdeptree-%{version}.dist-info

%changelog
