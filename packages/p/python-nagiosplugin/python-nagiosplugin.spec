#
# spec file for package python-nagiosplugin
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define skip_python36 1
Name:           python-nagiosplugin
Version:        1.3.3
Release:        0
Summary:        Class library for writing Nagios (Icinga) plugins
License:        ZPL-2.1
URL:            https://github.com/mpounsett/nagiosplugin
Source:         https://files.pythonhosted.org/packages/source/n/nagiosplugin/nagiosplugin-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
nagiosplugin is a Python class library which helps writing Nagios (or Icinga)
compatible plugins in Python. It cares for much of the boilerplate code
and default logic commonly found in Nagios checks, including:

- Nagios 3 Plugin API compliant parameters and output formatting
- Full Nagios range syntax support
- Automatic threshold checking
- Multiple independent measures
- Custom status line to communicate the main point quickly
- Long output and performance data
- Timeout handling
- Persistent "cookies" to retain state information between check runs
- Resumption of log file processing at the point where the last run left off
- No dependencies beyond the Python standard library

%prep
%setup -q -n nagiosplugin-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip because of gh#mpounsett/nagiosplugin#53
%pytest -k 'not test_check_users'

%files %{python_files}
%license LICENSE.txt
%doc README.txt
%{python_sitelib}/nagiosplugin
%{python_sitelib}/nagiosplugin-%{version}*-info

%changelog
