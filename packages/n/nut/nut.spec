#
# spec file for package nut
#
# Copyright (c) 2024 SUSE LLC
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


%define CGIPATH		%{apache_serverroot}/cgi-bin/%{name}
%define HTMLPATH	%{apache_serverroot}/htdocs/%{name}
%define MODELPATH	%{_libexecdir}/ups/driver
%define STATEPATH	%{_localstatedir}/lib/ups
%define CONFPATH	%{_sysconfdir}/ups
%define PIDPATH 	%{_rundir}
%define NUT_USER	upsd
%define NUT_GROUP	daemon
%define LBRACE		(
%define RBRACE		)
%define QUOTE		"
%define BACKSLASH	\\
# Collect all devices listed in ups-nut-device.fdi:
%define USBHIDDRIVERS    %(zcat %{SOURCE0} | tr a-z A-Z | grep -a -A1 USBHID-UPS | sed -n 's/.*ATTR{IDVENDOR}==%{QUOTE}%{BACKSLASH}%{LBRACE}[^%{QUOTE}]*%{BACKSLASH}%{RBRACE}%{QUOTE}, ATTR{IDPRODUCT}==%{QUOTE}%{BACKSLASH}%{LBRACE}[^%{QUOTE}]*%{BACKSLASH}%{RBRACE}%{QUOTE}, MODE=.*/modalias%{LBRACE}usb:v%{BACKSLASH}1p%{BACKSLASH}2d*dc*dsc*dp*ic*isc*ip*%{RBRACE}/p' | tr '%{BACKSLASH}n' ' ')
%define USBNONHIDDRIVERS %(zcat %{SOURCE0} | tr a-z A-Z | grep -a -A1 _USB       | sed -n 's/.*ATTR{IDVENDOR}==%{QUOTE}%{BACKSLASH}%{LBRACE}[^%{QUOTE}]*%{BACKSLASH}%{RBRACE}%{QUOTE}, ATTR{IDPRODUCT}==%{QUOTE}%{BACKSLASH}%{LBRACE}[^%{QUOTE}]*%{BACKSLASH}%{RBRACE}%{QUOTE}, MODE=.*/modalias%{LBRACE}usb:v%{BACKSLASH}1p%{BACKSLASH}2d*dc*dsc*dp*ic*isc*ip*%{RBRACE}/p' | tr '%{BACKSLASH}n' ' ')
%define systemdsystemdutildir %(pkg-config --variable=systemdutildir systemd)
%define bashcompletionsdir %(pkg-config bash-completion --variable=completionsdir)
%bcond_with texdoc
%if 0%{?suse_version} >= 1500
%bcond_without libi2c
%else
%bcond_with libi2c
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%bcond_without libmodbus
%else
%bcond_with libmodbus
%endif
%if 0%{?suse_version} == 1500
%bcond_without libnsl
%else
%bcond_with libnsl
%endif
%ifarch %{ix86} x86_64 ia64
%bcond_without libfreeipmi
%else
%bcond_with libfreeipmi
%endif
Name:           nut
Version:        2.8.2
Release:        0
Summary:        Network UPS Tools Core (Uninterruptible Power Supply Monitoring)
License:        GPL-2.0-or-later
Group:          Hardware/UPS
URL:            https://www.networkupstools.org/
Source0:        https://github.com/networkupstools/nut/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/networkupstools/nut/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:        README.SUSE
Source3:        nut.rpmlintrc
Source4:        nut.keyring
Source6:        nut.system-sleep
Patch0:         nut-preconfig.patch
Patch1:         nut-notifyflag.patch
# PATCH-FEATURE-OPENSUSE nut-doc-fixed-date.patch sbrabec@suse.cz -- Make doc builds reproducible.
Patch2:         nut-doc-fixed-date.patch
Patch10:        harden_nut-driver.service.patch
Patch11:        harden_nut-monitor.service.patch
Patch12:        harden_nut-server.service.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libcppunit-devel
BuildRequires:  libtool
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libgpiod) >= 1.0.0
BuildRequires:  pkgconfig(libpowerman)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(udev)
Requires:       logrotate
Requires:       usbutils
Requires(post): udev
# Package provides driver for USB HID UPSes, but people can live with hal addon:
Enhances:       %{USBHIDDRIVERS}
# Package provides the only avalailable driver for other USB UPSes:
Supplements:    %{USBNONHIDDRIVERS}
# for update from openSUSE <= 11.3, SLE <= 11
Provides:       nut-classic = %{version}
Obsoletes:      nut-classic < %{version}
Obsoletes:      nut-hal < %{version}
%{?systemd_requires}
%if %{with libfreeipmi}
BuildRequires:  pkgconfig(libfreeipmi)
%endif
%if %{with libi2c}
BuildRequires:  libi2c0-devel
%endif
%if %{with libmodbus}
BuildRequires:  pkgconfig(libmodbus)
%endif
%if %{with libnsl}
BuildRequires:  pkgconfig(libnsl)
%endif
%if %{with texdoc}
BuildRequires:  asciidoc-latex-backend
%else
# Obsolete all the docu stuff with disabled tex dependencies
Obsoletes:      %{name}-devel-doc-pdf <= %{version}
Obsoletes:      %{name}-doc-pdf <= %{version}
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  source-highlight
Requires(pre):  user(upsd)
%endif

%description
Core package of Network UPS Tools.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package drivers-net
Summary:        Network UPS Tools - Extra Networking Drivers (for Network Monitoring)
Group:          Hardware/UPS
Requires:       %{name} = %{version}
Enhances:       %{name}

%description drivers-net
Networking drivers for the Network UPS Tools. You will need them
together with nut to provide UPS networking support.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package -n libnutclient2
Summary:        Network UPS Tools Library (Uninterruptible Power Supply Monitoring)
Group:          System/Libraries
Conflicts:      libupsclient1

%description -n libnutclient2
Shared library for the Network UPS Tools.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package -n libnutscan2
Summary:        Network UPS Tools Library (Uninterruptible Power Supply Monitoring)
Group:          System/Libraries
Conflicts:      libupsclient1

%description -n libnutscan2
Shared library for the Network UPS Tools.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package -n libupsclient6
Summary:        Network UPS Tools Library (Uninterruptible Power Supply Monitoring)
Group:          System/Libraries
Conflicts:      libupsclient1

%description -n libupsclient6
Shared library for the Network UPS Tools.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package -n libnutclientstub1
Summary:        Network UPS Tools Library (Uninterruptible Power Supply Monitoring)
Group:          System/Libraries
Conflicts:      libupsclient1

%description -n libnutclientstub1
Shared library for the Network UPS Tools.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package cgi
Summary:        Network UPS Tools Web Server Support (UPS Status Pages)
Group:          Hardware/UPS
Requires:       %{name} = %{version}
Enhances:       %{name}
Supplements:    (%{name} and apache2)

%description cgi
Web server support package for the Network UPS Tools.

Predefined URL is http://localhost/nut/index.html

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package devel
Summary:        Network UPS Tools (Uninterruptible Power Supply Monitoring)
Group:          Development/Libraries/C and C++
Requires:       libnutclient2 = %{version}-%{release}
Requires:       libnutclientstub1 = %{version}-%{release}
Requires:       libnutscan2 = %{version}-%{release}
Requires:       libupsclient6 = %{version}-%{release}
Requires:       pkgconfig(openssl)

%description devel
Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package doc-asciidoc
Summary:        Network UPS Tools - Documentation in AsciiDoc Format
Group:          Documentation/Other
Requires:       %{name}-doc-images = %{version}
Recommends:     %{name} = %{version}
Enhances:       %{name}
BuildArch:      noarch

%description doc-asciidoc
NUT manuals in AsciiDoc format (human readable source).

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package devel-doc-html
Summary:        Network UPS Tools - Documentation in HTML
# For CSS files:
Group:          Documentation/HTML
Requires:       %{name}-doc-html = %{version}
Requires:       %{name}-doc-images = %{version}
Recommends:     %{name} = %{version}
Enhances:       %{name}
BuildArch:      noarch

%description devel-doc-html
Developer manual in HTML format.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package doc-html
Summary:        Network UPS Tools - Documentation in HTML
Group:          Documentation/HTML
Requires:       %{name}-doc-images = %{version}
Recommends:     %{name} = %{version}
Enhances:       %{name}
BuildArch:      noarch

%description doc-html
User manual in HTML format.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package doc-images
Summary:        Network UPS Tools - Images for Documentation
Group:          Documentation/Other
Requires:       %{name}-doc-images = %{version}
Recommends:     %{name} = %{version}
Enhances:       %{name}
BuildArch:      noarch

%description doc-images
Images for the documentation. It is a supplementary package for some NUT
documentation packages.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%if %{with texdoc}
%package doc-pdf
Summary:        Network UPS Tools - Documentation in PDF
Group:          Documentation/Other
Recommends:     %{name} = %{version}
Enhances:       %{name}
BuildArch:      noarch

%description doc-pdf
User manual in PDF format.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package devel-doc-pdf
Summary:        Network UPS Tools - Documentation in PDF
Group:          Documentation/Other
Recommends:     %{name} = %{version}
Enhances:       %{name}
BuildArch:      noarch

%description devel-doc-pdf
Developer manual in PDF format.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.
%endif

%prep
%autosetup -p1
cp -a %{SOURCE2} .
sed -i s/@now@/`date -r ChangeLog +%%Y-%%m-%%d`/g docs/docinfo.xml.in

%build
autoreconf -fvi
%configure \
	--disable-static \
	--sysconfdir=%{CONFPATH} \
	--datadir=%{_datadir}/%{name} \
	--with-all \
%if %{with texdoc}
	--with-doc="man html-single html-chunked pdf" \
%else
	--with-doc="man html-single html-chunked" \
%endif
	--with-ssl \
	--with-openssl \
	--without-nss \
%if %{without libmodbus}
	--without-modbus \
%endif
%if %{with libnsl}
	--with-wrap \
%endif
%if %{without libfreeipmi}
	--without-ipmi \
%endif
%if %{without libi2c}
	--without-i2c
%endif
	--with-htmlpath=%{HTMLPATH} \
	--with-cgipath=%{CGIPATH} \
	--with-statepath=%{STATEPATH} \
	--with-drvpath=%{MODELPATH} \
	--with-pidpath=%{PIDPATH} \
	--with-user=%{NUT_USER} \
	--with-group=%{NUT_GROUP} \
	--with-udev-dir=%{_udevrulesdir}/.. \
	--enable-option-checking=fatal

# does not create reproducible output with parallelism
%make_build -j1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{STATEPATH}
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_sbindir}

# initscript
ln -s service %{buildroot}%{_sbindir}/rcnut-driver
ln -s service %{buildroot}%{_sbindir}/rcnut-server
ln -s service %{buildroot}%{_sbindir}/rcnut-monitor
rename .sample "" %{buildroot}%{_sysconfdir}/ups/*.sample

install -D -m 750 %{SOURCE6} %{buildroot}%{systemdsystemdutildir}/system-sleep/%{name}.sh
install -D -m 644 scripts/logrotate/nutlogd %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -m 644 scripts/misc/nut.bash_completion %{buildroot}%{bashcompletionsdir}/%{name}

# Documentation
cp -a docs/*.txt docs/cables docs/images %{buildroot}%{_docdir}/%{name}/
cp -a docs/*.css docs/*.html %{buildroot}%{_docdir}/%{name}/
%if %{with texdoc}
cp -a docs/*.pdf %{buildroot}%{_docdir}/%{name}/
%endif

# Not needed for packaged contents:
rm -f %{buildroot}%{_docdir}/%{name}/packager-guide.*
rm -f %{buildroot}%{_docdir}/%{name}/cables/Makefile*
rm -f %{buildroot}%{_docdir}/%{name}/cables/*.txt-prepped

# Create symlinks for man pages
%fdupes -s %{buildroot}%{_mandir}

%pre
%if 0%{?suse_version} < 1330
getent passwd %{NUT_USER} >/dev/null || useradd -r -g %{NUT_GROUP} -s /bin/false -c "UPS daemon" -d /sbin %{NUT_USER} 2>/dev/null
%endif
%service_add_pre nut-server.service nut-monitor.service nut-driver-enumerator.path nut-driver-enumerator.service nut-driver.target nut.target

%post
# Generate initial passwords.
if grep -q "password = @UPSD_INITIAL_MASTER_PASSWORD@" %{CONFPATH}/upsmon.conf %{CONFPATH}/upsd.users; then
  UPSD_INITIAL_MASTER_PASSWORD=$(head -c 20 /dev/urandom | md5sum | head -c 10)
  sed -i s/@UPSD_INITIAL_MASTER_PASSWORD@/$UPSD_INITIAL_MASTER_PASSWORD/ %{CONFPATH}/upsmon.conf %{CONFPATH}/upsd.users
fi
if grep -q "password = @UPSD_INITIAL_SLAVE_PASSWORD@" %{CONFPATH}/upsd.users ; then
  UPSD_INITIAL_SLAVE_PASSWORD=$(head -c 20 /dev/urandom | md5sum | head -c 10)
  sed -i s/@UPSD_INITIAL_SLAVE_PASSWORD@/$UPSD_INITIAL_SLAVE_PASSWORD/ %{CONFPATH}/upsd.users
fi
# Migrate Suspend to Disc to the new convention (bnc#449861 and later bnc#871406):
# It was never on by default, but documentation up to 11.0 recommends
# "shutdown -z +0" for suspend to disc. It was discontinued before 11.0.
# Documentation since 11.0 up to 13.1 recommends /powersave -U.
# pm-utils (and powersave) were obsoleted after 13.1 in favor of systemd.
if grep "shutdown -z +0" %{_sysconfdir}/ups/upsmon.conf ; then
  sed -i 's:/sbin/shutdown -z +0:%{_bindir}/systemctl hibernate:;s:shutdown -z +0:%{_bindir}/systemctl hibernate:' %{_sysconfdir}/ups/upsmon.conf
fi
if grep "powersave -U" %{_sysconfdir}/ups/upsmon.conf ; then
  sed -i 's:%{_bindir}/powersave -U:%{_bindir}/systemctl hibernate:;s:powersave -U:%{_bindir}/systemctl hibernate:' %{_sysconfdir}/ups/upsmon.conf
fi
# And finally trigger udev to set permissions according to newly installed rules files.
udevadm trigger --subsystem-match=usb --property-match=DEVTYPE=usb_device
%service_add_post nut-server.service nut-monitor.service nut-driver-enumerator.path nut-driver-enumerator.service nut-driver.target nut.target
%tmpfiles_create %{_tmpfilesdir}/%{name}-common-tmpfiles.conf

%preun
%service_del_preun nut-server.service nut-monitor.service nut-driver-enumerator.path nut-driver-enumerator.service nut-driver.target nut.target

%postun
%service_del_postun nut-server.service nut-monitor.service nut-driver-enumerator.path nut-driver-enumerator.service nut-driver.target nut.target

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%ldconfig_scriptlets -n libnutclient2
%ldconfig_scriptlets -n libnutclientstub1
%ldconfig_scriptlets -n libnutscan2
%ldconfig_scriptlets -n libupsclient6
%else
%post   -n libnutclient2 -p /sbin/ldconfig
%postun -n libnutclient2 -p /sbin/ldconfig
%post   -n libnutclientstub1 -p /sbin/ldconfig
%postun -n libnutclientstub1 -p /sbin/ldconfig
%post   -n libnutscan2 -p /sbin/ldconfig
%postun -n libnutscan2 -p /sbin/ldconfig
%post   -n libupsclient6 -p /sbin/ldconfig
%postun -n libupsclient6 -p /sbin/ldconfig
%endif

%files
%doc AUTHORS ChangeLog MAINTAINERS NEWS.adoc README.adoc README.SUSE UPGRADING.adoc
%license COPYING
%config %{_sysconfdir}/logrotate.d/*
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man5/*%{ext_man}
%{_mandir}/man8/*%{ext_man}
%exclude %{_mandir}/man8/netxml-ups*.*
%exclude %{_mandir}/man8/snmp-ups*.*
%dir %{_libexecdir}/ups
%{_libexecdir}/nut-driver-enumerator.sh
%python_sitearch/PyNUT.py
%{_sbindir}/*
%{_udevrulesdir}/*.rules
%config(noreplace) %{CONFPATH}/hosts.conf
%config(noreplace) %attr(600,%{NUT_USER},root) %{CONFPATH}/upsd.conf
%config(noreplace) %attr(600,%{NUT_USER},root) %{CONFPATH}/upsd.users
%config(noreplace) %attr(600,%{NUT_USER},root) %{CONFPATH}/upsmon.conf
%dir %{CONFPATH}
%config(noreplace) %{CONFPATH}/nut.conf
%config(noreplace) %{CONFPATH}/ups.conf
%config(noreplace) %{CONFPATH}/upsset.conf
%config(noreplace) %{CONFPATH}/upssched.conf
%dir %{MODELPATH}
%{MODELPATH}/*
%exclude %{MODELPATH}/snmp-ups
%exclude %{MODELPATH}/netxml-ups
%dir %attr(700,%{NUT_USER},%{NUT_GROUP}) %{STATEPATH}
%{_unitdir}/*.path
%{_unitdir}/*.target
%{_unitdir}/*.service
%{systemdsystemdutildir}/system-shutdown/*
%{systemdsystemdutildir}/system-sleep/%{name}.sh
%{bashcompletionsdir}/*
%{_tmpfilesdir}/%{name}-common-tmpfiles.conf
%ghost %{_rundir}/%{name}
%ghost %attr(700,%{NUT_USER},%{NUT_GROUP}) %{STATEPATH}/upssched

%files drivers-net
%{MODELPATH}/snmp-ups
%{MODELPATH}/netxml-ups
%{_mandir}/man8/netxml-ups*%{ext_man}
%{_mandir}/man8/snmp-ups*%{ext_man}

%files -n libnutclient2
%{_libdir}/libnutclient.so.*

%files -n libnutclientstub1
%{_libdir}/libnutclientstub.so.*

%files -n libnutscan2
%{_libdir}/libnutscan.so.*

%files -n libupsclient6
%{_libdir}/libupsclient.so.*

%files cgi
%{CGIPATH}
%{HTMLPATH}
%config(noreplace) %{CONFPATH}/upsstats-single.html
%config(noreplace) %{CONFPATH}/upsstats.html

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libexecdir}/sockdebug
%{_mandir}/man3/*%{ext_man}
%python_sitearch/test_nutclient.py

%files doc-asciidoc
%doc %dir %{_docdir}/%{name}{,/cables}
%{_docdir}/%{name}/*.txt
%{_docdir}/%{name}/cables/*.txt

%files devel-doc-html
%{_docdir}/%{name}/developer-guide.html

%files doc-html
%{_docdir}/%{name}/ChangeLog.html
%{_docdir}/%{name}/FAQ.html
%{_docdir}/%{name}/cables.html
%{_docdir}/%{name}/release-notes.html
%{_docdir}/%{name}/solaris-usb.html
%{_docdir}/%{name}/user-manual.html
%{_docdir}/%{name}/*.css

%files doc-images
%doc %dir %{_docdir}/%{name}
%{_docdir}/%{name}/images

%if %{with texdoc}
%files doc-pdf
%doc %dir %{_docdir}/%{name}
%{_docdir}/%{name}/FAQ.pdf
%{_docdir}/%{name}/cables.pdf
%{_docdir}/%{name}/solaris-usb.pdf
%{_docdir}/%{name}/user-manual.pdf

%files devel-doc-pdf
%doc %dir %{_docdir}/%{name}
%{_docdir}/%{name}/developer-guide.pdf
%endif

%changelog
