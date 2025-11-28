#
# spec file for package python-pytest-salt-factories
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-pytest-salt-factories
Version:        1.0.5
Release:        0
Summary:        A pytest plugin for testing Salt
License:        Apache-2.0
URL:            https://pytest-salt-factories.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-salt-factories/pytest_salt_factories-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix_unit_tests.patch  this patch is removing the workaround in the unit test implementation so the test can pass when using our openSUSE Salt 3006.0 package
Patch1:         fix_unit_tests.patch
# PATCH-FIX-UPSTREAM gh#saltstack/pytest-salt-factories#194 & gh#saltstack/pytest-salt-factories#195
Patch2:         support-pytest-9.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6.0.0}
BuildRequires:  %{python_module pytest-shell-utilities}
BuildRequires:  %{python_module pytest-subtests if %python-pytest < 9}
BuildRequires:  %{python_module pytest-system-statistics}
BuildRequires:  %{python_module pyzmq}
BuildRequires:  %{python_module salt}
BuildRequires:  %{python_module setuptools >= 50.3.2}
BuildRequires:  %{python_module setuptools-declarative-requirements}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  salt-master
Requires:       python-PyYAML
Requires:       python-attrs >= 19.2.0
Requires:       python-msgpack
Requires:       python-psutil
Requires:       python-pytest >= 6.0.0
Requires:       python-pytest-helpers-namespace >= 2021.4.29
Requires:       python-pytest-shell-utilities >= 1.4.0
Requires:       python-pytest-skip-markers >= 1.1.3
Requires:       python-pytest-system-statistics >= 1.0.2
Requires:       python-pyzmq
Requires:       python-virtualenv
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
A pytest plugin for testing Salt.

%prep
%autosetup -p1 -n pytest_salt_factories-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/salt-factories
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Run test and exclude some that doesn't work fine in OBS.
donttest="ssh or echoext"
# Flaky tests for aarch64, ppc, arm
donttest+=" or test_all_messages_received"

# All these tests are failing with python >3.11
# tests/integration/factories/cli/test_salt.py::test_merged_json_out
# tests/integration/factories/cli/test_salt.py::test_merged_json_out_disabled
python312_donttest=" or test_merged_json_out or test_merged_json_out_disabled"
# tests/integration/factories/daemons/master/test_master.py::test_salt_cp_minion_id_as_first_argument
python312_donttest+=" or test_salt_cp_minion_id_as_first_argument"
# tests/integration/factories/daemons/master/test_master.py::test_salt_cp_explicit_minion_tgt
python312_donttest+=" or test_salt_cp_explicit_minion_tgt"
# tests/integration/factories/daemons/minion/test_minion.py::test_minion
python312_donttest+=" or test_minion"
# tests/integration/factories/daemons/minion/test_minion.py::test_show_jid
# tests/integration/factories/daemons/proxy/test_proxy_minion.py::test_show_jid
python312_donttest+=" or test_show_jid"
# tests/integration/factories/daemons/proxy/test_proxy_minion.py::test_proxy_minion
python312_donttest+=" or test_proxy_minion"
# tests/integration/utils/saltext/test_log_handlers.py::test_logs_forwarded_from_sub_processes
python312_donttest+=" or test_logs_forwarded_from_sub_processes"
python313_donttest=$python312_donttest

%pytest -k "not ($donttest ${$python_donttest})" ${$python_ignore}

%post
%python_install_alternative salt-factories

%postun
%python_uninstall_alternative salt-factories

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/saltfactories
%{python_sitelib}/pytest_salt_factories-%{version}.dist-info
%python_alternative %{_bindir}/salt-factories

%changelog
