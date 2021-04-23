#
# spec file for package gstreamer-devtools
#
# Copyright (c) 2021 SUSE LLC
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


%define _name   gst-devtools

Name:           gstreamer-devtools
Version:        1.18.3
Release:        0
Summary:        Development and debugging tools for GStreamer
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
Source:         %{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  hotdoc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{version}
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(json-glib-1.0)
Obsoletes:      gstreamer-validate < 1.18.1
Provides:       gstreamer-validate = %{version}

%description
Development and debugging tools for GStreamer

GstValidate detects when elements are not behaving as expected and
report it to the user so he knows how things are supposed to work
inside a GstPipeline. In the end, fixing issues found by the tool will
ensure that all elements behave all together in the expected way.

The easiest way of using GstValidate is to use one of its command-line
tools, located at tools/ directory. It is also possible to monitor
GstPipelines from any application by using the LD_PRELOAD gstvalidate
lib. The third way of using it is to write your own application that
links and uses libgstvalidate.

%package -n libgstvalidate-1_0-0
Summary:        GStreamer pipeline validator
# all the nice validator scripts live in the main package
Group:          System/Libraries

%description -n libgstvalidate-1_0-0
GstValidate detects when elements are not behaving as expected and
report it to the user so he knows how things are supposed to work
inside a GstPipeline. In the end, fixing issues found by the tool will
ensure that all elements behave all together in the expected way.

%package -n typelib-1_0-GstValidate-1_0
Summary:        GObject introspection bindings for the GStreamer pipeline validator
Group:          System/Libraries

%description -n typelib-1_0-GstValidate-1_0
GstValidate detects when elements are not behaving as expected and
report it to the user so he knows how things are supposed to work
inside a GstPipeline. In the end, fixing issues found by the tool will
ensure that all elements behave all together in the expected way.

%package devel
Summary:        Header files for the GStreamer development and debugging tools
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgstvalidate-1_0-0 = %{version}
Requires:       typelib-1_0-GstValidate-1_0 = %{version}
Obsoletes:      gstreamer-validate-devel < 1.18.0
Provides:       gstreamer-validate-devel = %{version}

%description devel
GstValidate detects when elements are not behaving as expected and
report it to the user so he knows how things are supposed to work
inside a GstPipeline. In the end, fixing issues found by the tool will
ensure that all elements behave all together in the expected way.

%prep
%autosetup -p1
sed -i -e '1{s,^#!/usr/bin/env python3,#!%{_bindir}/python3,}' validate/tools/gst-validate-launcher.in

%build
%meson
%meson_build

%install
%meson_install

%post -n libgstvalidate-1_0-0 -p /sbin/ldconfig
%postun -n libgstvalidate-1_0-0 -p /sbin/ldconfig

%files
%license validate/COPYING
%doc ChangeLog validate/README
%{_bindir}/gst-validate-1.0
%{_bindir}/gst-validate-images-check-1.0
%{_bindir}/gst-validate-launcher
%{_bindir}/gst-validate-media-check-1.0
%{_bindir}/gst-validate-transcoding-1.0
%{_libdir}/gst-validate-launcher/
%dir %{_datadir}/gstreamer-1.0/
%{_datadir}/gstreamer-1.0/validate/
%dir %{_libdir}/gstreamer-1.0/
%dir %{_libdir}/gstreamer-1.0/validate/

%files -n libgstvalidate-1_0-0
%{_libdir}/libgstvalidate-1.0.so.*
%{_libdir}/libgstvalidate-default-overrides-1.0.so.*
#%%{_libdir}/libgstvalidatevideo-1.0.so.*

%files -n typelib-1_0-GstValidate-1_0
%{_libdir}/girepository-1.0/GstValidate-1.0.typelib

%files devel
%{_datadir}/gir-1.0/GstValidate-1.0.gir
%{_includedir}/gstreamer-1.0/
%{_libdir}/gstreamer-1.0/libgstvalidatetracer.so
%{_libdir}/gstreamer-1.0/validate/libgstvalidatefaultinjection.so
%{_libdir}/gstreamer-1.0/validate/libgstvalidategapplication.so
%{_libdir}/gstreamer-1.0/validate/libgstvalidategtk.so
%{_libdir}/gstreamer-1.0/validate/libgstvalidatessim.so
%{_libdir}/pkgconfig/gst-validate-1.0.pc
%{_libdir}/libgstvalidate-1.0.so
%{_libdir}/libgstvalidate-default-overrides-1.0.so
#%%{_libdir}/libgstvalidatevideo-1.0.so

%changelog
