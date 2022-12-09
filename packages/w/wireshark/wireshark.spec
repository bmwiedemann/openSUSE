#
# spec file for package wireshark
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


# define libraries
%define libcodecs libwscodecs2
%define libtap libwiretap13
%define libutil libwsutil14
%define libwire libwireshark16
%define org_name org.wireshark.Wireshark
%if 0%{?suse_version} >= 1500
%bcond_without lz4
%else
%bcond_with lz4
%endif
Name:           wireshark
Version:        4.0.2
Release:        0
Summary:        A Network Traffic Analyser
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://www.wireshark.org/
Source:         https://www.wireshark.org/download/src/%{name}-%{version}.tar.xz
Source2:        https://www.wireshark.org/download/SIGNATURES-%{version}.txt#/%{name}-%{version}.tar.xz.hash
Source3:        https://www.wireshark.org/download/gerald_at_wireshark_dot_org.gpg#/wireshark.keyring
# PATCH-FIX-UPSTREAM wireshark-0000-wsutil-implicit_declaration_memcpy.patch
Patch0:         wireshark-0000-wsutil-implicit_declaration_memcpy.patch
# PATCH-FEATURE-SLE wireshark-0010-dumpcap-permission-denied.patch bsc#1180102
Patch10:        wireshark-0010-dumpcap-permission-denied.patch
BuildRequires:  %{rb_default_ruby_suffix}-rubygem-asciidoctor
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  glib2-devel >= 2.32
BuildRequires:  hicolor-icon-theme
BuildRequires:  krb5-devel
BuildRequires:  libbrotli-devel
# keep until libbrotli-devel bug is fixed
BuildRequires:  libbrotlidec1
BuildRequires:  libcap-devel
BuildRequires:  libcares-devel >= 1.5.0
BuildRequires:  libgcrypt-devel >= 1.4.2
BuildRequires:  libgnutls-devel >= 3.2
BuildRequires:  libpcap-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libsmi-devel
BuildRequires:  libtool
BuildRequires:  lua51-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  snappy-devel
BuildRequires:  spandsp-devel
BuildRequires:  tcpd-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.3.0
BuildRequires:  pkgconfig(Qt5Core) >= 5.3.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libssh) >= 0.6.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sbc)
BuildRequires:  pkgconfig(speexdsp)
# keep until libbrotli-devel bug is fixed
Requires:       libbrotlidec1
Requires(pre):  permissions
Requires(pre):  shadow
Recommends:     wireshark-ui = %{version}
Provides:       ethereal = %{version}
Obsoletes:      %{libcodecs} < %{version}
Obsoletes:      ethereal < %{version}
Provides:       group(wireshark)
%if 0%{?is_opensuse} && 0%{?suse_version} >= 1550
# enable ITU G.729 Annex A/B speech codec only in Tumbleweed
BuildRequires:  pkgconfig(libbcg729)
%endif
%if %{with lz4}
BuildRequires:  pkgconfig(liblz4)
# in openSUSE Leap 42.3, lz4 was incorrectly packaged
BuildConflicts: pkgconfig(liblz4) = 124
%endif

%description
Wireshark is a network protocol analyzer. It allows examining data
from a live network or from a capture file on disk. You can
interactively browse the capture data, viewing summary and detailed
information for each packet. Wireshark has several features,
including a rich display filter language and the ability to view the
reconstructed stream of a TCP session.

%package -n %{libutil}
Summary:        Library for wireshark utilities
Group:          System/Libraries

%description -n %{libutil}
The libwsutil library provides utility functions for libwireshark.

%package -n %{libwire}
Summary:        Network packet dissection library
Group:          System/Libraries

%description -n %{libwire}
The libwireshark library provides the network packet dissection services
developed by the Wireshark project.

%package -n %{libtap}
Summary:        Wireshark library for tapping
Group:          System/Libraries

%description -n %{libtap}
Wiretap, part of the Wireshark project, is a library that allows one to read
and write several packet capture file formats.

%package devel
Summary:        A Network Traffic Analyser
Group:          Development/Libraries/C and C++
Requires:       %{libtap} = %{version}
Requires:       %{libutil} = %{version}
Requires:       %{libwire} = %{version}
Requires:       %{name} = %{version}
Requires:       glib2-devel
Requires:       glibc-devel
Provides:       ethereal-devel = %{version}
Obsoletes:      ethereal-devel < %{version}

%description devel
Wireshark is a network protocol analyzer. It allows examining data
from a live network or from a capture file on disk.

%package ui-qt
Summary:        A Network Traffic Analyser - Qt UI
Group:          Productivity/Networking/Diagnostic
Requires:       %{name} = %{version}
Requires:       hicolor-icon-theme
Requires:       xdg-utils
Provides:       %{name}-ui = %{version}
# gtk is the deprecated ui so ensure its uninstall
Provides:       %{name}-ui-gtk = %{version}
Obsoletes:      %{name}-ui-gtk < %{version}

%description ui-qt
This package contains the Qt based UI for Wireshark.

%prep
# The publisher doesn't sign the source tarball, but a signatures file containing multiple hashes.
# Verify hashes in that file against source tarball.
echo "`grep %{name}-%{version}.tar.xz %{SOURCE2} | grep SHA256 | head -n1 | cut -d= -f2`  %{SOURCE0}" | sha256sum -c

%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_LIBDIR='%{_lib}/'
%if 0%{?is_opensuse}
%cmake_build
%else
# if the cmake_build makro does not exit we build it by hand...
%{_bindir}/make \
    %if "%{_bindir}/make" == "%{_bindir}/make"
        -O VERBOSE=1 \
    %else
        -v \
    %endif
    -j8
%endif

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print

# Ethereal support (remove when SLE-11 is out of scope
ln -fs wireshark %{buildroot}%{_bindir}/ethereal
ln -fs tshark %{buildroot}%{_bindir}/tethereal

install -d -m 0755 %{buildroot}%{_sysconfdir}
install -d -m 0755 %{buildroot}%{_mandir}/man1/

# -devel
install -d -m 0755  %{buildroot}%{_includedir}/wireshark
IDIR="%{buildroot}%{_includedir}/wireshark"
mkdir -p "${IDIR}/epan"
mkdir -p "${IDIR}/epan/crypt"
mkdir -p "${IDIR}/epan/ftypes"
mkdir -p "${IDIR}/epan/dfilter"
mkdir -p "${IDIR}/epan/dissectors"
mkdir -p "${IDIR}/epan/wmem"
mkdir -p "${IDIR}/wiretap"
mkdir -p "${IDIR}/wsutil"
install -m 644 *.h                              "${IDIR}/"
install -m 644 build/config.h                   "${IDIR}/"
install -m 644 epan/*.h				"${IDIR}/epan/"
install -m 644 epan/crypt/*.h			"${IDIR}/epan/crypt"
install -m 644 epan/ftypes/*.h			"${IDIR}/epan/ftypes"
install -m 644 epan/dfilter/*.h			"${IDIR}/epan/dfilter"
install -m 644 epan/dissectors/*.h		"${IDIR}/epan/dissectors"
install -m 644 wiretap/*.h			"${IDIR}/wiretap"
install -m 644 wsutil/*.h			"${IDIR}/wsutil"

# desktop file
cp resources/freedesktop/%{org_name}.desktop %{buildroot}%{_datadir}/applications/%{org_name}-su.desktop
sed -i -e 's|Name=Wireshark|Name=Wireshark - Super User Mode|g' %{buildroot}%{_datadir}/applications/%{org_name}-su.desktop
sed -i -e 's|Exec=wireshark %f|Exec=xdg-su -c wireshark %f|g' %{buildroot}%{_datadir}/applications/%{org_name}-su.desktop

%suse_update_desktop_file %{org_name}
%suse_update_desktop_file %{org_name}-su

rm -f %{buildroot}%{_datadir}/doc/wireshark/*.html

%pre
getent group wireshark >/dev/null || groupadd -r wireshark

%verifyscript
%verify_permissions -e %{_bindir}/dumpcap

%post
%set_permissions %{_bindir}/dumpcap
exit 0

%post -n %{libutil} -p /sbin/ldconfig
%postun -n %{libutil} -p /sbin/ldconfig
%post -n %{libwire} -p /sbin/ldconfig
%postun -n %{libwire} -p /sbin/ldconfig
%post -n %{libtap} -p /sbin/ldconfig
%postun -n %{libtap} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README.md README.linux
%{_mandir}/man1/[^i]*
%{_mandir}/man4/*
%{_bindir}/capinfos
%{_bindir}/captype
%{_bindir}/editcap
%{_bindir}/idl2wrs
%{_bindir}/mergecap
%{_bindir}/mmdbresolve
%{_bindir}/randpkt
%{_bindir}/rawshark
%{_bindir}/reordercap
%{_bindir}/sharkd
%{_bindir}/tethereal
%{_bindir}/text2pcap
%{_bindir}/tshark
%verify(not mode caps) %attr(0750,root,wireshark) %caps(cap_net_raw,cap_net_admin=ep) %{_bindir}/dumpcap
%{_libdir}/wireshark/
%{_datadir}/wireshark/

%files -n %{libutil}
%{_libdir}/libwsutil*.so.*

%files -n %{libwire}
%{_libdir}/libwireshark.so.*

%files -n %{libtap}
%{_libdir}/libwiretap.so.*

%files devel
%{_includedir}/wireshark
%{_includedir}/wireshark/config.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/wireshark.pc

%files ui-qt
%{_bindir}/wireshark
%{_bindir}/ethereal
%{_datadir}/applications/%{org_name}.desktop
%{_datadir}/applications/%{org_name}-su.desktop
%{_datadir}/icons/hicolor/*/apps/%{org_name}.png
%{_datadir}/icons/hicolor/*/mimetypes/%{org_name}-mimetype.png
%{_datadir}/icons/hicolor/scalable/apps/%{org_name}.svg
%{_datadir}/mime/packages/%{org_name}.xml
%{_datadir}/metainfo/%{org_name}.metainfo.xml

%post ui-qt
%desktop_database_post
%icon_theme_cache_post

%postun ui-qt
%desktop_database_postun
%icon_theme_cache_postun

%changelog
