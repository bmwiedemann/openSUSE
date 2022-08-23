#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-EasyProcess%{psuffix}
Version:        1.1
Release:        0
Summary:        Python subprocess interface
License:        BSD-2-Clause
URL:            https://github.com/ponty/easyprocess
Source:         https://github.com/ponty/EasyProcess/archive/%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module EasyProcess = %{version}}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyVirtualDisplay}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  ImageMagick
BuildRequires:  iputils
%endif
%python_subpackages

%description
EasyProcess is a Python subprocess interface.

Features include:
 - layer on top of subprocess module
 - starting and stopping of programs
 - retrieval of standard output/error, return code of programs
 - command can be list or string
 - logging
 - timeout
 - unit-tests
 - cross-platform, development on linux
 - global config file with program aliases
 - unicode support
 - supported python versions: 2.5, 2.6, 2.7, 3.1, 3.2, PyPy

Limitations:
 - shell is not supported
 - pipes are not supported
 - stdout/stderr is set only after the subprocess has finished
 - stop() does not kill whole subprocess tree

%prep
%setup -q -n EasyProcess-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/easyprocess
%{python_sitelib}/EasyProcess-%{version}*-info
%endif

%changelog
