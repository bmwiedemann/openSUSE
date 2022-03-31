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

%ifarch %{ix86} %{arm}
# cython optimizations not supported on 32-bit: https://github.com/dask/dask/issues/7489
%bcond_with cythonize
%else
%bcond_without cythonize
%endif
%if %{with cythonize}
%define cythonize --with-cython
%endif

# use this to run tests with xdist in parallel, unfortunately fails server side
%bcond_with paralleltests

%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
# ===> Note: python-dask MUST be updated in sync with python-distributed! <===
%define         ghversiontag 2022.03.0
Name:           python-distributed%{psuffix}
# ===> Note: python-dask MUST be updated in sync with python-distributed! <===
Version:        2022.3.0
Release:        0
Summary:        Library for distributed computing with Python
License:        BSD-3-Clause
URL:            https://distributed.dask.org
Source:         https://github.com/dask/distributed/archive/refs/tags/%{ghversiontag}.tar.gz#/distributed-%{ghversiontag}-gh.tar.gz
Source99:       python-distributed-rpmlintrc
# PATCH-FIX-UPSTREAM distributed-pr5952-py310.patch -- gh#dask/distributed#5952
Patch1:         distributed-pr5952-py310.patch
# PATCH-FIX-OPENSUSE distributed-ignore-thread-leaks.patch -- ignore leaking threads on obs, code@bnavigator.de
Patch2:         distributed-ignore-thread-leaks.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-certifi
Requires:       python-click >= 6.6
Requires:       python-cloudpickle >= 1.5.0
Requires:       python-dask = %{version}
Requires:       python-msgpack
Requires:       python-packaging >= 20.0
Requires:       python-psutil >= 5.0
Requires:       python-sortedcontainers
Requires:       python-tblib
Requires:       python-toolz >= 0.8.2
Requires:       python-tornado >= 6.0.3
Requires:       python-zict >= 0.1.3
Requires(post): update-alternatives
Requires(postun):update-alternatives
%if %{with cythonize}
BuildRequires:  %{python_module Cython}
# the cythonized scheduler needs Cython also as runtime dep for some checks
Requires:       python-Cython
%endif
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module bokeh}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module click >= 6.6}
BuildRequires:  %{python_module cloudpickle >= 1.5.0}
BuildRequires:  %{python_module dask-all = %{version}}
BuildRequires:  %{python_module distributed = %{version}}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-asyncio >= 0.17.2}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  %{python_module sparse}
BuildRequires:  %{python_module tblib}
BuildRequires:  %{python_module toolz >= 0.8.2}
BuildRequires:  %{python_module tornado >= 6.0.3}
BuildRequires:  %{python_module zict >= 0.1.3}
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
%autosetup -p1 -n distributed-%{ghversiontag}

sed -i -e '/addopts/ {s/--durations=20//; s/--color=yes//}' \
       -e 's/timeout_method = thread/timeout_method = signal/' setup.cfg

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
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# we obviously don't test a git repo
donttest="test_git_revision"
# logger error
donttest+=" or test_version_warning_in_cluster"

# Some tests randomly fail server-side -- too slow for obs (?)
# see also https://github.com/dask/distributed/issues/5818
donttest+=" or (test_asyncprocess and test_exit_callback)"
donttest+=" or (test_client and test_repr)"
donttest+=" or (test_priorities and test_compute)"
donttest+=" or (test_resources and test_prefer_constrained)"
donttest+=" or (test_steal and test_steal_twice)"
donttest+=" or (test_worker and test_gather_dep_one_worker_always_busy)"
donttest+=" or (test_worker and test_worker_reconnects_mid_compute)"

# Exception messages not caught -- https://github.com/dask/distributed/issues/5460#issuecomment-1079432890
python310_donttest+=" or test_exception_text"
python310_donttest+=" or test_worker_bad_args"

if [[ $(getconf LONG_BIT) -eq 32 ]]; then
  # OverflowError -- https://github.com/dask/distributed/issues/5252
  donttest+=" or test_ensure_spilled_immediately"
  donttest+=" or test_value_raises_during_spilling"
  donttest+=" or test_fail_to_pickle_target_1"
fi

%if %{with paralleltests}
# not fully supported parallel test suite: https://github.com/dask/distributed/issues/5186
# works locally, but fails with too many tests server-side
notparallel="rebalance or memory or upload"
notparallel+=" or test_open_close_many_workers"
notparallel+=" or test_recreate_error_array"
notparallel+=" or (test_preload and test_web_preload_worker)"
%pytest_arch distributed/tests -m "not avoid_ci" -n auto -k "not ($notparallel or $donttest ${$python_donttest})"
%pytest_arch distributed/tests -m "not avoid_ci" -k "($notparallel) and (not ($donttest ${$python_donttest}))"
%else
%pytest_arch distributed/tests -m "not avoid_ci" -k "not ($donttest ${$python_donttest})" --reruns 3 --reruns-delay 3
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
%{python_sitearch}/distributed
%{python_sitearch}/distributed-%{version}*-info

%endif

%changelog
