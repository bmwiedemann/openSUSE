#
# spec file for package python-concurrentloghandler
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-concurrentloghandler
Version:        0.9.31
Release:        0
Summary:        Concurrent logging handler
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/Preston-Landers/concurrent-log-handler
Source:         https://github.com/Preston-Landers/%{modname}/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module portalocker}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  sed
Requires:       python-portalocker >= 2.6.0
BuildArch:      noarch
%python_subpackages

%description
This module provides an additional log handler for Python's
standard logging package (PEP 282). This handler will write log
events to log file which is rotated when the log file reaches
a certain size. Multiple processes can safely write to the same
log file concurrently.

%prep
%autosetup -p1 -n concurrent-log-handler-%{version}
# __init__.py is an importable module installed as a non-executable file, so
# rpmlint flags its leading shebang as non-executable-script: drop that line
sed -i '1{/^#!/d}' src/concurrent_log_handler/__init__.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
# Remove files installed in wrong places
rm -rf %{buildroot}%{_usr}/{docs,tests}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests/stresstest.py as a script crashes in its own argparse setup
# (TestOptions.__annotations__[...].default); use the pytest suite instead
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/concurrent_log_handler
%{python_sitelib}/concurrent_log_handler-%{version}*-info

%changelog
