#
# spec file for package linphone
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


%define ldaplibdir %{buildroot}%{_libexecdir}/%{name}
#use_system_ldap set to 0 because liblinphone 5.x fails to build with system ldap
%define use_system_ldap 0
%define static_ldap 1
%if !0%{?static_ldap}
%define __provides_exclude ^(libldap\\.so.*|liblber\\.so.*)$
%define __requires_exclude ^(libldap\\.so.*|liblber\\.so.*)$
%endif
%define sover   10
%if 0%{?suse_version} >= 1600
%bcond_with slp
%else
%bcond_without slp
%endif
Name:           linphone
Version:        5.3.95
Release:        0
Summary:        Web Phone
License:        AGPL-3.0-or-later
Group:          Productivity/Telephony/SIP/Clients
URL:            https://linphone.org/technical-corner/liblinphone/
Source:         https://gitlab.linphone.org/BC/public/liblinphone/-/archive/%{version}/liblinphone-%{version}.tar.bz2
Source3:        https://gitlab.linphone.org/BC/public/external/openldap/-/archive/bc/openldap-bc.tar.bz2
Source11:       ITS#10011-1.patch
Source12:       ITS#10011-2.patch
Source13:       ITS#10011-3.patch
# PATCH-FIX-OPENSUSE linphone-fix-pkgconfig.patch sor.alexei@meowr.ru -- Install linphone.pc.
Patch0:         linphone-fix-pkgconfig.patch
# PATCH-FEATURE-OPENSUSE linphone-build-readline.patch sor.alexei@meowr.ru -- Add the ability to compile with readline to the build system.
Patch1:         linphone-build-readline.patch
# PATCH-FIX-UPSTREAM
Patch2:         reproducible.patch
# PATCH-FIX-OPENSUSE linphone-link-soci-sqlite3.patch -- force linking to libsoci_sqlite3 so that RPM finds the requirement boo#1140595 -- code@bnavigator.de
Patch3:         linphone-link-soci-sqlite3.patch
# PATCH-FIX-OPENSUSE linphone-build-jsoncpp.patch -- use pkgconfig to find jsoncpp and link against jsoncpp, not jsoncpp_object
Patch4:         linphone-build-jsoncpp.patch
Patch5:         set_current_version.patch
BuildRequires:  cmake >= 3.22
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  jsoncpp-devel
BuildRequires:  libeXosip2-devel
BuildRequires:  libgsm-devel
BuildRequires:  lime-devel >= %{version}
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-pystache
BuildRequires:  python3-six
BuildRequires:  python3-xml
BuildRequires:  readline-devel
BuildRequires:  sgmltool
%if 0%{?suse_version} >= 1600
BuildRequires:  liboqs-devel
# At the time of writing (22/Dec/2023), PQCE is only available on Tumbleweed.
BuildRequires:  postquantumcryptoengine-devel >= 5.3.0~git.20230802
%endif
BuildRequires:  db-devel
BuildRequires:  soci-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bctoolbox) >=  %{version}
BuildRequires:  pkgconfig(belcard) >= %{version}
BuildRequires:  pkgconfig(belle-sip) >= %{version}
BuildRequires:  pkgconfig(libavcodec) >= 51.0.0
BuildRequires:  pkgconfig(libbzrtp) >= %{version}
BuildRequires:  pkgconfig(libosip2)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libswscale) >= 0.7.0
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(libv4l2) >= 0.8.4
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mediastreamer) >= %{version}
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(ortp) >= %{version}
BuildRequires:  pkgconfig(speex) >= 1.1.6
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xerces-c)
BuildRequires:  pkgconfig(zxing)
%if %{with slp}
BuildRequires:  openslp-devel
%endif
BuildRequires:  chrpath
BuildRequires:  libtool

%description
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

%package cli
Summary:        Web Phone Command Line Interface
Group:          Productivity/Telephony/SIP/Clients
Requires:       lib%{name}-data = %{version}

%description cli
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

This package contains the command line interface.

%package -n lib%{name}%{sover}
Summary:        Web Phone library
Group:          Productivity/Telephony/SIP/Clients
Provides:       lib%{name} = %{version}

%description -n lib%{name}%{sover}
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

This package contains a library.

%package -n lib%{name}++%{sover}
Summary:        Web Phone C++ library
Group:          Productivity/Telephony/SIP/Clients

%description -n lib%{name}++%{sover}
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

This package contains a C++ library.

%package -n lib%{name}-data
Summary:        Web Phone data files
Group:          Productivity/Telephony/SIP/Clients
BuildArch:      noarch

%description -n lib%{name}-data
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

This package contains data files such as sounds.

%package -n lib%{name}-devel
Summary:        Web Phone Development files
Group:          Development/Languages/C and C++
Requires:       glibc-devel
Requires:       lib%{name}%{sover} = %{version}
Requires:       lib%{name}++%{sover} = %{version}
Requires:       lib%{name}-data = %{version}
Requires:       libeXosip2-devel
Requires:       libosip2-devel
Requires:       soci-devel
Requires:       soci-sqlite3-devel
Requires:       pkgconfig(alsa)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libavcodec) >= 51.0.0
Requires:       pkgconfig(libswscale) >= 0.7.0
Requires:       pkgconfig(speex)
# linphone-devel was last used in openSUSE Leap 42.3.
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}

%description -n lib%{name}-devel
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

%prep
%autosetup -n liblinphone-%{version} -p1

%build
#START build belledonne's libldap
mkdir aux
tar fx %{SOURCE3} -C aux
cd aux/openldap-bc
patch -p1 <%SOURCE11
patch -p1 <%SOURCE12
patch -p1 <%SOURCE13
autoreconf -vif
LDFLAGS="-Wl,-rpath,%ldaplibdir" ./configure \
  --enable-static=yes \
  --enable-shared=no \
  --with-pic         \
  --enable-slapd=no  \
  --enable-wrappers=no \
  --enable-spasswd   \
  --with-tls=openssl \
  --with-cyrus-sasl  \
  --enable-crypt     \
  --enable-ipv6=yes  \
  --enable-rewrite   \
%if %{with slp}
  --enable-slp       \
%endif
  --enable-lmpasswd  \
  --with-yielding-select \
  --prefix=$PWD/..   \
  --libdir=%{ldaplibdir}
make depend
make %{?_smp_mflags}
# do a preliminary install, because libldap is needed to build liblinphone
make install
cd ../..
#END build belledonne's libldap
#find and use belledonne's libldap
sed -i "/OPENLDAP_INCLUDE_DIRS/,/LDAP_LIB/s@\${CMAKE_INSTALL_PREFIX}@$PWD/aux@;s@\${CMAKE_INSTALL_PREFIX}@%{ldaplibdir}@;s@include/openldap@include@" cmake/FindOpenLDAP.cmake

%cmake \
  -DPYTHON_EXECUTABLE="%{_bindir}/python3" \
  -DENABLE_CXX_WRAPPER=ON      \
  -D_OpenLDAP_INCLUDE_DIRS=$PWD/../aux/include \
  -D_OpenLDAP_LIBRARY=%{ldaplibdir}/libldap.a \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,-rpath,%{ldaplibdir}" \
  -DENABLE_DOC=ON              \
  -DCMAKE_BUILD_TYPE=Release   \
  -DENABLE_ROOTCA_DOWNLOAD=OFF \
  -DENABLE_ZRTP=ON             \
  -DENABLE_LDAP=ON             \
  -DENABLE_TOOLS=OFF           \
  -DENABLE_STRICT=OFF          \
  -DENABLE_STATIC=OFF          \
  -DENABLE_FLEXIAPI=OFF        \
%if 0%{?suse_version} > 1500
  -DENABLE_QRCODE=OFF          \
%endif
  -DCMAKE_LINK_WHAT_YOU_USE=ON

%cmake_build

%install
#START reinstall belledonne's libldap
cd aux/openldap-bc
make install
cd ../..
cp aux/openldap-bc/LICENSE LICENSE.openldap
#END reinstall belledonne's libldap
%cmake_install
rm -r %{ldaplibdir}
rm %{buildroot}/%{_datadir}/LibLinphone/cmake/FindOpenLDAP.cmake
sed -i '59 a find_package(libxml2 REQUIRED)' %{buildroot}%{_datadir}/LibLinphone/cmake/LibLinphoneTargets.cmake
sed -i '60 a find_package(SQLite3 REQUIRED)' %{buildroot}%{_datadir}/LibLinphone/cmake/LibLinphoneTargets.cmake

mkdir -p %{buildroot}/%{_libdir}/liblinphone/plugins

chrpath -d %{buildroot}%{_libdir}/lib%{name}.so.%{sover}* %{buildroot}%{_libdir}/lib%{name}++.so.%{sover}*
chrpath -d %{buildroot}%{_bindir}/{linphone-daemon-pipetest,linphone-daemon,liblinphone-groupchat-benchmark,liblinphone-tester}

%fdupes %{buildroot}%{_datadir}/

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig
%post -n lib%{name}++%{sover} -p /sbin/ldconfig
%postun -n lib%{name}++%{sover} -p /sbin/ldconfig

%files cli
%{_bindir}/%{name}-daemon*

%files -n lib%{name}%{sover}
%dir %{_libdir}/lib%{name}
%dir %{_libdir}/lib%{name}/plugins
%{_libdir}/lib%{name}.so.%{sover}*

%files -n lib%{name}++%{sover}
%{_libdir}/lib%{name}++.so.%{sover}*

%files -n lib%{name}-data
%license LICENSE.txt
%if !0%{?use_system_ldap}
%license LICENSE.openldap
%endif
%doc CHANGELOG.md README.md
%{_datadir}/%{name}/
%{_datadir}/sounds/%{name}/
%{_datadir}/belr/grammars/*_grammar

%files -n lib%{name}-devel
%{_includedir}/%{name}*/
%{_bindir}/lib%{name}-tester
%{_bindir}/liblinphone-groupchat-benchmark
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}++.so
%{_datadir}/liblinphone-tester/
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_datadir}/LibLinphone/
%dir %{_datadir}/LibLinphone/cmake
%{_datadir}/LibLinphone/cmake/*
%dir %{_datadir}/LinphoneCxx/
%dir %{_datadir}/LinphoneCxx/cmake
%{_datadir}/LinphoneCxx/cmake/*
%{_datadir}/doc/lib%{name}-%{version}/

%changelog
