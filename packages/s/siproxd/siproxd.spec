#
# spec file for package siproxd
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


#
%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif
%define piddir          %_rundir/siproxd/
%define regdir          /var/lib/siproxd/
%define siproxduser     siproxd
%define siproxdgroup    siproxd

Name:           siproxd
Version:        0.8.2
Release:        0
Summary:        A SIP masquerading proxy with RTP support
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://siproxd.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Source1:        susefirewall2.%{name}
Source2:        %name.init.in
Source3:        %name.logrotate
Source4:        %name.8.gz
Source5:        syslog-ng.conf.addon	
Source6:        siproxd.service
# PATCH-FIX-FOR-UPSTREAM -- http://sourceforge.net/tracker/?func=detail&aid=3086321&group_id=60374&atid=493974
#Code to detect libltdl was placed before the code that populates the library locations.
#This caused libltdl to be undetected even after it was installed locally.
#The patch moves the library detection code in front of libltdl detection
#and also adds standard library (and include) locations, ie. /usr/local/lib
#After applying the patch, autogen.sh needs to be run (which, among other things, rebuilds "configure").
Patch0:         siproxd-libs.patch
#PATCH-FIX-FROM-DEBIAN use logger not user
Patch1:         siproxd-log.c.patch
Patch2:         siproxd.plugin_fix_bogus_via.c.patch
Patch3:         siproxd-multiple-definition.patch
BuildRequires:  docbook-utils
BuildRequires:  libosip2-devel
BuildRequires:  libtool
%if %suse_version > 1220
BuildRequires:  texlive-courier
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-jadetex
BuildRequires:  texlive-times
%endif
%if %suse_version > 1315
BuildRequires:  texlive-kpathsea
BuildRequires:  texlive-metafont
BuildRequires:  texlive-texconfig
BuildRequires:  texlive-wasy
%endif
Requires:       logrotate
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Requires(pre):  %insserv_prereq
%if %suse_version <= 1500
Suggests:       SuSEfirewall2
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Siproxd is an proxy/masquerading daemon for the SIP protocol. It handles
registrations of SIP clients on a private IP network and performs
rewriting of the SIP message bodies to make SIP connections possible
via an masquerading firewall. It allows SIP clients (like kphone,
linphone) to work behind an IP masquerading firewall or router.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/Other

%description doc
HTML and PDF documentation for %{name}

%prep
%setup -q

%patch0 -p1	
%patch1
%patch2 -p1
%patch3 -p1

cp %{S:5} .

%build
autoreconf --install --force
CFLAGS="%{optflags} -fno-strict-aliasing"
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mv %{buildroot}%{_sysconfdir}/%{name}.conf.example \
   %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

%if %suse_version <= 1500
install -d %{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/
install -m 644 %{S:1} %{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%endif

install -d %{buildroot}/%{_sysconfdir}/logrotate.d/
install -m 0644 %{S:3} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

install -d %{buildroot}/%{_datadir}/%{name}/scripts
install %{S:2} %{buildroot}/%{_datadir}/%{name}/scripts/%{name}
install -d %{buildroot}/%{_unitdir}
install -m 644 %{S:6} %{buildroot}/%{_unitdir}
sed -i "s#@%{name}_PIDDIR@#%{_rundir}/%{name}#" %{buildroot}%{_datadir}/%{name}/scripts/%{name}
install -d %buildroot/%{_sbindir}
ln -s %{_sbindir}/service %buildroot/%{_sbindir}/rc%{name}

mkdir -p %buildroot%_mandir/man8
install -m 0644 %{S:4} %{buildroot}/%{_mandir}/man8/%name.8.gz
#
sed -i -e "s@nobody@%{siproxduser}@" %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
sed -i -e "s@nobody@%{siproxduser}@" %{buildroot}%{_datadir}/%{name}/scripts/%{name}
#
# Directory needs to exist for packaging
%if %suse_version > 1120
mkdir -p %{buildroot}/%{_rundir}/%{name}
%endif

# cleanup
rm -f %{buildroot}/%{_sysconfdir}/siproxd_passwd.cfg
rm -f %{buildroot}/%{_libdir}/%{name}/*.a
rm -rf %{buildroot}/usr/share/doc/%{name}

%post
/sbin/ldconfig
%service_add_post siproxd.service

%pre
%service_add_pre siproxd.service
getent group %{siproxdgroup} >/dev/null || \
	%{_sbindir}/groupadd -r %{siproxdgroup}
getent passwd %{siproxduser} >/dev/null || \
	%{_sbindir}/useradd -r -g %{siproxdgroup} -s /bin/false \
	-c "Siproxd user" -d %{_rundir}/%{name} %{siproxduser}

%postun
%service_del_postun siproxd.service
/sbin/ldconfig

%preun
%service_del_preun siproxd.service

%files
%license COPYING
%doc README AUTHORS ChangeLog syslog-ng.conf.addon
%doc doc/siproxd.conf.example doc/siproxd_passwd.cfg doc/FAQ doc/KNOWN_BUGS doc/sample_*
%attr(0755,root,root) %{_libdir}/%{name}/
%{_sbindir}/rc%name
%{_sbindir}/%name
%{_datadir}/%{name}
%attr(0755,root,root) %{_datadir}/%{name}/scripts/%{name}
%config %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_unitdir}
%{_unitdir}/siproxd.service

%if %suse_version <= 1500
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%endif

%_mandir/man8/%name.8*

%dir %_sysconfdir/%name

%if %suse_version > 1120
 #make rpm know about a directory but do not package it
   %attr(0750,%{siproxduser},root) %ghost %{_rundir}/%{name}
%endif

%files doc
%doc doc/html/* doc/pdf/*

%changelog
