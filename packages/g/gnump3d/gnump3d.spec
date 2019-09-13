#
# spec file for package gnump3d
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


Name:           gnump3d
Url:            http://www.gnump3d.org
BuildRequires:  fdupes
BuildRequires:  perl-macros
BuildRequires:  pwdutils
BuildRequires:  pkgconfig(systemd)
Version:        3.0
Release:        0
Summary:        GNU MP3 Streaming Server
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Servers
Requires:       logrotate
Requires(pre):  /usr/sbin/useradd coreutils
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       perl >= 5.8.8
Source:         gnump3d-%{version}.tar.bz2
Source3:        gnump3d-rpmlintrc
Source2:        gnump3d.logrotate
Source4:        gnump3d.service
Patch:          gnump3d-Makefile.patch
Patch1:         avoidversion.diff
%{perl_requires}
%{?systemd_requires}

%description
gnump3d is a simple server that allows you to stream MP3s and OGG
Vorbis files across a network.



%prep
%setup -q
%patch
%patch1 -p1

%build

%install
rm -Rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/var/log/gnump3d
install -d -m 755 $RPM_BUILD_ROOT/etc/logrotate.d
install -d -m 755 $RPM_BUILD_ROOT/usr/sbin
install -d -m 755 $RPM_BUILD_ROOT/srv/mp3
install -d -m 755 $RPM_BUILD_ROOT/var/cache/gnump3d
install -d -m 755 $RPM_BUILD_ROOT/var/cache/gnump3d/serving
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/gnump3d
make PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT install
# Install inetd init script
install -D -m 0644 %SOURCE4 %{buildroot}%{_unitdir}/%{name}.service
(cd $RPM_BUILD_ROOT && ln -sf /usr/sbin/service usr/sbin/rcgnump3d)
(cd $RPM_BUILD_ROOT/usr/bin && ln -sfn gnump3d2 gnump3d)
%fdupes -s $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/useradd -r -o -g nogroup -u 63 -s /bin/false -c "GNUMP3 daemon" -d /var/lib/nobody gnump3d 2> /dev/null || :
%service_add_pre %{name}.service
%post
# if there is no access.log file, create one with correct permissions.
# gnump3d does not do this.
test -f /var/log/gnump3d/access.log || {
  touch /var/log/gnump3d/access.log;
  chmod 640 /var/log/gnump3d/access.log;
  chown gnump3d /var/log/gnump3d/access.log
}
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%doc COPYING AUTHORS README TODO
%doc %{_mandir}/man1/gnump3d-index.1.gz
%doc %{_mandir}/man1/gnump3d-top.1.gz
%doc %{_mandir}/man1/gnump3d.1.gz
%doc %{_mandir}/man1/gnump3d.conf.1.gz
%dir %{_sysconfdir}/gnump3d
%attr(644, root, root) %config %{_sysconfdir}/gnump3d/mime.types
%attr(644, root, root) %config(noreplace) %{_sysconfdir}/gnump3d/gnump3d.conf
%attr(644, root, root) %config %{_sysconfdir}/gnump3d/file.types
%dir %{_datadir}/gnump3d
%doc %{_datadir}/gnump3d/README
%{_datadir}/gnump3d/Avalon
%{_datadir}/gnump3d/LaFrere
%{_datadir}/gnump3d/Tabular
%{_datadir}/gnump3d/Thexder
%{_datadir}/gnump3d/default
%{_datadir}/gnump3d/dotNET
%{_datadir}/gnump3d/nausicaa
%{_datadir}/gnump3d/redgrey
%{_datadir}/gnump3d/simple
%{_datadir}/gnump3d/Clean
%{_datadir}/gnump3d/SchwartzNGrau
%{_datadir}/gnump3d/BlueBox
%{_datadir}/gnump3d/Liquid
%{_datadir}/gnump3d/Musicus
%{_datadir}/gnump3d/Nomad
%{_datadir}/gnump3d/handheld
%{_prefix}/lib/perl5/*/gnump3d
%{_bindir}/gnump3d
%{_bindir}/gnump3d2
%{_bindir}/gnump3d-index
%{_bindir}/gnump3d-top
%{_sbindir}/rcgnump3d
%config(noreplace) %{_sysconfdir}/logrotate.d/gnump3d
%attr(755,gnump3d,root) %dir %{_var}/log/gnump3d
%attr(755,gnump3d,root) %dir %{_var}/cache/gnump3d
%attr(755,gnump3d,root) %dir %{_var}/cache/gnump3d/serving
%attr(755,root,root) %dir /srv/mp3
%{_unitdir}/%{name}.service

%changelog
