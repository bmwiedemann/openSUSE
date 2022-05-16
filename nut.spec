#
# spec file for package nut
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


%bcond_with texdoc

%define CGIPATH		%{apache_serverroot}/cgi-bin/nut
%define HTMLPATH	%{apache_serverroot}/htdocs/nut
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
Name:           nut
Version:        2.7.4
Release:        0
Summary:        Network UPS Tools Core (Uninterruptible Power Supply Monitoring)
License:        GPL-2.0-or-later
Group:          Hardware/UPS
URL:            http://www.networkupstools.org/
Source:         http://www.networkupstools.org/source/2.7/%{name}-%{version}.tar.gz
Source2:        README.SUSE
Source6:        nut.system-sleep
Source7:        nut.sleep
Source8:        http://www.networkupstools.org/source/2.7/%{name}-%{version}.tar.gz.sig
Source9:        %{name}.keyring
Patch0:         nut-preconfig.patch
Patch3:         nut-notifyflag.patch
# PATCH-FIX-UPSTREAM nut-systemd-dirs.patch sbrabec@suse.cz -- Fix systemd targets.
Patch7:         nut-systemd-dirs.patch
# PATCH-FEATURE-OPENSUSE nut-doc-fixed-date.patch sbrabec@suse.cz -- Make doc builds reproducible.
Patch8:         nut-doc-fixed-date.patch
# PATCH-FIX-UPSTREAM nut-doc-cables.patch sbrabec@suse.cz -- Build HTML documentation of cables.
Patch9:         nut-doc-cables.patch
# PATCH-FIX-UPSTREAM use-pkg-config-gdlib.diff alarrosa@suse.com -- Use pkg-config to obtain CFLAGS and LDFLAGS to use when building with gd
Patch10:        use-pkg-config-gdlib.diff
Patch11:        openssl-1_1.patch
Patch12:        nut-upssched.patch
Patch13:        reproducible.patch
Patch14:        nutscanner-ftbfs.patch
Patch15:        harden_nut-driver.service.patch
Patch16:        harden_nut-monitor.service.patch
Patch17:        harden_nut-server.service.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  asciidoc
BuildRequires:  avahi-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libcppunit-devel
BuildRequires:  libtool
%if 0%{?suse_version} >= 1500
BuildRequires:  libnsl-devel
%endif
BuildRequires:  libusb-devel
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig
BuildRequires:  source-highlight
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libpowerman)
BuildRequires:  pkgconfig(libsystemd)
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
BuildRequires:  pkgconfig(bash-completion)
%ifarch %{ix86} x86_64 ia64
BuildRequires:  pkgconfig(libfreeipmi)
%endif
%if 0%{?suse_version} >= 1500
Requires(pre):  user(upsd)
%endif
%if %{with texdoc}
BuildRequires:  asciidoc-latex-backend
%else
# Obsolete all the docu stuff with disabled tex dependencies
Obsoletes:      %{name}-devel-doc-pdf <= %{version}
Obsoletes:      %{name}-doc-pdf <= %{version}
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

%package -n libnutclient0
Summary:        Network UPS Tools Library (Uninterruptible Power Supply Monitoring)
Group:          System/Libraries
Conflicts:      libupsclient1

%description -n libnutclient0
Shared library for the Network UPS Tools.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package -n libnutscan1
Summary:        Network UPS Tools Library (Uninterruptible Power Supply Monitoring)
Group:          System/Libraries
Conflicts:      libupsclient1

%description -n libnutscan1
Shared library for the Network UPS Tools.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package -n libupsclient4
Summary:        Network UPS Tools Library (Uninterruptible Power Supply Monitoring)
Group:          System/Libraries
Conflicts:      libupsclient1

%description -n libupsclient4
Shared library for the Network UPS Tools.

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package cgi
Summary:        Network UPS Tools Web Server Support (UPS Status Pages)
Group:          Hardware/UPS
Requires:       %{name} = %{version}
Enhances:       %{name}
Supplements:    packageand(%{name}:apache2)

%description cgi
Web server support package for the Network UPS Tools.

Predefined URL is http://localhost/nut/index.html

Network UPS Tools is a collection of programs which provide a common
interface for monitoring and administering UPS hardware.

%package devel
Summary:        Network UPS Tools (Uninterruptible Power Supply Monitoring)
Group:          Development/Libraries/C and C++
Requires:       libnutclient0 = %{version}-%{release}
Requires:       libnutscan1 = %{version}-%{release}
Requires:       libupsclient4 = %{version}-%{release}
Requires:       openssl-devel

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
%setup -q
cp -a %{SOURCE2} %{SOURCE6} %{SOURCE7} .
%patch0
%patch3
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
sed -i s/@now@/`date -r ChangeLog +%%Y-%%m-%%d`/g docs/docinfo.xml.in
%patch15 -p1
%patch16 -p1
%patch17 -p1

sed -i s:%{_prefix}/local/ups/bin:/bin: conf/upssched.conf.sample.in

%build
autoreconf -fvi
%if 0%{?suse_version} > 1500
export CXXFLAGS="%{optflags} -std=gnu++14"
%endif
%configure \
	--disable-static \
	--sysconfdir=%{CONFPATH} \
	--datadir=%{_datadir}/nut \
	--with-all \
%if %{with texdoc}
	--with-doc \
%else
	--with-doc="html-single html-chunked" \
%endif
	--with-ssl \
	--with-openssl \
	--without-nss \
	--with-wrap \
%ifnarch %{ix86} x86_64 ia64
	--without-ipmi \
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
make -j1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{STATEPATH}
# initscript
mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rcnut-driver
ln -s service %{buildroot}%{_sbindir}/rcnut-server
ln -s service %{buildroot}%{_sbindir}/rcnut-monitor
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 scripts/logrotate/nutlogd %{buildroot}%{_sysconfdir}/logrotate.d/nut
mkdir -p %{buildroot}%{STATEPATH}
rename .sample "" %{buildroot}%{_sysconfdir}/ups/*.sample

install -d %{buildroot}/usr/lib/systemd/system-sleep
install nut.system-sleep %{buildroot}/usr/lib/systemd/system-sleep/%{name}.sh

mkdir -p %{buildroot}%{bashcompletionsdir}
install -m0644 scripts/misc/nut.bash_completion %{buildroot}%{bashcompletionsdir}/nut

# Documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a docs/*.txt docs/cables docs/images %{buildroot}%{_docdir}/%{name}/
cp -a docs/*.css docs/*.html %{buildroot}%{_docdir}/%{name}/
%if %{with texdoc}
cp -a docs/*.pdf %{buildroot}%{_docdir}/%{name}/
%endif

# Not needed for packaged contents:
rm %{buildroot}%{_docdir}/%{name}/packager-guide.*

# Create symlinks for man pages
%fdupes -s %{buildroot}%{_mandir}

%pre
%if 0%{?suse_version} < 1330
getent passwd %{NUT_USER} >/dev/null || useradd -r -g %{NUT_GROUP} -s /bin/false -c "UPS daemon" -d /sbin %{NUT_USER} 2>/dev/null
%endif
%service_add_pre nut-driver.service nut-server.service nut-monitor.service

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
%service_add_post nut-driver.service nut-server.service nut-monitor.service

%preun
%service_del_preun nut-driver.service nut-server.service nut-monitor.service

%postun
%service_del_postun nut-driver.service nut-server.service nut-monitor.service

%post   -n libnutclient0 -p /sbin/ldconfig
%postun -n libnutclient0 -p /sbin/ldconfig
%post   -n libnutscan1 -p /sbin/ldconfig
%postun -n libnutscan1 -p /sbin/ldconfig
%post   -n libupsclient4 -p /sbin/ldconfig
%postun -n libupsclient4 -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog MAINTAINERS NEWS README README.SUSE UPGRADING
%license COPYING
%config %{_sysconfdir}/logrotate.d/*
%{_bindir}/*
%{_datadir}/nut
%{_mandir}/man5/*%{ext_man}
%{_mandir}/man8/*%{ext_man}
%exclude %{_mandir}/man8/netxml-ups*.*
%exclude %{_mandir}/man8/snmp-ups*.*
%dir %{_libexecdir}/ups
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
%attr(700,%{NUT_USER},%{NUT_GROUP}) %{STATEPATH}
%{_unitdir}/*.service
%{systemdsystemdutildir}/system-shutdown/*
/usr/lib/systemd/system-sleep/%{name}.sh
%{bashcompletionsdir}/*

%files drivers-net
%{MODELPATH}/snmp-ups
%{MODELPATH}/netxml-ups
%{_mandir}/man8/netxml-ups*%{ext_man}
%{_mandir}/man8/snmp-ups*%{ext_man}

%files -n libnutclient0
%{_libdir}/libnutclient.so.*

%files -n libnutscan1
%{_libdir}/libnutscan.so.*

%files -n libupsclient4
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
%{_mandir}/man3/*%{ext_man}

%files doc-asciidoc
%doc %dir %{_docdir}/%{name}
%{_docdir}/%{name}/*.txt
%{_docdir}/%{name}/cables

%files devel-doc-html
%{_docdir}/%{name}/developer-guide.html

%files doc-html
%{_docdir}/%{name}/FAQ.html
%{_docdir}/%{name}/cables.html
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
%{_docdir}/%{name}/user-manual.pdf

%files devel-doc-pdf
%doc %dir %{_docdir}/%{name}
%{_docdir}/%{name}/developer-guide.pdf

%endif

%changelog
