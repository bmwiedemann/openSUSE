#
# spec file for package ansible-lint
#
# Copyright (c) 2026 SUSE LLC and contributors
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

# SLE 16 ships black 25.1, cryptography 44 and filelock 3.18: ansible-lint does
# not import cryptography, upstream raised the cryptography and filelock floors
# for CVE fixes, which SUSE backports, and the jinja rule works with black 25.1
# upstream minimums from pyproject.toml; prep section fails on SLE 16 if they change
%define black_upstream 25.2.0
%define cryptography_upstream 46.0.7
%define filelock_upstream 3.20.3
%if 0%{?suse_version} >= 1600 && 0%{?suse_version} < 1699
%define black_min 25.1.0
%define cryptography_min 44.0.0
%define filelock_min 3.18.0
%else
%define black_min %{black_upstream}
%define cryptography_min %{cryptography_upstream}
%define filelock_min %{filelock_upstream}
%endif

%global lib_name ansiblelint
Name:           ansible-lint
Version:        26.11.0
Release:        0%{?dist}
Summary:        Best practices checker for Ansible
License:        MIT
URL:            https://github.com/ansible/ansible-lint
Source0:        https://github.com/ansible/ansible-lint/archive/v%{version}/ansible-lint-%{version}.tar.gz#/ansible-lint-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-rpm-macros
BuildRequires:  %{ansible_python}-base >= 3.12
BuildRequires:  %{ansible_python}-pip
BuildRequires:  %{ansible_python}-setuptools >= 65.3.0
BuildRequires:  %{ansible_python}-setuptools_scm >= 7.0.5
BuildRequires:  %{ansible_python}-wheel
BuildRequires:  fdupes

# SECTION tests
BuildRequires:  %{ansible_python}-flaky >= 3.7.0
# upstream already requires 9.0.0, which we do not have yet
BuildRequires:  %{ansible_python}-pytest >= 7.2.2
BuildRequires:  %{ansible_python}-pytest-cov
BuildRequires:  %{ansible_python}-pytest-xdist >= 2.1.0
BuildRequires:  %{ansible_python}-psutil
BuildRequires:  %{ansible_python}-black >= 23.10.1
BuildRequires:  %{ansible_python}-mypy
BuildRequires:  %{ansible_python}-flake8
# /SECTION

# Add runtime requirements (unless required for tests)
# to make sure this only builds if they are present
# https://github.com/ansible/ansible-lint/blob/main/pyproject.toml#L35
BuildRequires:  ansible-core >= 2.18
BuildRequires:  %{ansible_python}-ansible-compat >= 26.3.0
BuildRequires:  %{ansible_python}-black >= %{black_min}
# indirect dependency of ruamel-yaml
BuildRequires:  %{ansible_python}-cffi >= 1.15.1
BuildRequires:  %{ansible_python}-cryptography >= %{cryptography_min}
BuildRequires:  %{ansible_python}-filelock >= %{filelock_min}
BuildRequires:  %{ansible_python}-importlib_metadata >= 8.7.0
BuildRequires:  %{ansible_python}-jsonschema >= 4.10.0
BuildRequires:  %{ansible_python}-packaging >= 22.0
BuildRequires:  (%{ansible_python}-pathspec >= 1.0.3 with %{ansible_python}-pathspec < 1.2.0)
BuildRequires:  %{ansible_python}-PyYAML >= 6.0.1
BuildRequires:  %{ansible_python}-referencing >= 0.36.2
BuildRequires:  %{ansible_python}-ruamel.yaml >= 0.18.11
BuildRequires:  %{ansible_python}-ruamel.yaml.clib >= 0.2.12
BuildRequires:  %{ansible_python}-subprocess-tee >= 0.4.1
BuildRequires:  %{ansible_python}-wcmatch >= 8.5.0
BuildRequires:  %{ansible_python}-yamllint >= 1.38.0

#
# https://github.com/ansible/ansible-lint/blob/main/.config/requirements.in
Requires:       ansible-core >= 2.18
Requires:       %{ansible_python}-ansible-compat >= 25.8.2
Requires:       %{ansible_python}-black >= %{black_min}
# indirect dependency of ruamel-yaml
Requires:       %{ansible_python}-cffi >= 1.15.1
Requires:       %{ansible_python}-cryptography >= %{cryptography_min}
Requires:       %{ansible_python}-filelock >= %{filelock_min}
Requires:       %{ansible_python}-importlib_metadata >= 8.7.0
Requires:       %{ansible_python}-jsonschema >= 4.10.0
Requires:       %{ansible_python}-packaging >= 22.0
Requires:       (%{ansible_python}-pathspec >= 1.0.3 with %{ansible_python}-pathspec < 1.2.0)
Requires:       %{ansible_python}-PyYAML >= 6.0.1
Requires:       %{ansible_python}-referencing >= 0.36.2
Requires:       %{ansible_python}-ruamel.yaml >= 0.18.11
Requires:       %{ansible_python}-ruamel.yaml.clib >= 0.2.12
Requires:       %{ansible_python}-subprocess-tee >= 0.4.1
Requires:       %{ansible_python}-wcmatch >= 8.5.0
Requires:       %{ansible_python}-yamllint >= 1.38.0

%description
Checks playbooks for practices and behavior that could potentially be improved.

%prep
%setup -n %{name}-%{version}
sed -i '1{/\/usr\/bin\/env python/d;}' src/ansiblelint/__main__.py

sed -i 's/0.1.dev1/%{version}/' src/ansiblelint/version.py
%if 0%{?suse_version} >= 1600 && 0%{?suse_version} < 1699
# lower the runtime minimums in the installed metadata too, so pip check passes
deps=$(sed -n '/^dependencies = \[/,/^\]/p' pyproject.toml)
for req in "black>=%{black_upstream}" "cryptography>=%{cryptography_upstream}"; do
  echo "$deps" | grep -qF "\"$req\"" || {
    echo "pyproject.toml no longer requires $req: review the SLE 16 minimums" >&2
    exit 1
  }
done
echo "$deps" | grep -qF "\"filelock>=%{filelock_upstream} ;" || {
  echo "pyproject.toml no longer requires filelock>=%{filelock_upstream}: review the SLE 16 minimums" >&2
  exit 1
}
sed -i '/^dependencies = \[/,/^\]/{
  s/"black>=%{black_upstream}"/"black>=%{black_min}"/
  s/"cryptography>=%{cryptography_upstream}"/"cryptography>=%{cryptography_min}"/
  s/"filelock>=%{filelock_upstream} ;/"filelock>=%{filelock_min} ;/
}' pyproject.toml
%endif

%build
# The GitHub archive tarball carries no git metadata: without setuptools_scm and a
# pretend version the wheel is built as 0.0.0 and ansible-lint --version reports 0.0.0
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
cp -vr src/ansiblelint/schemas %{buildroot}/%{ansible_python_sitelib}/%{lib_name}/
cp -vr src/ansiblelint/data %{buildroot}/%{ansible_python_sitelib}/%{lib_name}/

%fdupes -s %{buildroot}/%{ansible_python_sitelib}

%files
%doc README.md
%license COPYING
%{_bindir}/ansible-lint
%{ansible_python_sitelib}/%{lib_name}/
%{ansible_python_sitelib}/ansible_lint-*.dist-info/

%changelog
