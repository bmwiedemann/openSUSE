#
# spec file for package netlabel
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           netlabel
%define         netlabel_docdir %{_docdir}/%{name}
Version:        0.21
Release:        0
Summary:        Explicit labeled networking for Linux
License:        GPL-2.0
Group:          Productivity/Networking/Security
Url:            https://github.com/netlabel/netlabel_tools/wiki
Source0:        https://github.com/netlabel/netlabel_tools/releases/download/v%{version}/netlabel_tools-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libnl-3.0)
# PATCH-FIX-OPENSUSE netlabel_tools-0.20-service.diff mt@suse.de
Patch1:         netlabel_tools-0.20-service.diff

%description
Explicit labeled networking for Linux

The NetLabel control utility, netlabelctl, is a command line program designed
to allow system administrators to configure the NetLabel system in the kernel.
The utility is based around different "modules" which correspond to the
different types of NetLabel commands supported by the kernel.

%package tools
Summary:        Control utility for explicit labeled networking for Linux
Group:          Productivity/Networking/Security

%description tools
Explicit labeled networking for Linux

The NetLabel control utility, netlabelctl, is a command line program designed
to allow system administrators to configure the NetLabel system in the kernel.
The utility is based around different "modules" which correspond to the
different types of NetLabel commands supported by the kernel.

#
# Note: there's no NetLabel Daemon implemented yet,
#       the libraries are not installed by default.
#
%prep
%setup -q -n netlabel_tools-%{version}
%patch1 -p0

%build
%configure --with-systemdsystemunitdir=%_unitdir

%install
%make_install
install -d -m 0755  %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcnetlabel

%pre tools
%service_add_pre netlabel.service

%post tools
%service_add_post netlabel.service

%preun tools
%service_del_preun netlabel.service

%postun tools
%service_del_postun netlabel.service

%files tools
%defattr(-,root,root)
%doc LICENSE README CHANGELOG
%config(noreplace) %attr(600,root,root) %{_sysconfdir}/netlabel.rules
%{_sbindir}/netlabelctl
%{_sbindir}/netlabel-config
%{_sbindir}/rcnetlabel
%{_unitdir}/netlabel.service
%{_mandir}/man8/netlabelctl.8.gz
%{_mandir}/man8/netlabel-config.8.gz

%changelog
