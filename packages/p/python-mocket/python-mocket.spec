#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%define skip_python2 1
Name:           python-mocket%{psuffix}
Version:        3.10.9
Release:        0
Summary:        Python socket mock framework
License:        BSD-3-Clause
URL:            https://github.com/mindflayer/python-mocket
Source0:        https://files.pythonhosted.org/packages/source/m/mocket/mocket-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator >= 4
Requires:       python-http-parser >= 0.9.0
Requires:       python-python-magic >= 0.4.5
Requires:       python-urllib3 >= 1.25.3
Suggests:       python-pook >= 0.2.1
Suggests:       python-xxhash
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module async_timeout}
BuildRequires:  %{python_module fastapi}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module mocket = %{version}}
BuildRequires:  %{python_module pook >= 0.2.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module xxhash}
BuildRequires:  ca-certificates-mozilla
%endif
%python_subpackages

%description
Socket Mock Framework - for all kinds of socket animals, web-clients
included, with gevent/asyncio/SSL support.

%prep
%setup -q -n mocket-%{version}
sed -i '/cov/ d' setup.cfg
sed -i '/pipenv/ d' setup.py

%build
%if !%{with test}
export LANG=en_US.UTF-8
%python_build
%endif

%install
%if !%{with test}
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
export SKIP_TRUE_HTTP=1
%if 0%{?suse_version} < 1550
# Ignore tests which are not supported on Python 3.6
pytest_python3_ignore="--ignore tests/tests37 --ignore tests/tests38"
%endif
# Requires a running Redis server
donttest="TrueRedisTestCase"
# Checks the ability to record a real request and response. Not available inside obs.
donttest="$donttest or test_asyncio_record_replay"
# The reference recording has different headers in this case
%if %{pkg_vcmp python3-httpx < 0.23}
donttest="$donttest or test_truesendall_with_dump_from_recording"
%endif
%pytest -rfEs -k "not ($donttest)" ${pytest_$python_ignore}
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/mocket
%{python_sitelib}/mocket-%{version}-py*.egg-info
%endif

%changelog
