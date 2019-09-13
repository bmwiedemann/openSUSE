#
# spec file for package libbonobo
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


Name:           libbonobo
Version:        2.32.1
Release:        0
Summary:        The Bonobo Component System for the GNOME 2.x Desktop Platform
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Url:            http://www.gnome.org/
#
Source:         http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.32/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE bonobo-activation-config.patch vuntz@opensuse.org -- Fix activation
Patch2:         bonobo-activation-config.patch
# PATCH-FIX-OPENSUSE libbonobo-lib64.patch vuntz@opensuse.org -- Handle libdir in addition to libexecdir on 64-bit machines for .server files
Patch3:         libbonobo-lib64.patch
# PATCH-FEATURE-OPENSUSE libbonobo-fate300461-server-gettext.patch fate300461 vuntz@novell.com -- Look for translation of .server files via gettext
Patch4:         libbonobo-fate300461-server-gettext.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libxml2-devel
BuildRequires:  orbit2-devel
BuildRequires:  popt-devel
BuildRequires:  translation-update-upstream
Recommends:     %{name}-lang = %{version}
# Obsolete for >=9.1:
Obsoletes:      bonobo-activation
Provides:       bonobo-activation

%description
Bonobo is a component system for the GNOME platform. Libbonobo is the
new version for the GNOME 2.x Desktop platform.

%package devel
Summary:        Development files for the Bonobo Component System
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       glib2-devel
Requires:       orbit2-devel
Requires:       popt-devel
# Obsolete for >=9.1:
Obsoletes:      bonobo-activation-devel
Provides:       bonobo-activation-devel
#

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package doc
Summary:        Additional Package Documentation for bonobo
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
# Obsolete for >=9.1:
Obsoletes:      bonobo-activation-doc
Provides:       bonobo-activation-doc

%description doc
Bonobo is a component system for the GNOME platform. Libbonobo is the
new version for the GNOME 2.x platform.

%lang_package

%prep
%setup -q
translation-update-upstream
%patch2
%if "%{_lib}" == "lib64"
%patch3 -p1
%endif
%patch4 -p1

%build
%configure --disable-static
echo "#undef G_DISABLE_DEPRECATED" >> config.h
# Do not use parallel build.. to many random fallouts
make -j1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%if "%{_lib}" == "lib64"
# we need to create the arch-independent directory for .servers file
install -d %{buildroot}%{_libexecdir}/bonobo/servers
%endif
%find_lang libbonobo-2.0
%fdupes %{buildroot}/%{_prefix}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_sbindir}/bonobo-activation-sysconf
%{_libdir}/*.so.*
%{_libdir}/bonobo/
%if "%{_libdir}" != "%{_libexecdir}"
%{_libexecdir}/bonobo/
%endif
%{_libexecdir}/bonobo-activation-server
%{_libdir}/orbit-2.0/*.so
%{_mandir}/man?/*%{ext_man}
%dir %{_sysconfdir}/bonobo-activation
%config %{_sysconfdir}/bonobo-activation/bonobo-activation-config.xml

%files lang -f libbonobo-2.0.lang

%files devel
%{_datadir}/idl/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_datadir}/gtk-doc/html/*
%dir %{_libdir}/bonobo-2.0
%{_libdir}/bonobo-2.0/samples

%changelog
