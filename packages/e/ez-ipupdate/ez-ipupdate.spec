#
# spec file for package ez-ipupdate
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ez-ipupdate
Version:        3.0.11b8
Release:        0
Summary:        A Small Utility for Updating a Dynamic DNS Service
License:        GPL-2.0+
Group:          Productivity/Networking/DNS/Utilities
Url:            http://ez-ipupdate.com/
Source0:        %{name}-%{version}.tar.bz2
Source1:        ez-ipupdate.init
Source2:        ez-ipupdate.example.conf
Source3:        ez-ipupdate.service
Source4:        ez-ipupdate.tmpfiles
Patch0:         ez-ipupdate.example.conf.patch
Patch1:         ez-ipupdate-3.0.11b8-include.diff
Patch2:         ez-ipupdate-format-string-vuln.patch
Patch3:         ez-ipupdate-includes.patch
Patch4:         ez-ipupdate-dnsexit.patch
# PATCH-FIX-UPSTREAM Various fixes for configure.ac and Makefile.am
Patch5:         ez-ipupdate-fix_autofoo.patch
# PATCH-FEATURE-UPSTREAM Add support for joker.com dyndns service
Patch6:         ez-ipupdate-joker_com.patch
# PATCH-FIX-UPSTREAM do type punning via memcpy
Patch7:         ez-ipupdate-type-punning.patch
# PATCH-FIX-UPSTREAM Reduce compiler warnings.
Patch8:         ez-ipupdate-code_cleanup.patch
BuildRequires:  automake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >=1230
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%else
Requires(pre):  %insserv_prereq
%endif
%{!?tmpfiles_create:%global tmpfiles_create systemd-tmpfiles --create}

%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif

%description
ez-ipupdate is a small utility for updating your hostname for any of
the dynamic DNS services offered at:

* http://www.ez-ip.net

* http://www.justlinux.com

* http://www.dhs.org

* http://www.dyndns.org

* http://www.ods.org

* http://gnudip.cheapnet.net (GNUDip)

* http://www.dyn.ca (GNUDip)

* http://www.tzo.com

* http://www.easydns.com

* http://www.dyns.cx

* http://www.hn.org

* http://www.zoneedit.com

* http://www.joker.com

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3
%patch4
mv configure.in configure.ac
%patch5
%patch6
%patch7
%patch8
rm acconfig.h

%build
find -name "example*" | xargs -n 1 sed -i "s@%{_prefix}/local/bin/@%{_bindir}/@"
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -m 755 -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_sbindir}
%if 0%{?suse_version} >=1230
install -m 755 -d %{buildroot}%{_unitdir}
%else
install -m 755 -d %{buildroot}%{_sysconfdir}/init.d
%endif
install -m 755 -d %{buildroot}%{_localstatedir}/lib/ez-ipupdate/
install -m 600 %{SOURCE2} %{buildroot}%{_sysconfdir}/ez-ipupdate.conf
%if 0%{?suse_version} >=1230
install -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/ez-ipupdate.service
sed -i -e 's,/run/,%{_rundir}/,g' %{buildroot}%{_unitdir}/ez-ipupdate.service
ln -sf %{_sbindir}/service  %{buildroot}%{_sbindir}/rcez-ipupdate
install -D -m0644 %{SOURCE4} %{buildroot}/%{_prefix}/lib/tmpfiles.d/%{name}.conf
sed -i -e 's,/run/,%{_rundir}/,g' %{buildroot}/%{_prefix}/lib/tmpfiles.d/%{name}.conf
%else
install -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/ez-ipupdate
ln -sf %{_initddir}/ez-ipupdate %{buildroot}%{_sbindir}/rcez-ipupdate
%endif

%pre
%if 0%{?suse_version} >=1230
%service_add_pre %{name}.service
%endif

%preun
%if 0%{?suse_version} >=1230
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%post
%if 0%{?suse_version} >=1230
%service_add_post %{name}.service
%tmpfiles_create %{_prefix}/lib/tmpfiles.d/%{name}.conf
%else
%{fillup_and_insserv -f %{name}}
%endif

%postun
%if 0%{?suse_version} >=1230
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif

%files
%defattr(-, root, root)
%doc README CHANGELOG COPYING example*
%{_bindir}/ez-ipupdate
%{_sbindir}/rcez-ipupdate
%config(noreplace) %{_sysconfdir}/ez-ipupdate.conf
%if 0%{?suse_version} >=1230
%{_unitdir}/%{name}.service
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%else
%{_sysconfdir}/init.d/ez-ipupdate
%endif
%{_localstatedir}/lib/ez-ipupdate/

%changelog
