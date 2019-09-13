#
# spec file for package entangle
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           entangle
Version:        2.0
Release:        0
Summary:        Tethered shooting & control of digital cameras
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
Url:            https://entangle-photo.org
Source0:        https://www.entangle-photo.org/download/sources/%{name}-%{version}.tar.xz
Source1:        https://www.entangle-photo.org/download/sources/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
Entangle is an application which uses GTK and libgphoto2 to provide a
graphical interface for tethered photography with digital cameras.

It includes control over camera shooting and configuration settings
and 'hands off' shooting directly from the controlling computer.

%package plugin-eclipse
Summary:        Eclipse totality automated capture for corona
Group:          Productivity/Graphics/Other
Requires:       %{name} = %{version}
Requires:       python3
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       typelib(GExiv2) = 0.10
Requires:       typelib(GstBase) = 1.0

%description plugin-eclipse
Entangle provides a graphical interface for "tethered shooting", aka
taking photographs with a digital camera completely controlled from
the computer.

This package provides the eclipse plugin for %{name}.

%package plugin-photobox
Summary:        Captive interface for public photo box
Group:          Productivity/Graphics/Other
Requires:       %{name} = %{version}
Requires:       python3
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       typelib(GExiv2) = 0.10
Requires:       typelib(GstBase) = 1.0

%description plugin-photobox
Entangle provides a graphical interface for "tethered shooting", aka
taking photographs with a digital camera completely controlled from
the computer.

This package provides the photobox plugin for %{name}.

%package plugin-shooter
Summary:        Repeated batch mode shooting
Group:          Productivity/Graphics/Other
Requires:       %{name} = %{version}
Requires:       python3
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       typelib(GExiv2) = 0.10
Requires:       typelib(GstBase) = 1.0

%description plugin-shooter
Entangle provides a graphical interface for "tethered shooting", aka
taking photographs with a digital camera completely controlled from
the computer.

This package provides the shooter plugin for %{name}.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
Entangle provides a graphical interface for "tethered shooting", aka
taking photographs with a digital camera completely controlled from
the computer.

Documentation for %{name}.

%package -n typelib-1_0-Entangle-0_1
Summary:        Introspection bindings for the %{name} plugins
Group:          Productivity/Graphics/Other

%description -n typelib-1_0-Entangle-0_1
Entangle provides a graphical interface for "tethered shooting", aka
taking photographs with a digital camera completely controlled from
the computer.

This package provides the GObject Introspection bindings for %{name}
plugins

%lang_package

%prep
%setup -q

%build
%meson -Denable-gtk-doc=true
%meson_build

%install
%meson_install

# We do not provide a devel subpackage
find %{buildroot}%{_libdir}/ -type l -name "*.so" -delete -print
rm -rf %{buildroot}%{_datadir}/gir-1.0

%find_lang %{name} %{?no_lang_C}

%post
%glib2_gsettings_schema_post
/sbin/ldconfig

%postun
%glib2_gsettings_schema_postun
/sbin/ldconfig

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_libdir}/lib%{name}_backend.so.*
%{_libdir}/lib%{name}_frontend.so.*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sRGB.icc
%{_datadir}/glib-2.0/schemas/org.%{name}-photo.manager.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}*.??g
%{_mandir}/man?/%{name}.?%{ext_man}
%license COPYING

%files plugin-eclipse
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/eclipse
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/eclipse

%files plugin-photobox
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/photobox
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/photobox

%files plugin-shooter
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/shooter
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/shooter

%files doc
%doc %{_datadir}/help/C/%{name}
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}

%files -n typelib-1_0-Entangle-0_1
%{_libdir}/girepository-1.0/Entangle-0.1.typelib

%files lang -f %{name}.lang

%changelog
