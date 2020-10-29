#
# spec file for package python-psutil
#
# Copyright (c) 2020 SUSE LLC
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
Version:        5.7.2
Release:        0
Summary:        A process utilities module for Python
License:        BSD-3-Clause
URL:            https://github.com/giampaolo/psutil
Source:         https://files.pythonhosted.org/packages/source/p/psutil/psutil-%{version}.tar.gz
Patch1:         skip-obs.patch
# PATCH-FIX-UPSTREAM skip_failing_tests.patch gh#giampaolo/psutil#1635 mcepl@suse.com
# skip tests failing because of incomplete emulation of the environment in osc build
Patch2:         skip_failing_tests.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       net-tools
Requires:       procps
%if %{with test}
BuildRequires:  net-tools
BuildRequires:  procps
%if %{with python2}
BuildRequires:  python-ipaddress
BuildRequires:  python-mock
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
find %{buildroot}%{_docdir}/%{$python_prefix}-psutil/scripts/ -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/env python|#!%__$python|" {} \;
%fdupes %{buildroot}%{_docdir}/%{$python_prefix}-psutil/
%fdupes %{buildroot}%{$python_sitearch}
}

%if %{with test}
%check
export LANG=en_US.UTF-8
export PSUTIL_TESTING=1
export TRAVIS=1

# Note test_fetch_all is a bit flaky, occasionally failing
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -Wa psutil/tests/runner.py
%endif

%files %{python_files}
%license LICENSE
%doc CREDITS HISTORY.rst README.rst
%{_docdir}/%{python_prefix}-psutil/scripts/
%{python_sitearch}/psutil/
%{python_sitearch}/psutil/_psutil_*.so
%{python_sitearch}/psutil-%{version}-py*.egg-info

%changelog
