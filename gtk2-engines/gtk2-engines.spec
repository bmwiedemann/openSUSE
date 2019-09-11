#
# spec file for package gtk2-engines
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gtk2-engines
%define _name gtk-engines
Summary:        GTK+ 2 Theme Engines
License:        LGPL-2.1+
Group:          System/GUI/GNOME
Version:        2.20.2
Release:        0
# FIXME: On new version, change <= Obsoletes to < (last checked: 2.20.2)
# FIXME: On new versions, check if bgo#607127 is solved, and if it is, enable
# the lua engine: uncomment lua-devel BuildRequires and configure options.
Url:            http://www.gnome.org
Source:         %{_name}-%{version}.tar.bz2
Source1:        README.openSUSE
Source99:       baselibs.conf
#
Patch0:         gtk-engines-bnc546966-clearlooks-fix-main-menu-icon-size.patch
# PATCH-FIX-UPSTREAM gtk-engines-glib.patch bgo#664914 dimstar@opensuse.org -- FIx build with new glib: only glib.h can be included.
Patch1:         gtk-engines-glib.patch
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  pkg-config
# See comment below on why this is disabled
#BuildRequires:  lua-devel
# We require the exact version of gtk2 we were compiled with since the engines are located in a versioned directory
%define gtk2_ver %(rpm -q --whatprovides --qf '%%{version}' gtk2)
Requires:       gtk2-engine-clearlooks
Requires:       gtk2-engine-crux
Requires:       gtk2-engine-glide
Requires:       gtk2-engine-hcengine
Requires:       gtk2-engine-industrial
Requires:       gtk2-engine-mist
Requires:       gtk2-engine-redmond95
Requires:       gtk2-engine-thinice
Requires:       gtk2-theme-clearlooks
Requires:       gtk2-theme-crux
Requires:       gtk2-theme-industrial
Requires:       gtk2-theme-mist
Requires:       gtk2-theme-redmond95
Requires:       gtk2-theme-thinice
# Prevent missing engine failures on bi-arch systems:
%ifarch x86_64 s390x
Recommends:     %{name}-32bit = %{version}
%endif
Enhances:       gtk2
# gnome-themes had Industrial before this version (<= SuSE Linux 9.2, <= NLD9).
Conflicts:      gnome-themes < 2.11.90
# For smooth upgrades: we removed translations during 12.2 development
# FIXME: should be < with next version (last checked: 2.20.2)
Obsoletes:      %{name}-lang <= %{version}
Provides:       gtk2-engines-lang = 2.14.1
Obsoletes:      gtk2-engines-lang < 2.14.1
# bug437293
%ifarch ppc64
Obsoletes:      gnome-themes-64bit
Obsoletes:      gtk2-engines-64bit
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package installs the theme engine libraries for GTK+ 2.

%package devel
Summary:        Development files for gtk2-engines
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
This package contains development files for gtk2-engines.

%package -n gtk2-engine-clearlooks
Summary:        Clearlooks GTK+ 2 Theme Engine
Group:          System/GUI/GNOME
Requires:       gtk2 = %{gtk2_ver}
Recommends:     gtk2-theme-clearlooks = %{version}

%description -n gtk2-engine-clearlooks
The Clearlooks engine was the default theme of GNOME 2 since 2.12. It is
a modular engine providing multiple styles such as glossy and gummy.

%package -n gtk2-theme-clearlooks
Summary:        Clearlooks Theme for GTK+ 2
Group:          System/GUI/GNOME
Requires:       gtk2-engine-clearlooks = %{version}
BuildArch:      noarch

%description -n gtk2-theme-clearlooks
This package provides the Clearlooks GTK+ 2 theme.

%package -n gtk2-engine-crux
Summary:        Crux GTK+ 2 Theme Engine
Group:          System/GUI/GNOME
Requires:       gtk2 = %{gtk2_ver}
Recommends:     gtk2-theme-crux = %{version}

%description -n gtk2-engine-crux
The Crux engine was a popular theme in the early GNOME 2 days.

%package -n gtk2-theme-crux
Summary:        Crux Theme for GTK+ 2
Group:          System/GUI/GNOME
Requires:       gtk2-engine-crux = %{version}
BuildArch:      noarch

%description -n gtk2-theme-crux
This package provides the Crux GTK+ 2 theme.

%package -n gtk2-engine-glide
Summary:        Glide GTK+ 2 Theme Engine
Group:          System/GUI/GNOME
Requires:       gtk2 = %{gtk2_ver}

%description -n gtk2-engine-glide
This packages provides the Glide engine for GTK+ 2, originally written
for the Glider theme.

%package -n gtk2-engine-hcengine
Summary:        HC GTK+ 2 Theme Engine
Group:          System/GUI/GNOME
Requires:       gtk2 = %{gtk2_ver}

%description -n gtk2-engine-hcengine
The High Contrast engine is targeted for usability themes, such as the
GNOME HighContrast theme.

%package -n gtk2-engine-industrial
Summary:        Industrial GTK+ 2 Theme Engine
Group:          System/GUI/GNOME
Requires:       gtk2 = %{gtk2_ver}
Recommends:     gtk2-theme-industrial = %{version}

%description -n gtk2-engine-industrial
The Industrial engine provides a simple and consistent appearance for
applications.

%package -n gtk2-theme-industrial
Summary:        Industrial Theme for GTK+ 2
Group:          System/GUI/GNOME
Requires:       gtk2-engine-industrial = %{version}
BuildArch:      noarch

%description -n gtk2-theme-industrial
This package provides the Industrial GTK+ 2 theme.

%package -n gtk2-engine-mist
Summary:        Mist GTK+ 2 Theme Engine
Group:          System/GUI/GNOME
Requires:       gtk2 = %{gtk2_ver}
Recommends:     gtk2-theme-mist = %{version}

%description -n gtk2-engine-mist
The Mist engine is a minimalist engine designed to provide a simple UI
experience.

%package -n gtk2-theme-mist
Summary:        Mist Theme for GTK+ 2
Group:          System/GUI/GNOME
Requires:       gtk2-engine-mist = %{version}
BuildArch:      noarch

%description -n gtk2-theme-mist
This package provides the Mist GTK+ 2 theme.

%package -n gtk2-engine-redmond95
Summary:        Redmond GTK+ 2 Theme Engine
Group:          System/GUI/GNOME
Requires:       gtk2 = %{gtk2_ver}
Recommends:     gtk2-theme-redmond95 = %{version}

%description -n gtk2-engine-redmond95
The Redmond engine and theme are designed to mimic the appearance of
another well known OS.

%package -n gtk2-theme-redmond95
Summary:        Redmond Theme for GTK+ 2
Group:          System/GUI/GNOME
Requires:       gtk2-engine-redmond95 = %{version}
BuildArch:      noarch

%description -n gtk2-theme-redmond95
The Redmond engine and theme are designed to mimic the appearance of
another well known OS.

%package -n gtk2-engine-thinice
Summary:        ThinIce GTK+ 2 Theme Engine
Group:          System/GUI/GNOME
Requires:       gtk2 = %{gtk2_ver}
Recommends:     gtk2-theme-thinice = %{version}

%description -n gtk2-engine-thinice
The ThinIce engine features thin edges and Icy Colors, and provides a
simple mostly clean appearance many find satisfying.

%package -n gtk2-theme-thinice
Summary:        ThinIce Theme for GTK+ 2
Group:          System/GUI/GNOME
Requires:       gtk2-engine-thinice = %{version}
BuildArch:      noarch

%description -n gtk2-theme-thinice
This package provides the ThinIce GTK+ 2 theme.

%prep
%setup -q -n %{_name}-%{version}
cp -a %{S:1} .
%patch0 -p1
%patch1 -p1

%build
%configure \
        --enable-animation
#        --enable-lua \
#        --with-system-lua
make %{?jobs:-j%jobs}

%install
%makeinstall
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.*a
# Remove translations: they are only needed to generate translations in xml files
rm %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/%{_name}.mo
# Fix spurious-executable-perm on source files; test will fail if we can remove this
test -x engines/mist/AUTHORS
chmod a-x engines/mist/AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README README.openSUSE

%files -n gtk2-engine-clearlooks
%defattr(-, root, root)
%doc engines/clearlooks/AUTHORS COPYING NEWS README
%{_libdir}/gtk-2.0/*/engines/libclearlooks.so
%dir %{_datadir}/gtk-engines/
%{_datadir}/gtk-engines/clearlooks.xml

%files -n gtk2-theme-clearlooks
%defattr(-, root, root)
%{_datadir}/themes/Clearlooks/

%files -n gtk2-engine-crux
%defattr(-, root, root)
%doc engines/crux/AUTHORS COPYING NEWS README
%{_libdir}/gtk-2.0/*/engines/libcrux-engine.so
%dir %{_datadir}/gtk-engines/
%{_datadir}/gtk-engines/crux-engine.xml

%files -n gtk2-theme-crux
%defattr(-, root, root)
%{_datadir}/themes/Crux/

%files -n gtk2-engine-glide
%defattr(-, root, root)
%doc engines/glide/AUTHORS COPYING NEWS README
%{_libdir}/gtk-2.0/*/engines/libglide.so
%dir %{_datadir}/gtk-engines/
%{_datadir}/gtk-engines/glide.xml

%files -n gtk2-engine-hcengine
%defattr(-, root, root)
%doc engines/hc/AUTHORS COPYING NEWS README
%{_libdir}/gtk-2.0/*/engines/libhcengine.so
%dir %{_datadir}/gtk-engines/
%{_datadir}/gtk-engines/hcengine.xml

%files -n gtk2-engine-industrial
%defattr(-, root, root)
%doc engines/industrial/AUTHORS COPYING NEWS README
%{_libdir}/gtk-2.0/*/engines/libindustrial.so
%dir %{_datadir}/gtk-engines/
%{_datadir}/gtk-engines/industrial.xml

%files -n gtk2-theme-industrial
%defattr(-, root, root)
%{_datadir}/themes/Industrial/

%files -n gtk2-engine-mist
%defattr(-, root, root)
%doc engines/mist/AUTHORS COPYING NEWS README
%{_libdir}/gtk-2.0/*/engines/libmist.so
%dir %{_datadir}/gtk-engines/
%{_datadir}/gtk-engines/mist.xml

%files -n gtk2-theme-mist
%defattr(-, root, root)
%{_datadir}/themes/Mist/

%files -n gtk2-engine-redmond95
%defattr(-, root, root)
%doc engines/redmond/AUTHORS COPYING NEWS README
%{_libdir}/gtk-2.0/*/engines/libredmond95.so
%dir %{_datadir}/gtk-engines/
%{_datadir}/gtk-engines/redmond95.xml

%files -n gtk2-theme-redmond95
%defattr(-, root, root)
%{_datadir}/themes/Redmond/

%files -n gtk2-engine-thinice
%defattr(-, root, root)
%doc engines/thinice/AUTHORS COPYING NEWS README
%{_libdir}/gtk-2.0/*/engines/libthinice.so
%dir %{_datadir}/gtk-engines/
%{_datadir}/gtk-engines/thinice.xml

%files -n gtk2-theme-thinice
%defattr(-, root, root)
%{_datadir}/themes/ThinIce/

%files devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/*.pc

%changelog
