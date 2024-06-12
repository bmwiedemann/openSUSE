#
# spec file for package python-mocket
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-mocket%{psuffix}
Version:        3.12.8
Release:        0
Summary:        Python socket mock framework
License:        BSD-3-Clause
URL:            https://github.com/mindflayer/python-mocket
Source0:        https://files.pythonhosted.org/packages/source/m/mocket/mocket-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator >= 4
Requires:       python-httptools
Requires:       python-python-magic >= 0.4.5
Requires:       python-urllib3 >= 1.25.3
Suggests:       python-pook >= 0.2.1
Suggests:       python-xxhash
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module asgiref}
BuildRequires:  %{python_module fastapi}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module httptools}
BuildRequires:  %{python_module mocket = %{version}}
BuildRequires:  %{python_module pook >= 0.2.1}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module xxhash}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  redis
%endif
%python_subpackages

%description
Socket Mock Framework - for all kinds of socket animals, web-clients
included, with gevent/asyncio/SSL support.

%prep
%autosetup -p1 -n mocket-%{version}
#sed -i '/cov/ d' setup.cfg
#sed -i '/pipenv/ d' setup.py

%build
%if !%{with test}
export LANG=en_US.UTF-8
%pyproject_wheel
%endif

%install
%if !%{with test}
export LANG=en_US.UTF-8
%pyproject_install
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

%{_sbindir}/redis-server --version | grep ' v=7\.' && redis7args="--enable-debug-command yes --enable-module-command yes"
%{_sbindir}/redis-server --port 6379 --save "" $redis7args &
victims="$!"
trap "kill $victims || true" EXIT
sleep 2

# Checks the ability to record a real request and response. Not available inside obs.
donttest="test_asyncio_record_replay or test_truesendall_with_dump_from_recording or test_no_dangling_fds"
# The reference recording has different headers in this case
%if %{pkg_vcmp python311-httpx < 0.23}
donttest="$donttest or test_truesendall_with_dump_from_recording"
%endif
# these fail after the python 3.11 patches
#donttest="$donttest or test_http_session or test_https_session or test_httprettish_session"
%pytest -rfEs -k "not ($donttest)" ${pytest_$python_ignore}
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/mocket
%{python_sitelib}/mocket-%{version}.dist-info
%endif

%changelog
