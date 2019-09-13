#
# spec file for package monitoring-plugins-openvpn
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


Name:           monitoring-plugins-openvpn
Summary:        Verify the state of the clients connected to a openvpn server
License:        GPL-3.0
Group:          System/Monitoring
Version:        1.1
Release:        0
Url:            https://www.monitoringexchange.org/inventory/Check-Plugins/Software/Misc/check_openvpn_pl
Source0:        check_openvpn.pl
Patch1:         check_openvpn-add-perfdata.patch
BuildRequires:  nagios-rpm-macros
Provides:       nagios-plugins-openvpn = %{version}-%{release}
Obsoletes:      nagios-plugins-openvpn < %{version}-%{release}
Requires:       monitoring-plugins-common
Requires:       perl
Requires:       perl(Net::Telnet)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The -H [IP or hostname of the openvpn server] and -p options [port of the
openvpn server] are always obligatory. If plugin can be connected with the
management interface it will show the common name (as it is specified in the
client certificate) of the connected clients. Otherwise, it will finish with
critical state. The -i option shows the remote IP address of the client instead
of their common name and the -n option shows the number of connected clients.
It is possible to be verified that a client in particular is connected using
one of these two options -C [common name] or -r [remote IP address]. If these
options are used, also the exit state is due to specify that will give back
plugin if it does not find the client through the -w [warning] -c [critical]
options.

%prep
%setup -q -T -c %name
install -m644 %{SOURCE0} .
%patch1 -p0

%build

%install
mkdir -p %buildroot/%{nagios_plugindir}
sed "s|/usr/nagios/libexec|%{nagios_plugindir}|g" check_openvpn.pl > %buildroot/%{nagios_plugindir}/check_openvpn
chmod +x %buildroot/%{nagios_plugindir}/check_openvpn

%clean
rm -rf %buildroot

%files 
%defattr(-,root,root)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_openvpn

%changelog
