#
# spec file for package ladish
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


%define enable_gui 0
Name:           ladish
Version:        0.3.150.g27e38d3f
Release:        0
Summary:        LADI Session Handler
License:        GPL-2.0-or-later AND AFL-2.1
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://ladish.org/
Source:         %{name}-%{version}.tar.bz2
# old version of waf doesn't work with py3
Source2:        waf-2.0.20.tar.bz2
Patch0:         ladish.compile.patch
Patch1:         ladish-python3.patch
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  dbus-1-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  intltool
BuildRequires:  lash-devel
BuildRequires:  libexpat-devel
BuildRequires:  libjack-devel
BuildRequires:  libpng16-devel
BuildRequires:  perl
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
Requires:       a2jmidid
# Technically to use ladish on its own you'd need laditools
# however we are adding it to openSUSE to use with cadence
# that will work as a front end and its therefore not needed
# laditools is currently unmaintained
Suggests:       laditools
%if %{enable_gui}
BuildRequires:  libflowcanvas5-devel
BuildRequires:  libgnomecanvasmm-devel
%endif

%description
LADI Session Handler or simply ladish is a session management system for JACK applications on GNU/Linux.

%prep
%autosetup -p1

%build
tar -xf %{SOURCE2}
cp waf-2.0.20/waf .
cp -r waf-2.0.20/waflib .
export CFLAGS="%{optflags} -Wno-error"
export CXXFLAGS="%{optflags} -Wno-unused-but-set-variable"
# --enable-pylash doesn't work with py3
/usr/bin/python3 waf configure --prefix=%{_prefix} --enable-liblash
/usr/bin/python3 waf build %{?_smp_mflags}

%install
/usr/bin/python3 waf install --destdir=%{buildroot}
%ifarch x86_64
mv "%{buildroot}/usr/lib" "%{buildroot}%{_libdir}"
%endif
%if %{enable_gui}
%suse_update_desktop_file -r -i gladish "AudioVideo;Midi;"
%else
rm %{buildroot}/%{_datadir}/applications/gladish.desktop
rm -r %{buildroot}/%{_datadir}/icons/
rm -r %{buildroot}/%{_datadir}/locale/
%endif
%fdupes -s %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%dir %{_datadir}/ladish
%{_datadir}/ladish/*
%{_bindir}/ladish_control
%{_bindir}/ladishd
%{_bindir}/jmcore
%{_bindir}/ladiconfd
%{_datadir}/dbus-1/services/org.ladish.conf.service
%{_datadir}/dbus-1/services/org.ladish.jmcore.service
%{_datadir}/dbus-1/services/org.ladish.service
%{_libdir}/libalsapid.so

%if %{enable_gui}
%{_bindir}/gladish
%{_datadir}/applications/gladish.desktop
%{_datadir}/icons/hicolor/16x16/apps/gladish.png
%{_datadir}/icons/hicolor/22x22/apps/gladish.png
%{_datadir}/icons/hicolor/24x24/apps/gladish.png
%{_datadir}/icons/hicolor/256x256/apps/gladish.png
%{_datadir}/icons/hicolor/32x32/apps/gladish.png
%{_datadir}/icons/hicolor/48x48/apps/gladish.png
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/ladish.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/ladish.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/ladish.mo
%endif

%exclude %{_includedir}/lash*
%exclude %{_libdir}/liblash.so*
%exclude %{_libdir}/pkgconfig/lash-1.0.pc
%exclude %{_libdir}/python2.7/site-packages/_lash.so
%exclude %{_libdir}/python2.7/site-packages/lash.py

%changelog
