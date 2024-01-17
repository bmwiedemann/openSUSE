#
# spec file for package nxtvepg
#
# Copyright (c) 2020 SUSE LLC
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


Name:           nxtvepg
Version:        2.8.1
Release:        0
Summary:        Nextview EPG Decoder and Browser
License:        GPL-2.0-or-later
Group:          Hardware/TV
URL:            http://nxtvepg.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/nxtvepg/%{name}-%{version}.tar.gz
Source2:        nxtvepg.service
Patch1:         nxtvepg-Makefile.patch
Patch2:         nxtvepg-no-hardcoded-tcl-dir.patch
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)

%description
In this software package, find a decoder for Nextview--an electronic TV
program guide for the analog domain (as opposed to the various digital
EPGs that come with most digital broadcasts). It allows you to decode
and browse TV program listings for most of the major networks in
Germany, Austria, France, and Switzerland.

Currently, Nextview EPG is transmitted by: * In Germany and Austria:
   Kabel1, 3Sat, RTL-II, EuroNews (coverage: apx. 31 networks)

* In Switzerland: SF1, TSR1, TSI1, EuroNews, 3sat, Kabel1 (coverage:
   apx. 37 networks)

* In France: Canal+, M6 (coverage: 8 networks)

* In Turkey: TRT-1 (coverage: 17 networks)

%prep
%setup -q
%patch1
%patch2

%build
export	CFLAGS="%{optflags}"
make	prefix=%{_prefix}			\
	mandir=%{_mandir}/man1	\
	SYS_DBDIR=%{_localstatedir}/tmp/nxtvdb

%install
make	ROOT=%{buildroot}		\
	prefix=%{_prefix}			\
	mandir=%{buildroot}%{_mandir}/man1	\
	SYS_DBDIR=%{_localstatedir}/tmp/nxtvdb	\
	install
# remove the daemon-only binary - /usr/bin/nxtvepg is capable of running as
# daemon too, so packaging nxtvepgd would mean duplication for most use cases
rm %{buildroot}%{_bindir}/nxtvepgd %{buildroot}%{_mandir}/man1/nxtvepgd.1*
# systemd service file
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/nxtvepg.service

%pre
%service_add_pre nxtvepg.service

%post
%service_add_post nxtvepg.service

%preun
%service_del_preun nxtvepg.service

%postun
%service_del_postun nxtvepg.service

%files
%defattr(-,root,root)
%{_unitdir}/nxtvepg.service
%{_bindir}/nxtvepg
%{_datadir}/nxtvepg
%{_mandir}/man1/nxtvepg.1*
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Nxtvepg
%doc CHANGES COPYRIGHT TODO README manual.html

%changelog
