#
# spec file for package python-celery
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
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
Name:           python-celery%{psuffix}
Version:        5.0.5
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
Requires:       python-billiard >= 3.6.3.0
Requires:       python-click >= 7.0
Requires:       python-click-didyoumean >= 0.0.3
Requires:       python-click-plugins >= 1.1.1
Requires:       python-click-repl >= 0.1.6
Requires:       python-kombu >= 5.0.0
Requires:       python-pytz >= 2016.7
Requires:       python-vine >= 5.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-curses
Recommends:     python-cryptography
Suggests:       python-eventlet
Suggests:       python-gevent
Suggests:       python-pymongo
Suggests:       python-python-daemon
Suggests:       python-pytyrant
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module boto3 >= 1.9.178}
BuildRequires:  %{python_module case >= 1.3.1}
BuildRequires:  %{python_module celery = %{version}}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module eventlet >= 0.26.1}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module moto >= 1.3.7}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module pymongo >= 3.3.0}
BuildRequires:  %{python_module pytest >= 4.5.0}
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
%setup -q -n celery-%{version}
%autopatch -p1
# do not hardcode versions
sed -i -e 's:==:>=:g' requirements/*.txt

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
# test_init_mongodb_dns_seedlist - does not work with new pymongo, will be fixed in 5.1
%pytest -k 'not test_init_mongodb_dns_seedlist'
%endif

%if !%{with test}
%post
%python_install_alternative celery

%postun
%python_uninstall_alternative celery

%files %{python_files}
%{python_sitelib}/*
%license LICENSE
%doc README.rst TODO
%python_alternative %{_bindir}/celery
%endif

%changelog
