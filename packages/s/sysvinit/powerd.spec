#
# spec file for package powerd
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


%if 0%{?suse_version} >= 1550
%define sbindir %_sbindir
%else
%define sbindir /sbin
%endif

Name:           powerd
Version:        2.0.2
Release:        0
Summary:        UPS monitoring daemon
License:        GPL-2.0-or-later
Group:          System/Base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  systemd-rpm-macros
URL:            https://power.sourceforge.net/
Source0:        powerd-%{version}.tar.bz2
Source2:        powerd.service
Patch0:         powerd-%{version}.dif
Patch1:         powerd-%{version}-getaddrinfo.patch
%if %{undefined _unitdir}
%{expand: %%global %_unitdir %(pkg-config systemd --variable=systemdsystemunitdir)}
%endif

%description -n powerd
powerd monitors the serial port connected to an UPS device and will perform
an unattended shutdown of the system if the UPS is on battery longer
than a specified number of minutes.

%prep
%setup -q
%patch0
%patch1
%_fixowner .
%_fixgroup .
/bin/chmod -Rf a+rX,g-w,o-w .

%build
  RPM_OPT_FLAGS="${RPM_OPT_FLAGS} $(getconf LFS_CFLAGS) -pipe"
  CC=%__cc
  export RPM_OPT_FLAGS CC
  %configure --prefix= --bindir='$(DESTDIR)%{sbindir}' \
	--mandir='$(DESTDIR)%{_mandir}' \
	--sbindir='$(DESTDIR)%{sbindir}'
  make %{?_smp_mflags} CFLAGS="-I. $RPM_OPT_FLAGS -DWITH_SYSVINIT"

%install
  mkdir -m 755 -p %{buildroot}/etc
  mkdir -m 755 -p %{buildroot}/sbin
  mkdir -m 755 -p %{buildroot}%{_sbindir}
  mkdir -m 755 -p %{buildroot}%{_mandir}/man8
  make install DESTDIR=%{buildroot}
  echo '# ' > %{buildroot}/etc/powerd.conf
  echo '# /etc/powerd.conf  for powerd version-%{version}' >> %{buildroot}/etc/powerd.conf
  echo '# ' >> %{buildroot}/etc/powerd.conf
  echo '# read manual page of detectups(8) and powerd(8) its self.' >> %{buildroot}/etc/powerd.conf
  echo '# ' >> %{buildroot}/etc/powerd.conf
  echo '# to enable powerd service run the command' >> %{buildroot}/etc/powerd.conf
  echo '#    systemctl enable powerd.service' >> %{buildroot}/etc/powerd.conf
  echo '#    systemctl start  powerd.service' >> %{buildroot}/etc/powerd.conf
  mkdir -p %{buildroot}/%{_unitdir}
  install -m 0644 %{S:2} %{buildroot}/%{_unitdir}/powerd.service
  ln -sf service %{buildroot}%{_sbindir}/rcpowerd

%pre
%service_add_post powerd.service

%preun
%service_del_preun powerd.service

%post
%service_add_post powerd.service

%postun
%service_del_postun powerd.service

%files -n powerd
%defattr (-,root,root,755)
%license COPYING
%doc README SUPPORTED FAQ powerd.conf.monitor powerd.conf.peer
%{sbindir}/powerd
%{sbindir}/detectups
%{_sbindir}/rcpowerd
%config /etc/powerd.conf
%attr(0644,root,root) %{_unitdir}/powerd.service
%doc %{_mandir}/man8/powerd.8.gz
%doc %{_mandir}/man8/detectups.8.gz

%changelog
