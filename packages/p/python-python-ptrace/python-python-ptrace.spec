#
# spec file for package python-python-ptrace
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%define pyversion 0.9.9
%define cversion 0.6.1
%if "%{flavor}" == ""
%define pkgname python-ptrace
%define pkgversion %{pyversion}
%bcond_with test
%endif
%if "%{flavor}" == "cptrace"
%define pkgname cptrace
%define pkgversion %{cversion}
%bcond_with test
%endif
%if "%{flavor}" == "test"
%define pkgname python-ptrace-test
%define pkgversion %{pyversion}+%{cversion}
%bcond_without test
ExcludeArch:    %arm
%endif

Name:           python-%{pkgname}
Version:        %{pkgversion}
Release:        0
Summary:        Python binding for ptrace
License:        GPL-2.0-only
URL:            https://github.com/vstinner/python-ptrace
Source:         https://github.com/haypo/python-ptrace/archive/%{pyversion}.tar.gz#/python-ptrace-%{pyversion}.tar.gz
# PATCH-FIX-UPSTREAM gh#vstinner/python-ptrace#91
Patch0:         support-python314.patch
%if "%{flavor}" == "cptrace"
BuildRequires:  %{python_module devel}
%else
BuildArch:      noarch
Recommends:     python-cptrace = %{cversion}
%endif
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if %{with test}
BuildRequires:  %{python_module cptrace = %{cversion}}
BuildRequires:  %{python_module python-ptrace = %{pyversion}}
%endif
%python_subpackages

%description
python-ptrace is a debugger using ptrace written in Python.

%prep
%autosetup -p1 -n python-ptrace-%{pyversion}
sed -i 's/\x0D$//' doc/*.rst
chmod 0644 examples/*.py

%build
%if !%{with test}
%if "%{flavor}" == "cptrace"
mv setup.py setup_python-ptrace.py
mv setup_cptrace.py setup.py
%endif
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%if "%{flavor}" == "cptrace"
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%else
%python_clone -a %{buildroot}%{_bindir}/gdb.py
%python_clone -a %{buildroot}%{_bindir}/strace.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif
%endif

%if %{with test}
%check
%python_exec runtests.py -v
%endif

%if !%{with test}
%if "%{flavor}" == ""
%post
%python_install_alternative strace.py
%python_install_alternative gdb.py

%postun
%python_uninstall_alternative strace.py
%python_uninstall_alternative gdb.py

%files %{python_files}
%license COPYING
%doc README.rst
%doc doc/* examples
%python_alternative %{_bindir}/gdb.py
%python_alternative %{_bindir}/strace.py
%{python_sitelib}/ptrace/
%{python_sitelib}/python_ptrace-%{pkgversion}.dist-info
%endif

%if "%{flavor}" == "cptrace"
%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitearch}/cptrace*.so
%{python_sitearch}/cptrace-%{pkgversion}.dist-info
%endif
%endif

%changelog
