#
# spec file for package python-concurrentloghandler
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


%define modname concurrent-log-handler
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-concurrentloghandler
Version:        0.9.19
Release:        0
Summary:        Concurrent logging handler
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/Preston-Landers/concurrent-log-handler
Source:         https://github.com/Preston-Landers/%{modname}/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM test_returncode.patch bsc#[0-9]+ mcepl@suse.com
# test script should return errorlevel
# Patch0:         test_returncode.patch
BuildRequires:  %{python_module portalocker}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  sed
BuildArch:      noarch
%python_subpackages

%description
This module provides an additional log handler for Python's
standard logging package (PEP 282). This handler will write log
events to log file which is rotated when the log file reaches
a certain size. Multiple processes can safely write to the same
log file concurrently.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
# Remove files installed in wrong places
rm -rf %{buildroot}%{_usr}/{docs,tests}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
rm -rf test_output
$python stresstest.py
}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
