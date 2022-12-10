#
# spec file for package python-psutil
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%ifarch x86_64 %{ix86}
%bcond_without  test
%else
%bcond_with     test
%endif
%bcond_without python2
Name:           python-psutil
Version:        5.9.4
Release:        0
Summary:        A process utilities module for Python
License:        BSD-3-Clause
URL:            https://github.com/giampaolo/psutil
Source:         https://files.pythonhosted.org/packages/source/p/psutil/psutil-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip_failing_tests.patch gh#giampaolo/psutil#1635 mcepl@suse.com
# skip tests failing because of incomplete emulation of the environment in osc build
Patch2:         skip_failing_tests.patch
# PATCH-FIX-SLE skip_rlimit_tests_on_python2.patch alarrosa@suse.com
Patch3:         skip_rlimit_tests_on_python2.patch
# PATCH-FIX-SLE adopt change of used memory of procps
Patch4:         mem-used-bsc1181475.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       procps
%if %{with test}
BuildRequires:  net-tools
BuildRequires:  procps
%if %{with python2}
BuildRequires:  python-ipaddress
BuildRequires:  python-mock
BuildRequires:  python-unittest2
%endif
%endif
%ifpython2
Requires:       python-ipaddress
%endif
%python_subpackages

%description
A graphical interface that lets you easily analyze and introspect unaltered running Python processes.

%prep
%setup -q -n psutil-%{version}
%autopatch -p1

# Remove shebangs
sed -i "1s/#!.*//" psutil/{__init__.py,_compat.py,_psbsd.py,_pslinux.py,_psosx.py,_psposix.py,_pssunos.py,_pswindows.py}

%build
%python_build

%install
%python_install

%{python_expand mkdir -p %{buildroot}%{_docdir}/%{$python_prefix}-psutil
cp -r scripts %{buildroot}%{_docdir}/%{$python_prefix}-psutil/
find %{buildroot}%{_docdir}/%{$python_prefix}-psutil/scripts/ -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/env python.*|#!%{__$python}|" {} \;
%fdupes %{buildroot}%{_docdir}/%{$python_prefix}-psutil/
%fdupes %{buildroot}%{$python_sitearch}
}

%if %{with test}
%check
export LANG=en_US.UTF-8
export PSUTIL_TESTING=1
export PSUTIL_DEBUG=1
export PYTHONDONTRWRITEBYTECODE=1
mkdir testd
pushd testd
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -Wa -m psutil.tests
popd
%endif

%files %{python_files}
%license LICENSE
%doc CREDITS HISTORY.rst README.rst
%{_docdir}/%{python_prefix}-psutil/scripts/
%{python_sitearch}/psutil/
%exclude %{python_sitearch}/psutil/tests
%{python_sitearch}/psutil-%{version}*-info

%changelog
