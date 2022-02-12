#
# spec file for package linphone
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


%define ldaplibdir %{buildroot}%{_libexecdir}/%{name}
%define sover   10
Name:           linphone
Version:        5.0.67
Release:        0
Summary:        Web Phone
License:        GPL-3.0-only
Group:          Productivity/Telephony/SIP/Clients
URL:            https://linphone.org/technical-corner/liblinphone/
Source:         https://gitlab.linphone.org/BC/public/liblinphone/-/archive/%{version}/liblinphone-%{version}.tar.bz2
Source1:        %{name}-manual.tar.bz2
Source3:        https://gitlab.linphone.org/BC/public/external/openldap/-/archive/bc/openldap-bc.tar.bz2
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
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libeXosip2-devel
BuildRequires:  libgsm-devel
BuildRequires:  lime-devel >= 5.0.0
#BuildRequires:  openldap2-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-pystache
BuildRequires:  python3-six
BuildRequires:  python3-xml
BuildRequires:  readline-devel
BuildRequires:  sgmltool
BuildRequires:  soci-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  xsd
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bctoolbox) >= 5.0.0
BuildRequires:  pkgconfig(belcard) >= 4.5.0
BuildRequires:  pkgconfig(belle-sip) >= 5.0.0
BuildRequires:  pkgconfig(libavcodec) >= 51.0.0
BuildRequires:  pkgconfig(libbzrtp) >= 5.0.0
BuildRequires:  pkgconfig(libosip2)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libswscale) >= 0.7.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(libv4l2) >= 0.8.4
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mediastreamer) >= 5.0.0
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(ortp) >= 5.0.0
BuildRequires:  pkgconfig(speex) >= 1.1.6
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xerces-c)
#for openldap
BuildRequires:  chrpath
BuildRequires:  db-devel
BuildRequires:  openslp-devel

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
Recommends:     lib%{name}-lang
Provides:       lib%{name} = %{version}

%description -n lib%{name}%{sover}
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

This package contains a library.

%lang_package -n lib%{name}

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
%setup -q -n liblinphone-%{version} -D -T -a 1

%build
#START build belledonne's libldap
mkdir aux
tar fx %{SOURCE3} -C aux
cd aux/openldap-bc
LDFLAGS="-Wl,-rpath,%ldaplibdir" ./configure \
  --enable-static=no \
  --enable-slapd=no  \
  --enable-wrappers=no \
  --enable-spasswd   \
  --with-tls=openssl \
  --with-cyrus-sasl  \
  --enable-crypt     \
  --enable-ipv6=yes  \
  --enable-rewrite   \
  --enable-slp       \
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
  -DOPENLDAP_INCLUDE_DIRS=$PWD/../aux/include \
  -DLDAP_LIB=%{ldaplibdir}/libldap.so \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,-rpath,%{ldaplibdir}" \
  -DENABLE_DOC=ON              \
  -DCMAKE_BUILD_TYPE=Release   \
  -DENABLE_ROOTCA_DOWNLOAD=OFF \
  -DENABLE_ZRTP=ON             \
  -DENABLE_LDAP=ON             \
  -DENABLE_TOOLS=OFF           \
  -DENABLE_STRICT=OFF          \
  -DENABLE_STATIC=OFF          \
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
#remove unnecessary files
rm %{ldaplibdir}/*.{la,so}
#fix rpath in openldap libs and make them executable
find %{ldaplibdir} -type f -exec chrpath -r %{_libexecdir}/%{name} {} \; -exec chmod a+x {} \;
#fix rpath in liblinphone
find %{buildroot}%{_libdir} -type f -name "liblinphone*" -exec chrpath -r %{_libexecdir}/%{name} {} \;

# Install the manual.
mkdir -p %{buildroot}%{_datadir}/gnome/help/
cp -a %{name} %{buildroot}%{_datadir}/gnome/help/%{name}/
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/
#disable rpmlint complain about rpath
export NO_BRP_CHECK_RPATH=true

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig
%post -n lib%{name}++%{sover} -p /sbin/ldconfig
%postun -n lib%{name}++%{sover} -p /sbin/ldconfig

%files cli
%{_bindir}/%{name}c*
%{_bindir}/%{name}-daemon*

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/

%files -n lib%{name}-lang -f %{name}.lang
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/

%files -n lib%{name}++%{sover}
%{_libdir}/lib%{name}++.so.%{sover}*

%files -n lib%{name}-data
%license LICENSE.txt LICENSE.openldap
%doc CHANGELOG.md README.md
%{_datadir}/%{name}/
%{_datadir}/sounds/%{name}/
%{_datadir}/belr/grammars/*_grammar

%files -n lib%{name}-devel
%{_includedir}/%{name}*/
%{_bindir}/lib%{name}_tester
%{_bindir}/groupchat_benchmark
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}++.so
%{_datadir}/liblinphone_tester/
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/Linphone/
%{_datadir}/LinphoneCxx/
%{_datadir}/doc/lib%{name}-5.0.0/

%changelog
