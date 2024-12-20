#
# spec file for package python-nox
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
%global padded_version 2024.04.15
Name:           python-nox
Version:        2024.10.9
Release:        0
Summary:        Flexible test automation
License:        Apache-2.0
URL:            https://nox.thea.codes
Source:         https://github.com/wntrblm/nox/archive/refs/tags/%{padded_version}.tar.gz#/nox-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-broken-mock-test.patch (gh#28bbaa5)
Patch0:         fix-broken-mock-test.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       python-argcomplete >= 1.9.4
Requires:       python-colorlog >= 2.6.1
Requires:       python-virtualenv >= 14.0.0
Requires:       (python-tomli if python-base < 3.11)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-Jinja2
Suggests:       python-tox
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module argcomplete >= 1.9.4}
BuildRequires:  %{python_module colorlog >= 2.6.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tox}
BuildRequires:  %{python_module virtualenv >= 14.0.0}
# Missing deps conda
# /SECTION
%python_subpackages

%description
Flexible test automation.

%prep
%autosetup -p1 -n nox-%{padded_version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/tox-to-nox
%python_clone -a %{buildroot}%{_bindir}/nox
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative tox-to-nox
%python_install_alternative nox

%postun
%python_uninstall_alternative tox-to-nox
%python_uninstall_alternative nox

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/nox
%python_alternative %{_bindir}/tox-to-nox
%{python_sitelib}/nox*

%changelog
