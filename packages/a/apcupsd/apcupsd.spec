#
# spec file for package apcupsd
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?suse_version} >= 1550
%{nil}
%else
%bcond_without gapcmon
%endif
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           apcupsd
Version:        3.14.14
Release:        0
Summary:        APC UPS Daemon (Powerful Daemon for APC UPSs)
License:        GPL-2.0-only
Group:          Hardware/UPS
URL:            http://www.apcupsd.com/
Source:         https://sourceforge.net/projects/apcupsd/files/apcupsd%%20-%%20Stable/%{version}/apcupsd-%{version}.tar.gz
Source2:        README.SUSE
Source4:        %{name}.hibernate
Source5:        %{name}.sysconfig
Source6:        %{name}.logrotate
Source7:        apcupsd-httpd.conf
Source8:        https://sourceforge.net/projects/apcupsd/files/apcupsd%%20-%%20Stable/%{version}/apcupsd-%{version}.tar.gz.sig
Source9:        %{name}.keyring
# PATCH-FIX-OPENSUSE apcupsd-suse.patch sbrabec@suse.cz -- Do not perform halt script alternation on install.
Patch0:         apcupsd-suse.patch
# PATCH-FEATURE-OPENSUSE apcupsd-hibernate.patch sbrabec@suse.cz -- Support for hibernation on powerfail.
Patch2:         apcupsd-hibernate.patch
# PATCH-FIX-OPENSUSE apcupsd-3.14.8-systemd.patch p.drouand@gmail.com -- systemd support
Patch11:        apcupsd-3.14.8-systemd.patch
# PATCH-FIX-OPENSUSE apcupsd-3.14.9-fixgui.patch rhbz#578276 p.drouand@gmail.com -- fix crash in gui
Patch13:        apcupsd-3.14.9-fixgui.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libusb-devel
BuildRequires:  mailx
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(gdlib)
Requires:       mailx
Requires(post): %fillup_prereq
Requires(post): grep
Requires(post): sed
Recommends:     logrotate
%{?systemd_requires}
%if 0%{?suse_version} > 1500
BuildRequires:  util-linux-tty-tools
Requires:       util-linux-tty-tools
%endif
%if %{with gapcmon}
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(x11)
%endif

%description
Controls and monitors the status of an APC UPS under Linux. Allows your
computer or server to run for a specified length of time on UPS power
then executes a controlled shutdown in the case of an extended power
failure. Find APC on the Internet at http://www.apc.com/.

APC also made their PowerChute plus available for download at
http://www.apc.com/tools/download/.

%package cgi
Summary:        Web interface for apcupsd
Group:          Hardware/UPS
Requires:       %{name} = %{version}

%description cgi
A CGI interface to the APC UPS monitoring daemon.

%if %{with gapcmon}
%package gui
Summary:        APC UPS Monitor GUI (for APC UPSs)
Group:          Hardware/UPS
Requires:       %{name} = %{version}

%description gui
Controls and monitors the status of an APC UPS under Linux. Allows your
computer or server to run for a specified length of time on UPS power
then executes a controlled shutdown in the case of an extended power
failure. Find APC on the Internet at http://www.apc.com/.

APC also made their PowerChute plus available for download at
http://www.apc.com/tools/download/.
%endif

%prep
%autosetup -p1
cp -a %{SOURCE2} %{SOURCE4} .

%build
%configure \
	--sysconfdir=%{_sysconfdir}/%{name} \
	--with-libwrap \
	--with-lock-dir=%{_localstatedir}/lock \
	SHUTDOWN=%{_sbindir}/shutdown \
%if %{with gapcmon}
	--enable-gapcmon \
%else
	--disable-gapcmon \
%endif
	--enable-cgi \
	--enable-usb \
	--enable-modbus-usb \
	--enable-test \
	--with-cgi-bin=%{apache_serverroot}/cgi-bin \
%if 0%{?suse_version}
	--with-distname=suse \
%endif
        %{nil}
make %{?_smp_mflags}

%install
%make_install
install -m744 platforms/apccontrol \
              %{buildroot}%{_sysconfdir}/%{name}/apccontrol
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}
%if %{with gapcmon}
%suse_update_desktop_file gapcmon
chmod 644 %{buildroot}/%{_datadir}/pixmaps/*.png
%endif
# Cleanup for later doc macro processing
chmod -x examples/*.c
rm examples/*.in
find examples users_guide -type f | xargs chmod 644
# fix end-of-line encoding
dos2unix -o examples/status/SmartUPS-vs-650.status examples/snoopdecode.c examples/rpt/Smart-UPS-1500.rpt \
	examples/rpt/Back-UPS-ES-550.rpt examples/rpt/Back-UPS-CS-650.rpt examples/rpt/Back-UPS-BR-800.rpt
# hid-ups.rpt is duplicate by BackUPS.rpt
%fdupes -s examples/rpt/

rm -r %{buildroot}/%{_datadir}/hal
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-sleep
sed "s:@PWRFAILDIR@:%{_sysconfdir}/%{name}:g" <%{name}.hibernate >%{buildroot}%{_prefix}/lib/systemd/system-sleep/apcupsd.sh
chmod +x %{buildroot}%{_prefix}/lib/systemd/system-sleep/apcupsd.sh

mkdir -p %{buildroot}%{_fillupdir}
cp %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.%{name}

# systemd support and remove initd support for opensuse 12.2 and higher
install -p -D -m644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m755 %{name}_shutdown %{buildroot}%{_prefix}/lib/systemd/system-shutdown/%{name}_shutdown
rm %{buildroot}%{_initddir}/%{name}

install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -m0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -d %{buildroot}%{_sysconfdir}/apache2/conf.d/
install -m0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/apache2/conf.d/%{name}.conf

%pre
%service_add_pre %{name}.service

%post
%fillup_only
%service_add_post %{name}.service
# Remove HALT_POWERDOWN_INSERT, it is not needed with systemd (it was last time filled in 13.1).
# We need to handle only the last form, which was already used in SLE11.
if test -f etc/sysconfig/shutdown ; then
  if usr/bin/grep -q '^HALT_POWERDOWN_INSERT=' etc/sysconfig/shutdown ; then
    if ! usr/bin/grep -q '^HALT_POWERDOWN_INSERT=""' etc/sysconfig/shutdown ; then
      if usr/bin/grep -q '^HALT_POWERDOWN_INSERT="%{_sysconfdir}/init\.d/apcupsd try-powerdown"' etc/sysconfig/shutdown ; then
        usr/bin/sed -i 's:^\(HALT_POWERDOWN_INSERT="\)%{_sysconfdir}/init\.d/apcupsd try-powerdown":\1":' etc/sysconfig/shutdown
      else
        echo >&2 "apcupsd: WARNING: Unknown value of HALT_POWERDOWN_INSERT in %{_sysconfdir}/sysconfig/shutdown."
        echo >&2 "         Keeping unchanged. If it still exists, it should be:"
        echo >&2 "HALT_POWERDOWN_INSERT=\"\""
      fi
    fi
  fi
fi
# User installed file, by default in docdir. Not needed any more, and will never be.
rm -f etc/init.d/apcupsd-early-powerdown

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc ChangeLog examples ReleaseNotes README.SUSE
%{_sbindir}/%{name}
%{_sbindir}/apcaccess
%{_sbindir}/apctest
%{_sbindir}/smtp
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_systemd_util_dir}/system-shutdown/
%{_systemd_util_dir}/system-sleep/
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/changeme
%config(noreplace) %{_sysconfdir}/%{name}/commfailure
%config(noreplace) %{_sysconfdir}/%{name}/commok
%config(noreplace) %{_sysconfdir}/%{name}/onbattery
%config(noreplace) %{_sysconfdir}/%{name}/offbattery
%config(noreplace) %{_sysconfdir}/logrotate.d/apcupsd
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0755,root,root) %{_sysconfdir}/%{name}/apccontrol
%{_mandir}/man?/*.*
%{_fillupdir}/sysconfig.%{name}

%if %{with gapcmon}
%files gui
%{_bindir}/gapcmon
%{_datadir}/applications/gapcmon.desktop
%{_datadir}/pixmaps/*.png
%endif

%files cgi
%config(noreplace) %{_sysconfdir}/apache2/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.css
%config(noreplace) %{_sysconfdir}/%{name}/hosts.conf
%config(noreplace) %{_sysconfdir}/%{name}/multimon.conf
%{apache_serverroot}/cgi-bin/multimon.cgi
%{apache_serverroot}/cgi-bin/upsfstats.cgi
%{apache_serverroot}/cgi-bin/upsstats.cgi
%{apache_serverroot}/cgi-bin/upsimage.cgi

%changelog
