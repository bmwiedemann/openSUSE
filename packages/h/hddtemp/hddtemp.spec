#
# spec file for package hddtemp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2002-2012 Manfred Tremmel <Manfred.Tremmel@iiv.de>
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

%define veronly 0.3
%define state   beta15_e16aed6

Name:           hddtemp
Version:        %{veronly}_%{state}
Release:        0
Summary:        Hard disk temperature tool
License:        GPL-2.0+
Group:          System/Monitoring
Summary(de):    Festplatten Temperatur-Ausleseprogramm
Url:            https://github.com/guzu/hddtemp
Source0:        %{name}-%{veronly}-%{state}.tar.bz2
Source1:        %{name}.db
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.service
Patch0:         hddtemp-db.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  net-tools
BuildRequires:  perl
BuildRequires:  syslogd
%if %suse_version >= 1210
BuildRequires:  pkgconfig(systemd)
%define has_systemd 1
%else
PreReq:         insserv
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
hddtemp is tool that gives you the temperature of your hard drive by
reading S.M.A.R.T. information.

%description -l de
htddtemp ist ein Tool zum auslesen der Festplattentemperatur aus den
S.M.A.R.T Informationenen.

%prep
%setup -q -n %{name}-%{veronly}-%{state}

cp -p %{SOURCE1} ./hddtemp.db
%patch0

%build
aclocal -I m4
autoconf
automake --add-missing --foreign --copy
CFLAGS="%{optflags} -D_GNU_SOURCE" \
%configure
make %{?_smp_mflags}

%install
%makeinstall
mkdir -p %{buildroot}%{_sysconfdir}/default
mkdir -p %{buildroot}%{_datadir}/misc/
mkdir -p %{buildroot}%{_fillupdir}
install -m 0644 hddtemp.db %{buildroot}%{_datadir}/misc/
pushd %{buildroot}%{_sysconfdir}
ln -s ..%{_datadir}/misc/hddtemp.db ./hddtemp.db
popd
install -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.%{name}

%if 0%{?has_systemd}
install -D -m0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}
%else
mkdir -p %{buildroot}%{_initddir}
install -m 0755 %{SOURCE2} %{buildroot}%{_initddir}/%{name}
pushd %{buildroot}%{_sbindir}
ln -s ../..%{_initddir}/%{name} rc%{name}
popd
%endif

%find_lang %{name}

%preun
%if 0%{?has_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%postun
%if 0%{?has_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif

%pre
%if 0%{?has_systemd}
%service_add_pre %{name}.service
%endif

%post
%{fillup_only %{name}}
%if 0%{?has_systemd}
%service_add_post %{name}.service
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING README TODO contribs
%{_datadir}/misc/hddtemp.db
%{_fillupdir}/sysconfig.%{name}
%config(noreplace) %{_sysconfdir}/hddtemp.db
%doc %{_mandir}/man8/hddtemp.8*
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%if 0%{?has_systemd}
%{_unitdir}/%{name}.service
%else
%{_initddir}/%{name}
%endif

%changelog
