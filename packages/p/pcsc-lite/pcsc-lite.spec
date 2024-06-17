#
# spec file for package pcsc-lite
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# FIXME: Maybe we should use /usr/lib/pcsc/drivers as others do:
%define ifddir %{_libdir}/readers
%define PKG_USER	scard
%define PKG_GROUP	scard
Name:           pcsc-lite
Version:        2.2.3
Release:        0
Summary:        PC/SC Smart Cards Library
License:        BSD-3-Clause AND GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://pcsclite.apdu.fr/
Source:         https://pcsclite.apdu.fr/files/%{name}-%{version}.tar.xz
Source1:        %{name}.sysconfig
Source2:        README.SUSE
Source4:        baselibs.conf
Source6:        pcsc-lite-reader-conf
Source7:        https://pcsclite.apdu.fr/files/%{name}-%{version}.tar.xz.asc
Source8:        %{name}.keyring
Source9:        %{name}.sysusers
Patch0:         systemd-service.patch
Patch1:         harden_pcscd.service.patch
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  sysuser-tools
## BuildRequires:  systemd-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
Requires:       libpcsclite1 = %{version}
Requires(post): %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  polkit-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libudev)
%{?systemd_requires}
%sysusers_requires

%description
PC/SC Lite provides a Windows SCard interface in a small form factor
for communication with smart cards and readers.

Security aware people should read the SECURITY file for possible
vulnerabilities of pcsclite and how to fix them. For information on how
to install drivers please read the DRIVERS file.

Memory cards will be supported through the MCT specification, which is
an APDU like manner sent normally through the SCardTransmit() function.
This functionality is exercised in the driver.

%package -n libpcsclite1
Summary:        PC/SC Smart Card Library
License:        BSD-3-Clause
Group:          System/Libraries
Recommends:     pcsc-lite >= %{version}

%description -n libpcsclite1
PC/SC Lite provides a Windows SCard interface in a small form factor
for communication with smart cards and readers.

Security aware people should read the SECURITY file for possible
vulnerabilities of pcsclite and how to fix them. For information on how
to install drivers please read the DRIVERS file.

Memory cards will be supported through the MCT specification, which is
an APDU like manner sent normally through the SCardTransmit() function.
This functionality is exercised in the driver.

%package -n libpcscspy0
Summary:        PC/SC Smart Card Library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libpcscspy0
Supporting library for the PC/SC spy tool.

%package devel
Summary:        Development package for the MUSCLE project SmartCards library
License:        BSD-3-Clause AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       libpcsclite1 = %{version}
Requires:       libpcscspy0 = %{version}

%description devel
This package contains the development files for pcsc-lite. It allows to
compile plugins for the pcsc-lite package.

%prep
%setup
%patch -P 0 -p1
cp -a %{SOURCE1} %{SOURCE2} %{SOURCE6} .
%patch -P 1 -p1

%build
%sysusers_generate_pre %{SOURCE9} %{PKG_USER} %{PKG_USER}.conf
%meson \
       -D usbdropdir=%{ifddir} \
       -D polkit=TRUE \
       -D libsystemd=TRUE \
       -D systemdunit=system

%meson_build %{?_smp_mflags}

%install
%meson_install
mkdir -p %{buildroot}%{ifddir}
mkdir -p %{buildroot}%{_sysconfdir}/reader.conf.d/
sed s:@ifddir@:%{ifddir}: <pcsc-lite-reader-conf >%{buildroot}%{_sysconfdir}/reader.conf.d/reader.conf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcpcscd
mkdir -p %{buildroot}%{_fillupdir}
cp %{name}.sysconfig %{buildroot}%{_fillupdir}/sysconfig.pcscd
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a AUTHORS ChangeLog COPYING HELP NEWS README README.SUSE SECURITY %{buildroot}%{_docdir}/%{name}
mv %{buildroot}/usr/share/doc/%{name}/* %{buildroot}%{_docdir}/%{name}
rm -d %{buildroot}/usr/share/doc/%{name}
# Remove useless la files
find %{buildroot} -type f -name "*.la" -delete -print
install -Dm0644 %{SOURCE9} %{buildroot}%{_sysusersdir}/%{PKG_USER}.conf
%python3_fix_shebang

%pre -f %{PKG_USER}.pre
%service_add_pre pcscd.service pcscd.socket

%post
%service_add_post pcscd.service pcscd.socket
%fillup_only -n pcscd

%preun
%service_del_preun pcscd.service pcscd.socket

%postun
%service_del_postun pcscd.service pcscd.socket

%post -n libpcsclite1 -p /sbin/ldconfig

%postun -n libpcsclite1 -p /sbin/ldconfig

%post -n libpcscspy0 -p /sbin/ldconfig

%postun -n libpcscspy0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%docdir %{_docdir}/%{name}
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/setup_spy.sh
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/HELP
%{_docdir}/%{name}/NEWS
%{_docdir}/%{name}/README
%{_docdir}/%{name}/README.SUSE
%{_docdir}/%{name}/SECURITY
%doc %{_mandir}/man?/*.*
%{_sbindir}/*
%dir %{_sysconfdir}/reader.conf.d
%config(noreplace) %{_sysconfdir}/reader.conf.d/reader.conf
%{ifddir}
%{_unitdir}/pcsc*
%{_sysusersdir}/%{PKG_USER}.conf
%{_fillupdir}/sysconfig.pcscd
# libpcsclite.so should stay in the main package (#732911). Third party packages may need it for dlopen().
%{_libdir}/libpcsclite.so
%{_libdir}/libpcsclite_real.so
%{_datadir}/polkit-1/actions/org.debian.pcsc-lite.policy

%files -n libpcsclite1
%defattr(-,root,root)
%{_libdir}/libpcsclite.so.*
%{_libdir}/libpcsclite_real.so.*

%files -n libpcscspy0
%defattr(-,root,root)
%{_libdir}/libpcscspy.so.*

%files devel
%defattr(-,root,root)
%docdir %{_docdir}/%{name}
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/Change*
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_bindir}/*
# libpcsclite.so should stay in the main package (#732911). Third party packages may need it for dlopen().
%exclude %{_libdir}/libpcsclite.so

%changelog
