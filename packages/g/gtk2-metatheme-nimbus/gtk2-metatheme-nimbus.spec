#
# spec file for package gtk2-metatheme-nimbus
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           gtk2-metatheme-nimbus
%define _name   nimbus
Version:        0.1.7
Release:        1
Summary:        Nimbus Metatheme for GNOME
License:        LGPL-2.0+
Url:            https://nimbus.dev.java.net/
Group:          System/GUI/GNOME
Source:         http://dlc.sun.com/osol/jds/downloads/extras/%{_name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM gtk2-metatheme-nimbus-fix-warning.patch vuntz@opensuse.org -- Fix trivial build warning
Patch0:         gtk2-metatheme-nimbus-fix-warning.patch
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  icon-naming-utils
BuildRequires:  intltool
Requires:       gtk2-engine-nimbus
Requires:       nimbus-icon-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Nimbus is the name of a look-and-feel designed by Sun for the Java
Desktop System.

%package -n gtk2-engine-nimbus
License:        LGPL-2.0+
Summary:        Nimbus GTK Theme Engine
Group:          System/GUI/GNOME
Recommends:     gtk2-metatheme-nimbus

%description -n gtk2-engine-nimbus
Nimbus is the name of a look-and-feel designed by Sun for the Java
Desktop System.

%package -n nimbus-icon-theme
License:        LGPL-2.0+
Summary:        Nimbus Icon Theme
Group:          System/GUI/GNOME
Requires:       tango-icon-theme
Recommends:     gtk2-metatheme-nimbus
%if %suse_version >= 1120
BuildArch:      noarch
%endif

%description -n nimbus-icon-theme
Nimbus is the name of a look-and-feel designed by Sun for the Java
Desktop System.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%configure --disable-static
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall
find %{buildroot} -type f -name "*.la" -delete -print
%if 0%{?suse_version} >= 1140
%icon_theme_cache_create_ghost nimbus
%endif
%fdupes %{buildroot}%{_datadir}/icons
%fdupes %{buildroot}%{_datadir}/themes

%clean
%{__rm} -rf %{buildroot}

%if 0%{?suse_version} >= 1140

%post -n nimbus-icon-theme
%icon_theme_cache_post nimbus

# No need for %%icon_theme_cache_postun in %postun since the theme won't exist anymore
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%{_datadir}/themes/nimbus
%{_datadir}/themes/dark-nimbus
%{_datadir}/themes/light-nimbus

%files -n gtk2-engine-nimbus
%defattr(-,root,root)
%{_libdir}/gtk-2.*/2.*.*/engines/libnimbus.so

%files -n nimbus-icon-theme
%defattr(-,root,root)
%if 0%{?suse_version} >= 1140
%ghost %{_datadir}/icons/nimbus/icon-theme.cache
%endif
%{_datadir}/icons/nimbus/

%changelog
