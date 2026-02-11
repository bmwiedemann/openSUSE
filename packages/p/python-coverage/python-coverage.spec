#
# spec file for package python-coverage
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-coverage%{psuffix}
Version:        7.10.7
Release:        0
Summary:        Code coverage measurement for Python
License:        Apache-2.0
URL:            https://github.com/nedbat/coveragepy
Source:         https://files.pythonhosted.org/packages/source/c/coverage/coverage-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/coveragepy/coveragepy/commit/cf95edab0c3be47ab934f0425f12743745dd2da5 test: a Python error message changed slightly
Patch0:         string.patch
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
# coverage[toml]
Recommends:     python-tomli
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif

%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module coverage = %{version}}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module hypothesis >= 6}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli}
# for database (sqlite3) support
BuildRequires:  %{pythons}
# /SECTION
%endif
%python_subpackages

%description
Coverage.py measures code coverage, typically during test execution. It uses
the code analysis tools and tracing hooks provided in the Python standard
library to determine which lines are executable, and which have been executed.

%prep
%autosetup -p1 -n coverage-%{version}

# we define everything necessary ourselves below
sed -i -e '/addopts/d' setup.cfg

%build
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
rm -vf %{buildroot}%{_bindir}/coverage{2,3}
%python_clone -a %{buildroot}%{_bindir}/coverage
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
export LANG=en_US.UTF8
%python_flavored_alternatives
%{python_expand # indicate a writeable .pth directory for tests
mkdir -p build/mysite
cp %{python_sitearch}/zzzz-import-failed-hooks.pth build/mysite/
}
# the tests need the empty leading part for importing local test projects"
export PYTHONPATH=":$PWD/build/mysite"

export COVERAGE_CORE="pytrace"

%python_exec -mcoverage debug sys

# d:l:p:backports 15.4_py39 does not have python3
if [ ! -x "$(which python3)" ]; then
  mypython=$(find %{_bindir} -name 'python3.*[0-9]' -executable -print -quit)
else
  mypython=python3
fi
# installs some test modules into tests/ (flavor agnostic)
$mypython igor.py zip_mods

# test_version - checks for non-compiled variant, we ship only compiled one
donttest="test_version"
# test_xdist_sys_path_nuttiness_is_fixed - xdist check that we actually fail on purpose
donttest+=" or test_xdist_sys_path_nuttiness_is_fixed"
# does not find a usable venv
donttest+=" or test_venv"
# writes in /usr/
donttest+=" or test_process"
# requires additional plugins
donttest+=" or test_plugins"
# asserts PYTHONPATH is empty, which it can't be
donttest+=" or test_report_wildcard or test_run_omit_vs_report_omit"
%ifarch i586
# flaky due to bad hypothesis performance
donttest+=" or test_numbits.py"
%endif

%pytest_arch -n auto --no-flaky-report -k "$donttest" -rp ||:
%pytest_arch -n auto --no-flaky-report -k "not ($donttest)"
%endif

%pre
%python_libalternatives_reset_alternative coverage

%post
%python_install_alternative coverage

%postun
%python_uninstall_alternative coverage

%if %{without test}
%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTORS.txt README.rst howto.txt
%python_alternative %{_bindir}/coverage
%{python_sitearch}/coverage/
%{python_sitearch}/coverage-%{version}.dist-info
%endif

%changelog
