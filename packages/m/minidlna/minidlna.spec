#
# spec file for package minidlna
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 by Lars Vogdt <lars@linux-schulserver.de>
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


Name:           minidlna
Version:        1.2.1
Release:        0
Summary:        DLNA compatible server
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            http://sourceforge.net/projects/minidlna/
Source0:        http://prdownloads.sourceforge.net/minidlna/%{name}-%{version}.tar.gz
# Systemd unit file
Source1:        %{name}.service
# tmpfiles configuration for the /run directory
Source2:        %{name}-tmpfiles.conf
# logrotate configuration
Source3:        minidlna_logrotate
# VDR FIX thanks to Boris from openSuse
Patch0:         minidlna-vdr.diff
Patch1:         minidlna-multiple_definition.patch
#BuildRequires:  cvs
BuildRequires:  e2fsprogs-devel
BuildRequires:  flac-devel
BuildRequires:  libexif-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libuuid-devel
BuildRequires:  libvorbis-devel
BuildRequires:  sqlite-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
Requires:       logrotate
Requires:       sqlite3
Requires(pre):  pwdutils
Provides:       ReadyMedia = %{version}

%description
MiniDLNA (aka ReadyDLNA) is server software with the aim of being fully
compliant with DLNA/UPnP-AV clients.

%prep
%setup -q
%patch0
%patch1 -p1

%build
#./autogen.sh

# Edit the default config file
sed -i 's/#log_dir=\/var\/log/#log_dir=\/var\/log\/minidlna/' \
  %{name}.conf

CFLAGS="%{optflags} -I/usr/include/ffmpeg"
%configure \
  --with-db-path=%{_localstatedir}/cache/%{name} \
  --with-log-path=%{_localstatedir}/log/%{name} \
  --enable-tivo

make %{?_smp_mflags}

%install
%make_install
# install service file
install -D -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
# install tmpfiles configuration
install -D -m0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
#
install -d %{buildroot}%{_sbindir}
ln -s /sbin/service %{buildroot}%{_sbindir}/rc%{name}
# install logrotate file
install -D -m0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
# install cache directory
install -d -m0700 %{buildroot}%{_var}/cache/%{name}
# install log directory
install -d -m0700 %{buildroot}%{_var}/log/%{name}
# install manpages
install  -D -m0644 minidlna.conf.5 %{buildroot}/%{_mandir}/man5/minidlna.conf.5
install  -D -m0644 minidlnad.8 %{buildroot}/%{_mandir}/man8/minidlnad.8
# install example config
install  -D -m0644 minidlna.conf %{buildroot}/%{_sysconfdir}/minidlna.conf
# find language dependent files
%find_lang minidlna

%pre
getent group minidlna >/dev/null || groupadd -r minidlna
getent passwd minidlna >/dev/null || \
useradd -r -g minidlna -d /dev/null -s /sbin/nologin \
  -c "minidlna service account" minidlna
%service_add_pre minidlna.service

%preun
%service_del_preun minidlna.service

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post minidlna.service

%postun
%service_del_postun minidlna.service

%files -f minidlna.lang
%license LICENCE* COPYING
%doc NEWS README TODO
%attr(-,minidlna,minidlna) %config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_sbindir}/*
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%attr(0700,minidlna,minidlna) %{_var}/cache/%{name}
%attr(0700,minidlna,minidlna) %{_var}/log/%{name}

%changelog
