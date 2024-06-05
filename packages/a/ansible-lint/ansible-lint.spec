#
# spec file for package ansible-lint
#
# Copyright (c) 2022 SUSE LLC
# Copyright 2018 by Lars Vogdt
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

%global lib_name ansiblelint
%{?python_enable_dependency_generator}
Name:           ansible-lint
Version:        24.6.0
Release:        0%{?dist}
Summary:        Best practices checker for Ansible
License:        MIT
URL:            https://github.com/ansible-community/ansible-lint
Source0:        https://github.com/ansible-community/ansible-lint/archive/v%{version}/ansible-lint-%{version}.tar.gz#/ansible-lint-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-rpm-macros
BuildRequires:  %{ansible_python}-base >= 3.10
BuildRequires:  %{ansible_python}-pip
BuildRequires:  %{ansible_python}-wheel
BuildRequires:  fdupes

# SECTION tests
BuildRequires:  %{ansible_python}-flaky >= 3.7.0
BuildRequires:  %{ansible_python}-pytest >= 7.2.2
BuildRequires:  %{ansible_python}-pytest-cov
BuildRequires:  %{ansible_python}-pytest-xdist >= 2.1.0
BuildRequires:  %{ansible_python}-psutil
BuildRequires:  %{ansible_python}-black >= 23.10.1
BuildRequires:  %{ansible_python}-mypy
BuildRequires:  %{ansible_python}-pylint
BuildRequires:  %{ansible_python}-flake8
# /SECTION

# Add runtime requirements (unless required for tests)
# to make sure this only builds if they are present
# https://github.com/ansible/ansible-lint/blob/main/.config/requirements.in
BuildRequires:  ansible-core >= 2.15.5
BuildRequires:  %{ansible_python}-ansible-compat >= 4.1.11
BuildRequires:  %{ansible_python}-black >= 23.10.1
BuildRequires:  %{ansible_python}-enrich >= 1.2.7
BuildRequires:  %{ansible_python}-filelock >= 3.3.0
BuildRequires:  %{ansible_python}-jsonschema >= 4.17.3
BuildRequires:  %{ansible_python}-packaging >= 23.1
BuildRequires:  %{ansible_python}-PyYAML >= 6.0.1
BuildRequires:  %{ansible_python}-requests >= 2.31.0
BuildRequires:  %{ansible_python}-rich >= 13.5.2
BuildRequires:  %{ansible_python}-ruamel.yaml >= 0.18.5
BuildRequires:  %{ansible_python}-subprocess-tee >= 0.4.1
BuildRequires:  %{ansible_python}-tenacity
BuildRequires:  %{ansible_python}-wcmatch >= 8.4.1
BuildRequires:  %{ansible_python}-yamllint >= 1.32.0

#
# https://github.com/ansible/ansible-lint/blob/main/.config/requirements.in
Requires:       ansible-core >= 2.15.5
Requires:       %{ansible_python}-ansible-compat >= 4.1.10
Requires:       %{ansible_python}-black >= 23.10.1
Requires:       %{ansible_python}-bracex >= 2.2.1
Requires:       %{ansible_python}-enrich >= 1.2.7
Requires:       %{ansible_python}-filelock  >= 3.3.0
Requires:       %{ansible_python}-importlib-metadata
Requires:       %{ansible_python}-jsonschema >= 4.17.3
Requires:       %{ansible_python}-packaging >= 23.1
Requires:       %{ansible_python}-PyYAML  >= 6.0.1
Requires:       %{ansible_python}-requests >= 2.31.0
Requires:       %{ansible_python}-rich >= 13.5.2
Requires:       %{ansible_python}-ruamel.yaml >= 0.17.31
Requires:       %{ansible_python}-subprocess-tee >= 0.4.1
Requires:       %{ansible_python}-tenacity
Requires:       %{ansible_python}-wcmatch >= 8.4.1
Requires:       %{ansible_python}-yamllint >= 1.32.0

%description
Checks playbooks for practices and behavior that could potentially be improved.

%prep
%setup -n %{name}-%{version}
sed -i '/^dynamic/ s/"version", //' pyproject.toml
sed -i '/^description/a version = "%{version}"' pyproject.toml
sed -i '1{/\/usr\/bin\/env python/d;}' src/ansiblelint/__main__.py
sed -i '/__version__ =/ s/0.1.dev1/%{version}/' src/ansiblelint/version.py

%build
%{ansible_python_executable} -mpip wheel --no-deps --disable-pip-version-check --use-pep517 --no-build-isolation --progress-bar off --verbose --wheel-dir ./build/ .
mkdir -p ./dist
cp ./build/ansible_lint-*-none-any.whl ./dist/

%install

%{ansible_python_executable} -mpip install --root %{buildroot} --disable-pip-version-check --no-compile --no-deps --progress-bar off --ignore-installed --no-index --verbose --find-links build/ansible_lint-*.whl ansible_lint==%{version}
find %{buildroot}/%{ansible_python_sitelib} -name '*.pyc' -delete
%{ansible_python_executable} -m compileall %{buildroot}/%{ansible_python_sitelib}
%{ansible_python_executable} -O -m compileall %{buildroot}/%{ansible_python_sitelib}
cp -vr src/ansiblelint/schemas %{buildroot}/%{ansible_python_sitelib}/%{lib_name}/
cp -vr src/ansiblelint/data %{buildroot}/%{ansible_python_sitelib}/%{lib_name}/

%fdupes -s %{buildroot}/%{ansible_python_sitelib}

%files
%doc README.md
%license COPYING
%{_bindir}/ansible-lint
%{ansible_python_sitelib}/%{lib_name}/
%{ansible_python_sitelib}/ansible_lint-%{version}.dist-info/

%changelog
