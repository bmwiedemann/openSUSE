#
# spec file for package privoxy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define chroot %{_localstatedir}/lib/privoxy
%if 0%{?suse_version} > 1210
%define with_systemd 1
%else
%define with_systemd 0
%endif
%if %{with_systemd}
%if 0%{?suse_version} < 1230
%define _unitdir /lib/systemd/system
%else
%define _unitdir %{_libexecdir}/systemd/system
%endif
%endif
Name:           privoxy
Version:        3.0.28
Release:        0
Summary:        The Internet Junkbuster - HTTP Proxy Server
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Proxy
Url:            http://www.privoxy.org/
Source:         http://sourceforge.net/projects/ijbswa/files/Sources/%{version}%%20%%28stable%%29/%{name}-%{version}-stable-src.tar.gz
Source2:        %{name}-3.0.16-init.suse
Source3:        %{name}.service
Patch1:         %{name}-3.0.21-config.patch
Patch2:         %{name}-3.0.17-utf8.patch
BuildRequires:  automake
BuildRequires:  pcre-devel
BuildRequires:  w3m
BuildRequires:  zlib-devel
Requires:       cron
Requires:       logrotate
Provides:       ijb = %{version}
Obsoletes:      ijb < %{version}
Provides:       junkbuster = %{version}
Obsoletes:      junkbuster < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with_systemd}
BuildRequires:  systemd
%endif
%if %{with_systemd}
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{_sbindir}/useradd %{_sbindir}/groupadd
%{?systemd_requires}
%else
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %fillup_prereq %insserv_prereq %{_sbindir}/useradd %{_sbindir}/groupadd
%endif
%if %{with_systemd}
Source1:        %{name}.logrotate.systemd
%else
Source1:        %{name}.logrotate
%endif
%if %{with_systemd}
Patch3:         %{name}-3.0.16-networkmanager.systemd.patch
%else
Patch3:         %{name}-3.0.16-networkmanager.patch
%endif

%description
The Internet Junkbuster - HTTP Proxy Server: A non-caching HTTP proxy
server that runs between a web browser and a web server and filters
contents as described in the configuration files.

%package doc
Summary:        The documentation of Privoxy
Group:          Productivity/Networking/Web/Proxy
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
Documentation files for the Privoxy: The Internet Junkbuster - HTTP
Proxy Server. A non-caching HTTP proxy server that runs between a web
browser and a web server and filters contents as described in the
configuration files.

%prep
%setup -q -n privoxy-%{version}-stable
%patch1 -p1
%patch2
%patch3

%build
autoreconf -fiv
%configure --enable-zlib
make %{?_smp_mflags}

%install
%if %{with_systemd}
mkdir -p %{buildroot}/%{_unitdir}
%else
mkdir -p %{buildroot}%{_sysconfdir}/init.d
%endif
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}/%{chroot}/etc
mkdir -p %{buildroot}%{_prefix}/sbin
mkdir -p %{buildroot}/%{chroot}/log
mkdir -p %{buildroot}/%{chroot}%{_localstatedir}/log
mkdir -p %{buildroot}/%{chroot}%{_localstatedir}/run
mkdir -p %{buildroot}/%{chroot}/%{_lib}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d
cp -a templates %{buildroot}/%{chroot}/etc
install -m 644 config *.action *.filter trust %{buildroot}/%{chroot}/etc
%if %{with_systemd}
sed -e 's/@lib@/%{_lib}/g' %{SOURCE3} > %{buildroot}/%{_unitdir}/%{name}.service
%if 0%{?suse_version} >= 1310
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%else
ln -sf /sbin/service %{buildroot}%{_sbindir}/rc%{name}
%endif
%else
install -m 755 %{SOURCE2} %{buildroot}%{_initddir}/privoxyd
ln -sf ../..%{_initddir}/privoxyd %{buildroot}%{_sbindir}/rcprivoxyd
ln -sf ../..%{_initddir}/privoxyd %{buildroot}%{_sbindir}/rcprivoxy
%endif
install -m 755 privoxy %{buildroot}%{_prefix}/sbin
install -m 755 privoxy_nm %{buildroot}%{_sysconfdir}/NetworkManager/dispatcher.d/privoxyd
install -m 644 privoxy.1 %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/privoxy
ln -s ../../log %{buildroot}/%{chroot}%{_localstatedir}/log/privoxy
ln -sf %{chroot}%{_sysconfdir}/ %{buildroot}%{_sysconfdir}/privoxy

%pre
%if %{with_systemd}
mkdir -p %{_localstatedir}/lib/systemd/migrated || :
if test $1 -eq 1; then
  touch %{_localstatedir}/lib/systemd/migrated/%{name} || :
else
  if test ! -e %{_localstatedir}/lib/systemd/migrated/%{name}; then
    # %{_sbindir}/systemd-sysv-convert --save privoxy{d}
    find_service() {
      local runlevel
      runlevel=$1
      priority=-1
      for l in %{_sysconfdir}/rc.d/rc$runlevel.d/*; do
	test -f "$l" || continue
	initscript=$(basename $l)
	case "$initscript" in
	  S??privoxyd) ;;
	  *) continue ;;
	esac
	n="$(echo "$initscript" | cut -b2,3)"
	if [ $n -ge 0 -a $n -le 99 ] &&
	   [ $n -ge $priority ]; then
	  if [ ${n%%?} = 0 ]; then
	    priority=${n#?}
	  else
	    priority=$n
	  fi
	fi
      done
      if test $priority -ge 0; then
	return $priority
      else
	return 255
      fi
    }
    if test -r %{_initddir}/privoxyd; then
      for runlevel in 2 3 4 5; do
	find_service $runlevel
	priority=$?
	if test $priority -lt 255; then
	  printf "%%s\t%%s\t%%s\n" %{name} $runlevel $priority >> %{_localstatedir}/lib/systemd/sysv-convert/database
	fi
      done
    fi
  fi
fi
%endif
%{_sbindir}/groupadd -r privoxy 2> /dev/null ||:
%{_sbindir}/useradd -r -g privoxy -s /bin/false -c "Daemon user for privoxy" \
 -d %{_localstatedir}/lib/privoxy privoxy 2> /dev/null ||:
exit 0

%post
%if %{with_systemd}
%service_add_post %{name}.service
%else
%{fillup_and_insserv privoxyd}
%endif
# create logfiles if missing
for i in ./%{chroot}/log/logfile ./%{chroot}/log/jarfile; do
	if ! test -e $i; then touch $i; chown privoxy: $i; chmod 640 $i ; fi
done
exit 0

%preun
%if %{with_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal privoxyd
%endif

%postun
%if %{with_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update privoxyd
%insserv_cleanup
%endif

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README ChangeLog
%{_sbindir}/privoxy
%{_sysconfdir}/NetworkManager/dispatcher.d/privoxyd
%dir %{_sysconfdir}/NetworkManager
%dir %{_sysconfdir}/NetworkManager/dispatcher.d
%{_mandir}/man1/privoxy.1.gz
%config(noreplace) %{_sysconfdir}/logrotate.d/privoxy
%dir /%{chroot}/etc
%config(noreplace) /%{chroot}%{_sysconfdir}/config
%config(noreplace) /%{chroot}%{_sysconfdir}/trust
%config /%{chroot}%{_sysconfdir}/match-all.action
%config %attr(640,privoxy,root) /%{chroot}%{_sysconfdir}/default.action
%config(noreplace) %attr(640,privoxy,root) /%{chroot}%{_sysconfdir}/user.action
%config(noreplace) /%{chroot}%{_sysconfdir}/*.filter
%dir %{chroot}
%{chroot}%{_sysconfdir}/templates
%dir %attr(770,root,privoxy) %{chroot}/log
%{chroot}/var
%{chroot}/%{_lib}
%{chroot}%{_sysconfdir}/regression-tests.action
%if %{with_systemd}
%{_unitdir}/%{name}.service
%else
%config %{_initddir}/privoxyd
%{_sbindir}/rcprivoxyd
%endif
%{_sbindir}/rcprivoxy
%{_sysconfdir}/privoxy

%files doc
%defattr(-,root,root)
%doc doc/source

%changelog
