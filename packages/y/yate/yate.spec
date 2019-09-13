#
# spec file for package yate
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011, Sascha Peilicke <saschpe@gmx.de>
# Copyright (c) 2011, Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           yate
Version:        6.1.0
Release:        0
Summary:        Yet Another Telephony Engine
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Clients
URL:            http://www.yate.null.ro/
Source0:        http://yate.null.ro/tarballs/yate6/yate-%{version}-1.tar.gz
Patch1:         dont-mess-with-cflags.patch
Patch2:         add-arm64-support.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libgsm-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(spandsp)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} <= 1500
BuildRequires:  libqt4-devel
%else
# Needed to avoid conflicts caused by providers.conf which is now in the main package
Obsoletes:      yate-qt4 <= %{version}-%{release}
%endif
%if 0%{?packman_bs}
BuildRequires:  libamrnb-devel
%endif

%description
Yate is a telephony engine. Its focus is on Voice over Internet
Protocol (VoIP) and PSTN. It can be extended. Voice, video, data and
instant messenging can be unified under Yate's routing engine.

%package -n libyate6
Summary:        Shared libraries for Yate
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libyate6
Yate is a telephony engine. Its focus is on Voice over Internet
Protocol (VoIP) and PSTN. It can be extended. Voice, video, data and
instant messenging can be unified under Yate's routing engine.

%package devel
Summary:        Development package for Yate
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
Requires:       libyate6 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use Yate.

%if 0%{?suse_version} <= 1500
%package qt4
Summary:        Qt4 client package for Yate
License:        GPL-2.0-only
Group:          Productivity/Telephony/Clients
Requires:       %{name} = %{version}

%description qt4
The yate-qt4 package includes the files needed to use Yate as a VoIP client
with a Qt4 graphical interface.
%endif

%package scripts
Summary:        External scripting package for Yate
License:        GPL-2.0-only
Group:          Productivity/Telephony/Clients
Requires:       %{name}

%description scripts
The yate-scripts package includes libraries for using external scripts with Yate.

%package with-amrnb
Summary:        Yate with AMRNB codec support
License:        GPL-2.0-only
Group:          Productivity/Telephony/Clients
Requires:       %{name} = %{version}-%{release}

%description with-amrnb
Guarantees Yate with AMRNB codec support.

%prep
%setup -q -n %{name}
%patch1 -p1
%patch2 -p1

%build
autoreconf -fiv
%configure \
  --docdir=%{_docdir} \
  --enable-sctp
make #%%{?_smp_mflags} # Parallel build causes side-effects (compile errors)

%install
%make_install
%if 0%{?suse_version} <= 1500
%suse_update_desktop_file -i %{name}-qt4 Network Telephony Qt
rm %{buildroot}%{_prefix}/lib/menu/yate-qt4.menu # Unused, causes lots of rpmlint warnings
%endif
mkdir -p %{buildroot}%{_docdir}/%{name} # We want docs in /usr/share/doc/packages/yate
mv %{buildroot}%{_datadir}/doc/%{name}-%{version} %{buildroot}%{_docdir}/%{name}

%if 0%{?packman_bs}
cat <<EOF >README.amrnb
This %{name} package has been built with AMRNB support.
EOF
%endif

%if 0%{?suse_version} > 1500
# These files are installed unconditionally but belong to the -qt4 package
rm -fr %{buildroot}%{_datadir}/%{name}/skins
rm -fr %{buildroot}%{_datadir}/%{name}/help
rm %{buildroot}%{_sysconfdir}/%{name}/yate-qt4.conf
%endif

%fdupes %{buildroot}/%{_prefix}

%post   -n libyate6 -p /sbin/ldconfig
%postun -n libyate6 -p /sbin/ldconfig
%if 0%{?suse_version} <= 1500
%post qt4 -p /sbin/ldconfig
%postun qt4 -p /sbin/ldconfig
%endif

%files
%license COPYING
%doc ChangeLog README
%doc %{_docdir}/%{name}/%{name}-%{version}/
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8%{?ext_man}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_datadir}/%{name}/sounds
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/analyzer.yate
%{_libdir}/%{name}/callfork.yate
%{_libdir}/%{name}/callgen.yate
%{_libdir}/%{name}/cdrbuild.yate
%{_libdir}/%{name}/cdrfile.yate
%{_libdir}/%{name}/cdrcombine.yate
%{_libdir}/%{name}/client
%{_libdir}/%{name}/conference.yate
%{_libdir}/%{name}/dumbchan.yate
%{_libdir}/%{name}/enumroute.yate
%{_libdir}/%{name}/extmodule.yate
%{_libdir}/%{name}/fileinfo.yate
%{_libdir}/%{name}/filetransfer.yate
%{_libdir}/%{name}/faxchan.yate
%{_libdir}/%{name}/gvoice.yate
%{_libdir}/%{name}/gsmcodec.yate
%{_libdir}/%{name}/ilbccodec.yate
%{_libdir}/%{name}/ilbcwebrtc.yate
%{_libdir}/%{name}/isaccodec.yate
%{_libdir}/%{name}/jabber
%{_libdir}/%{name}/javascript.yate
%{_libdir}/%{name}/moh.yate
%{_libdir}/%{name}/msgsniff.yate
%{_libdir}/%{name}/mux.yate
%{_libdir}/%{name}/openssl.yate
%{_libdir}/%{name}/pbx.yate
%{_libdir}/%{name}/regexroute.yate
%{_libdir}/%{name}/rmanager.yate
%{_libdir}/%{name}/server
%{_libdir}/%{name}/sip
%{_libdir}/%{name}/speexcodec.yate
%{_libdir}/%{name}/tonedetect.yate
%{_libdir}/%{name}/tonegen.yate
%{_libdir}/%{name}/wavefile.yate
%{_libdir}/%{name}/yiaxchan.yate
%{_libdir}/%{name}/yjinglechan.yate
%{_libdir}/%{name}/yrtpchan.yate
%{_libdir}/%{name}/ysipchan.yate
%{_libdir}/%{name}/ysockschan.yate
%{_libdir}/%{name}/ystunchan.yate
%{_libdir}/%{name}/zlibcompress.yate
%if 0%{?packman_bs}
%{_libdir}/%{name}/amrnbcodec.yate
%{_libdir}/%{name}/efrcodec.yate
%endif
%dir %{_libdir}/%{name}/radio
%{_libdir}/%{name}/radio/dummyradio.yate
%{_libdir}/%{name}/radio/radiotest.yate
%{_libdir}/%{name}/radio/ybladerf.yate
%dir %{_libdir}/%{name}/sig
%{_libdir}/%{name}/sig/camel_map.yate
%{_libdir}/%{name}/sig/isupmangler.yate
%{_libdir}/%{name}/sig/ss7_lnp_ansi.yate
%dir %config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/accfile.conf
%config(noreplace) %{_sysconfdir}/%{name}/analog.conf
%config(noreplace) %{_sysconfdir}/%{name}/amrnbcodec.conf
%config(noreplace) %{_sysconfdir}/%{name}/cache.conf
%config(noreplace) %{_sysconfdir}/%{name}/callcounters.conf
%config(noreplace) %{_sysconfdir}/%{name}/callfork.conf
%config(noreplace) %{_sysconfdir}/%{name}/camel_map.conf
%config(noreplace) %{_sysconfdir}/%{name}/ccongestion.conf
%config(noreplace) %{_sysconfdir}/%{name}/cdrbuild.conf
%config(noreplace) %{_sysconfdir}/%{name}/cdrfile.conf
%config(noreplace) %{_sysconfdir}/%{name}/ciscosm.conf
%config(noreplace) %{_sysconfdir}/%{name}/clustering.conf
%config(noreplace) %{_sysconfdir}/%{name}/cpuload.conf
%config(noreplace) %{_sysconfdir}/%{name}/dbpbx.conf
%config(noreplace) %{_sysconfdir}/%{name}/dsoundchan.conf
%config(noreplace) %{_sysconfdir}/%{name}/dummyradio.conf
%config(noreplace) %{_sysconfdir}/%{name}/enumroute.conf
%config(noreplace) %{_sysconfdir}/%{name}/eventlogs.conf
%config(noreplace) %{_sysconfdir}/%{name}/extmodule.conf
%config(noreplace) %{_sysconfdir}/%{name}/filetransfer.conf
%config(noreplace) %{_sysconfdir}/%{name}/fileinfo.conf
%config(noreplace) %{_sysconfdir}/%{name}/gvoice.conf
%config(noreplace) %{_sysconfdir}/%{name}/h323chan.conf
%config(noreplace) %{_sysconfdir}/%{name}/heartbeat.conf
%config(noreplace) %{_sysconfdir}/%{name}/isupmangler.conf
%config(noreplace) %{_sysconfdir}/%{name}/jabberclient.conf
%config(noreplace) %{_sysconfdir}/%{name}/jabberserver.conf
%config(noreplace) %{_sysconfdir}/%{name}/javascript.conf
%config(noreplace) %{_sysconfdir}/%{name}/jbfeatures.conf
%config(noreplace) %{_sysconfdir}/%{name}/lateroute.conf
%config(noreplace) %{_sysconfdir}/%{name}/lksctp.conf
%config(noreplace) %{_sysconfdir}/%{name}/mgcpca.conf
%config(noreplace) %{_sysconfdir}/%{name}/mgcpgw.conf
%config(noreplace) %{_sysconfdir}/%{name}/moh.conf
%config(noreplace) %{_sysconfdir}/%{name}/monitoring.conf
%config(noreplace) %{_sysconfdir}/%{name}/mux.conf
%config(noreplace) %{_sysconfdir}/%{name}/mysqldb.conf
%config(noreplace) %{_sysconfdir}/%{name}/openssl.conf
%config(noreplace) %{_sysconfdir}/%{name}/pbxassist.conf
%config(noreplace) %{_sysconfdir}/%{name}/pgsqldb.conf
%config(noreplace) %{_sysconfdir}/%{name}/presence.conf
%config(noreplace) %{_sysconfdir}/%{name}/providers.conf
%config(noreplace) %{_sysconfdir}/%{name}/queues.conf
%config(noreplace) %{_sysconfdir}/%{name}/queuesnotify.conf
%config(noreplace) %{_sysconfdir}/%{name}/radiotest.conf
%config(noreplace) %{_sysconfdir}/%{name}/regexroute.conf
%config(noreplace) %{_sysconfdir}/%{name}/regfile.conf
%config(noreplace) %{_sysconfdir}/%{name}/register.conf
%config(noreplace) %{_sysconfdir}/%{name}/rmanager.conf
%config(noreplace) %{_sysconfdir}/%{name}/sip_cnam_lnp.conf
%config(noreplace) %{_sysconfdir}/%{name}/sigtransport.conf
%config(noreplace) %{_sysconfdir}/%{name}/sipfeatures.conf
%config(noreplace) %{_sysconfdir}/%{name}/sqlitedb.conf
%config(noreplace) %{_sysconfdir}/%{name}/ss7_lnp_ansi.conf
%config(noreplace) %{_sysconfdir}/%{name}/subscription.conf
%config(noreplace) %{_sysconfdir}/%{name}/tdmcard.conf
%config(noreplace) %{_sysconfdir}/%{name}/tonegen.conf
%config(noreplace) %{_sysconfdir}/%{name}/users.conf
%config(noreplace) %{_sysconfdir}/%{name}/wpcard.conf
%config(noreplace) %{_sysconfdir}/%{name}/yate.conf
%config(noreplace) %{_sysconfdir}/%{name}/ybladerf.conf
%config(noreplace) %{_sysconfdir}/%{name}/yiaxchan.conf
%config(noreplace) %{_sysconfdir}/%{name}/yjinglechan.conf
%config(noreplace) %{_sysconfdir}/%{name}/yradius.conf
%config(noreplace) %{_sysconfdir}/%{name}/yrtpchan.conf
%config(noreplace) %{_sysconfdir}/%{name}/ysigchan.conf
%config(noreplace) %{_sysconfdir}/%{name}/ysipchan.conf
%config(noreplace) %{_sysconfdir}/%{name}/ysnmpagent.conf
%config(noreplace) %{_sysconfdir}/%{name}/ysockschan.conf
%config(noreplace) %{_sysconfdir}/%{name}/ystunchan.conf
%config(noreplace) %{_sysconfdir}/%{name}/zapcard.conf
%config(noreplace) %{_sysconfdir}/%{name}/zlibcompress.conf

%files -n libyate6
%{_libdir}/libyate.so.6*
%{_libdir}/libyateasn.so.6*
%{_libdir}/libyatejabber.so.6*
%{_libdir}/libyatesig.so.6*
%{_libdir}/libyatemgcp.so.6*
%{_libdir}/libyatescript.so.6*
%{_libdir}/libyateradio.so.6*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.so
%{_bindir}/%{name}-config
%{_mandir}/man8/%{name}-config.8%{?ext_man}
%{_libdir}/pkgconfig/%{name}.pc

%if 0%{?suse_version} <= 1500
%files qt4
%{_bindir}/yate-qt4
%{_libdir}/libyateqt4.so.*
%{_libdir}/%{name}/qt4
%{_datadir}/applications/yate-qt4.desktop
%{_datadir}/pixmaps/null_team-*.png
%{_datadir}/%{name}/skins
%{_datadir}/%{name}/help
%config(noreplace) %{_sysconfdir}/%{name}/yate-qt4.conf
%endif

%files scripts
%{_datadir}/%{name}/scripts

%if 0%{?packman_bs}
%files with-amrnb
%doc README.amrnb
%endif

%changelog
