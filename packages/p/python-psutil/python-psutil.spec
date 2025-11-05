#
# spec file for package python-psutil
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
%if "%{flavor}" == "test"
%ifarch x86_64 %{ix86}
%define psuffix -%{flavor}
%bcond_without  test
%else
ExclusiveArch:  donotbuild
%endif
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-psutil%{psuffix}
Version:        7.1.2
Release:        0
Summary:        A process utilities module for Python
License:        BSD-3-Clause
URL:            https://github.com/giampaolo/psutil
Source:         https://files.pythonhosted.org/packages/source/p/psutil/psutil-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       procps
BuildRequires:  pkgconfig(libsystemd)
%if %{with test}
%if 0%{?suse_version} > 1500
BuildRequires:  /usr/bin/who
%endif
BuildRequires:  %{python_module psutil = %{version}}
BuildRequires:  %{python_module pytest-subtests}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  net-tools
%endif
%python_subpackages

%description
A graphical interface that lets you easily analyze and introspect unaltered running Python processes.

%prep
%autosetup -p1 -n psutil-%{version}
# do not require pytest-instafail
sed -i '/instafail/d' pyproject.toml

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install

%{python_expand mkdir -p %{buildroot}%{_docdir}/%{$python_prefix}-psutil
cp -r scripts %{buildroot}%{_docdir}/%{$python_prefix}-psutil/
find %{buildroot}%{_docdir}/%{$python_prefix}-psutil/scripts/ -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/env python.*|#!%{__$python}|" {} \;
%fdupes %{buildroot}%{_docdir}/%{$python_prefix}-psutil/
%fdupes %{buildroot}%{$python_sitearch}
}
%endif

%if %{with test}
%check
export LANG=en_US.UTF-8
export PSUTIL_TESTING=1
export PSUTIL_DEBUG=1
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
# needs to be built with extensions to run scripts
%python_expand PYTHON=$python make build
# test_who, test_users - need running session
SKIPTEST="(test_who and Scripts) or (test_users and TestMiscAPIs)"
# test_import_all - pulls in too many dependencies
SKIPTEST="$SKIPTEST or (test_import_all and Scripts)"
# test_all - flaky
SKIPTEST="$SKIPTEST or (test_all and TestFetchAllProcesses)"
# test_multi_sockets_procs - not sure why it fails
SKIPTEST="$SKIPTEST or (test_multi_sockets_procs and TestSystemWideConnections)"
%pytest_arch -n auto --ignore=psutil/tests/test_memleaks.py --ignore=psutil/tests/test_sudo.py -k "not ($SKIPTEST)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc CREDITS HISTORY.rst README.rst
%{_docdir}/%{python_prefix}-psutil/scripts/
%{python_sitearch}/psutil/
%exclude %{python_sitearch}/psutil/tests
%{python_sitearch}/psutil-%{version}.dist-info

%endif

%changelog
