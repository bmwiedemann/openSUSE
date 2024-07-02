#
# spec file for package clamav
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


%bcond_without	clammspack
%bcond_with	valgrind

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%bcond_without sysuser_vscan
%endif
%if 0%{?suse_version} <= 1500
%define vgcc 13
%if 0%{?sle_version} < 150400
%define vrust 1.69
%define vcmake 3
%endif
%endif
%global confdir %_prefix%_sysconfdir

Name:           clamav
Version:        1.3.1
Release:        0
Summary:        Antivirus Toolkit
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            https://www.clamav.net
Source0:        https://www.clamav.net/downloads/production/%{name}-%{version}.tar.gz
Source1:        https://www.clamav.net/downloads/production/%{name}-%{version}.tar.gz.sig
Source4:        clamav-rpmlintrc
Source6:        clamav-tmpfiles.conf
Source7:        service.clamd
Source8:        service.freshclam
Source9:        service.clamav-milter
Source10:       timer.freshclam
# w3m https://www.clamav.net/downloads | sed -n '/-BEGIN /,/-END /p'
Source11:       clamav.keyring
Source12:       service.clamonacc
Source65:       system-user-vscan.conf
Patch1:         clamav-conf.patch
Patch5:         clamav-obsolete-config.patch
Patch12:        clamav-fips.patch
Patch14:        clamav-document-maxsize.patch
Patch15:        clamav-format.patch
ExcludeArch:    %{arml}

BuildRequires:  cargo%{?vrust}
BuildRequires:  cmake%{?vcmake}
BuildRequires:  gcc%{?vgcc}
BuildRequires:  gcc%{?vgcc}-c++
BuildRequires:  libbz2-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libopenssl-devel >= 1.0.2
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  rust%{?vrust}
#BuildRequires:  rust+cargo >= 1.61.0
#BuildRequires:  rust+rustc >= 1.61.0
BuildRequires:  sendmail-devel
BuildRequires:  systemd
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libcurl) >= 7.45
BuildRequires:  pkgconfig(libpcre2-8) >= 10.30
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python(abi) >= 3.6
%if 0%{?suse_version} >= 1500
BuildRequires:  python3-pytest
%endif
#
# Workaround to keep "make check" from using an existing libclamav
# instead of the just built one. This should rather be fixed
# by keeping libtool from adding libdir to rpath and LD_LIBRARY_PATH
# of the test binaries.
#
#!BuildIgnore:    clamav
Obsoletes:      clamav-db < 0.88.3
Provides:       clamav-nodb = %{version}
Obsoletes:      clamav-nodb < %{version}
%if %{without clammspack}
BuildRequires:  pkgconfig(libmspack)
%endif
%if %{with valgrind}
BuildRequires:  valgrind
%endif
%if %{with sysuser_vscan}
Requires(pre):  group(vscan)
Requires(pre):  user(vscan)
%else
BuildRequires:  sysuser-tools
%sysusers_requires
%endif
%{?systemd_ordering}

%description
ClamAV is an antivirus engine designed for detecting trojans,
viruses, malware and other malicious threats. It is the de-facto
standard for mail gateway scanning. It provides a multi-threaded
scanning daemon, command line utilities for on-demand file scanning,
and a tool for automatic signature updates. The core ClamAV library
provides numerous file format detection mechanisms, file unpacking
support, archive support, and multiple signature languages for
detecting threats.

%package docs-html
Summary:        Documentation for ClamAV in HTML format
Group:          Productivity/Security
Requires:       %{name} = %{version}
BuildArch:      noarch

%description docs-html
Optional HTML documentation for ClamAV antivirus engine

%package milter
Summary:        ClamAV Milter compatible mail scanner
Group:          Productivity/Security
Requires:       %{name} = %{version}
Provides:       %{name}:/usr/sbin/clamav-milter

%description milter
ClamAV-milter is a filter for sendmail(1) mail server. It uses a
mail scanning engine built into clamd(8). ClamAV-milter can use
load balancing and fault tolerant techniques to connect to more
than one clamd(8) server and seamlessly hot-swap to even the load
between different machines and to keep scanning for viruses even
when a server goes down.

%package -n libclamav12
Summary:        ClamAV antivirus engine runtime
Group:          System/Libraries

%description -n libclamav12
ClamAV is an antivirus engine designed for detecting trojans,
viruses, malware and other malicious threats.

%package -n libfreshclam3
Summary:        ClamAV updater library
Group:          System/Libraries

%description -n libfreshclam3
ClamAV is an antivirus engine designed for detecting trojans,
viruses, malware and other malicious threats.

%package -n libclammspack0
Summary:        ClamAV antivirus engine runtime
Group:          System/Libraries

%description -n libclammspack0
ClamAV is an antivirus engine designed for detecting trojans,
viruses, malware and other malicious threats.

%package devel
Summary:        Development files for libclamav, an antivirus engine
Group:          Development/Libraries/C and C++
Requires:       libclamav12 = %{version}
Requires:       libfreshclam3 = %{version}

%description devel
ClamAV is an antivirus engine designed for detecting trojans,
viruses, malware and other malicious threats.

This subpackage contains header files for developing applications
that want to make use of libclamav.

%prep
%setup -q
%patch -P 1
%patch -P 5
%patch -P 12
%patch -P 14
%patch -P 15
chmod -x docs/html/images/flamegraph.svg

%build
%if %{without sysuser_vscan}
# Create vscan user
%sysusers_generate_pre %{SOURCE65} vscan
%endif
%cmake \
%if "%{?vgcc}" != ""
    -DCMAKE_C_COMPILER=gcc-%{vgcc} \
    -DCMAKE_CXX_COMPILER=g++-%{vgcc} \
%endif
    -DCMAKE_BUILD_TYPE=DEBUG \
    -DCLAMAV_USER=vscan \
    -DCLAMAV_GROUP=vscan \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%name \
    -DAPP_CONFIG_DIRECTORY:PATH=%_sysconfdir \
    -DDATABASE_DIRECTORY:PATH=%_localstatedir/lib/clamav \
    -DENABLE_CLAMONACC=ON \
    -DENABLE_MILTER=ON \
    -DSYSTEMD_UNIT_DIR=%{_unitdir} \
%if %{without clammspack}
    -DENABLE_EXTERNAL_MSPACK=ON
%endif

%install

%cmake_install
install -d -m755 %{buildroot}%{_localstatedir}/lib/clamav
install -d -m755 %{buildroot}%{_tmpfilesdir}
install -m644 %SOURCE6 %{buildroot}%{_tmpfilesdir}/clamav.conf
%if 0%{?suse_version} <= 1500
mkdir -p %{buildroot}%{_localstatedir}/spool/amavis
%endif
mkdir -p -m 0755 %{buildroot}{%_sysconfdir,/run/clamav}
find %{buildroot} -type f -name "*.la" -delete -print

for f in %{buildroot}%{_sysconfdir}/*.conf.sample;
do
    mv $f ${f%.sample}
done

# Systemd...
rm -f %{buildroot}%{_unitdir}/clamav-*
install -m 0644 %SOURCE7 %{buildroot}%{_unitdir}/clamd.service
install -m 0644 %SOURCE8 %{buildroot}%{_unitdir}/freshclam.service
install -m 0644 %SOURCE9 %{buildroot}%{_unitdir}/clamav-milter.service
install -m 0644 %SOURCE10 %{buildroot}%{_unitdir}/freshclam.timer
install -m 0644 %SOURCE12 %{buildroot}%{_unitdir}/clamonacc.service
for srvname in clamd freshclam clamav-milter clamonacc; do
	(export PATH=%_prefix/sbin:/sbin:$PATH ;ln -sf service %{buildroot}/%{_sbindir}/rc${srvname})
done

%check
# regression tests
%if !0%{?qemu_user_space_build:1} && ( 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150500 )
# Run ctest with a single job to avoid failures
# due to race conditions, e.g. on s390x.
%define _smp_mflags -j1
%ctest
%undefine _smp_mflags
%endif

%if %{with sysuser_vscan}
%pre
%else

%pre -f vscan.pre
%endif
%service_add_pre clamd.service clamonacc.service

%post
%tmpfiles_create %{_tmpfilesdir}/clamav.conf
%service_add_post clamd.service clamonacc.service

%preun
if [ $1 -eq 0 ]; then
	# package will be uninstalled
	rm -f %{_localstatedir}/lib/clamav/*
fi
%service_del_preun clamd.service clamonacc.service

%postun
%service_del_postun clamd.service clamonacc.service

%pre milter
%service_add_pre clamav-milter.service

%post milter
%service_add_post clamav-milter.service

%preun milter
%service_del_preun clamav-milter.service

%postun milter
%service_del_postun clamav-milter.service

%if 0%{?suse_version} > 1500
%ldconfig_scriptlets -n libclamav12
%ldconfig_scriptlets -n libfreshclam3
%if %{with clammspack}
%ldconfig_scriptlets -n libclammspack0
%endif
%else
%post   -n libclamav12 -p /sbin/ldconfig
%postun -n libclamav12 -p /sbin/ldconfig
%post   -n libfreshclam3 -p /sbin/ldconfig
%postun -n libfreshclam3 -p /sbin/ldconfig
%if %{with clammspack}
%post   -n libclammspack0 -p /sbin/ldconfig
%postun -n libclammspack0 -p /sbin/ldconfig
%endif
%endif

%files
%license COPYING*
%config(noreplace) %{_sysconfdir}/clamd.conf
%config(noreplace) %{_sysconfdir}/freshclam.conf
%{_bindir}/clamav-config
%{_bindir}/clambc
%{_bindir}/clamconf
%{_bindir}/clamdscan
%{_bindir}/clamdtop
%{_bindir}/clamscan
%{_bindir}/clamsubmit
%{_bindir}/freshclam
%{_bindir}/sigtool
%{_sbindir}/clamd
%{_sbindir}/clamonacc
%{_sbindir}/rcclamd
%{_sbindir}/rcfreshclam
%{_sbindir}/rcclamonacc
%{_mandir}/man1/clambc.1%{?ext_man}
%{_mandir}/man1/clamconf.1%{?ext_man}
%{_mandir}/man1/clamdscan.1%{?ext_man}
%{_mandir}/man1/clamdtop.1%{?ext_man}
%{_mandir}/man1/clamscan.1%{?ext_man}
%{_mandir}/man1/clamsubmit.1%{?ext_man}
%{_mandir}/man1/freshclam.1%{?ext_man}
%{_mandir}/man1/sigtool.1%{?ext_man}
%{_mandir}/man5/clamd.conf.5%{?ext_man}
%{_mandir}/man5/freshclam.conf.5%{?ext_man}
%{_mandir}/man8/clamd.8%{?ext_man}
%{_mandir}/man8/clamonacc.8%{?ext_man}
%{_tmpfilesdir}/*
%{_unitdir}/clamd.service
%{_unitdir}/freshclam.service
%{_unitdir}/freshclam.timer
%{_unitdir}/clamonacc.service
%defattr(-,vscan,vscan)
%dir %{_localstatedir}/lib/clamav
%if 0%{?suse_version} <= 1500
%dir %attr(750,vscan,vscan) %{_localstatedir}/spool/amavis
%endif
%ghost %attr(755,vscan,vscan) /run/clamav

%files docs-html
%doc %_docdir/%name

%files milter
%config(noreplace) %{_sysconfdir}/clamav-milter.conf
%{_unitdir}/clamav-milter.service
%{_sbindir}/clamav-milter
%{_sbindir}/rcclamav-milter
%{_mandir}/man5/clamav-milter.conf.5%{?ext_man}
%{_mandir}/man8/clamav-milter.8%{?ext_man}

%files -n libclamav12
%{_libdir}/libclam*.so.12*

%files -n libfreshclam3
%{_libdir}/libfreshclam.so.3*

%if %{with clammspack}
%files -n libclammspack0
%{_libdir}/libclammspack.so.0*
%endif

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libclam*.so
%{_libdir}/libfreshclam*.so
%{_libdir}/libclamav_rust.a

%changelog
