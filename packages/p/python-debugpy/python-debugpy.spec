#
# spec file for package python-debugpy
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
# multibuild: some tests fail to find modules in a custom PYTHONPATH, test installed instead
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Python 3.6 is officially supported, but debugpy is in openSUSE for ipykernel 6 which is for Python >= 3.7.
# Skip Py36 in order to save resources.
%define skip_python36 1
%define modname debugpy
Name:           python-%{modname}%{psuffix}
Version:        1.3.0
Release:        0
Summary:        An implementation of the Debug Adapter Protocol for Python
License:        MIT
URL:            https://github.com/microsoft/debugpy/
Source:         https://github.com/microsoft/%{modname}/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE pydevd-openSUSE-attach-autoarch.patch -- support more than intel: use rpmbuild compiled attach library and let gdb figure out the architecture automatically. code@bnavigator.de
Patch0:         pydevd-openSUSE-attach-autoarch.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module %{modname} = %{version}}
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module gevent}
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
%autosetup -p1 -n %{modname}-%{version}

# don't remove vendored pydevd until it is packaged as a separate package (which is not upstream's intention)
# rm -rv src/debugpy/_vendored

# remove precompiled libs
rm src/debugpy/_vendored/pydevd/pydevd_attach_to_process/*.{so,dll,dylib,exe,pdb}
# remove script interpreter lines
sed -i '1 {/^#!/ d}' \
  src/debugpy/_vendored/pydevd/pydevd_attach_to_process/winappdbg/*/*.py \
  src/debugpy/_vendored/pydevd/_pydevd_frame_eval/vendored/bytecode/tests/sanitytest.py
# remove gitignore file
find src/debugpy/_vendored/pydevd/ -name .gitignore -delete

%build
%if ! %{with test}
export CFLAGS='%{optflags}'
cp -r src/debugpy/_vendored src/debugpy/_vendored_clean
%{python_expand # cythonize and the attach library are compile in-place
# TODO: find out how to do it not-in-place
rm -r src/debugpy/_vendored
cp -r src/debugpy/_vendored_clean src/debugpy/_vendored
pushd src/debugpy/_vendored/pydevd/pydevd_attach_to_process/linux_and_mac/
g++ %{optflags} -shared -o ../attach_SUSE.so -fPIC -nostartfiles attach.cpp
popd
%{$python_build}
}
%endif

%install
%if !%{with test}
# Dont compile pydevd again
export SKIP_CYTHON_BUILD=1
%{python_expand # override install-lib: the vendored pydevd is not pure
%{$python_install} --install-lib %{$python_sitearch}
rm -r %{buildroot}%{$python_sitearch}/debugpy/_vendored/pydevd/pydevd_attach_to_process/{common,linux_and_mac,windows}/
rm %{buildroot}%{$python_sitearch}/debugpy/_vendored/pydevd/_*/*.{c,h,pxd,pyx}
%fdupes %{buildroot}%{$python_sitearch}
}
%endif

%if %{with test}
%check
# extra flags are not added
donttest="test_custom_python_args"
# breakpoints and killing fail
donttest+=" or (test_flask and (breakpoint or exception))"
%pytest_arch -x -rfEs -k "not ($donttest)"
%endif

%if ! %{with test}
%files %{python_files}
%{python_sitearch}/%{modname}
%{python_sitearch}/%{modname}-%{version}*-info
%endif

%changelog
