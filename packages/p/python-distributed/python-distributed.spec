#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
%if "%{flavor}" == "test-py38"
%define psuffix -test-py38
%define skip_python39 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py39"
%define psuffix -test-py39
%define skip_python38 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py310"
%define psuffix -test-py310
%define skip_python38 1
%define skip_python39 1
%bcond_without test
%endif
%if "%{flavor}" == ""
%bcond_with test
%endif
# use this to run tests with xdist in parallel, unfortunately fails server side
%bcond_with paralleltests

Name:           python-distributed%{psuffix}
# ===> Note: python-dask MUST be updated in sync with python-distributed! <===
Version:        2022.11.1
Release:        0
Summary:        Library for distributed computing with Python
License:        BSD-3-Clause
URL:            https://distributed.dask.org
Source:         https://github.com/dask/distributed/archive/refs/tags/%{version}.tar.gz#/distributed-%{version}-gh.tar.gz
Source99:       python-distributed-rpmlintrc
# PATCH-FIX-UPSTREAM distributed-pr7286-tornado-6-2.patch gh#dask/distributed#7286
Patch2:         distributed-pr7286-tornado-6-2.patch
# PATCH-FIX-OPENSUSE distributed-ignore-off.patch -- ignore that we can't probe addresses on obs, code@bnavigator.de
Patch3:         distributed-ignore-offline.patch
# PATCH-FIX-OPENSUSE distributed-ignore-thread-leaks.patch -- ignore leaking threads on obs, code@bnavigator.de
Patch4:         distributed-ignore-thread-leaks.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-certifi
Requires:       python-click >= 7.0
Requires:       python-cloudpickle >= 1.5.0
Requires:       python-dask = %{version}
Requires:       python-locket >= 1.0.0
Requires:       python-msgpack >= 0.6.0
Requires:       python-packaging >= 20.0
Requires:       python-psutil >= 5.0
Requires:       python-sortedcontainers
Requires:       python-tblib
Requires:       python-toolz >= 0.10.0
Requires:       python-tornado >= 6.2
Requires:       python-urllib3
Requires:       python-zict >= 0.1.3
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if %{with test}
# bokeh 3: see gh#dask/distributed#7329, gh#dask/dask#9659, we provide a legacy bokeh2 in Tumbleweed
BuildRequires:  %{python_module bokeh >= 2.4.2 with %python-bokeh < 2.4.4}
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
    -e 's/timeout_method = thread/timeout_method = signal/' \
    -i setup.cfg

%build
%if ! %{with test}
%python_build
%endif

%install
%if ! %{with test}
%python_install
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

# Some tests randomly fail server-side -- too slow for obs (?)
# see also https://github.com/dask/distributed/issues/5818
donttest+=" or (test_asyncprocess and (test_exit_callback or test_simple))"
donttest+=" or (test_client and test_repr)"
donttest+=" or (test_client and test_profile_server)"
donttest+=" or (test_metrics and test_wall_clock)"
donttest+=" or (test_priorities and test_compute)"
donttest+=" or (test_resources and test_prefer_constrained)"
donttest+=" or (test_steal and test_steal_twice)"
donttest+=" or (test_variable and test_variable_in_task)"
donttest+=" or (test_worker and test_worker_reconnects_mid_compute)"
# server-side fail due to the non-network warning in a subprocess where the patched filter does not apply
donttest+=" or (test_client and test_quiet_close_process)"
if [[ $(getconf LONG_BIT) -eq 32 ]]; then
  # OverflowError -- https://github.com/dask/distributed/issues/5252
  donttest+=" or test_ensure_spilled_immediately"
  donttest+=" or test_value_raises_during_spilling"
  donttest+=" or test_fail_to_pickle_execute_1"
  # https://github.com/dask/distributed/issues/7175
  donttest+=" or (test_sizeof_error and larger)"
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
notparallel+=" or test_popen_timeout"
notparallel+=" or test_plugin_internal_exception"
notparallel+=" or test_runspec_regression_sync"
notparallel+=" or test_client_async_before_loop_starts"

%pytest distributed/tests -m "not avoid_ci" -n auto -k "not ($notparallel or $donttest ${$python_donttest})"
%pytest distributed/tests -m "not avoid_ci" -k "($notparallel) and not ($donttest ${$python_donttest})"
%else
%pytest distributed/tests -m "not avoid_ci" -k "not ($donttest ${$python_donttest})" --reruns 3 --reruns-delay 3
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
%{python_sitelib}/distributed-%{version}*-info

%endif

%changelog
