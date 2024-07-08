#
# spec file for package python-distributed
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


%define psuffix %{nil}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test-py310"
%define psuffix -test-py310
%define skip_python311 1
%define skip_python312 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py311"
%define psuffix -test-py311
%define skip_python310 1
%define skip_python312 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py312"
%define psuffix -test-py312
%define skip_python310 1
%define skip_python311 1
%bcond_without test
%endif
%if "%{flavor}" == ""
%bcond_with test
%else
# globally stop testing this one
%define skip_python39 1
%endif
# use this to run tests with xdist in parallel, unfortunately fails server side
%bcond_with paralleltests

Name:           python-distributed%{psuffix}
# ===> Note: python-dask MUST be updated in sync with python-distributed! <===
Version:        2024.6.2
Release:        0
Summary:        Library for distributed computing with Python
License:        BSD-3-Clause
URL:            https://distributed.dask.org
# SourceRepository: https://github.com/dask/distributed
Source:         https://github.com/dask/distributed/archive/refs/tags/%{version}.tar.gz#/distributed-%{version}-gh.tar.gz
Source99:       python-distributed-rpmlintrc
# PATCH-FIX-OPENSUSE distributed-ignore-off.patch -- ignore that we can't probe addresses on obs, code@bnavigator.de
Patch3:         distributed-ignore-offline.patch
# PATCH-FIX-OPENSUSE distributed-ignore-thread-leaks.patch -- ignore leaking threads on obs, code@bnavigator.de
Patch4:         distributed-ignore-thread-leaks.patch
# PATCH-FIX-OPENSUSE distributed-ignore-rerun.patch -- extend ignore pytest array, mimi.vx@gmail.com
Patch5:         distributed-ignore-rerun.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module versioneer-toml >= 0.29}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.10.3
Requires:       python-PyYAML >= 5.3.1
Requires:       python-click >= 8.0
Requires:       python-cloudpickle >= 1.5.0
Requires:       python-dask = %{version}
Requires:       python-locket >= 1.0.0
Requires:       python-msgpack >= 1.0.0
Requires:       python-packaging >= 20.0
Requires:       python-psutil >= 5.7.0
Requires:       python-sortedcontainers >= 2.0.5
Requires:       python-tblib >= 1.6.0
Requires:       python-toolz >= 0.10.0
Requires:       python-tornado >= 6.0.4
Requires:       python-urllib3 >= 1.24.3
Requires:       python-zict >= 2.2.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module bokeh >= 3.1}
BuildRequires:  %{python_module dask-complete = %{version}}
BuildRequires:  %{python_module distributed = %{version}}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sparse}
BuildRequires:  %{python_module zict >= 3}
%if %{with paralleltests}
BuildRequires:  %{python_module pytest-xdist}
%endif
%endif
%python_subpackages

%description
Dask.distributed is a library for distributed computing in Python. It
extends both the concurrent.futures and dask APIs to moderate sized
clusters.

%prep
%autosetup -p1 -n distributed-%{version}

sed -e '/--durations=20/d' \
    -e '/--color=yes/d'  \
    -e '/--cov/d'  \
    -e 's/timeout_method = thread/timeout_method = signal/' \
    -i pyproject.toml

%build
%if ! %{with test}
%pyproject_wheel
%endif

%install
%if ! %{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/dask-ssh
%python_clone -a %{buildroot}%{_bindir}/dask-scheduler
%python_clone -a %{buildroot}%{_bindir}/dask-worker
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# test local src dir, not installed path: looks for test certificates and not installed test modules
export PYTHONPATH=":x"
# disable profiling completely -- https://github.com/dask/distributed/pull/6490
sed '/enable profiling/ {s/enabled: True/enabled: False/}' -i distributed/distributed.yaml
# make sure the change was successful, this is only for the tests, we didn't patch any installed source
grep 'enabled: False .*enable profiling' distributed/distributed.yaml

# we obviously don't test a git repo
donttest="test_git_revision"
# logger error
donttest+=" or test_version_warning_in_cluster"
# invalid task state
donttest+=" or test_fail_to_pickle_execute_2"
# too slow for obs
donttest+=" or test_nanny_timeout"

# Some tests randomly fail server-side -- too slow for obs (?)
# see also https://github.com/dask/distributed/issues/5818
donttest+=" or (test_asyncprocess and (test_exit_callback or test_simple))"
donttest+=" or (test_client and test_repr)"
donttest+=" or (test_client and test_profile_server)"
donttest+=" or (test_client and test_forget_errors)"
donttest+=" or (test_dask_collections and test_sparse_arrays)"
donttest+=" or (test_metrics and test_wall_clock)"
donttest+=" or (test_nanny and test_failure_during_worker_initialization)"
donttest+=" or (test_priorities and test_compute)"
donttest+=" or (test_resources and test_prefer_constrained)"
donttest+=" or (test_scheduler and test_tell_workers_when_peers_have_left)"
donttest+=" or (test_steal and test_steal_twice)"
donttest+=" or (test_utils and test_popen_timeout)"
donttest+=" or (test_variable and test_variable_in_task)"
donttest+=" or (test_worker and test_gather_dep_from_remote_workers_if_all_local_workers_are_busy)"
donttest+=" or (test_worker and test_worker_reconnects_mid_compute)"
donttest+=" or (test_worker_memory and test_digests)"
donttest+=" or (test_worker_memory and test_pause_while_spilling)"
donttest+=" or test_computations_futures"
donttest+=" or test_task_state_instance_are_garbage_collected"
donttest+=" or test_computation_object_code_client_submit_list_comp"
donttest+=" or test_computation_object_code_client_submit_dict_comp"
# server-side fail due to the non-network warning in a subprocess where the patched filter does not apply
donttest+=" or (test_client and test_quiet_close_process)"
# should return > 3, returns 3 exactly
donttest+=" or (test_statistical_profiling_cycle)"
# pytest7 on py312: returns len==2 instead of 1
donttest+=" or test_computation_object_code_dask_compute"
# flakey on 3.10
donttest+=" or (test_client_worker)"
if [[ $(getconf LONG_BIT) -eq 32 ]]; then
  # OverflowError -- https://github.com/dask/distributed/issues/5252
  donttest+=" or test_ensure_spilled_immediately"
  donttest+=" or test_value_raises_during_spilling"
  donttest+=" or test_fail_to_pickle_execute_1"
  # https://github.com/dask/distributed/issues/7175
  donttest+=" or (test_sizeof_error and larger)"
  #
  donttest+=" or test_task_groups"
fi

%if %{with paralleltests}
# not fully supported parallel test suite: https://github.com/dask/distributed/issues/5186
# works locally, but fails with too many tests server-side
notparallel="rebalance or memory or upload"
notparallel+=" or test_open_close_many_workers"
notparallel+=" or test_recreate_error_array"
notparallel+=" or (test_preload and test_web_preload)"
#  Recursion error, https://github.com/dask/distributed/issues/6406
notparallel+=" or test_stack_overflow"
#
notparallel+=" or test_dashboard_host"
notparallel+=" or test_close_properly"
notparallel+=" or test_plugin_internal_exception"
notparallel+=" or test_runspec_regression_sync"
notparallel+=" or test_client_async_before_loop_starts"
# added in 2023.5.1
notparallel+=" or test_ensure_no_new_clients"

%pytest distributed/tests -m "not avoid_ci" -n auto -k "not ($notparallel or $donttest ${$python_donttest})"
%pytest distributed/tests -m "not avoid_ci" -k "($notparallel) and not ($donttest ${$python_donttest})"
%else
%pytest distributed/tests -m "not avoid_ci" -k "not ($donttest ${$python_donttest})"
%endif
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
%{python_sitelib}/distributed
%{python_sitelib}/distributed-%{version}.dist-info

%endif

%changelog
