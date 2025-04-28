#
# spec file for package dracut-sshd
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


Name:           dracut-sshd
Version:        0.6.7
Release:        0
Summary:        Provide SSH access to initramfs early user space
License:        GPL-3.0-or-later
Group:          System/Boot
URL:            https://github.com/gsauthof/dracut-sshd
Source:         https://github.com/gsauthof/dracut-sshd/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-Add-sshd-auth-binary.patch
Patch2:         0002-eliminate-misleading-error-message-with-openssh-9.patch
BuildRequires:  dracut
Requires:       dracut
Suggests:       systemd-network
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This Dracut module integrates the OpenSSH sshd into your
initramfs. It allows for remote unlocking of a fully encrypted
root filesystem and remote access to the Dracut emergency shell
(i.e. early userspace).

%prep
%autosetup -p1 -n %{name}-%{version}

%build
# empty

%install
mkdir -p %{buildroot}%{_prefix}/lib/dracut/modules.d
cp -r 46sshd %{buildroot}%{_prefix}/lib/dracut/modules.d/

%files
%dir %{_prefix}/lib/dracut/modules.d/46sshd
%{_prefix}/lib/dracut/modules.d/46sshd/module-setup.sh
%{_prefix}/lib/dracut/modules.d/46sshd/motd
%{_prefix}/lib/dracut/modules.d/46sshd/profile
%{_prefix}/lib/dracut/modules.d/46sshd/sshd.service
%config(noreplace)
%{_prefix}/lib/dracut/modules.d/46sshd/sshd_config
%doc README.md
%doc example/20-wired.network

%changelog
