#
# spec file for package pptpd
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           pptpd
Version:        1.4.0
Release:        0
Url:            http://www.poptop.org/
Summary:        PoPToP - PPTP Daemon, Linux as Microsoft VPN Server
License:        GPL-2.0+
Group:          Productivity/Networking/PPP
Source:         http://downloads.sourceforge.net/project/poptop/pptpd/pptpd-%{version}/pptpd-%{version}.tar.gz
Source1:        rcpptpd
Source3:        pptp-install.tar.bz2
Source4:        pptpd.conf
Source5:        options.ppp0
Source7:        README.SUSE
Source8:        LIESMICH.SUSE
Source9:        pptpd.service
Patch0:         makefile.diff
Patch1:         pptpd-cflags.patch
Patch3:         pptpd-stringcompare.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  ppp-devel
Requires:       ppp
%if 0%{?suse_version} > 1140
BuildRequires:  systemd
%{?systemd_requires}
%define has_systemd 1
%else
PreReq:         %fillup_prereq %insserv_prereq
%endif

%description
PoPToP is a PPTP(Point-to-Point Tunneling Protocol) server solution for
Linux, it allows Linux servers to function seamlessly in the PPTP VPN
environment. This release supports Windows 95/98/NT/2000 PPTP clients
and PPTP Linux clients.

%prep
%setup -q -a 3
%patch0
%patch1 -p1
%patch3
rm plugins/patchlevel.h

%build
autoreconf -i -f
%configure
make OPTFLAGS="$RPM_OPT_FLAGS"

%install
make install DESTDIR=%{buildroot}
install -m 0755 pptpd			%{buildroot}/usr/sbin/pptpd
install -m 0755 pptpctrl		%{buildroot}/usr/sbin/pptpctrl

%if 0%{?has_systemd}
install -D -m 0644 %{S:9} %{buildroot}%{_unitdir}/`basename %{S:9}`
mkdir -p %{buildroot}/usr/lib/modules-load.d
echo "ppp_mppe" > %{buildroot}/usr/lib/modules-load.d/pptpd.conf
%else
mkdir -p %{buildroot}/etc/init.d
install -m 0744 %{S:1}			%{buildroot}/etc/init.d/pptpd
ln -sf ../../etc/init.d/pptpd %{buildroot}/usr/sbin/rcpptpd
%endif
install -Dm 0644 %{S:4}			%{buildroot}/etc/pptpd.conf
find {samples,PPTP-Installation,pptp-server} -type f -exec chmod -x {} +
chmod -x AUTHORS COPYING ChangeLog INSTALL NEWS README* TODO
mkdir -p %{buildroot}/usr/lib/modules-load.d

%pre
%if 0%{?has_systemd}
%service_add_pre %{name}.service
%endif

%preun 
%if 0%{?has_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal pptpd
%endif

%post
%if 0%{?has_systemd}
%service_add_post %{name}.service
%else
%{fillup_and_insserv pptpd}
%endif

%postun
%if 0%{?has_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update pptpd
%{insserv_cleanup}
%endif

%files
%defattr (-, root, root)
%doc $RPM_SOURCE_DIR/README.SUSE $RPM_SOURCE_DIR/LIESMICH.SUSE
%doc $RPM_SOURCE_DIR/options.ppp0
%doc AUTHORS COPYING ChangeLog NEWS README* TODO
%doc samples PPTP-Installation pptp-server
%config /etc/pptpd.conf
%{_mandir}/*/pptp*
%{_mandir}/man8/bcrelay.8.gz
/usr/sbin/pptpctrl
/usr/sbin/pptpd
/usr/sbin/bcrelay
/usr/lib/pptpd
%if 0%{?has_systemd}
%{_unitdir}/%{name}.service
/usr/lib/modules-load.d/pptpd.conf
%else
/usr/sbin/rcpptpd
/etc/init.d/pptpd
%endif

%changelog
