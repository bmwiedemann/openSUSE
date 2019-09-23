#
# spec file for package linphone
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover   9
%bcond_with linphone_gtkui
%bcond_without linphone_cplusplus
Name:           linphone
Version:        3.12.0
Release:        0
Summary:        Web Phone
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          Productivity/Telephony/SIP/Clients
URL:            https://linphone.org/technical-corner/liblinphone/overview
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-manual.tar.bz2
Source2:        baselibs.conf
# PATCH-FIX-OPENSUSE linphone-fix-pkgconfig.patch sor.alexei@meowr.ru -- Install linphone.pc.
Patch0:         linphone-fix-pkgconfig.patch
# PATCH-FIX-OPENSUSE linphone-fix-gtkui-build.patch -- Fix building of GtkUI.
Patch1:         linphone-fix-gtkui-build.patch
# PATCH-FEATURE-OPENSUSE linphone-build-readline.patch sor.alexei@meowr.ru -- Add the ability to compile with readline to the build system.
Patch2:         linphone-build-readline.patch
# PATCH-FIX-UPSTREAM
Patch3:         reproducible.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libeXosip2-devel
BuildRequires:  libgsm-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  sgmltool
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bctoolbox) >= 0.6.0
BuildRequires:  pkgconfig(belcard)
BuildRequires:  pkgconfig(belle-sip) >= 1.6.2
BuildRequires:  pkgconfig(libavcodec) >= 51.0.0
BuildRequires:  pkgconfig(libbzrtp) >= 1.0.6
BuildRequires:  pkgconfig(libosip2)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libswscale) >= 0.7.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(libv4l2) >= 0.8.4
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mediastreamer) >= 2.16.0
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(ortp) >= 1.0.2
BuildRequires:  pkgconfig(speex) >= 1.1.6
BuildRequires:  pkgconfig(sqlite3)
%if 0%{?suse_version} >= 1500
BuildRequires:  python2
BuildRequires:  python2-six
BuildRequires:  python2-xml
%else
BuildRequires:  python
BuildRequires:  python-six
BuildRequires:  python-xml
%endif
%if %{with linphone_cplusplus}
%if 0%{?suse_version} >= 1500
BuildRequires:  python2-pystache
%else
BuildRequires:  python-pystache
%endif
%endif
%if %{with linphone_gtkui}
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libnotify)
Requires:       lib%{name}-data = %{version}
Recommends:     %{name}-cli = %{version}
Obsoletes:      %{name}-lang < %{version}
%endif

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
Group:          System/Libraries
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

%if %{with linphone_cplusplus}
%package -n lib%{name}++%{sover}
Summary:        Web Phone C++ library
Group:          System/Libraries

%description -n lib%{name}++%{sover}
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

This package contains a C++ library.
%endif

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
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       lib%{name}%{sover} = %{version}
Requires:       lib%{name}-data = %{version}
Requires:       libeXosip2-devel
Requires:       libosip2-devel
Requires:       pkgconfig(alsa)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libavcodec) >= 51.0.0
Requires:       pkgconfig(libswscale) >= 0.7.0
Requires:       pkgconfig(speex)
# linphone-devel was last used in openSUSE Leap 42.3.
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}
%if %{with linphone_cplusplus}
Requires:       lib%{name}++%{sover} = %{version}
%endif

%description -n lib%{name}-devel
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

%prep
%setup -q
%setup -q -D -T -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake \
  -DPYTHON_EXECUTABLE="%{_bindir}/python2" \
%if %{with linphone_cplusplus}
  -DENABLE_CXX_WRAPPER=ON      \
%else
  -DENABLE_CXX_WRAPPER=OFF     \
%endif
  -DENABLE_ROOTCA_DOWNLOAD=OFF \
  -DENABLE_ZRTP=ON             \
  -DENABLE_LDAP=ON             \
%if %{with linphone_gtkui}
  -DENABLE_GTK_UI=ON           \
%endif
  -DENABLE_TOOLS=OFF           \
  -DENABLE_STRICT=OFF          \
  -DENABLE_STATIC=OFF
make %{?_smp_mflags} V=1

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}/
mv -T %{buildroot}%{_datadir}/doc/%{name}-%{version}/ \
  %{buildroot}%{_docdir}/%{name}/

%if %{with linphone_gtkui}
install -Dpm 0755 share/%{name}.appdata.xml \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%suse_update_desktop_file -r -D "%{name}/index.xml.html" %{name} Network Telephony
# Remove a duplicate COPYING.
rm -f %{buildroot}%{_datadir}/%{name}/COPYING
%endif

# Install the manual.
mkdir -p %{buildroot}%{_datadir}/gnome/help/
cp -a %{name} %{buildroot}%{_datadir}/gnome/help/%{name}/
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500 && %{with linphone_gtkui}
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%post -n lib%{name}%{sover} -p /sbin/ldconfig

%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%if %{with linphone_cplusplus}
%post -n lib%{name}++%{sover} -p /sbin/ldconfig

%postun -n lib%{name}++%{sover} -p /sbin/ldconfig
%endif

%if %{with linphone_gtkui}
%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/audio-assistant.desktop
%{_datadir}/icons/hicolor/*/*/%{name}*
%{_datadir}/pixmaps/%{name}/
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%endif

%files cli
%{_bindir}/%{name}c*
%{_bindir}/%{name}-daemon*

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%files -n lib%{name}-lang -f %{name}.lang
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/

%if %{with linphone_cplusplus}
%files -n lib%{name}++%{sover}
%{_libdir}/lib%{name}++.so.%{sover}*
%endif

%files -n lib%{name}-data
%license COPYING
%doc AUTHORS NEWS README.md
%doc %{_docdir}/%{name}/
%{_datadir}/sounds/%{name}/

%files -n lib%{name}-devel
%{_includedir}/%{name}*/
%{_bindir}/lib%{name}_tester
%{_libdir}/lib%{name}.so
%if %{with linphone_cplusplus}
%{_libdir}/lib%{name}++.so
%endif
%{_datadir}/liblinphone_tester/
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/Linphone/
%if %{with linphone_cplusplus}
%{_datadir}/LinphoneCxx/
%endif

%changelog
