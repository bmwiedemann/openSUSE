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
%bcond_without test
%define psuffix -%{flavor}
%else
%bcond_with test
%define psuffix %{nil}
%endif
Name:           python-wcwidth%{psuffix}
Version:        0.1.9
Release:        0
Summary:        Number of Terminal column cells of wide-character codes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jquast/wcwidth
Source:         https://files.pythonhosted.org/packages/source/w/wcwidth/wcwidth-%{version}.tar.gz
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
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

%build
%python_build

%install
%if ! %{with test}
%python_install

# Remove tests from runtime
%{python_expand rm -r %{buildroot}%{$python_sitelib}/wcwidth/tests/
%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%check
%if %{with test}
%pytest
%endif

%if ! %{with test}

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*
%endif

%changelog
