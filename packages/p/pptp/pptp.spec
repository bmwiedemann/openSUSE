#
# spec file for package pptp
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


Name:           pptp
Version:        1.8.0
Release:        0
Summary:        Point-to-Point Tunneling Protocol (PPTP) Client
License:        GPL-2.0+
Group:          Productivity/Networking/Security
Url:            http://pptpclient.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/pptpclient/pptp/pptp-%{version}/%{name}-%{version}.tar.gz
Source1:        pptp-command
Source2:        options.pptp
Source3:        pptp_fe.pl
Source4:        xpptp_fe.pl
Patch1:         pptp-makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A client for the proprietary Microsoft Point-to-Point Tunneling
Protocol, PPTP.  It allows connections to a PPTP based VPN as used by
employers and some cable and ADSL service providers. It requires MPPE
support in the kernel. Use the ppp-mppe package.

%prep
%setup -q
%patch1

%build
make CFLAGS="%{optflags}"

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/ppp
mkdir -p %{buildroot}%{_sysconfdir}/pptp.d

cp %{SOURCE1} %{buildroot}%{_sbindir}/pptp-command
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/ppp

find Documentation	-name CVS | xargs rm -rf
find Reference		-name CVS | xargs rm -rf

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING NEWS README TODO USING Documentation
%attr(0755,root,root) %{_sbindir}/pptp
%attr(0755,root,root) %{_sbindir}/pptpsetup
%attr(0444,root,root) %{_mandir}/man8/pptp.8.gz
%attr(0444,root,root) %{_mandir}/man8/pptpsetup.8.gz
%attr(0755,root,root) %{_sbindir}/pptp-command
%attr(750, root, root) %dir %{_sysconfdir}/ppp
%config %attr(0600,root,root) %{_sysconfdir}/ppp/options.pptp
%attr(0755,root,root) %{_sysconfdir}/pptp.d

%changelog
