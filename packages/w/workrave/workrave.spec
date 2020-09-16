#
# spec file for package workrave
#
# Copyright (c) 2020 SUSE LLC
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


%define upstream_version    1_10_44
Name:           workrave
Version:        1.10.44
Release:        0
Summary:        Recovery and prevention of Repetitive Strain Injury program
License:        GPL-3.0-only
Group:          Productivity/Other
URL:            http://www.workrave.org
Source:         https://github.com/rcaelers/workrave/archive/v%{upstream_version}.tar.gz
Source2:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  libpulse-devel
BuildRequires:  libtool
BuildRequires:  python-xml
BuildRequires:  python3-Jinja2
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-devel
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(sigc++-2.0)
# other requirements that are documented or previously used but (currently?) not needed. let's see if there are problems without them
#BuildRequires:  gdome2-devel
#BuildRequires:  gnome-panel-devel
#BuildRequires:  libbonobo-devel
#BuildRequires:  libgmodule-2_0-0
#BuildRequires:  libgthread-2_0-0
#BuildRequires:  pkg-config
#BuildRequires:  pkgconfig(glib-2.0)
#BuildRequires:  pkgconfig(gstreamer-0.10)
#BuildRequires:  gconfmm-devel
#BuildRequires:  xorg-x11-Xvfb

%description
Workrave is a program that assists in the recovery and prevention of Repetitive Strain Injury (RSI). The program frequently alerts you to take micro-pauses, rest breaks and restricts you to your daily limit.

%package devel
Summary:        Development Files for %{name}
Group:          Development/Libraries/Other

%description devel
This package contains header files needed for developing plugins for
Workrave.

%package -n typelib-1_0-Workrave-1_0
Summary:        Introspection bindings for Workrave
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n typelib-1_0-Workrave-1_0
This package contains typelib files needed for developing plugins for
Workrave.

%prep
%setup -q -n %{name}-%{upstream_version}

%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}/%{_libdir} -type f -name "*.la" -delete
%suse_update_desktop_file %{name}
rm -f %{buildroot}/%{_libdir}/libworkrave-private-1.0.so
%fdupes %{buildroot}/%{_prefix}
%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md ABOUT-NLS
%{_bindir}/workrave
%dir %{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus*/*
%dir %{_datadir}/sounds/%{name}
%{_datadir}/sounds/%{name}/*
%{_datadir}/%{name}/*
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/extensions
%dir %{_datadir}/gnome-shell/extensions/workrave@workrave.org
%{_datadir}/gnome-shell/extensions/workrave@workrave.org/*
%if 0%{?suse_version} > 1140
%{_datadir}/glib-2.0/schemas/org.workrave.enums.xml
%{_datadir}/glib-2.0/schemas/org.workrave.gschema.xml
%{_datadir}/glib-2.0/schemas/org.workrave.gui.gschema.xml
%else
%{_libdir}/bonobo/servers/Workrave-Applet.server
%{_datadir}/gnome-2.0/ui/GNOME_WorkraveApplet.xml
%endif
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/workrave.appdata.xml
%{_datadir}/cinnamon/applets/workrave@workrave.org/applet.js
%{_datadir}/cinnamon/applets/workrave@workrave.org/metadata.json
%dir /usr/share/cinnamon/
%dir /usr/share/cinnamon/applets/
%dir /usr/share/cinnamon/applets/workrave@workrave.org/
%{_libdir}/libworkrave-private-*

%files devel
%{_datadir}/gir-1.0/Workrave-1.0.gir

%files -n typelib-1_0-Workrave-1_0
%{_libdir}/girepository-1.0/Workrave-1.0.typelib

%changelog
