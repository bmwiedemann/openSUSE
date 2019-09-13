#
# spec file for package python-psutil
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%ifarch x86_64 %{ix86}
%bcond_without  test
%else
%bcond_with     test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-psutil
Version:        5.6.1
Release:        0
Summary:        A process utilities module for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/giampaolo/psutil
Source:         https://files.pythonhosted.org/packages/source/p/psutil/psutil-%{version}.tar.gz
Patch0:         pr_1364.patch
Patch1:         skip-test-missing-warnings.patch
Patch2:         skip-flaky-i586.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       net-tools
Requires:       procps
%if %{with test}
BuildRequires:  net-tools
BuildRequires:  procps
BuildRequires:  python-ipaddress
BuildRequires:  python-mock
%endif
%ifpython2
Requires:       python-ipaddress
%endif
%python_subpackages

%description
A graphical interface that lets you easily analyze and introspect unaltered running Python processes.

%prep
%setup -q -n psutil-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Remove shebangs
sed -i "1s/#!.*//" psutil/{__init__.py,_compat.py,_psbsd.py,_pslinux.py,_psosx.py,_psposix.py,_pssunos.py,_pswindows.py}

%build
%python_build

%install
%python_install

%{python_expand mkdir -p %{buildroot}%{_docdir}/%{$python_prefix}-psutil
cp -r scripts %{buildroot}%{_docdir}/%{$python_prefix}-psutil/
find %{buildroot}%{_docdir}/%{$python_prefix}-psutil/scripts/ -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/env python|#!%__$python|" {} \;
find %{buildroot}%{$python_sitearch}/psutil/tests/ -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/env python|#!%__$python|" {} \;
rm -r %{buildroot}%{$python_sitearch}/psutil/tests/
%fdupes %{buildroot}%{_docdir}/%{$python_prefix}-psutil/
%fdupes %{buildroot}%{$python_sitearch}
}

%if %{with test}
%check
export LANG=en_US.UTF-8
export PSUTIL_TESTING=1
export TRAVIS=1

# Note test_fetch_all is a bit flaky, occasionally failing
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
cp -r scripts %{buildroot}%{$python_sitearch}/
cp -r psutil/tests %{buildroot}%{$python_sitearch}/psutil
$python -W default %{buildroot}%{$python_sitearch}/psutil/tests/__main__.py
rm -r %{buildroot}%{$python_sitearch}/scripts %{buildroot}%{$python_sitearch}/psutil/tests
}
%endif

%files %{python_files}
%license LICENSE
%doc CREDITS HISTORY.rst README.rst
%{_docdir}/%{python_prefix}-psutil/scripts/
%{python_sitearch}/psutil/
%{python_sitearch}/psutil/_psutil_*.so
%{python_sitearch}/psutil-%{version}-py*.egg-info

%changelog
