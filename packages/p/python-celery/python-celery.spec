#
# spec file for package python-celery
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


%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_with ringdisabled
%{?sle15_python_module_pythons}
Name:           python-celery%{psuffix}
Version:        5.4.0
Release:        0
Summary:        Distributed Task Queue module for Python
License:        BSD-3-Clause
URL:            http://celeryproject.org
Source:         https://files.pythonhosted.org/packages/source/c/celery/celery-%{version}.tar.gz
Patch0:         move-pytest-configuration-to-conftest.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  netcfg
BuildRequires:  python-rpm-macros
Requires:       python-billiard >= 4.1.0
Requires:       python-click >= 8.0.3
Requires:       python-click-didyoumean >= 0.0.3
Requires:       python-click-plugins >= 1.1.1
Requires:       python-click-repl >= 0.2.0
Requires:       python-kombu >= 5.3
Requires:       python-python-dateutil
Requires:       python-tzdata
Requires:       python-vine >= 5.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-cryptography
Recommends:     python-curses
Suggests:       python-eventlet
Suggests:       python-gevent
Suggests:       python-pymongo
Suggests:       python-python-daemon
Suggests:       python-pytyrant
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module boto3 >= 1.9.178}
BuildRequires:  %{python_module case >= 1.3.1}
BuildRequires:  %{python_module celery = %{version}}
BuildRequires:  %{python_module cryptography >= 36.0.2}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module eventlet >= 0.32.0}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module google-cloud-storage}
BuildRequires:  %{python_module moto >= 2.2.6}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module pymongo >= 4.0.2}
BuildRequires:  %{python_module pytest >= 4.5.0}
BuildRequires:  %{python_module pytest-click}
BuildRequires:  %{python_module pytest-subtests}
%if %{with ringdisabled}
ExclusiveArch:  do-not-build
%endif
%endif
%python_subpackages

%description
Celery is an asynchronous task queue/job queue based on distributed
message passing. It is focused on real-time operation, but supports
scheduling as well.

%prep
%autosetup -p1 -n celery-%{version}

%build
%if !%{with test}
%python_build
%endif

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/celery
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# test_check_privileges_no_fchown - first it deletes fchown from the system, so it needs root privileges, and then it runs the worker and complains about root privileges
# test_init_mongodb_dnspython2_pymongo4_seedlist - pymongo.errors.ConfigurationError: cannot open /etc/resolv.conf

# Temporary, remove
# test_aaa_eventlet_patch::test_aaa_blockdetecet - AssertionError: expected call not found.
# test_AsynPool::test_gen_not_started

%pytest -k "not test_check_privileges_no_fchown and not test_aaa_blockdetecet and not test_gen_not_started and not test_init_mongodb_dnspython2_pymongo4_seedlist"

%endif

%if !%{with test}
%post
%python_install_alternative celery

%postun
%python_uninstall_alternative celery

%files %{python_files}
%{python_sitelib}/celery
%{python_sitelib}/celery-%{version}*-info
%license LICENSE
%doc README.rst TODO
%python_alternative %{_bindir}/celery
%endif

%changelog
