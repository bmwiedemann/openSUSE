#
# spec file for package python-debugpy
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
# multibuild: some tests fail to find modules in a custom PYTHONPATH, test installed instead
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-debugpy%{psuffix}
Version:        1.8.2
Release:        0
Summary:        An implementation of the Debug Adapter Protocol for Python
License:        MIT
URL:            https://github.com/microsoft/debugpy/
Source:         https://github.com/microsoft/debugpy/archive/v%{version}.tar.gz#/debugpy-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module debugpy = %{version}}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  gdb
%endif
%python_subpackages

%description
debugpy is an implementation of the Debug Adapter Protocol for Python.

%prep
%autosetup -p1 -n debugpy-%{version}

# don't remove vendored pydevd: upstream's intention is to always bundle it. Development happens in debugpy anyway

# remove precompiled libs
rm src/debugpy/_vendored/pydevd/pydevd_attach_to_process/*.{so,dll,dylib,exe,pdb}
# remove script interpreter lines
sed -i '1 {/^#!/ d}' \
  src/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/*/*.py
# remove gitignore file
find src/debugpy/_vendored/pydevd/ -name .gitignore -delete
# remove a performance tweak not compatible with older gdb: https://github.com/microsoft/debugpy/issues/762
sed -i '/set auto-solib-add off/d' src/debugpy/_vendored/pydevd/pydevd_attach_to_process/add_code_to_python_process.py

%build
%if ! %{with test}
export CFLAGS='%{optflags}'
cp -r src/debugpy/_vendored src/debugpy/_vendored_clean
%{python_expand # cythonize and the attach library are compile in-place
# TODO: find out how to do it not-in-place
rm -r src/debugpy/_vendored
cp -r src/debugpy/_vendored_clean src/debugpy/_vendored
pushd src/debugpy/_vendored/pydevd/pydevd_attach_to_process/linux_and_mac/
# see /src/debugpy/_vendored/pydevd/pydevd_attach_to_process/add_code_to_python_process.py::get_target_filename
%{python_expand pyarch=$($python -c 'import platform; print(platform.machine())')}
g++ %{optflags} -shared -o ../attach_${pyarch}.so -fPIC -nostartfiles attach.cpp
# if on intel architectures, use the default upstream names
%ifarch x86_64
mv ../attach_${pyarch}.so ../attach_linux_amd64.so
%endif
%ifarch %ix86
mv ../attach_${pyarch}.so ../attach_linux_x86.so
%endif
popd
%{$python_build}
}
%endif

%install
%if !%{with test}
# Dont compile pydevd again
export SKIP_CYTHON_BUILD=1
%python_install
%{python_expand # remove source files
rm -r %{buildroot}%{$python_sitearch}/debugpy/_vendored/pydevd/pydevd_attach_to_process/{common,linux_and_mac,windows}/
rm %{buildroot}%{$python_sitearch}/debugpy/_vendored/pydevd/_*/*.{c,h,pxd,pyx}
%fdupes %{buildroot}%{$python_sitearch}
}
%endif

%if %{with test}
%check
export DEBUGPY_TEST=1
export DEBUGPY_PROCESS_EXIT_TIMEOUT=30
export DEBUGPY_PROCESS_SPAWN_TIMEOUT=90
# extra flags are not added
donttest="test_custom_python_args"
# python 3.11 failures
donttest="$donttest or test_redirect_output or test_with_no_output or test_systemexit or test_exceptions_and_partial_exclude_rules or test_exception_stack or test_flask_template_exception_no_multiproc or test_flask_exception_no_multiproc or test_gevent"
rm -v tests/debugpy/test_exception.py tests/debugpy/test_django.py
# gh#microsoft/debugpy#1462
donttest="$donttest or test_attach_pid_client"

# Disable broken tests in s390x, bsc#1217019
%ifarch s390x
sed -i "s/timeout=30/timeout=60/g" pytest.ini
donttest+=" or test_attach_api or test_reattach or test_break_api or test_set_variable or test_unicode or test_debugpySystemInfo or test_debug_this_thread or test_tracing"
%endif

# Do not have numpy dependency
donttest+=" or test_numpy"
# Skip all attach_pid tests, it fails in OBS enviroment bsc#1219921
donttest+=" or attach_pid"

%pytest_arch -k "not ($donttest)"
%endif

%if ! %{with test}
%files %{python_files}
%{python_sitearch}/debugpy
%{python_sitearch}/debugpy-%{version}*-info
%endif

%changelog
