#
# spec file for package clamav
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


%define clamav_check --enable-check
%bcond_with clammspack
Name:           clamav
Version:        0.103.0
Release:        0
Summary:        Antivirus Toolkit
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            http://www.clamav.net
Source0:        http://www.clamav.net/downloads/production/%name-%version.tar.gz
Source1:        http://www.clamav.net/downloads/production/%name-%version.tar.gz.sig
Source4:        clamav-rpmlintrc
Source6:        clamav-tmpfiles.conf
Source7:        service.clamd
Source8:        service.freshclam
Source9:        service.clamav-milter
Source11:       clamav.keyring
Patch1:         clamav-conf.patch
Patch4:         clamav-disable-timestamps.patch
Patch5:         clamav-obsolete-config.patch
Patch6:         clamav-disable-yara.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  check-devel
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  libcurl-devel >= 7.45
BuildRequires:  libjson-c-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  pwdutils
BuildRequires:  sed
BuildRequires:  sendmail-devel
BuildRequires:  systemd-rpm-macros
#BuildRequires:  valgrind
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libsystemd)
Requires(pre):  %_bindir/awk
Requires(pre):  %_sbindir/groupadd
Requires(pre):  %_sbindir/useradd
Requires(pre):  %_sbindir/usermod
Requires(pre):  /bin/sed
Requires(pre):  /bin/tar
Obsoletes:      clamav-db < 0.88.3
Provides:       clamav-nodb = %version
Obsoletes:      clamav-nodb <= 0.98.4
%systemd_requires
%if %{without clammspack}
BuildRequires:  libmspack-devel
%endif

%description
ClamAV is an antivirus engine designed for detecting trojans,
viruses, malware and other malicious threats. It is the de-facto
standard for mail gateway scanning. It provides a multi-threaded
scanning daemon, command line utilities for on-demand file scanning,
and a tool for automatic signature updates. The core ClamAV library
provides numerous file format detection mechanisms, file unpacking
support, archive support, and multiple signature languages for
detecting threats.

%package -n libclamav9
Summary:        ClamAV antivirus engine runtime
Group:          System/Libraries

%description -n libclamav9
ClamAV is an antivirus engine designed for detecting trojans,
viruses, malware and other malicious threats.

%package -n libfreshclam2
Summary:        ClamAV updater library
Group:          System/Libraries

%description -n libfreshclam2
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
Requires:       libclamav9 = %version
Requires:       libfreshclam2 = %version

%description devel
ClamAV is an antivirus engine designed for detecting trojans,
viruses, malware and other malicious threats.

This subpackage contains header files for developing applications
that want to make use of libclamav.

%prep
%setup -q
%patch1
%patch4
%patch5
%patch6

%build
CFLAGS="-fstack-protector"
CXXFLAGS="-fstack-protector"
export CFLAGS="%optflags $CFLAGS -fPIE -fno-strict-aliasing"
export CXXFLAGS="%optflags $CXXFLAGS -fPIE -fno-strict-aliasing -std=gnu++98"
export LDFLAGS="-pie"
%if "%_lib" == "lib64"
# tomsfastmath needs this for correct operation on 64-bit platforms
CFLAGS="$CFLAGS -DFP_64BIT"
%endif
%configure \
	--disable-clamav \
	--disable-static \
	--with-dbdir=%{_localstatedir}/lib/clamav \
	--with-user=vscan \
	--with-group=vscan \
	--enable-milter \
	%clamav_check \
	--enable-clamdtop \
	--disable-zlib-vcheck \
	--disable-timestamps \
	--disable-yara \
%if %{without clammspack}
	--with-system-libmspack
%endif

%make_build

%install
%make_install
install -d -m755 %buildroot%{_localstatedir}/lib/clamav
install -d -m755 %buildroot/%_tmpfilesdir
install -m644 %SOURCE6 %buildroot%_tmpfilesdir/clamav.conf
mkdir -p %buildroot%{_localstatedir}/spool/amavis
mkdir -p -m 0755 %buildroot/run/clamav
find %buildroot -type f -name "*.la" -delete -print

# libclammspack is not meant to be linked against by anything but
# libclamav
rm -f %buildroot%_libdir/pkgconfig/libclammspack.pc
rm -f %buildroot%_libdir/libclammspack.so

# fix the new config file names
pushd %buildroot%_sysconfdir
mv clamd.conf.sample clamd.conf
mv clamav-milter.conf.sample clamav-milter.conf
mv freshclam.conf.sample freshclam.conf
popd

# Systemd...
install -d -m 0755 %buildroot/%_unitdir
install -m 0644 %SOURCE7 %buildroot/%_unitdir/clamd.service
install -m 0644 %SOURCE8 %buildroot/%_unitdir/freshclam.service
install -m 0644 %SOURCE9 %buildroot/%_unitdir/clamav-milter.service
rm -f %buildroot/%_unitdir/clamav-clamonacc.service
rm -f %buildroot/%_unitdir/clamav-daemon.service
rm -f %buildroot/%_unitdir/clamav-daemon.socket
rm -f %buildroot/%_unitdir/clamav-freshclam.service
# this is broken if system does not have systemd so don't
# use it at all on systems without mandatory systemd
for srvname in clamd freshclam clamav-milter;do
        (export PATH=%_prefix/sbin:/sbin:$PATH ;ln -sf $(which service) %buildroot/%_sbindir/rc${srvname})
done

%check

# regression tests
%if !0%{?qemu_user_space_build:1}
make check VG=1
%endif

%post   -n libclamav9 -p /sbin/ldconfig
%postun -n libclamav9 -p /sbin/ldconfig
%post   -n libfreshclam2 -p /sbin/ldconfig
%postun -n libfreshclam2 -p /sbin/ldconfig
%post   -n libclammspack0 -p /sbin/ldconfig
%postun -n libclammspack0 -p /sbin/ldconfig

%files
%config(noreplace) %_sysconfdir/*.conf
#systemd...
%_unitdir/clamd.service
%_unitdir/freshclam.service
%_unitdir/clamav-milter.service
%_tmpfilesdir
%license COPYING*
%doc docs/html/*
%_mandir/*/*
%_bindir/*
%_sbindir/*
%defattr(-,vscan,vscan)
%dir %attr(750,vscan,vscan) %{_localstatedir}/spool/amavis
%dir %{_localstatedir}/lib/clamav
%ghost %attr(755,vscan,vscan) /run/clamav

%files -n libclamav9
%_libdir/libclam*.so.9*

%files -n libfreshclam2
%_libdir/libfreshclam.so.2*

%if %{with clammspack}
%files -n libclammspack0
%_libdir/libclammspack.so.0*
%endif

%files devel
%_libdir/pkgconfig/*
%_libdir/libclam*.so
%_libdir/libfreshclam*.so
%_includedir/*

%pre
getent group vscan >/dev/null || %_sbindir/groupadd -r vscan
getent passwd vscan >/dev/null || \
	%_sbindir/useradd -r -o -g vscan -u 65 -s /bin/false \
	-c "Vscan account" -d %{_localstatedir}/spool/amavis vscan
%_sbindir/usermod vscan -g vscan
%service_add_pre clamd.service freshclam.service clamav-milter.service

%post
%tmpfiles_create %_tmpfilesdir/clamav.conf
%service_add_post clamd.service freshclam.service clamav-milter.service

%preun
%service_del_preun clamd.service freshclam.service clamav-milter.service

%postun
%service_del_postun clamd.service freshclam.service clamav-milter.service

%changelog
