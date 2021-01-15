#
# spec file for package python-typing_extensions
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


%define modname typing_extensions
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-typing_extensions%{psuffix}
Version:        3.7.4.3
Release:        0
Summary:        Backported and Experimental Type Hints for Python 35+
License:        Python-2.0
URL:            https://github.com/python/typing/
Source0:        https://files.pythonhosted.org/packages/source/t/typing_extensions/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Provides:       python-typing-extensions = %{version}
%if 0%{?suse_version} > 1320 && %{with test}
BuildRequires:  %{python_module testsuite}
%endif
%if %{with python2}
BuildRequires:  python-typing >= 3.7.4
%endif
BuildRequires:  (python3-typing >= 3.7.4 if python3-base < 3.5)
%if %{python_version_nodots} < 35
Requires:       python-typing >= 3.7.4
%endif
%python_subpackages

%description
The ``typing`` module was added to the standard library in Python
3.5 on a provisional basis and will no longer be provisional in
Python 3.7. However, this means users of Python 3.5 - 3.6 who are
unable to upgrade will not be able to take advantage of new types
added to the ``typing`` module, such as ``typing.Text`` or
``typing.Coroutine``.

The ``typing_extensions`` module contains both backports of these
changes as well as experimental types that will eventually be
added to the ``typing`` module, such as ``Protocol``.

Users of other Python versions should continue to install and use
the ``typing`` module from PyPi instead of using this one unless
specifically writing code that must be compatible with multiple
Python versions or requires experimental types.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%if ! %{with test}
%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# X.Y -> X
%{python_expand current_bin_suffix=%{$python_bin_suffix}
$python src_py${current_bin_suffix:0:1}/test_typing_extensions.py
}
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/typing_extensions.py*
%pycache_only %{python_sitelib}/__pycache__/typing_extensions*
%{python_sitelib}/typing_extensions-%{version}*-info
%endif

%changelog
