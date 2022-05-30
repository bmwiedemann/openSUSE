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
Version:        5.4.0
Release:        1%{?dist}
Summary:        Best practices checker for Ansible
License:        MIT
URL:            https://github.com/ansible-community/ansible-lint
Source0:        https://github.com/ansible-community/ansible-lint/archive/v%{version}/ansible-lint-%{version}.tar.gz
Patch0:         https://github.com/ansible/ansible-lint/commit/aa6c1c6577f8178643591ddc06996a5d5588cb9a.patch#/deprecated-pytest-hook.patch
BuildArch:      noarch
BuildRequires:  python-rpm-macros
BuildRequires:  python3-PyYAML
BuildRequires:  python3-pip
BuildRequires:  python3-six
BuildRequires:  python3-wheel
# SECTION tests
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-flaky
BuildRequires:  python3-packaging
BuildRequires:  python3-tenacity
BuildRequires:  python3-yamllint
#BuildRequires:     git
BuildRequires:  python3-enrich >= 1.2.6
BuildRequires:  ansible
BuildRequires:  python3-rich >= 9.5.1
BuildRequires:  python3-ruamel.yaml >= 0.15.37
BuildRequires:  python3-wcmatch >= 7.0
# /SECTION
BuildRequires:  fdupes
Requires:       ansible
Requires:       python3-PyYAML
Requires:       python3-enrich >= 1.2.6
Requires:       python3-packaging
Requires:       python3-rich >= 9.5.1
Requires:       python3-ruamel.yaml >= 0.15.37
Requires:       python3-six
Requires:       python3-tenacity
Requires:       python3-wcmatch >= 7.0

%description
Checks playbooks for practices and behavior that could potentially be improved.

%prep
%setup -n ansible-lint-%{version}
%patch0 -p1
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

%check
# exclude some tests depending on internet access (galaxy modules)
# exclude test_cli_auto_detect which depends on a local git repository
# exclude test_co and test_call_from_outside_venv because of https://github.com/ansible-community/ansible-lint/issues/1885 FIXED!
PYTHONPATH=${PYTHONPATH:+$PYTHONPATH:}%{buildroot}/%{python3_sitelib} PATH=${PATH:+$PATH:}%{buildroot}/%{_bindir} PYTHONDONTWRITEBYTECODE=1 pytest -v -k 'not (test_prerun_reqs_v1 or test_prerun_reqs_v2 or test_install_collection or test_require_collection_wrong_version or test_cli_auto_detect or test_eco or test_call_from_outside_venv)'

%files
%doc README.rst
%license LICENSE
%{_bindir}/ansible-lint
%{python3_sitelib}/%{lib_name}/
%{python3_sitelib}/ansible_lint-%{version}.dist-info/

%changelog
