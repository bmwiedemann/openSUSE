#
# spec file for package python-systemd
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-systemd
Version:        235
Release:        0
Summary:        Python wrappers for systemd functionality
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/systemd/python-systemd
Source:         https://github.com/systemd/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE iso-c-90.patch makes the building iso-c-90 compatible to allow building on SLE12 SP3
Patch1:         iso-c-90.patch
# PATCH-FIX-OPENSUSE OBS_missing_etc_machine_id.patch gh#systemd/python-systemd#118 mcepl@suse.com
# build environment doesn't have /etc/machine-id
Patch2:         OBS_missing_etc_machine_id.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
Requires:       systemd
Suggests:       %{name}-doc
# /SECTION
BuildRequires:  %{python_module pytest}
%python_subpackages

%description
Python module for native access to the systemd facilities. Functionality is seperated into a number of modules:
* systemd.journal supports sending of structured messages to the journal and reading journal files,
* systemd.daemon wraps parts of libsystemd useful for writing daemons and socket activation,
* systemd.id128 provides functions for querying machine and boot identifiers and a lists of message identifiers provided by systemd,
* systemd.login wraps parts of libsystemd used to query logged in users and available seats and machines.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Not sure about the first exclusion,
export PYTEST_ADDOPTS="-k 'not (test_reader_this_machine or test_get_machine)'"
%python_expand make PYTHON=python%{$python_version} check

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitearch}/systemd
%{python_sitearch}/systemd_python-%{version}*-info

%changelog
