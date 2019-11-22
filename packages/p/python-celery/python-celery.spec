#
# spec file for package python-celery
#
# Copyright (c) 2019 SUSE LLC.
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
Version:        4.3.0
Release:        0
Summary:        Distributed Task Queue module for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://celeryproject.org
Source:         https://files.pythonhosted.org/packages/source/c/celery/celery-%{version}.tar.gz
Patch0:         pytest5.patch
Patch2:         unpin-pytest.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  netcfg
BuildRequires:  python-rpm-macros
Requires:       python-billiard >= 3.6.0
Requires:       python-kombu >= 4.4.0
Requires:       python-python-dateutil
Requires:       python-pytz >= 2016.7
Requires:       python-vine >= 1.3.0
Recommends:     python-curses
Recommends:     python-pyOpenSSL
Suggests:       python-eventlet
Suggests:       python-gevent
Suggests:       python-pymongo
Suggests:       python-python-daemon
Suggests:       python-pytyrant
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module billiard >= 3.6.0}
BuildRequires:  %{python_module boto3 >= 1.9.125}
BuildRequires:  %{python_module case >= 1.3.1}
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module kombu >= 4.4.0}
BuildRequires:  %{python_module moto >= 1.3.7}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest >= 4.3.1}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz >= 2016.7}
BuildRequires:  %{python_module vine >= 1.3.0}
%if %{with ringdisabled}
ExclusiveArch:  do-not-build
%endif
%endif
%ifpython3
Requires:       python3-dbm
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
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/*
%license LICENSE
%doc Changelog README.rst TODO
%python3_only %{_bindir}/celery*
%endif

%changelog
