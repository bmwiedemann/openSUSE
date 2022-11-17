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


%global lib_name ansiblelint
%{?python_enable_dependency_generator}
Name:           ansible-lint
Version:        6.8.6
Release:        0%{?dist}
Summary:        Best practices checker for Ansible
License:        MIT
URL:            https://github.com/ansible-community/ansible-lint
Source0:        https://github.com/ansible-community/ansible-lint/archive/v%{version}/ansible-lint-%{version}.tar.gz#/ansible-lint-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  fdupes

# https://github.com/ansible/ansible-lint/blob/main/setup.cfg#L98
# SECTION tests
BuildRequires:  python3-flaky >= 3.7.0
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-xdist >= 2.1.0
BuildRequires:  python3-psutil
BuildRequires:  python3-black >= 22.1.0
BuildRequires:  python3-mypy
BuildRequires:  python3-pylint
BuildRequires:  python3-flake8
# /SECTION

# Add runtime requirements (unless required for tests)
# to make sure this only builds if they are present
BuildRequires:  ansible-core >= 2.12
BuildRequires:  python3-ansible-compat >= 2.2.1
BuildRequires:  python3-enrich >= 1.2.6
BuildRequires:  python3-jsonschema >= 4.9.0
BuildRequires:  python3-packaging
BuildRequires:  python3-PyYAML
BuildRequires:  python3-rich >= 9.5.1
BuildRequires:  python3-ruamel.yaml >= 0.15.37
BuildRequires:  python3-six
BuildRequires:  python3-tenacity
BuildRequires:  python3-wcmatch >= 7.0
BuildRequires:  python3-yamllint >= 1.25.0

# https://github.com/ansible/ansible-lint/blob/main/setup.cfg#L69
Requires:       ansible-core >= 2.12
Requires:       python3-ansible-compat >= 2.2.1
Requires:       python3-black >= 22.1.0
Requires:       python3-enrich >= 1.2.6
Requires:       python3-jsonschema >= 4.9.0
Requires:       python3-packaging
Requires:       python3-PyYAML
Requires:       python3-rich >= 9.5.1
Requires:       python3-ruamel.yaml >= 0.15.37
Requires:       python3-six
Requires:       python3-tenacity
Requires:       python3-wcmatch >= 7.0
Requires:       python3-yamllint >= 1.25.0

%description
Checks playbooks for practices and behavior that could potentially be improved.

%prep
%setup -n %{name}-%{version}
sed -ri 's/(\[metadata\])/\1\nversion = %{version}/' setup.cfg
sed -i '1{/\/usr\/bin\/env python/d;}' src/ansiblelint/__main__.py

%build
python3 -mpip wheel --no-deps --disable-pip-version-check --use-pep517 --no-build-isolation --progress-bar off --verbose . -w build/

%install
python3 -mpip install --root %{buildroot} --disable-pip-version-check --no-compile --no-deps --progress-bar off build/ansible_lint-*.whl
find %{buildroot}/%{python3_sitelib} -name '*.pyc' -delete
python3 -m compileall %{buildroot}/%{python3_sitelib}
python3 -O -m compileall %{buildroot}/%{python3_sitelib}

%fdupes -s %{buildroot}/%{python3_sitelib}

%files
%doc README.md
%license COPYING
%{_bindir}/ansible-lint
%{python3_sitelib}/%{lib_name}/
%{python3_sitelib}/ansible_lint-%{version}.dist-info/

%changelog
