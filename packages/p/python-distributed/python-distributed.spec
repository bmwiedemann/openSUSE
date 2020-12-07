#
# spec file for package python-distributed
#
# Copyright (c) 2020 SUSE LLC
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
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without     test
Name:           python-distributed
Version:        2.30.1
Release:        0
Summary:        Library for distributed computing with Python
License:        BSD-3-Clause
URL:            https://distributed.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/source/d/distributed/distributed-%{version}.tar.gz
Source99:       python-distributed-rpmlintrc
BuildRequires:  %{python_module joblib >= 0.10.2}
BuildRequires:  %{python_module scikit-learn >= 0.17.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-certifi
Requires:       python-click >= 6.6
Requires:       python-cloudpickle >= 1.5.0
Requires:       python-dask >= 2.9.0
Requires:       python-joblib >= 0.10.2
Requires:       python-msgpack
Requires:       python-psutil >= 5.0
Requires:       python-scikit-learn >= 0.17.1
Requires:       python-sortedcontainers
Requires:       python-tblib
Requires:       python-toolz >= 0.8.2
%if %{python_version_nodots} >= 38
Requires:       python-tornado >= 6.0.3
%else
Requires:       python-contextvars
Requires:       python-tornado >= 5
%endif
Requires:       python-zict >= 0.1.3
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module click >= 6.6}
BuildRequires:  %{python_module cloudpickle >= 1.5.0}
BuildRequires:  %{python_module dask >= 2.9.0}
BuildRequires:  %{python_module dask-bag >= 2.9.0}
BuildRequires:  %{python_module dask-distributed >= 2.9.0}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  %{python_module tblib}
BuildRequires:  %{python_module toolz >= 0.8.2}
%if %{python_version_nodots} >= 38
BuildRequires:  %{python_module tornado >= 6.0.3}
%else
BuildRequires:  %{python_module tornado >= 5}
%endif
BuildRequires:  %{python_module zict >= 0.1.3}
%endif
%python_subpackages

%description
Dask.distributed is a library for distributed computing in Python. It
extends both the concurrent.futures and dask APIs to moderate sized
clusters.

%prep
%setup -q -n distributed-%{version}

%build
%python_build

%install
%python_install
%{python_expand rm -rf %{buildroot}%{$python_sitelib}/distributed/tests/
# Deduplicating files can generate a RPMLINT warning for pyc mtime
%fdupes %{buildroot}%{$python_sitelib}
}

%if %{with test}
%check
# test_reconnect from test_client.py and all tests in test_core.py need network connection
rm distributed/tests/test_core.py
# many tests from multiple files are broken by new pytest-asyncio (see https://github.com/dask/distributed/pull/4212 for explanation)
# as a proof build it with old pytest-asyncio and see these tests pass
ASYNCIO_FAIL="test_worker_nthreads or test_identity or test_worker_port_range or test_worker_waits_for_scheduler or test_io_loop\
 or test_deque_handler or test_bad_ or test_update_latency or test_heartbeat_comm_closed or test_get_client or test_lifetime\
 or test_dashboard_link_ or test_shutdown or test_config or test_client_gather_semaphore_loop or test_secede_\
 or test_event_on_workers or test_two_events_on_workers or test_lock or test_serializable or test_nanny_closes_cleanly or test_nanny_port_range\
 or test_nanny_closed_by_keyboard_interrupt or test_worker_start_exception or test_2220 or test_config_stealing or test_async_context_manager\
 or test_allowed_failures_config or test_no_danglng_asyncio_tasks or test_multiple_listeners or test_oversubscribing_leases\
 or test_security_dict_input or test_worker_client or test_tls_scheduler or test_release_once_too_many_resilience or test_close_async\
 or test_access_semaphore_by_name or test_release_simple or test_worker_breaks_and_returns or test_num_fds or test_retire_names_str or test_gather_allow_worker_reconnect"
# test_worker_client.py and test_preload.py are also heavily affected by new asyncio, more than half of all tests there are broken
rm distributed/tests/test_worker_client.py distributed/tests/test_preload.py
# test_fail_write_to_disk randomly fails
export PYTHONPATH=.
%pytest distributed/tests/ -k "not (test_reconnect or $ASYNCIO_FAIL or test_fail_write_to_disk)"
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/dask-ssh
%{_bindir}/dask-scheduler
%{_bindir}/dask-worker
%{python_sitelib}/distributed*

%changelog
