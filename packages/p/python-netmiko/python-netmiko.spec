#
# spec file for package python-netmiko
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-netmiko
Version:        4.5.0
Release:        0
Summary:        Multi-vendor library to simplify Paramiko SSH connections to network devices
License:        MIT
URL:            https://github.com/ktbyers/netmiko
Source:         https://files.pythonhosted.org/packages/source/n/netmiko/netmiko-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module setuptools >= 65.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 6.0.2
Requires:       python-cffi >= 1.17.0
Requires:       python-ntc-templates >= 3.1.0
Requires:       python-paramiko >= 2.9.5
Requires:       python-pyserial >= 3.3
Requires:       python-scp >= 0.13.6
Requires:       python-setuptools
Requires:       python-tenacity
Requires:       python-textfsm >= 1.1.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.3}
BuildRequires:  %{python_module paramiko >= 2.6.0}
BuildRequires:  %{python_module pyserial >= 3.3}
BuildRequires:  %{python_module scp >= 0.13.2}
BuildRequires:  %{python_module textfsm >= 1.1.3}
# /SECTION
%python_subpackages

%description
Multi-vendor library to simplify Paramiko SSH connections to network devices.

%prep
%setup -q -n netmiko-%{version}
# drop shebang
sed -i -e '/^#!\//, 1d' \
  netmiko/nokia/nokia_sros.py \
  netmiko/cdot/cdot_cros_ssh.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/netmiko-bulk-encrypt
%python_clone -a %{buildroot}%{_bindir}/netmiko-cfg
%python_clone -a %{buildroot}%{_bindir}/netmiko-encrypt
%python_clone -a %{buildroot}%{_bindir}/netmiko-grep
%python_clone -a %{buildroot}%{_bindir}/netmiko-show
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Fix python-bytecode-inconsistent-mtime
pushd %{buildroot}%{python_sitelib}
find . -name '*.pyc' -exec rm -f '{}' ';'
python%python_bin_suffix -m compileall *.py ';'
popd

%check
# NOTE: for testing, we have to manually run it against a given device.
#
# See https://github.com/ktbyers/netmiko/blob/develop/TESTING.md
#
# Unfortunately, we can't do that during build as those doesn't appeared
# to be unit tests.

%post
%python_install_alternative netmiko-bulk-encrypt
%python_install_alternative netmiko-cfg
%python_install_alternative netmiko-encrypt
%python_install_alternative netmiko-grep
%python_install_alternative netmiko-show

%postun
%python_uninstall_alternative netmiko-bulk-encrypt
%python_uninstall_alternative netmiko-cfg
%python_uninstall_alternative netmiko-encrypt
%python_uninstall_alternative netmiko-grep
%python_uninstall_alternative netmiko-show

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/netmiko-bulk-encrypt
%python_alternative %{_bindir}/netmiko-cfg
%python_alternative %{_bindir}/netmiko-encrypt
%python_alternative %{_bindir}/netmiko-grep
%python_alternative %{_bindir}/netmiko-show
%{python_sitelib}/netmiko
%{python_sitelib}/netmiko-%{version}.dist-info

%changelog
