#
# spec file for package thttpd
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


%define serverroot /srv/www
%if 0%{?suse_version} > 1220
%define with_systemd 1
%else
%define with_systemd 0
%endif
Name:           thttpd
Version:        2.29
Release:        0
Summary:        Small and simple webserver
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Servers
URL:            http://www.acme.com/software/thttpd/
Source:         http://www.acme.com/software/thttpd/%{name}-%{version}.tar.gz
Source1:        %{name}-initd.script
Source2:        %{name}.service
Source3:        %{name}.logrotate
Source4:        %{name}.conf
Patch0:         %{name}-2.25b-configure.patch
Patch1:         %{name}-2.25b-dirs.patch
Patch2:         %{name}-2.25b-time_h.patch
Patch3:         %{name}-2.25b-newautoconf.patch
Patch4:         %{name}-2.25b-sec.patch
Patch5:         %{name}-2.25b-static.patch
Patch6:         %{name}-2.25b-pie.patch
Patch7:         %{name}-2.25b-syslogtocern.diff
Patch8:         %{name}-2.25b-overflow.diff
Patch9:         %{name}-2.25b-chown.diff
Patch10:        %{name}-2.25b-zerolen.patch
# PATCH-FIX-SUSE CVE-2012-5640
Patch13:        thttpd-2.25b-CVE-2012-5640-check_crypt_return_value.patch
Patch14:        thttpd-CVE-2013-0348.patch
Patch15:        thttpd-crypt_is_in_crypt.h.patch
BuildRequires:  automake
BuildRequires:  libtool
Requires(post): permissions
Requires:       group(www)
Recommends:     logrotate
# both packages provide /srw/www/htdocs/index.html
Conflicts:      apache2-example-pages
# both packages provide /usr/bin/htpasswd
Conflicts:      apache2-utils
Provides:       http_daemon
%if %{with_systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%else
Requires(post): %fillup_prereq
Requires(post): %insserv_prereq
%endif

%description
Thttpd is a compact httpd serving daemon that can handle
high loads. While lacking many of the advanced features of Roxen
or Apache, thttpd operates without forking and is efficient
in memory use. Basic support for CGI scripts, authentication, and SSI
is provided. Advanced features include the ability to throttle
traffic.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10
%patch13 -p1
%patch14 -p1
%patch15 -p1

%build
cp %{_datadir}/automake-1.*/config.* .
mv aclocal.m4 acinclude.m4
libtoolize --force
aclocal --force
autoconf -f
export V_CCOPT="%{optflags} -fPIC -DPIC -fPIE"
export CFLAGS="%{optflags} -fPIC -DPIC -fPIE"
export LDFLAGS="-pie -Wl,-z,relro,-z,now"
%configure
# parallel build causes problems, single thread build takes only 10s anyway
make -j1

%install
install -d %{buildroot}%{_bindir} \
    %{buildroot}%{_sbindir} \
    %{buildroot}%{_mandir}/man1 \
    %{buildroot}%{_mandir}/man8 \
    %{buildroot}%{serverroot}/htdocs/users
%make_install
install -D -m0644 index.html %{buildroot}/%{serverroot}/htdocs/index.html
install -D -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}.conf
install -D -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%if %{with_systemd}
install -D -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%else
install -D -m0644 %{SOURCE1} %{buildroot}%{_initddir}/%{name}
ln -s %{buildroot}%{_initddir}/%{name} %{buildroot}%{_sbindir}/rc%{name}
%endif

%if %{with_systemd}
%pre
%service_add_pre %{name}.service
%endif

%post
%if %{with_systemd}
%service_add_post %{name}.service
%else
%{fillup_and_insserv thttpd}
%endif
%set_permissions %{_bindir}/makeweb

%verifyscript
%verify_permissions -e %{_bindir}/makeweb

%preun
%if %{with_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal thttpd
%endif

%postun
%if %{with_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update thttpd
%insserv_cleanup
%endif

%files
%doc README config.h
%{serverroot}/htdocs/*
%attr(775, root, www) %{serverroot}/htdocs/users
%verify(not mode) %attr(2751, root, www) %{_bindir}/makeweb
%{_bindir}/htpasswd
%{_sbindir}/*
%{_mandir}/*/*
%config %{_sysconfdir}/logrotate.d/%{name}
%if %{with_systemd}
%{_unitdir}/%{name}.service
%else
%config %{_initddir}/thttpd
%endif
%config(noreplace) %{_sysconfdir}/thttpd.conf

%changelog
