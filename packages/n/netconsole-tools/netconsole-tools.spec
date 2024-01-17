#
# spec file for package netconsole-tools
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


Name:           netconsole-tools
Version:        20030909
Release:        0
Summary:        Configure netconsole Kernel Module
License:        SUSE-Public-Domain
Group:          System/Kernel
Source0:        netconsole-server.sh
Source2:        netlogging.txt
BuildArch:      noarch

%description
netconsole is a kernel feature to log the dmesg output via the network.
The used network driver must support the polling function.

netconsole-server is a wrapper for insmod to load netconsole.o with the
correct options. Use netcat on the client side to receive the kernel
messages.

%prep
cp -av %{SOURCE2} netlogging.txt

%build

%install
%if 0%{?suse_version} < 1550
install -Dpm 0755 %{SOURCE0} %{buildroot}/sbin/netconsole-server
%else
install -Dpm 0755 %{SOURCE0} %{buildroot}%{_sbindir}/netconsole-server
%endif

%files
%doc netlogging.txt
%if 0%{?suse_version} < 1550
/sbin/netconsole-server
%else
%{_sbindir}/netconsole-server
%endif

%changelog
