#
# spec file for package gnome-desktop2
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


%define IS_DEFAULT_GNOME_DESKTOP 0
%define _name   gnome-desktop
Name:           gnome-desktop2
Version:        2.32.1
Release:        0
Summary:        The GNOME Desktop API Library
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org
Source:         http://ftp.gnome.org/pub/GNOME/sources/%{_name}/2.32/%{_name}-%{version}.tar.bz2
Source99:       baselibs.conf
# PATCH-FEATURE-OPENSUSE gnome-desktop-recently-used-apps.patch -- Add launched .desktop files to recently used apps.
Patch3:         gnome-desktop2-recently-used-apps.patch
# PATCH-FEATURE-OPENSUSE gnome-desktop-fate300461-desktop-gettext.patch fate300461 vuntz@novell.com -- Look for translation of desktop entry strings via gettext
Patch5:         gnome-desktop2-fate300461-desktop-gettext.patch
# PATCH-FIX-UPSTREAM gnome-desktop2-one-slide-slideshow.patch bgo#630498 vuntz@opensuse.org -- Correctly handle one-slide slideshows
Patch6:         gnome-desktop2-one-slide-slideshow.patch
BuildRequires:  fdupes
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
Recommends:     %{name}-lang
Recommends:     gnome-about = %{version}
Obsoletes:      gnome-core
%if %{IS_DEFAULT_GNOME_DESKTOP}
Provides:       %{_name} = %{version}
Obsoletes:      %{_name} < %{version}
%endif

%description
This package contains some desktop-wide documents.

%if %{IS_DEFAULT_GNOME_DESKTOP}
%package -n gnome-about
Summary:        Information dialog about GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Recommends:     %{name}-lang

%description -n gnome-about
The gnome-about program helps find which version of GNOME is installed.
%endif

%package -n libgnome-desktop-2-17
Summary:        The GNOME Desktop API Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Recommends:     %{name}-lang

%description -n libgnome-desktop-2-17
The libgnome-desktop library provides API shared by several applications
on the desktop, but that cannot live in the platform for various
reasons. There is no API or ABI guarantee, although we are doing our
best to provide stability. Documentation for the API is available with
gtk-doc.

%package -n libgnome-desktop-2-devel
Summary:        The GNOME Desktop API Library -- Development Files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Requires:       libgnome-desktop-2-17 = %{version}
%if %{IS_DEFAULT_GNOME_DESKTOP}
Provides:       %{_name}-devel = %{version}
Obsoletes:      %{_name}-devel < %{version}
Provides:       %{_name}-doc = %{version}
Obsoletes:      %{_name}-doc < %{version}
%endif

%description -n libgnome-desktop-2-devel
The libgnome-desktop library provides API shared by several applications
on the desktop, but that cannot live in the platform for various
reasons. There is no API or ABI guarantee, although we are doing our
best to provide stability. Documentation for the API is available with
gtk-doc.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
translation-update-upstream
%patch3 -p1
%patch5
%patch6 -p1

%build
%configure --with-pic\
	--disable-static\
	--disable-scrollkeeper\
	--with-gnome-distributor="SUSE"\
%if ! %{IS_DEFAULT_GNOME_DESKTOP}
        --disable-gnome-about \
        --disable-desktop-docs \
%endif
        --disable-date-in-gnome-version
make %{?_smp_mflags}

%install
%make_install
%if 0%{?suse_version} <= 1110
rm %{buildroot}%{_datadir}/locale/ig/LC_MESSAGES/*
%endif
%if 0%{?suse_version} <= 1120
rm %{buildroot}%{_datadir}/locale/en@shaw/LC_MESSAGES/*
%endif
%find_lang %{_name}-2.0 %{?no_lang_C}
%if %{IS_DEFAULT_GNOME_DESKTOP}
%find_lang fdl %{?no_lang_C} %{_name}-2.0.lang
%find_lang gpl %{?no_lang_C} %{_name}-2.0.lang
%find_lang lgpl %{?no_lang_C} %{_name}-2.0.lang
%suse_update_desktop_file gnome-about Documentation
%endif
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%if %{IS_DEFAULT_GNOME_DESKTOP}
%post -n gnome-about
%desktop_database_post

%postun -n gnome-about
%desktop_database_postun
%endif

%post -n libgnome-desktop-2-17 -p /sbin/ldconfig
%postun -n libgnome-desktop-2-17 -p /sbin/ldconfig

%files
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/*.xpm

%if %{IS_DEFAULT_GNOME_DESKTOP}
%files -n gnome-about
%license COPYING

%{_bindir}/gnome-about
%{_datadir}/applications/gnome-about.desktop
%{_datadir}/gnome-about/
%{_mandir}/man1/gnome-about.1*
%endif

%files -n libgnome-desktop-2-17
%license COPYING.LIB
%doc AUTHORS NEWS README
%if %{IS_DEFAULT_GNOME_DESKTOP}
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/*/
%doc %{_datadir}/gnome/help/*/C/
%dir %{_datadir}/omf/
%dir %{_datadir}/omf/*/
%doc %{_datadir}/omf/*/*-C.omf
%endif
%{_datadir}/libgnome-desktop/
%{_libdir}/libgnome-desktop-2.so.*

%files -n libgnome-desktop-2-devel
%{_includedir}/gnome-desktop-2.0/
%{_libdir}/libgnome-desktop-2.so
%{_libdir}/pkgconfig/gnome-desktop-2.0.pc
%doc %{_datadir}/gtk-doc/html/gnome-desktop/

%files lang -f %{_name}-2.0.lang

%changelog
