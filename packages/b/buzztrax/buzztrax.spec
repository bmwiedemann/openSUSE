#
# spec file for package buzztrax
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


%define rev 1f57d1b6ff55dd3d574f92039bb06a768d613d67
%define relver 0.11.0

%define gir gobject-introspection-1.0
%define gstreamer_pluginsdir %(pkg-config --variable=pluginsdir gstreamer-1.0)
%define girdir %{_datadir}/gir-1.0
%define typelibdir %(pkg-config --variable=typelibdir %{gir})
%define core_soname 1
%define ic_soname 1
%define girsoname 1.1
%define gst_soname 1
%define bml_soname 1
%define glib_version 2.32.0
%define gst_version 1.2.0
Name:           buzztrax
Version:        0.10.2+git20191209
Release:        0
Summary:        A music studio inspired by Buzz
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://buzztrax.org
Source0:        https://github.com/Buzztrax/buzztrax/archive//%{rev}.tar.gz#/%{name}-%{version}.tar.gz
#http://files.buzztrax.org/releases/%%{name}-%%{version}.tar.gz
Source1:        autogen.sh
Source2:        COPYING-DOCS
Patch0:         0001-Fix-build-with-fluidsynth-2.x.patch
BuildRequires:  automake >= 1.13
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  shared-mime-info
BuildRequires:  yelp-devel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(%{gir})
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gmodule-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gstreamer-controller-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(orc-0.4)
BuildRequires:  pkgconfig(pango)
Requires:       %{name}-plugins = %{version}
Requires:       gstreamer-1_0-plugins-buzztrax = %{version}
Requires:       yelp
Recommends:     gstreamer-plugins-good-jack
# We provide appdata(buzztrax-edit.appdata.xml) to prevent installation system error see:
# boo#961304 which is marked duplicate of boo#952304
#Provides:       appdata(buzztrax-edit.appdata.xml)
Provides:       buzztard = %{version}
Obsoletes:      buzztard < %{version}

%description
buzztrax aims to be a music studio that allows one to compose
songs using only a computer with a soundcard. If you've used
tracker programs like FastTracker, Impulse Tracker, or the
original AMIGA SoundTracker, that will give you an idea
of how one can sequence music in Buzztrax. The Buzztrax
editor uses a similar concept, where a song consists
of a sequence with tracks and in each track one uses patterns
with events (musical notes and control changes). In contrast
to other Tracker programs, tracks are not simply sample players:
a user can make a song using an arrangment of virtual audio
plugins that are linked together to create different effects.
Each of these machines can be controlled realtime or via
patterns in the sequencer.

%package -n gstreamer-1_0-plugins-buzztrax
Summary:        Buzztrax GStreamer plugin
Group:          Productivity/Multimedia/Other
Requires:       buzztrax = %{version}
Provides:       gstreamer-0_10-plugins-buzztard = %{version}
Obsoletes:      gstreamer-0_10-plugins-buzztard < %{version}

%description -n gstreamer-1_0-plugins-buzztrax
Plugin to play Buzztrax songs from any GStreamer compatible app.

%package -n libbuzztrax-ic%{ic_soname}
Summary:        Interaction controller support classes for buzztrax based applications
Group:          System/Libraries

%description -n libbuzztrax-ic%{ic_soname}
This package provides interaction controller support classes for buzztrax based applications.

%package -n libbuzztrax-core%{core_soname}
Summary:        Core support classes for buzztrax based applications
Group:          System/Libraries

%description -n libbuzztrax-core%{core_soname}
This package provides core support classes for buzztrax based applications.
Hotel Seminar Kraftquelle Schlossblick, Embach 1 - A 6320 Angerberg

%package -n libbuzztrax-gst%{gst_soname}
Summary:        Core support classes for buzztrax based applications
Group:          System/Libraries
Provides:       libgstbuzztard0 = %{version}
Obsoletes:      libgstbuzztard0 < %{version}

%description -n libbuzztrax-gst%{gst_soname}
This package provides gst support classes for buzztrax based applications.

%package -n libbuzztrax-gst-devel
Summary:        Development files for libbuzztrax-gst
Group:          Development/Libraries/C and C++
Requires:       libbuzztrax-gst%{gst_soname} = %{version}
Provides:       libgstbuzztard-devel = %{version}
Obsoletes:      libgstbuzztard-devel < %{version}

%description -n libbuzztrax-gst-devel
This package provides the development files for libbuzztrax-gst.

%package -n libbuzztrax-ic-devel
Summary:        Development files for libbuzztrax-ic
Group:          Development/Libraries/C and C++
Requires:       libbuzztrax-ic%{ic_soname} = %{version}

%description -n libbuzztrax-ic-devel
This package provides the development files for libbuzztrax-ic.

%package -n libbuzztrax-core-devel
Summary:        Development files for libbuzztrax-core
Group:          Development/Libraries/C and C++
Requires:       libbuzztrax-core%{core_soname} = %{version}

%description -n libbuzztrax-core-devel
This package provides the development files for libbuzztrax-core.

%package -n typelib-1_0-BuzztraxIc-1_1
Summary:        BuzztraxIc introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-BuzztraxIc-1_1
This package provides the GObject Introspection bindings for BuzztraxIc.

%package -n typelib-1_0-BuzztraxCore-1_1
Summary:        BuzztraxCore Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-BuzztraxCore-1_1
This package provides the GObject Introspection bindings for BuzztraxCore.

%package -n libbml%{bml_soname}
Summary:        Buzztrax Machine Loader
Group:          System/Libraries

%description -n libbml%{bml_soname}
This package provides bml support classes for buzztrax based applications.

%package -n libbml-devel
Summary:        Development files for libbml
Group:          Development/Libraries/C and C++
Requires:       libbml%{bml_soname} = %{version}

%description -n libbml-devel
This package provides the development files for libbml.

%package plugins
Summary:        Buzztrax plugins
Group:          Productivity/Multimedia/Other
Requires:       buzztrax = %{version}
Requires:       libbml%{bml_soname} = %{version}
Requires:       libbuzztrax-core%{core_soname} = %{version}
Requires:       libbuzztrax-gst%{gst_soname} = %{version}
Requires:       libbuzztrax-ic%{ic_soname} = %{version}

%description plugins
This package contains buzztrax plugins

%lang_package

%prep
%setup -q -n %{name}-%{rev}

%autopatch -p1
# Rpmlint complains that COPYING-DOCS is outdated
cp -v %{SOURCE2} .
cp -v %{SOURCE1} .
if ! `test -a AUTHORS`; then
touch AUTHORS
fi

%build
test -x "$(type -p gcc-8)" && export CC="$_"
test -x "$(type -p g++-8)" && export CXX="$_"
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
export CFLAGS="$CFLAGS -Wno-error=format-truncation= -Wno-error=format-overflow= -Wno-error=incompatible-pointer-types -Wno-error=restrict"
%ifarch i586
export CFLAGS="$CFLAGS -Wno-error=format"
%endif
export CXXFLAGS="$CFLAGS"

/bin/sh ./autogen.sh --noconfigure
%configure --disable-static \
    --disable-schemas-compile \
    --disable-update-mime \
    --disable-update-desktop \
    --disable-update-icon-cache \
    --disable-silent-rules \
    --enable-deprecated \
    --enable-debug \
    --disable-rpath \
    --with-pic \
    --enable-man \
    --disable-dllwrapper \
    --enable-gtk-doc
cp -v docs/version.entities docs/help/bt-edit/C/

make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
echo %{buildroot}
%find_lang %{name}-%{relver}
mv %{buildroot}%{_datadir}/applications/buzztrax-edit.desktop %{buildroot}%{_datadir}/applications/buzztrax.desktop
#%%find_gconf_schemas
# ensure the icons in hicolor are the REAL files. fdupes links them the 'wrong way around' for xdg-app and appstream-builder
for icon in 48x48/apps/buzztrax.png scalable/apps/buzztrax.svg; do
  ln -sf %{_datadir}/icons/hicolor/${icon} %{buildroot}%{_datadir}/icons/gnome/${icon}
done
%fdupes -s %{buildroot}/%{_datadir}/
# WARNING: this creates baselibs.conf
printf 'libbuzztrax-ic%{ic_soname}\n
libbuzztrax-core%{core_soname}\n
libbuzztrax-gst%{gst_soname}\n
typelib-1_0-BuzztraxIc-1_1\n
\t+^%{typelibdir}/BuzztraxIc-%{girsoname}.typelib$\n
typelib-1_0-BuzztraxCore-1_1\n
\t+^%{typelibdir}/BuzztraxCore-%{girsoname}.typelib$\n' > %{_sourcedir}/baselibs.conf

%post -n libbuzztrax-ic%{ic_soname} -p /sbin/ldconfig

%post -n libbuzztrax-core%{core_soname} -p /sbin/ldconfig

%post -n libbuzztrax-gst%{gst_soname} -p /sbin/ldconfig

%post -n libbml%{bml_soname} -p /sbin/ldconfig

%postun -n libbuzztrax-ic%{ic_soname} -p /sbin/ldconfig

%postun -n libbuzztrax-core%{core_soname} -p /sbin/ldconfig

%postun -n libbuzztrax-gst%{gst_soname} -p /sbin/ldconfig

%postun -n libbml%{bml_soname} -p /sbin/ldconfig

%files
%defattr(0644,root,root,0755)
%doc AUTHORS NEWS README.md TODO
%license COPYING COPYING-DOCS
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/buzztrax
%{_datadir}/applications/buzztrax.desktop
%{_datadir}/appdata/buzztrax.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/gnome
%{_datadir}/help/C/*
%{_mandir}/man1/*
%{_datadir}/gtk-doc/html/buzztrax-cmd
%{_datadir}/gtk-doc/html/buzztrax-edit
%{_datadir}/mime/packages/buzztrax.xml
# NOTE: These files need a proper home and correct handling.
%{_datadir}/GConf/gsettings/buzztrax.convert
%{_datadir}/glib-2.0/schemas/org.buzztrax.gschema.xml

%files -n gstreamer-1_0-plugins-buzztrax
%defattr(0644,root,root,0755)
%{gstreamer_pluginsdir}/lib*.so
%dir %{_datadir}/gstreamer-1.0/presets
%{_datadir}/gstreamer-1.0/presets/GstBtEBeats.prs
%{_datadir}/gstreamer-1.0/presets/GstBtSimSyn.prs

%files -n libbuzztrax-ic%{ic_soname}
%defattr(0644,root,root,0755)
%{_libdir}/libbuzztrax-ic.so.%{ic_soname}*

%files -n libbuzztrax-core%{ic_soname}
%defattr(0644,root,root,0755)
%{_libdir}/libbuzztrax-core.so.%{core_soname}*

%files -n libbuzztrax-ic-devel
%defattr(0644,root,root,0755)
%{_includedir}/libbuzztrax-ic/
%{_libdir}/libbuzztrax-ic.so
%{_libdir}/pkgconfig/libbuzztrax-ic.pc
%dir %{girdir}
%{girdir}/BuzztraxIc-%{girsoname}.gir
%{_datadir}/gtk-doc/html/buzztrax-ic/

%files -n libbuzztrax-core-devel
%defattr(0644,root,root,0755)
%{_includedir}/libbuzztrax-core/
%{_libdir}/libbuzztrax-core.so
%{_libdir}/pkgconfig/libbuzztrax-core.pc
%dir %{girdir}
%{girdir}/BuzztraxCore-%{girsoname}.gir
%{_datadir}/gtk-doc/html/buzztrax-core/

%files -n typelib-1_0-BuzztraxIc-1_1
%defattr(0644,root,root,0755)
%{typelibdir}/BuzztraxIc-%{girsoname}.typelib

%files -n typelib-1_0-BuzztraxCore-1_1
%defattr(0644,root,root,0755)
%{typelibdir}/BuzztraxCore-%{girsoname}.typelib

%files -n libbuzztrax-gst%{gst_soname}
%defattr(0644,root,root,0755)
%{_libdir}/libbuzztrax-gst.so.%{gst_soname}*

%files -n libbuzztrax-gst-devel
%defattr(0644,root,root,0755)
%{_libdir}/libbuzztrax-gst.so
%dir %{_includedir}/libbuzztrax-gst
%{_includedir}/libbuzztrax-gst/*
%{_datadir}/gtk-doc/html/buzztrax-gst/
%{_libdir}/pkgconfig/libbuzztrax-gst.pc

%files -n libbml%{bml_soname}
%defattr(0644,root,root,0755)
%{_libdir}/libbml.so.%{bml_soname}*

%files -n libbml-devel
%defattr(0644,root,root,0755)
%{_libdir}/libbml.so
%dir %{_includedir}/libbml
%{_includedir}/libbml/*
%{_libdir}/pkgconfig/libbml.pc

%files plugins
%defattr(0644,root,root,0755)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_datadir}/applications/buzztrax-songio-buzz.desktop
%{_datadir}/mime/packages/buzztrax-songio-buzz.xml
%dir %{_libdir}/buzztrax-songio
%{_libdir}/buzztrax-songio/*.so

%files lang -f %{name}-%{relver}.lang
%defattr (-, root, root)

%changelog
