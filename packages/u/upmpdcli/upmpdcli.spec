#
# spec file for package upmpdcli
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


Name:           upmpdcli
Version:        1.6.2
Release:        0
Summary:        UPnP Media Renderer front-end to MPD, the Music Player Daemon
License:        GPL-2.0-or-later
URL:            https://www.lesbonscomptes.com/updmpdcli
Source0:        https://www.lesbonscomptes.com/upmpdcli/downloads/upmpdcli-%{version}.tar.gz
Source1:        https://www.lesbonscomptes.com/upmpdcli/downloads/upmpdcli-%{version}.tar.gz.asc
Source2:        https://www.lesbonscomptes.com/pages/jf-at-dockes.org.pub#/%{name}.keyring
Patch0:         harden_upmpdcli.service.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  group(audio)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnpupnp)
BuildRequires:  pkgconfig(libupnpp)
Requires(pre):  group(audio)
Requires(pre):  shadow
%{?systemd_ordering}

%description
Upmpdcli turns MPD, the Music Player Daemon into an UPnP Media Renderer,
usable with most UPnP Control Point applications, such as those which run
on Android tablets or phones.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
install -D -m 644 systemd/upmpdcli.service %{buildroot}%{_unitdir}/upmpdcli.service
mkdir -p %{buildroot}/%{_sbindir}
ln -s service %{buildroot}/%{_sbindir}/rcupmpdcli

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_bindir}/scctl
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_unitdir}/upmpdcli.service
%{_sbindir}/rcupmpdcli
%config(noreplace) %{_sysconfdir}/upmpdcli.conf

%pre
getent passwd upmpdcli >/dev/null || useradd -r -g audio -d /nonexistent -s /sbin/nologin -c "user for upmpdcli" upmpdcli
%service_add_pre upmpdcli.service

%post
%service_add_post upmpdcli.service

%preun
%service_del_preun upmpdcli.service

%postun
%service_del_postun upmpdcli.service

%changelog
