#
# spec file for package ekiga
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define with_evolution 1
%define with_gstreamer_0_10 0
Name:           ekiga
Version:        4.1.0
Release:        0
Summary:        A GNOME based SIP/H323 teleconferencing application
License:        SUSE-GPL-2.0-with-openssl-exception
Group:          Productivity/Telephony/SIP/Clients
Url:            http://www.ekiga.org/
#Source:         http://download.gnome.org/sources/ekiga/4.0/%{name}-%{version}.tar.xz
Source:         ekiga-12641b735a9886a080949465d4da6d4569822ed2.tar.bz2
# PATCH-FIX-UPSTREAM boost-configure.patch schwab@suse.de -- AX_BOOST_BASE: add aarch64 to the list of lib64 architectures
Patch0:         boost-configure.patch
# PATCH-FIX-UPSTREAM ekiga-appdata.patch badshah400@gmail.com -- Add, translate and install appstream metainfo file taken from upstream git
Patch1:         ekiga-appdata.patch
Patch2:         ekiga-audiooutput-fallback-to-primary-device-if-secondary.patch
# PATCH-FIX-OPENSUSE ekiga-4.0.1-libresolv.patch mcrha@redhat.com -- Add a patch to avoid libresolv check for res_gethostbyaddr()
# Sourced from: https://src.fedoraproject.org/cgit/rpms/ekiga.git/commit/?id=dbf5f5ba449d22bd79f0394cddb7d4d8a88ec6ac
Patch3:         ekiga-4.0.1-libresolv.patch
# PATCH-FIX-UPSTREAM ekiga-dont-require-gnome-icon-theme.patch badshah400@opensuse.org -- Patch configure.ac to not check for gnome-icon-theme; all required icons are already in hicolor-icon-theme.
Patch4:         ekiga-dont-require-gnome-icon-theme.patch
Patch5:         ekiga-po-Makefile.patch
Patch6:         ekiga-signals2-leftover.patch
Patch7:         ekiga-missing-includes.patch

%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gconf2-devel
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  gtk3-devel
BuildRequires:  clutter-gtk-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  libgudev-1_0-devel
BuildRequires:  intltool
BuildRequires:  libavahi-glib-devel
BuildRequires:  libnotify-devel
BuildRequires:  libopal-devel >= 3.10.10
BuildRequires:  libpt-devel >= 2.10.10
BuildRequires:  libsigc++2-devel
BuildRequires:  libsoup-devel
BuildRequires:  libv4l-devel
BuildRequires:  openldap2-devel
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(xv)
BuildRequires:  gettext
# Required for Patch1
BuildRequires:  libtool
Requires:       hicolor-icon-theme
Recommends:     %{name}-lang
Provides:       gnomemeeting = %{version}
Obsoletes:      gnomemeeting < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{gconf_schemas_prereq}
%if %{with_evolution}
BuildRequires:  evolution-data-server-devel
%endif
%if %{with_gstreamer_0_10}
BuildRequires:  gstreamer-0_10-plugins-base-devel
%endif
%if ! %{with_evolution}
# In case we cannot build the evolution plugin, we obsolete the sub package
Obsoletes:      ekiga-plugins-evolution < %{version}
%endif

%description
Ekiga (formely known as GnomeMeeting) is an open source VoIP and video
conferencing application for GNOME. Ekiga uses both the H.323 and SIP
protocols. It supports many audio and video codecs, and is
interoperable with other SIP compliant software and also with Microsoft
NetMeeting.

%if %{with_gstreamer_0_10}
%package -n ekiga-plugins-gstreamer
Summary:        Gstreamer plugin for %{name}
Group:          System/Libraries
Supplements:    packageand(ekiga:pulseaudio)

%description -n ekiga-plugins-gstreamer
This plugin enables gstreamer support in %{name}.
%endif

%if %{with_evolution}
%package -n ekiga-plugins-evolution
Summary:        Evolution plugin for %{name}
Group:          System/Libraries
Supplements:    packageand(ekiga:evolution-data-server)

%description -n ekiga-plugins-evolution
This plugin enables evolution support in %{name}.
%endif

%lang_package

%prep
%setup -q -n ekiga
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
translation-update-upstream
cp -av /usr/share/gnome-doc-utils/gnome-doc-utils.make .

%build
%if 0%{?suse_version} < 1500
export CXXFLAGS="%optflags -fexceptions"
%endif
autoreconf -fi
%configure \
    --disable-schemas-install \
    --disable-scrollkeeper \
    --enable-dbus \
%if %{with_gstreamer_0_10}
    --enable-gstreamer \
%endif
    --enable-xcap \
    --enable-avahi \
%if %{with_evolution}
    --enable-eds
%else
    --disable-eds
%endif
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
%find_gconf_schemas
%find_lang %{name} %{?no_lang_C}
cat %{name}.schemas_list >%{name}.lst
%suse_update_desktop_file %{name}
%fdupes %{buildroot}

%pre -f %{name}.schemas_pre

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%endif

%preun -f %{name}.schemas_preun

%posttrans -f %{name}.schemas_posttrans

%if 0%{?suse_version} < 1500
%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files -f %{name}.lst
%defattr(-,root,root)
%doc ChangeLog README FAQ
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/%{name}/
%doc %{_datadir}/gnome/help/%{name}/C/
%dir %{_datadir}/omf/
%dir %{_datadir}/omf/%{name}/
%doc %{_datadir}/omf/%{name}/%{name}-C.omf
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{version}/
%dir %{_libdir}/%{name}/%{version}/plugins/
%{_bindir}/*
%{_datadir}/applications/ekiga.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/hicolor/*/apps/ekiga.png
%{_datadir}/pixmaps/ekiga
%{_datadir}/sounds/ekiga
%{_libdir}/ekiga/%{version}/libekiga.so
%{_libdir}/ekiga/%{version}/plugins/libgmavahi.so
%{_libdir}/ekiga/%{version}/plugins/libgmldap.so
%{_libdir}/ekiga/%{version}/plugins/libgmlibnotify.so
%{_libdir}/ekiga/%{version}/plugins/libgmresource_list.so
%{_libdir}/ekiga/%{version}/plugins/libgmxcap.so
%{_mandir}/man1/ekiga.1*
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml

%if %{with_gstreamer_0_10}
%files -n ekiga-plugins-gstreamer
%defattr(-,root,root)
%{_libdir}/ekiga/%{version}/plugins/libgmgstreamer.so
%endif

%if %{with_evolution}
%files -n ekiga-plugins-evolution
%defattr(-,root,root)
%{_libdir}/ekiga/%{version}/plugins/libgmevolution.so
%endif

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
