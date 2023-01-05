#
# spec file for package python-coverage
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


Name:           python-coverage
Version:        7.0.3
Release:        0
Summary:        Code coverage measurement for Python
License:        Apache-2.0
URL:            https://github.com/nedbat/coveragepy
Source:         https://files.pythonhosted.org/packages/source/c/coverage/coverage-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires(post): update-alternatives
Requires(postun):update-alternatives
# coverage[toml]
Recommends:     python-tomli
# SECTION test requirements
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module hypothesis >= 6}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli}
# for database (sqlite3) support
BuildRequires:  %{pythons}
# /SECTION
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
%pyproject_wheel

%install
%pyproject_install
rm -vf %{buildroot}%{_bindir}/coverage{2,3}
%python_clone -a %{buildroot}%{_bindir}/coverage
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LANG=en_US.UTF8
%python_flavored_alternatives
%{python_expand # indicate a writeable .pth directory for tests
mkdir -p build/mysite
cp %{python_sitearch}/zzzz-import-failed-hooks.pth build/mysite/
}
# the tests need the empty leading part for importing local test projects"
export PYTHONPATH=":$PWD/build/mysite"

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
# test_debug_sys_ctracer - requires dep on ctracer
donttest+=" or test_debug_sys_ctracer"
# does not find a usable venv
donttest+=" or test_venv"
# writes in /usr/
donttest+=" or test_process"
# requires additional plugins
donttest+=" or test_plugins"

%pytest_arch -n auto --no-flaky-report -k "$donttest" -rp ||:
%pytest_arch -n auto --no-flaky-report -k "not ($donttest)"

%post
%python_install_alternative coverage

%postun
%python_uninstall_alternative coverage

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTORS.txt README.rst howto.txt
%python_alternative %{_bindir}/coverage
%{python_sitearch}/coverage/
%{python_sitearch}/coverage-%{version}.dist-info

%changelog
