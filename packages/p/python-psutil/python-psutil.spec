#
# spec file for package python-psutil
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


%ifarch x86_64 %{ix86}
%bcond_without  test
%else
%bcond_with     test
%endif
%{?sle15_python_module_pythons}
Name:           python-psutil
Version:        6.1.0
Release:        0
Summary:        A process utilities module for Python
License:        BSD-3-Clause
URL:            https://github.com/giampaolo/psutil
Source:         https://files.pythonhosted.org/packages/source/p/psutil/psutil-%{version}.tar.gz
# PATCH-FIX-SLE adopt change of used memory of procps
Patch4:         mem-used-bsc1181475.patch
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
BuildRequires:  net-tools
BuildRequires:  procps
%endif
%python_subpackages

%description
A graphical interface that lets you easily analyze and introspect unaltered running Python processes.

%prep
%autosetup -p1 -n psutil-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

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
%{python_sitearch}/psutil-%{version}.dist-info

%changelog
