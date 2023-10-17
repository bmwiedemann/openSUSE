#
# spec file for package python-pytest-salt-factories
#
# Copyright (c) 2023 SUSE LLC
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


%define _version 1.0.0
%define _rc_version rc27
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-pytest-salt-factories
Version:        %{_version}~%{_rc_version}
Release:        0
Summary:        A pytest plugin for testing Salt
License:        Apache-2.0
URL:            https://pytest-salt-factories.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-salt-factories/pytest-salt-factories-%{_version}%{_rc_version}.tar.gz
# PATCH-FIX-OPENSUSE fix_unit_tests.patch  this patch is removing the workaround in the unit test implementation so the test can pass when using our openSUSE Salt 3006.0 package
Patch1:         fix_unit_tests.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6.0.0}
BuildRequires:  %{python_module pytest-shell-utilities}
BuildRequires:  %{python_module pytest-subtests}
BuildRequires:  %{python_module pytest-system-statistics}
BuildRequires:  %{python_module setuptools >= 50.3.2}
BuildRequires:  %{python_module setuptools-declarative-requirements}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python3-salt
BuildRequires:  salt-master
BuildRequires:  python-rpm-macros
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
%setup -q -n pytest-salt-factories-%{_version}%{_rc_version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/salt-factories
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=%{buildroot}%{python_sitelib}

# Run test and exclude some that doesn't work fine in OBS.
pytest-%{python_bin_suffix} -vvv -k 'not ssh and not echoext'
 
%post
%python_install_alternative salt-factories

%postun
%python_uninstall_alternative salt-factories

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/saltfactories
%{python_sitelib}/pytest_salt_factories-%{_version}%{_rc_version}*-info
%python_alternative %{_bindir}/salt-factories

%changelog
