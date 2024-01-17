#
# spec file for package conman
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


#
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} > 1140
%define have_systemd 1
 %ifarch x86_64
  %define have_freeipmi 1
 %endif
%endif

%if 0%{?have_systemd}
 %if 0%{?sle_version} >= 150000 || 0%{?is_opensuse}
  %define conmandir conman/
  %define conman_g %name
  %define conman_u %name
  %define have_sysuser 1
 %else
  %define conman_g root
  %define conman_u root
 %endif
%else
 %define conman_g root
 %define conman_u daemon
%endif

Name:           conman
Version:        0.3.1
Release:        0

Summary:        The Console Manager
License:        GPL-3.0-or-later
Group:          System/Console
URL:            http://dun.github.io/conman/

Requires:       expect
Requires:       logrotate

BuildRequires:  tcpd-devel
%if 0%{?have_freeipmi}
BuildRequires:  freeipmi-devel
%endif
Source0:        https://github.com/dun/conman/archive/%{name}-%{version}.tar.gz
Source1:        %{name}.service.in
%if 0%{?have_systemd}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
%{?have_sysuser:BuildRequires:  sysuser-tools}
%{?systemd_requires}
Requires(pre):  shadow
Requires(post): %fillup_prereq sed
Requires(postun):coreutils
%endif

Patch1:         conman-suse-fix-expect-scripts.patch

# 8/15/14 karl.w.schulz@intel.com - include prereq
%if 0%{?sles_version} || 0%{?suse_version}
PreReq:         %{fillup_prereq}
%endif

%description
ConMan is a serial console management program designed to support a large
number of console devices and simultaneous users.  It supports:
  - local serial devices
  - remote terminal servers (via the telnet protocol)
  - IPMI Serial-Over-LAN (via FreeIPMI)
  - Unix domain sockets
  - external processes (eg, using Expect for telnet/ssh/ipmi-sol connections)

Its features include:
  - logging (and optionally timestamping) console device output to file
  - connecting to consoles in monitor (R/O) or interactive (R/W) mode
  - allowing clients to share or steal console write privileges
  - broadcasting client output to multiple consoles

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch1 -p1

%build
./bootstrap
%configure --with-tcp-wrappers \
%if 0%{?have_freeipmi}
           --with-freeipmi \
%endif

make %{?_smp_mflags}

%install
%make_install

%if 0%{?have_systemd}
mkdir -p %{buildroot}%{_unitdir}
sed -e "s/@conman_u@/%conman_u/" -e "s/@conman_g@/%conman_g/" <%{SOURCE1} >%{buildroot}%{_unitdir}/%{name}.service
chmod 0644 %{buildroot}%{_unitdir}/%{name}.service
rm -rf %{buildroot}%{_sysconfdir}/init.d
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcconman
%else
awk "/END INIT INFO/ { print \"# Default-Start:  3 5\"; } {print;}" \
    %{buildroot}%_sysconfdir/init.d/conman > %{buildroot}%_sysconfdir/init.d/conman.tmp
mv %{buildroot}%_sysconfdir/init.d/conman.tmp %{buildroot}%_sysconfdir/init.d/conman
ln -s %{_sysconfdir}/init.d/conman %{buildroot}%{_sbindir}/rcconman
chmod u+x %{buildroot}%{_sysconfdir}/init.d/conman
%endif
mkdir -p %{buildroot}%{_fillupdir}
mv etc/conman.sysconfig \
    %{buildroot}%{_fillupdir}/sysconfig.conman
for i in $(find %{buildroot}/usr/share/conman) ; do
  if [ -f $i -a -x $i ]; then
     if ! head -1 $i | grep "^#!"; then
	 echo "#!/usr/bin/expect -f" > /tmp/$(basename $i)
	 cat $i >> /tmp/$(basename $i)
         mv /tmp/$(basename $i) $i
	 chmod 0755 $i
     fi
  fi
done
sed -i -e '1 s@#!.*/bin/env perl@#!%{_bindir}/perl@' \
    %{buildroot}%{_bindir}/conmen

%if 0%{?conmandir:1}
mkdir -p %{buildroot}%{_tmpfilesdir}
cat >> %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
d %_localstatedir%_rundir/%{name} 0755 %{conman_u} %{conman_g} -
EOF
mkdir -p %{buildroot}%{_localstatedir}/log/%{?conmandir}
%endif
if ! grep "^SERVER" %{buildroot}/etc/conman.conf > /dev/null; then
    cat <<EOF >> %{buildroot}/etc/conman.conf
SERVER keepalive=ON
SERVER logdir="/var/log/%{?conmandir}"
SERVER logfile="/var/log/%{?conmandir}conman.log"
SERVER loopback=ON
SERVER pidfile="/var/run/%{?conmandir}conman.pid"
SERVER tcpwrappers=ON
SERVER timestamp=1h
GLOBAL seropts="115200,8n1"
GLOBAL log="console.%N"
GLOBAL logopts="sanitize,timestamp"
EOF
fi
%if 0%{?have_sysuser}
%define user_home %_localstatedir%_rundir/%{?conmandir}
%define user_descr Connection Manager service
echo -en "u %conman_u - \"%user_descr\" %user_home\nm %conman_u dialout\n" > system-user-%{name}.conf
%sysusers_generate_pre system-user-%{name}.conf %{name} system-user-%{name}.conf
install -D -m 644 system-user-%{name}.conf %{buildroot}%{_sysusersdir}/system-user-%{name}.conf
%endif

%if 0%{?have_systemd}
%pre %{?have_sysuser:-f %{name}.pre}
%service_add_pre conman.service
%endif

%preun
%if 0%{?have_systemd}
%service_del_preun conman.service
%else
%{stop_on_removal conman}
%endif

%post
%define migrated conman_user_migrated
%fillup_only conman
%if 0%{?have_systemd}
%{?tmpfiles_create:%{tmpfiles_create %{_tmpfilesdir}/%{name}.conf}}
%service_add_post conman.service
[ -d %_localstatedir/lib/conman ] || mkdir %_localstatedir/lib/conman || :
if [ $1 -eq 2 -a ! -e %_localstatedir/lib/conman/%migrated ]; then
    tmpfile=$(mktemp /tmp/tmp-XXXX)
    sed  -e "s@^\(server\)\|\(SERVER\) \+logdir=.*@SERVER logdir=\"/var/log/%{?conmandir}\"@" \
	-e "s@^\(server\)\|\(SERVER\) \+logfile=.*@SERVER logfile=\"/var/log/%{?conmandir}conman.log\"@" \
	-e "s@^\(server\)\|\(SERVER\) \+pidfile=.*@SERVER pidfile=\"/var/run/%{?conmandir}conman.pid\"@" \
	< /etc/conman.conf > $tmpfile
    if ! cmp /etc/conman.conf $tmpfile; then
	mv /etc/conman.conf /etc/conman.conf.rpmsave
	mv $tmpfile /etc/conman.conf
	chown %conman_u:%conman_g /etc/conman.conf
	cat > %_localstatedir/adm/update-messages/%{name}-%{version}-%{release}-%{name}.txt <<EOF

The conman configuration in %_sysconfdir/conman.conf has been updated to the new pid and log
directory. Please check this file to make sure it is correct. The original version is available
in /etc/conman.conf.rpmsave.
EOF
    else
	rm $tmpfile
    fi
fi
touch %_localstatedir/lib/conman/%migrated || :
%endif

%postun
%if 0%{?have_systemd}
[ $1 -eq 0 ] && rm -rf %_localstatedir/lib/conman
%service_del_postun conman.service
%else
%{restart_on_update conman}
%endif

%if 0%{?sle_version} > 120200 || 0%{?suse_version} > 1320
%define files_license %license
%else
%define files_license %doc
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS
%doc DISCLAIMER*
%doc FAQ
%files_license COPYING
%doc NEWS
%doc README
%doc PLATFORMS
%doc README.md
%doc THANKS
%config(noreplace) %attr(-,%conman_u,%conman_g) %{_sysconfdir}/conman.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/conman
%if 0%{?conmandir:1}
%dir %attr(-,%conman_u,%conman_g) %{_localstatedir}/log/conman
%{_tmpfilesdir}/%{name}.conf
%endif
%{_fillupdir}/sysconfig.conman
%{_bindir}/*
%{_sbindir}/*
%{_prefix}/share/conman
%if 0%{?have_systemd}
%{_prefix}/lib/systemd/*
%else
%{_sysconfdir}/init.d/*
%endif
%{_mandir}/*/*
%{?have_sysuser:%{_sysusersdir}/system-user-%{name}.conf}

%changelog
