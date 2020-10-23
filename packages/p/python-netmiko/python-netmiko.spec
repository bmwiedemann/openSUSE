#
# spec file for package python-netmiko
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
%define skip_python2 1
Name:           python-netmiko
Version:        3.3.2
Release:        0
Summary:        Multi-vendor library to simplify Paramiko SSH connections to network devices
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ktbyers/netmiko
Source:         https://files.pythonhosted.org/packages/source/n/netmiko/netmiko-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-paramiko >= 2.6.0
Requires:       python-pyserial
Requires:       python-scp >= 0.13.2
Requires:       python-tenacity
Requires:       python-textfsm
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module paramiko >= 2.6.0}
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module scp >= 0.13.2}
BuildRequires:  %{python_module textfsm}
# /SECTION
%python_subpackages

%description
Multi-vendor library to simplify Paramiko SSH connections to network devices.

%prep
%setup -q -n netmiko-%{version}
# drop shebang
sed -i -e '/^#!\//, 1d' netmiko/nokia/nokia_sros_ssh.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# NOTE: for testing, we have to manually run it against a given device.
#
# See https://github.com/ktbyers/netmiko/blob/develop/TESTING.md
#
# Unfortunately, we can't do that during build as those doesn't appeared
# to be unit tests.

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
