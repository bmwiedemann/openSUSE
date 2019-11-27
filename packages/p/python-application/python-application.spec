#
# spec file for package python-application
#
# Copyright (c) 2019 SUSE LLC
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
Name:           python-application
Version:        2.7.0
Release:        0
Summary:        Basic building blocks for Python applications
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/AGProjects/python-application
Source:         https://github.com/AGProjects/python-application/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This module provides some basic components that can be used to simplify
building Python applications.

The components included by this package encapsulate the functionality to
handle the following tasks:

 - UNIX process management (forking, signal handling, pid file creation)
 - A very simple to use interface to handle .ini configuration files.
 - An extensible system logger for console and/or syslog.
 - Miscellaneous utilities and helpers.
 - Memory troubleshooting and execution timing.
 - Communicate inside the application using a notification system.
 - Manage the version number for applications, modules and packages.

%prep
%setup -q -n %{name}-release-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# testsuite does not exist yet

%files %{python_files}
%license LICENSE
%doc ChangeLog NEWS README examples/
%{python_sitelib}/application
%{python_sitelib}/python_application*

%changelog
