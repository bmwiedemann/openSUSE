#
# spec file for package docsible
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%if 0%{?suse_version} < 1550
# Leap15, SLES15
%if %pythons == "python310"
%define ansible_python python310
%define ansible_python_executable python3.10
%define ansible_python_sitelib %python310_sitelib
%endif
%if %pythons == "python311"
%define ansible_python python311
%define ansible_python_executable python3.11
%define ansible_python_sitelib %python311_sitelib
%endif
%else
# Tumbleweed
%define pythons python3
%define ansible_python python3
%define ansible_python_executable python3
%define ansible_python_sitelib %python3_sitelib
%endif

Name:           docsible
Version:        0.8.0
Release:        0
Summary:        Auto documentation for Ansible roles and collections
License:        MIT
URL:            https://github.com/docsible/docsible
# PyPI tarball does not contain tests directory...
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{ansible_python}-Jinja2 >= 3.1.2
BuildRequires:  %{ansible_python}-PyYAML >= 6.0.1
BuildRequires:  %{ansible_python}-click >= 8.1.7
BuildRequires:  %{ansible_python}-pip
BuildRequires:  %{ansible_python}-poetry-core
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{ansible_python}-pytest
# /SECTION
BuildRequires:  fdupes
Requires:       %{ansible_python}-Jinja2 >= 3.1.2
Requires:       %{ansible_python}-PyYAML >= 6.0.1
Requires:       %{ansible_python}-click >= 8.1.7
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%description
Docsible is a command-line interface (CLI) written in Python that automates the
documentation of Ansible roles and collections. It generates a
Markdown-formatted README file for role or collection by scanning the Ansible
YAML files.

%prep
%autosetup -p1 -n docsible-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/docsible
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/git_detect_url.py

%post
%python_install_alternative docsible

%postun
%python_uninstall_alternative docsible

%files
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/docsible
%{python_sitelib}/docsible
%{python_sitelib}/docsible-%{version}.dist-info
%pycache_only %{python_sitelib}/docsible/__pycache__/

%changelog
