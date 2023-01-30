#
# spec file for package pitivi
#
# Copyright (c) 2023 SUSE LLC
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


Name:           pitivi
Version:        2022.06
Release:        0
Summary:        Video editing software
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://www.pitivi.org/
Source0:        https://download.gnome.org/sources/pitivi/2022/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gnome-doc-utils-devel >= 0.18.0
BuildRequires:  gobject-introspection >= 1.31.1
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-cairo-devel
BuildRequires:  python3-gobject
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.14.1
BuildRequires:  pkgconfig(gstreamer-transcoder-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.10.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
Requires:       gstreamer-transcoder >= 1.8.2
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-gst >= 1.17.90
Requires:       python3-matplotlib-gtk3
Requires:       python3-numpy
# We need a minimal version of the GES-1.0 package, so we have to specify it manually
Requires:       typelib-1_0-GES-1_0 >= 1.17.90
Requires:       typelib-1_0-Gst-1_0 >= 1.17.90
# Pitivi can use the Frei0r plugins, and since this enables lots of effects, we
# really want that by default if possible
Recommends:     frei0r-plugins

%description
Pitivi is a non-linear, featureful movie editor.
It supports realtime trimming previews, ripple and roll editing,
grouping and snapping, realtime assets management and searching,
playhead-centric zooming and editing, non-modal cutting, detachable
interface components, smooth scrolling, and automatic zoom
adjustment.

%lang_package

%prep
%autosetup -p1
sed -i -e '1s!/usr/bin/env !/usr/bin/!' bin/pitivi.in

# Remove bunlded gst-transcoder
rm -rf subprojects/gst-transcoder

%build
%meson -Ddisable-help=false
%meson_build

python3 -m compileall -q -j 0 .

%install
%meson_install
rm -v %{buildroot}%{_libdir}/pitivi/python/pitivi/coptimizations/renderer.c

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}

%post
if test -x usr/bin/update-mime-database ; then
  usr/bin/update-mime-database usr/share/mime >/dev/null
fi

%postun
if test -x usr/bin/update-mime-database ; then
  usr/bin/update-mime-database usr/share/mime >/dev/null
fi

%files
%license COPYING
%doc AUTHORS NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/pitivi
%{_libdir}/pitivi/
%{_datadir}/applications/org.pitivi.Pitivi.desktop
%{_datadir}/icons/hicolor/*/*/*.*
%{_datadir}/metainfo/org.pitivi.Pitivi.appdata.xml
%{_datadir}/mime/packages/org.pitivi.Pitivi-mime.xml
%{_datadir}/pitivi/

%files lang -f %{name}.lang

%changelog
