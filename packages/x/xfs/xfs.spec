#
# spec file for package xfs
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


%if 0%{?suse_version} < 1550
  %define _distconfdir %{_prefix}%{_sysconfdir}
%endif
Name:           xfs
Version:        1.2.1
Release:        0
Summary:        X font server
License:        HPND
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/xfs-%{version}.tar.xz
Source1:        xfs.config
Source2:        xfs.init.d
Source3:        xfs.service
Source10:       https://xorg.freedesktop.org/releases/individual/app/xfs-%{version}.tar.xz.sig
Source11:       xfs.keyring
BuildRequires:  font-util >= 1.1
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xorg-macros) >= 1.10
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xtrans)
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %fillup_prereq
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
xfs is the X Window System font server. It supplies fonts to X Window
System display servers.

%prep
%setup -q

%build
%configure --with-default-config-file=%{_sysconfdir}/X11/fs/config,%{_distconfdir}/X11/fs/config CFLAGS="%{optflags} -Wno-error=array-bounds"
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_sbindir} \
         %{buildroot}%{_unitdir}
rm -f %{buildroot}%{_sysconfdir}/X11/fs/config
install -D -m 0644 %{SOURCE1} %{buildroot}%{_distconfdir}/X11/fs/config
install -D -m 0444 %{SOURCE3} %{buildroot}%{_unitdir}/xfs.service
install -D -m 0755 %{SOURCE2} %{buildroot}%{_sbindir}/rcxfs

%pre
%service_add_pre xfs.service

%post
%service_add_post xfs.service

%preun
%service_del_preun xfs.service

%postun
%service_del_postun xfs.service

%files
%license COPYING
%doc ChangeLog README.md
%dir %{_distconfdir}
%dir %{_distconfdir}/X11
%dir %{_distconfdir}/X11/fs
%{_distconfdir}/X11/fs/config
%{_unitdir}/xfs.service
%{_sbindir}/rcxfs
%{_bindir}/xfs
%{_mandir}/man1/xfs.1%{?ext_man}

%changelog
