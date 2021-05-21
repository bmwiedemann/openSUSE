#
# spec file for package python-distributed-test
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define skip_python36 1
%ifnarch %{ix86} %{arm}
%define cythonize --with-cython
# cython optimizations not supported on 32-bit: https://github.com/dask/dask/issues/7489
%endif
Name:           python-distributed%{psuffix}
# Note: please always update together with python-dask
Version:        2021.5.0
Release:        0
Summary:        Library for distributed computing with Python
License:        BSD-3-Clause
URL:            https://distributed.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/source/d/distributed/distributed-%{version}.tar.gz
Source99:       python-distributed-rpmlintrc
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-certifi
Requires:       python-click >= 6.6
Requires:       python-cloudpickle >= 1.5.0
Requires:       python-dask = %{version}
Requires:       python-msgpack
Requires:       python-psutil >= 5.0
Requires:       python-sortedcontainers
Requires:       python-tblib
Requires:       python-toolz >= 0.8.2
Requires:       python-tornado >= 6.0.3
Requires:       python-zict >= 0.1.3
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module bokeh}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module click >= 6.6}
BuildRequires:  %{python_module cloudpickle >= 1.5.0}
BuildRequires:  %{python_module dask-all = %{version}}
# need built extension
BuildRequires:  %{python_module distributed = %{version}}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  %{python_module sparse}
BuildRequires:  %{python_module tblib}
BuildRequires:  %{python_module toolz >= 0.8.2}
BuildRequires:  %{python_module tornado >= 6.0.3}
BuildRequires:  %{python_module zict >= 0.1.3}
%endif
%python_subpackages

%description
Dask.distributed is a library for distributed computing in Python. It
extends both the concurrent.futures and dask APIs to moderate sized
clusters.

%prep
%autosetup -p1 -n distributed-%{version}

%build
%if ! %{with test}
%python_build %{?cythonize}
%endif

%install
%if ! %{with test}
%python_install %{?cythonize}
%python_clone -a %{buildroot}%{_bindir}/dask-ssh
%python_clone -a %{buildroot}%{_bindir}/dask-scheduler
%python_clone -a %{buildroot}%{_bindir}/dask-worker
%{python_expand #
chmod -x %{buildroot}%{$python_sitearch}/distributed/tests/test_utils_test.py
%fdupes %{buildroot}%{$python_sitearch}
}
%endif

%if %{with test}
%check
# many tests from multiple files are broken by new pytest-asyncio
# (see https://github.com/dask/distributed/pull/4212 and https://github.com/pytest-dev/pytest-asyncio/issues/168)
# as a proof build it with old pytest-asyncio and see these tests pass
%if %{pkg_vcmp python3-pytest-asyncio >= 0.14}
donttest+=" or (test_asyncprocess and test_child_main_thread)"
donttest+=" or (test_asyncprocess and test_close)"
donttest+=" or (test_asyncprocess and test_exitcode)"
donttest+=" or (test_asyncprocess and test_num_fds)"
donttest+=" or (test_asyncprocess and test_performance_report)"
donttest+=" or (test_asyncprocess and test_signal)"
donttest+=" or (test_client and test_add_worker_after_task)"
donttest+=" or (test_client and test_bad_tasks_fail)"
donttest+=" or (test_client and test_futures_in_subgraphs)"
donttest+=" or (test_client and test_get_client)"
donttest+=" or (test_client and test_logs)"
donttest+=" or (test_client and test_lose_scattered_data)"
donttest+=" or (test_client and test_performance_report)"
donttest+=" or (test_client and test_quiet_client_close)"
donttest+=" or (test_client and test_repr_async)"
donttest+=" or (test_client and test_secede_balances)"
donttest+=" or (test_client and test_secede_simple)"
donttest+=" or (test_client and test_serialize_collections)"
donttest+=" or (test_client_executor and test_cancellation)"
donttest+=" or (test_client_loop and test_close_loop_sync)"
donttest+=" or (test_collections and test_sparse_arrays)"
donttest+=" or (test_events and test_event_on_workers)"
donttest+=" or (test_events and test_set_not_set_many_events)"
donttest+=" or (test_events and test_two_events_on_workers)"
donttest+=" or (test_failed_workers and test_broken_worker_during_computation)"
donttest+=" or (test_failed_workers and test_gather_then_submit_after_failed_workers)"
donttest+=" or (test_failed_workers and test_restart)"
donttest+=" or (test_failed_workers and test_worker_time_to_live)"
donttest+=" or (test_failed_workers and test_worker_who_has_clears_after_failed_connection)"
donttest+=" or (test_locks and test_lock)"
donttest+=" or (test_locks and test_serializable)"
donttest+=" or (test_nanny and test_mp_pool_worker_no_daemon)"
donttest+=" or (test_nanny and test_mp_process_worker_no_daemon)"
donttest+=" or (test_nanny and test_nanny)"
donttest+=" or (test_nanny and test_num_fds)"
donttest+=" or (test_preload and test_web_preload)"
donttest+=" or (test_profile and test_watch)"
donttest+=" or (test_publish and test_publish_simple)"
donttest+=" or (test_queues and test_2220)"
donttest+=" or (test_resources and test_prefer_constrained)"
donttest+=" or (test_scheduler and test_balance_many_workers)"
donttest+=" or (test_scheduler and test_bandwidth_clear)"
donttest+=" or (test_scheduler and test_dashboard_address)"
donttest+=" or (test_scheduler and test_dont_recompute_if_persisted)"
donttest+=" or (test_scheduler and test_file_descriptors)"
donttest+=" or (test_scheduler and test_gather_allow_worker_reconnect)"
donttest+=" or (test_scheduler and test_idle_timeout)"
donttest+=" or (test_scheduler and test_include_communication_in_occupancy)"
donttest+=" or (test_scheduler and test_log_tasks_during_restart)"
donttest+=" or (test_scheduler and test_restart)"
donttest+=" or (test_scheduler and test_scheduler_init_pulls_blocked_handlers_from_config)"
donttest+=" or (test_scheduler and test_service_hosts)"
donttest+=" or (test_scheduler and test_steal_when_more_tasks)"
donttest+=" or (test_scheduler and test_task_groups)"
donttest+=" or (test_semaphor and test_getvalue)"
donttest+=" or (test_semaphore and test_access_semaphore_by_name)"
donttest+=" or (test_semaphore and test_close_async)"
donttest+=" or (test_semaphore and test_oversubscribing_leases)"
donttest+=" or (test_semaphore and test_release_failure)"
donttest+=" or (test_semaphore and test_release_once_too_many_resilience)"
donttest+=" or (test_semaphore and test_release_semaphore_after_timeout)"
donttest+=" or (test_semaphore and test_release_simple)"
donttest+=" or (test_semaphore and test_threadpoolworkers_pick_correct_ioloop)"
donttest+=" or (test_sparse_arrays and concurrent)"
donttest+=" or (test_spec and test_address_default_none)"
donttest+=" or (test_spec and test_child_address_persists)"
donttest+=" or (test_steal and test_balance)"
donttest+=" or (test_steal and test_dont_steal_already_released)"
donttest+=" or (test_steal and test_dont_steal_few_saturated_tasks_many_workers)"
donttest+=" or (test_steal and test_dont_steal_unknown_functions)"
donttest+=" or (test_steal and test_eventually_steal_unknown_functions)"
donttest+=" or (test_steal and test_restart)"
donttest+=" or (test_steal and test_steal_more_attractive_tasks)"
donttest+=" or (test_steal and test_steal_twice)"
donttest+=" or (test_steal and test_steal_when_more_tasks)"
donttest+=" or (test_steal and test_worksteal_many_thieves)"
donttest+=" or (test_stress and test_cancel_stress)"
donttest+=" or (test_tls_functional and test_retire_workers)"
donttest+=" or (test_tls_functional and test_worker_client)"
donttest+=" or (test_utils and test_sync_closed_loop)"
donttest+=" or (test_worker and test_dont_overlap_communications_to_same_worker)"
donttest+=" or (test_worker and test_gather_many_small)"
donttest+=" or (test_worker and test_get_client)"
donttest+=" or (test_worker and test_lifetime)"
donttest+=" or (test_worker and test_robust_to_bad_sizeof_estimates)"
donttest+=" or (test_worker and test_share_communication)"
donttest+=" or (test_worker and test_statistical_profiling_2)"
donttest+=" or (test_worker and test_stop_doing_unnecessary_work)"
donttest+=" or (test_worker and test_wait_for_outgoing)"
donttest+=" or (test_worker and test_workerstate_executing)"
donttest+=" or (test_worker_client and test_async)"
donttest+=" or (test_worker_client and test_client_executor)"
donttest+=" or (test_worker_client and test_compute_within_worker_client)"
donttest+=" or (test_worker_client and test_gather_multi_machine)"
donttest+=" or (test_worker_client and test_local_client_warning)"
donttest+=" or (test_worker_client and test_scatter_from_worker)"
donttest+=" or (test_worker_client and test_scatter_singleton)"
donttest+=" or (test_worker_client and test_secede_without_stealing_issue_1262)"
donttest+=" or (test_worker_client and test_submit_different_names)"
donttest+=" or (test_worker_client and test_submit_from_worker)"
%endif
# false version mismatch
donttest+=" or test_version_warning_in_cluster"
# ambiguous order in returned message
donttest+=" or (test_client and test_as_completed_async_for_cancel)"
# too many open files
donttest+=" or (test_stress and test_stress_communication)"
# randomly fail even with old asyncio -- too slow for obs (?)
donttest+=" or (test_asyncprocess and test_exit_callback)"
donttest+=" or (test_client and test_cleanup_after_broken_client_connection)"
donttest+=" or (test_client and test_open_close_many_workers)"
donttest+=" or (test_client and test_profile)"
donttest+=" or (test_client and test_quiet_quit_when_cluster_leaves)"
donttest+=" or (test_client and test_reconnect)"
donttest+=" or (test_client and test_sub_submit_priority)"
donttest+=" or (test_client and test_upload_file_exception_sync)"
donttest+=" or (test_client and test_upload_file_sync)"
donttest+=" or (test_diskutils and test_workspace_concurrency)"
donttest+=" or (test_failed_workers and test_fast_kill)"
donttest+=" or (test_metrics and time)"
donttest+=" or (test_queues and test_race)"
donttest+=" or (test_scheduler and test_gather_failing_cnn_recover)"
donttest+=" or (test_steal and test_dont_steal_fast_tasks_compute_time)"
donttest+=" or (test_stress and test_close_connections)"
donttest+=" or (test_worker and test_fail_write_to_disk)"
donttest+=" or test_queue_in_task or test_variable_in_task"
# https://github.com/dask/distributed/pull/4719: "This test is heavily influenced by hard-to-control factors such as memory management"
# probably influenced by OBS scheduling
donttest+=" or (test_scheduler and test_memory)"
# likely related to the above (https://github.com/dask/distributed/pull/4651)
donttest+=" or (test_worker and test_spill_to_disk)"
# flaky on i586
donttest+=" or (test_client_executor and test_map)"
%pytest_arch -rfE -n auto distributed/tests/ -k "not (${donttest:4})" -m "not avoid_travis" --timeout 180
%endif

%if ! %{with test}
%post
%python_install_alternative dask-ssh dask-scheduler dask-worker

%postun
%python_uninstall_alternative dask-ssh

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/dask-ssh
%python_alternative %{_bindir}/dask-scheduler
%python_alternative %{_bindir}/dask-worker
%{python_sitearch}/distributed
%{python_sitearch}/distributed-%{version}*-info
%endif

%changelog
