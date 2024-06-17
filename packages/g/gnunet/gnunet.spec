#
# spec file for package gnunet
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           gnunet
Version:        0.21.2
Release:        0
Summary:        Security focused Peer-to-Peer Framework
License:        AGPL-3.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://www.gnunet.org/
Source0:        https://ftp.gnu.org/pub/gnu/gnunet/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/pub/gnu/gnunet/%{name}-%{version}.tar.gz.sig
# https://gnunet.org/~schanzen/3D11063C10F98D14BD24D1470B0998EF86F59B6A
Source2:        %{name}.keyring
BuildRequires:  libtool >= 2.2
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  python3-Sphinx
BuildRequires:  sysuser-tools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gnutls) >= 3.2.12
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcurl) >= 7.34.0
BuildRequires:  pkgconfig(libextractor)
BuildRequires:  pkgconfig(libgcrypt) >= 1.6.0
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libmicrohttpd) >= 0.9.63
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libsodium) >= 1.0.18
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zbar)
BuildRequires:  pkgconfig(zlib)
# openssl for gnunet-gns-proxy-setup-ca
Requires:       %{_bindir}/openssl
# certutil for gnunet-gns-proxy-setup-ca
Requires:       mozilla-nss-tools
Recommends:     miniupnpc
%sysusers_requires

%description
GNUnet is peer-to-peer framework focusing on security. The first and primary
application for GNUnet is anonymous file-sharing. GNUnet is currently developed
by a worldwide group of independent free software developers.

GNUnet is a part of the GNU project (https://www.gnu.org/).

# A list of all shared libraries shipped in this package
# Will be run through two generator macros: once in -devel
# and again to generate individual packages
%define gnunet_libs \
%gnunet_libpackage -l gnunetarm -s 2\
%gnunet_libpackage -l gnunetblockgroup -s 0\
%gnunet_libpackage -l gnunetblock -s 0\
%gnunet_libpackage -l gnunetcadet -s 7\
%gnunet_libpackage -l gnunetconsensus -s 0\
%gnunet_libpackage -l gnunetcore -s 0\
%gnunet_libpackage -l gnunetcurl -s 0\
%gnunet_libpackage -l gnunetdatacache -s 0\
%gnunet_libpackage -l gnunetdatastore -s 1\
%gnunet_libpackage -l gnunetdht -s 4\
%gnunet_libpackage -l gnunetdid -s 0\
%gnunet_libpackage -l gnunetdns -s 0\
%gnunet_libpackage -l gnunetfs -s 2\
%gnunet_libpackage -l gnunetgnsrecordjson -s 0\
%gnunet_libpackage -l gnunetgnsrecord -s 0\
%gnunet_libpackage -l gnunetgns -s 0\
%gnunet_libpackage -l gnunethello -s 0\
%gnunet_libpackage -l gnunetidentity -s 1\
%gnunet_libpackage -l gnunetjson -s 0\
%gnunet_libpackage -l gnunetmessenger -s 0\
%gnunet_libpackage -l gnunetnamecache -s 0\
%gnunet_libpackage -l gnunetnamestore -s 0\
%gnunet_libpackage -l gnunetnatauto -s 0\
%gnunet_libpackage -l gnunetnatnew -s 2\
%gnunet_libpackage -l gnunetnse -s 0\
%gnunet_libpackage -l gnunetpeerstore -s 0\
%gnunet_libpackage -l gnunetpq -s 5\
%gnunet_libpackage -l gnunetreclaim -s 0\
%gnunet_libpackage -l gnunetregexblock -s 1\
%gnunet_libpackage -l gnunetregex -s 3\
%gnunet_libpackage -l gnunetrest -s 0\
%gnunet_libpackage -l gnunetrevocation -s 0\
%gnunet_libpackage -l gnunetscalarproduct -s 0\
%gnunet_libpackage -l gnunetsecretsharing -s 0\
%gnunet_libpackage -l gnunetseti -s 0\
%gnunet_libpackage -l gnunetset -s 0\
%gnunet_libpackage -l gnunetsetu -s 0\
%gnunet_libpackage -l gnunetsq -s 0\
%gnunet_libpackage -l gnunetstatistics -s 2\
%gnunet_libpackage -l gnunettestbed -s 0\
%gnunet_libpackage -l gnunettestingarm -s 0\
%gnunet_libpackage -l gnunettesting -s 3\
%gnunet_libpackage -l gnunettestingtestbed -s 0\
%gnunet_libpackage -l gnunettestingtransport -s 0\
%gnunet_libpackage -l gnunettransportapplication -s 0\
%gnunet_libpackage -l gnunettransportcommunicator -s 0\
%gnunet_libpackage -l gnunettransportcore -s 0\
%gnunet_libpackage -l gnunettransportmonitor -s 0\
%gnunet_libpackage -l gnunetutil -s 16\
%gnunet_libpackage -l gnunetvpn -s 0\
%gnunet_libpackage -l nss_gns4 -s 2 -d \-\
%gnunet_libpackage -l nss_gns6 -s 2 -d \-\
%gnunet_libpackage -l nss_gns -s 2\
%{nil}
# generator macro for -devel
%define gnunet_libpackage(l:s:d:) Requires: lib%{-l*}%{-d*}%{-s*} = %{version}

%package        devel
Summary:        Security focused Peer-to-Peer Framework
Group:          Development/Libraries/C and C++
Requires:       pkgconfig(libextractor)
Requires:       pkgconfig(libgcrypt)
Requires:       pkgconfig(libsodium)
%{gnunet_libs}

%description    devel
GNUnet is peer-to-peer framework focusing on security. The first and primary
application for GNUnet is anonymous file-sharing. GNUnet is currently developed
by a worldwide group of independent free software developers.

This package contains header files and libraries needed to develop
application that use %{name}.

%lang_package

# generator macro for individual packages
%define gnunet_libpackage(l:s:d:) %package -n lib%{-l*}%{-d*}%{-s*}\
Summary: GNUnet library lib%{-l*} \
%description -n lib%{-l*}%{-d*}%{-s*} \
This package contains the lib%{-l*} library for GNUnet. \
%files -n lib%{-l*}%{-d*}%{-s*} \
%%license COPYING \
%{_libdir}/lib%{-l*}.so.%{-s*}* \
%ldconfig_scriptlets -n lib%{-l*}%{-d*}%{-s*} \
%{nil}
%{gnunet_libs}

%prep
%autosetup -p1

%build
%configure \
	--libexecdir=%{_prefix}/lib/gnunet/libexec/ \
	%{nil}
%make_build
%sysusers_generate_pre contrib/services/systemd/sysusers-gnunet.conf gnunet system-user-gnunet.conf

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# license files installed via file list
rm -rf %{buildroot}%{_datadir}/doc/gnunet
# not needed
rm -rf %{buildroot}%{_datadir}/gnunet/services/openrc

install -D -m 644 contrib/services/systemd/sysusers-gnunet.conf	%{buildroot}/%{_sysusersdir}/system-user-gnunet.conf
install -D -m 644 contrib/services/systemd/gnunet.service	%{buildroot}/%{_unitdir}/gnunet.service

%suse_update_desktop_file gnunet-uri
%find_lang %{name}

%pre -f gnunet.pre
%service_add_pre gnunet.service

%post
%service_add_post gnunet.service

%preun
%service_del_preun gnunet.service

%postun
%service_del_postun gnunet.service

%files
%license COPYING
%doc AUTHORS ChangeLog README*
%{_bindir}/*
%{_libdir}/gnunet
%{_datadir}/gnunet
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%{_infodir}/gnunet.info%{?ext_info}
%{_sysusersdir}/system-user-gnunet.conf
%{_datadir}/applications/*.desktop
%{_unitdir}/gnunet.service

%files devel
%license COPYING
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}*.pc
%{_libdir}/*.so
%{_datadir}/aclocal/gnunet.m4

%files lang -f %{name}.lang
%license COPYING

%changelog
