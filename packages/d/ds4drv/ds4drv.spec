#
# spec file for package ds4drv
#
# Copyright (c) 2026 SUSE LLC
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

Name:           ds4drv
Version:        0.5.1
Release:        0
Summary:        A Sony DualShock 4 userspace driver for Linux
License:        MIT
Url:            https://github.com/chrippa/ds4drv
Source:         %{name}-%{version}.tar.gz
Patch0:         ds4drv-no-hcitool.patch
Patch1:         ds4drv-fix-bluetooth-packet-crc.patch
Patch2:         ds4drv-fix-hidraw-usb-broken-pipe.patch
Patch3:         ds4drv-add-battery-udp-telemetry.patch
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  fdupes
BuildRequires:  systemd
BuildRequires:  udev
Requires:       bluez
Requires:       python3-evdev
Requires:       python3-pyudev
Requires:       python3-dbus-python
BuildArch:      noarch

%description
Sony DualShock 4 userspace driver for Linux with Bluetooth LED patch.

%prep
%autosetup -p1

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir=%{buildroot} dist/*.whl

mkdir -p %{buildroot}%{_udevrulesdir}
install -m 0644 udev/50-ds4drv.rules %{buildroot}%{_udevrulesdir}/50-ds4drv.rules

mkdir -p %{buildroot}%{_unitdir}
install -m 0644 systemd/ds4drv.service %{buildroot}%{_unitdir}/ds4drv.service

mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 ds4drv.conf %{buildroot}%{_sysconfdir}/ds4drv.conf

mkdir -p %{buildroot}%{_licensedir}/%{name}
install -m 0644 LICENSE %{buildroot}%{_licensedir}/%{name}/

find %{buildroot} -name "*.pyc" -delete

%fdupes %{buildroot}%{python3_sitelib}

%pre
%service_add_pre ds4drv.service

%post
%service_add_post ds4drv.service

%preun
%service_del_preun ds4drv.service

%postun
%service_del_postun ds4drv.service

%files
%license LICENSE
%doc README.rst HISTORY.rst
%{_bindir}/ds4drv
%{python_sitelib}/ds4drv
%{python_sitelib}/ds4drv-%{version}.dist-info
%{_udevrulesdir}/50-ds4drv.rules
%{_unitdir}/ds4drv.service
%config(noreplace) %{_sysconfdir}/ds4drv.conf

%changelog
