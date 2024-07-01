#
# spec file for package python-pipx
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


%{?sle15_python_module_pythons}
Name:           python-pipx
Version:        1.6.0
Release:        0
Summary:        Install and Run Python Applications in Isolated Environments
License:        MIT
URL:            https://github.com/pypa/pipx
Source:         https://files.pythonhosted.org/packages/source/p/pipx/pipx-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs >= 0.4}
BuildRequires:  %{python_module hatchling >= 1.18}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python >= 3.8
Requires:       python-argcomplete >= 1.9.4
Requires:       python-packaging >= 20
Requires:       python-platformdirs >= 2.1
Requires:       python-tomli
Requires:       python-userpath >= 1.6
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module argcomplete >= 1.9.4}
BuildRequires:  %{python_module packaging >= 20}
BuildRequires:  %{python_module platformdirs >= 2.1}
BuildRequires:  %{python_module userpath >= 1.6}
# /SECTION
%python_subpackages

%description
Install and Run Python Applications in Isolated Environments

%prep
%autosetup -p1 -n pipx-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pipx
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pipx

%postun
%python_uninstall_alternative pipx

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/pipx
%{python_sitelib}/pipx
%{python_sitelib}/pipx-%{version}.dist-info

%changelog
