#
# spec file for package gstreamer-validate
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _name   gst-validate
Name:           gstreamer-validate
Version:        1.16.1
Release:        0
Summary:        GStreamer pipeline validator
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            http://gstreamer.freedesktop.org
Source:         https://gstreamer.freedesktop.org/src/%{_name}/%{_name}-%{version}.tar.xz
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

%description
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
Recommends:     %{name}

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
Summary:        Header files for the GStreamer pipeline validator
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgstvalidate-1_0-0 = %{version}
Requires:       typelib-1_0-GstValidate-1_0 = %{version}

%description devel
GstValidate detects when elements are not behaving as expected and
report it to the user so he knows how things are supposed to work
inside a GstPipeline. In the end, fixing issues found by the tool will
ensure that all elements behave all together in the expected way.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgstvalidate-1_0-0 -p /sbin/ldconfig
%postun -n libgstvalidate-1_0-0 -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog README
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
%{_libdir}/libgstvalidatevideo-1.0.so.*

%files -n typelib-1_0-GstValidate-1_0
%{_libdir}/girepository-1.0/GstValidate-1.0.typelib

%files devel
%{_datadir}/gir-1.0/GstValidate-1.0.gir
%{_datadir}/gtk-doc/html/gst-validate-1.0
%{_datadir}/gtk-doc/html/gst-validate-plugins-1.0/
%{_includedir}/gstreamer-1.0/
%{_libdir}/gstreamer-1.0/libgstvalidatetracer.so
%{_libdir}/gstreamer-1.0/validate/libgstvalidatefaultinjection.so
%{_libdir}/gstreamer-1.0/validate/libgstvalidategapplication.so
%{_libdir}/gstreamer-1.0/validate/libgstvalidategtk.so
%{_libdir}/gstreamer-1.0/validate/libgstvalidateflow.so
%{_libdir}/gstreamer-1.0/validate/libgstvalidatessim.so
%{_libdir}/pkgconfig/gst-validate-1.0.pc
%{_libdir}/libgstvalidate-1.0.so
%{_libdir}/libgstvalidate-default-overrides-1.0.so
%{_libdir}/libgstvalidatevideo-1.0.so

%changelog
