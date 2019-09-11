#
# spec file for package bwbar
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           bwbar
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
Url:            http://www.kernel.org/pub/software/web/bwbar/
Summary:        Bandwidth usage bar
License:        GPL-2.0+
Group:          Productivity/Networking/Other
Version:        1.2.3 
Release:        0
Source:         %{name}-%{version}.tar.bz2
Source1:        COPYING
Source2:        bwbar_config
Source3:        bwbar_initscript
Source4:        bwbar.service
# http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/net-analyzer/bwbar/files/bwbar-1.2.3-libpng15.patch?revision=1.1&pathrev=HEAD
# PATCH-FIX-UPSTREAM bwbar-1.2.3-libpng15.patch andreas.stieger@gmx.de -- fixes build against libpng15
Patch0:         bwbar-1.2.3-libpng15.patch
#
%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%define has_systemd 1
%endif
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
bwbar is a small program that generates a text and a graphical readout
of the current bandwidth use to be displayed on a web page.

It is used, among others, at http://www.kernel.org/.

Authors:
--------
    H. Peter Anvin <hpa@zytor.com>

%prep
%setup -q
%patch0

%{__cp} %{SOURCE1} .

%build
CFLAGS="-Wall $RPM_OPT_FLAGS"  
%configure --prefix=%{_prefix} \
           --infodir=%{_infodir} \
           --mandir=%{_mandir} 
%__make %{?_smp_mflags}

%install
install -d %buildroot%{_bindir} 
install -m 755 bwbar %buildroot%{_bindir}
install -m 644 -D %{SOURCE2} %buildroot%{_fillupdir}/sysconfig.%{name}
#
%if 0%{?has_systemd}
install -m 644 -D %{SOURCE4} %buildroot/%{_unitdir}/%name.service
%else
install -m 755 -D %{SOURCE3} %buildroot%{_sysconfdir}/init.d/%{name}
mkdir -p %buildroot%{_sbindir}
ln -svf ../../etc/init.d/%{name} %buildroot/%{_sbindir}/rc%{name}  
%endif
#

%pre
%if 0%{?has_systemd}
%service_add_pre bwbar.service
%endif

%post
%if 0%{?has_systemd}
%service_add_post bwbar.service
%{fillup_only}
%else
%{fillup_and_insserv}
%endif

%preun
%if 0%{?has_systemd}
%service_del_preun bwbar.service
%else
%stop_on_removal
%endif

%postun
%if 0%{?has_systemd}
%service_del_postun bwbar.service
%else
%insserv_cleanup
%restart_on_update
%endif

%files 
%defattr(-, root, root)
%doc README COPYING
%{_bindir}/*
%{_fillupdir}/sysconfig.%{name}
%if 0%{?has_systemd}
%{_unitdir}/%{name}.service
%else
%{_sbindir}/*
%config %{_sysconfdir}/init.d/%{name}
%endif

%changelog
