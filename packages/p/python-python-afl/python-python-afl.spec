#
# spec file for package python-python-afl
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-python-afl
Version:        0.7.3
Release:        0
Summary:        American fuzzy lop fork server and instrumentation for pure-Python code
License:        MIT
URL:            https://jwilk.net/software/python-afl
Source:         https://files.pythonhosted.org/packages/source/p/python-afl/python-afl-%{version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch0:         https://github.com/jwilk/python-afl/compare/%{version}...sebix:0.7.2-fix-setup-tests.patch#/Use-setuptools-and-use-test-command-for-setup.patch
Patch1:         remove-nose.patch
BuildRequires:  %{python_module Cython >= 0.19}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       afl >= 2
Requires(post): update-alternatives
Requires(postun): update-alternatives
# name with _ automatically redirected by pypi to name with -
Provides:       python-python_afl
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  afl >= 2
BuildRequires:  procps
# /SECTION
%python_subpackages

%description
python-afl is an experimental module that enables American fuzzy lop fork server and instrumentation for pure-Python code.

The scripts to run the fuzzer are only in the package for python3.

%prep
%setup -q -n python-afl-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/py-afl-tmin
%python_clone -a %{buildroot}%{_bindir}/py-afl-showmap
%python_clone -a %{buildroot}%{_bindir}/py-afl-fuzz
%python_clone -a %{buildroot}%{_bindir}/py-afl-cmin
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
rm tests/test_cmin.py tests/test_fuzz.py tests/test_showmap.py tests/test_tmin.py
%pytest_arch

%post
%python_install_alternative py-afl-tmin
%python_install_alternative py-afl-showmap
%python_install_alternative py-afl-fuzz
%python_install_alternative py-afl-cmin

%postun
%python_uninstall_alternative py-afl-tmin
%python_uninstall_alternative py-afl-showmap
%python_uninstall_alternative py-afl-fuzz
%python_uninstall_alternative py-afl-cmin

%files %{python_files}
%doc doc/changelog doc/README doc/trophy-case
%license doc/LICENSE
%python_alternative %{_bindir}/py-afl-cmin
%python_alternative %{_bindir}/py-afl-fuzz
%python_alternative %{_bindir}/py-afl-showmap
%python_alternative %{_bindir}/py-afl-tmin
%{python_sitearch}/afl.cpython-*.so
%{python_sitearch}/python_afl-%{version}.dist-info

%changelog
