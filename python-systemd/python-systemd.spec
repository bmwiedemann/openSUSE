#
# spec file for package python-systemd
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-systemd
Version:        234
Release:        0
Summary:        Python wrappers for systemd functionality
License:        LGPL-2.1+
Group:          Development/Languages/Python
Url:            https://github.com/systemd/python-systemd
Source:         https://github.com/systemd/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE iso-c-90.patch makes the building iso-c-90 compatible to allow building on SLE12 SP3
Patch1:         iso-c-90.patch
# PATCH-FIX-OPENSUSE exclude-tests-on-obs.patch removes a test when running tests at OBS. Should be removed as soon as OBS is fixed
Patch100:       exclude-tests-on-obs.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-devel
Requires:       systemd
Suggests:       %{name}-doc
# /SECTION
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Python module for native access to the systemd facilities. Functionality is seperated into a number of modules:
* systemd.journal supports sending of structured messages to the journal and reading journal files,
* systemd.daemon wraps parts of libsystemd useful for writing daemons and socket activation,
* systemd.id128 provides functions for querying machine and boot identifiers and a lists of message identifiers provided by systemd,
* systemd.login wraps parts of libsystemd used to query logged in users and available seats and machines.

%prep
%setup -q
%patch1 -p1
%patch100 -p1

%build
%python_build

%install
%python_install
%fdupes %{buildroot}

%if %{with test}
%check
%python_exec setup.py check
%endif

%files %{python_files}
%doc LICENSE.txt README.md
%{python_sitearch}/*

%changelog
