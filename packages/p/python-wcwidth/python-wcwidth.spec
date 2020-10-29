#
# spec file for package python
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without python2
Name:           python-wcwidth%{psuffix}
Version:        0.2.5
Release:        0
Summary:        Number of Terminal column cells of wide-character codes
License:        MIT
URL:            https://github.com/jquast/wcwidth
Source:         https://github.com/jquast/wcwidth/archive/%{version}.tar.gz#/wcwidth-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wcwidth >= %{version}}
%if %{with python2}
BuildRequires:  python-backports.functools_lru_cache >= 1.2.1
%endif
%endif
%ifpython2
Requires:       python-backports.functools_lru_cache >= 1.2.1
%endif
%python_subpackages

%description
This API is mainly for Terminal Emulator implementors -- any python
program that attempts to determine the printable width of a string on
a Terminal. It is implemented in python (no C library calls) and has
no 3rd-party dependencies.

It is certainly possible to use your Operating System's wcwidth(3)
and wcswidth(3) calls if it is POSIX-conforming, but this would not
be possible on non-POSIX platforms, such as Windows, or for
alternative Python implementations, such as jython.  It is also
commonly many releases older than the most current Unicode Standard
release files, which this project aims to track.

%prep
%setup -q -n wcwidth-%{version}
sed -i 's/--cov[-=a-z]*//g' tox.ini
# this option is nonsense
sed -i 's/looponfailroots.*//' tox.ini

%build
%python_build

%install
%if ! %{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest tests
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*
%endif

%changelog
