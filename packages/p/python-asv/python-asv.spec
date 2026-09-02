#
# spec file for package python-asv
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-asv
Version:        0.6.6
Release:        0
Summary:        Airspeed Velocity: A Python history benchmarking tool
License:        BSD-3-Clause AND MIT
URL:            https://github.com/airspeed-velocity/asv
Source:         https://files.pythonhosted.org/packages/source/a/asv/asv-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#airspeed-velocity/asv#1620
Patch0:         support-python315.patch
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-PyYAML
Requires:       python-Pympler
Requires:       python-asv-runner >= 0.3.1
Requires:       python-build
Requires:       python-importlib-metadata
Requires:       python-json5
Requires:       python-packaging
Requires:       python-tabulate
Requires:       python-virtualenv
Suggests:       python-python-hglib >= 1.5
%if %{python_version_nodots} < 311
Requires:       python-tomli
%endif
# SECTION test requirements
BuildRequires:  %{python_module json5}
BuildRequires:  %{python_module asv-runner >= 0.3.1}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  git
# /SECTION
%python_subpackages

%description
airspeed velocity (asv) is a tool for benchmarking Python packages
over their lifetime.

It is designed to benchmark a single project over its lifetime using
a given suite of benchmarks. The results are displayed in an
interactive web frontend that requires only a basic static webserver
to host.

%prep
%autosetup -p1 -n asv-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/asv
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm %{buildroot}%{$python_sitearch}/asv/_rangemedian.cpp

%check
# Requires network
ignore="--ignore=test/test_check.py --ignore=test/test_continuous.py"
ignore+=" --ignore=test/test_profile.py"
donttest="test_verbose_logs_UserError or test_discover_benchmarks"
donttest+=" or test_find_benchmarks_cwd_imports or test_import_failure_retry"
donttest+=" or test_conf_inside_benchmarks_dir or test_code_extraction"
donttest+=" or test_matrix_environments or test_interpolate_multiple_wheels_raises"
donttest+=" or (test_asv_benchmark and virtualenv)"
donttest+=" or (test_find and not test_find_timeout)"
donttest+=" or test_branch_name_is_also_filename or test_run_spec"
donttest+=" or test_run_build_failure or test_run_with_repo_subdir"
donttest+=" or test_benchmark_param_selection or test_run_append_samples"
donttest+=" or test_cpu_affinity or test_env_matrix_value or test_parallel"
donttest+=" or test_filter_date_period or test_return_code or test_run_python_same"
donttest+=" or test_run_accepts_HEAD_range or test_quick or test_run_import_failure"
donttest+=" or test_timeraw_benchmark or test_asv_package_not_on_sys_path"
donttest+=" or test_builtin_statistics_module_not_shadowed"
%pytest_arch $ignore -k "not ($donttest)"

%pre
%python_libalternatives_reset_alternative asv

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%python_alternative %{_bindir}/asv
%{python_sitearch}/asv
%{python_sitearch}/asv-%{version}.dist-info

%changelog
