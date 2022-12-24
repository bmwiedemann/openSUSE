#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%nil

%define _name webkitgtk
%if "%{flavor}" == ""
# gtknamesuffix is just so we do not have to rename the source package - no package is generated here
%define _gtknamesuffix gtk3
ExclusiveArch:  do-not-build
%endif

%define usegcc10 0%{?sle_version} && 0%{?sle_version} <= 150400

%if "%{flavor}" == "gtk3"
%define _gtknamesuffix gtk3
%define _pkgname_no_slpp libwebkit2gtk3
%define _apiver 4.1
%define _sover -4_1-0
%define _wk2sover -4_1-0
%define _sonamever 4.1
%define _sonameverpkg 4_1
%define _gtkver 3.0
%define _jscver 4.1
%define _pkgconfig_suffix gtk-3.0
%define _usesoup2 0
%endif

%if "%{flavor}" == "gtk3-soup2"
%define _gtknamesuffix gtk3-soup2
%define _pkgname_no_slpp libwebkit2gtk3
%define _apiver 4.0
%define _sover -4_0-18
%define _wk2sover -4_0-37
%define _sonamever 4.0
%define _sonameverpkg 4_0
%define _gtkver 3.0
%define _jscver 4
%define _pkgconfig_suffix gtk-3.0
%define _usesoup2 1
%endif

%if "%{flavor}" == "gtk4"
%define _gtknamesuffix gtk4
%define _pkgname_no_slpp libwebkit2gtk4
%define _apiver 5.0
%define _sover -5_0-0
%define _wk2sover -5_0-0
%define _sonamever 5.0
%define _sonameverpkg 5_0
%define _gtkver 4.0
%define _jscver 5.0
%define _pkgconfig_suffix gtk-4.0
%define _usesoup2 0
%endif

Name:           webkit2%{_gtknamesuffix}
Version:        2.38.3
Release:        0
Summary:        Library for rendering web content, GTK+ Port
License:        BSD-3-Clause AND LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://webkitgtk.org
Source0:        %{url}/releases/%{_name}-%{version}.tar.xz
Source1:        %{url}/releases/%{_name}-%{version}.tar.xz.asc
Source98:       baselibs.conf
Source99:       webkit2gtk3.keyring

# PATCH-FIX-OPENSUSE no-forced-sse.patch jengelh@iani.de -- cure execution of illegal instruction in i586 webkit
Patch0:         no-forced-sse.patch

BuildRequires:  Mesa-libEGL-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  Mesa-libGLESv1_CM-devel
BuildRequires:  Mesa-libGLESv2-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  bison >= 2.3
BuildRequires:  bubblewrap
BuildRequires:  cmake
BuildRequires:  enchant-devel
BuildRequires:  flex
%if %usegcc10
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++ >= 8.3
%endif
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf >= 3.0.1
BuildRequires:  hyphen-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  ninja
BuildRequires:  openjpeg2
BuildRequires:  openjpeg2-devel
BuildRequires:  perl >= 5.10.0
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  ruby >= 1.9
BuildRequires:  xdg-dbus-proxy
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(atspi-2) >= 2.5.3
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(fontconfig) >= 2.8.0
BuildRequires:  pkgconfig(freetype2) >= 2.4.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.4
%if %usegcc10
BuildRequires:  pkgconfig(glproto)
%endif
BuildRequires:  pkgconfig(gnutls) >= 3.0.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.14.0
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)
BuildRequires:  pkgconfig(gstreamer-fft-1.0)
BuildRequires:  pkgconfig(gstreamer-gl-1.0)
BuildRequires:  pkgconfig(gstreamer-mpegts-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
%if "%{flavor}" == "gtk3" || "%{flavor}" == "gtk3-soup2"
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
%endif
%if "%{flavor}" == "gtk4"
BuildRequires:  pkgconfig(gtk4) >= 3.98.50
BuildRequires:  pkgconfig(xcomposite)
%endif
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(harfbuzz) >= 0.9.18
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libavif) >= 0.9.0
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsecret-1)
%if %{_usesoup2}
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.54.0
%else
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0.0
%endif
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwoff2dec)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.8.0
BuildRequires:  pkgconfig(libxslt) >= 1.1.7
BuildRequires:  pkgconfig(manette-0.2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wpe-1.0) >= 1.3.0
BuildRequires:  pkgconfig(wpebackend-fdo-1.0) >= 1.6.0
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser.  It is made to be
embedded in other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It
also supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and
more.

%package -n libwebkit2gtk%{_wk2sover}
Summary:        Library for rendering web content, GTK+ Port
# Require the injected bundles. The bundles are dlopen()ed
Group:          System/Libraries
Requires:       bubblewrap
Requires:       libjavascriptcoregtk%{_sover} = %{version}
Requires:       webkit2gtk-%{_sonameverpkg}-injected-bundles
Requires:       xdg-dbus-proxy
Provides:       %{_pkgname_no_slpp} = %{version}
Provides:       WebKit2GTK-%{_apiver}
Obsoletes:      webkit2gtk3-plugin-process-gtk2 < %{version}
Recommends:     geoclue2
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-good
Recommends:     xdg-desktop-portal-gtk

%description -n libwebkit2gtk%{_wk2sover}
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser.  It is made to be
embedded in other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It
also supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and
more.

%package -n webkit2gtk-%{_sonameverpkg}-injected-bundles
Summary:        Injected bundles for %{name}
Group:          System/Libraries

%description -n webkit2gtk-%{_sonameverpkg}-injected-bundles
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser.  It is made to be
embedded in other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It
also supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and
more.

%package -n libjavascriptcoregtk%{_sover}
Summary:        JavaScript Core Engine, GTK+ Port
Group:          System/Libraries

%description -n libjavascriptcoregtk%{_sover}
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser.  It is made to be
embedded in other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It
also supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and
more.

%package -n typelib-1_0-WebKit2-%{_sonameverpkg}
Summary:        Introspection bindings for %{name}
Group:          System/Libraries

%description -n typelib-1_0-WebKit2-%{_sonameverpkg}
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser.  It is made to be
embedded in other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It
also supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and
more.

This package provides the GObject Introspection bindings for the GTK+
port of WebKit2.

%package -n typelib-1_0-WebKit2WebExtension-%{_sonameverpkg}
Summary:        Introspection bindings for %{name}
Group:          System/Libraries

%description -n typelib-1_0-WebKit2WebExtension-%{_sonameverpkg}
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser.  It is made to be
embedded in other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It
also supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and
more.

This package provides the GObject Introspection bindings for the GTK+
port of WebKit2.

%package -n typelib-1_0-JavaScriptCore-%{_sonameverpkg}
Summary:        Introspection bindings for the GTK+ port of the JavaScript Core Engine
Group:          System/Libraries

%description -n typelib-1_0-JavaScriptCore-%{_sonameverpkg}
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser.  It is made to be
embedded in other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It
also supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and
more.

This package provides the GObject Introspection bindings for the GTK+
port of the JavaScript Core engine.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libjavascriptcoregtk%{_sover} = %{version}
Requires:       libwebkit2gtk%{_wk2sover} = %{version}
Requires:       typelib-1_0-JavaScriptCore-%{_sonameverpkg}
Requires:       typelib-1_0-WebKit2-%{_sonameverpkg}
Requires:       typelib-1_0-WebKit2WebExtension-%{_sonameverpkg}

%description devel
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser.  It is made to be
embedded in other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It
also supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and
more.

%package -n webkit-jsc-%{_jscver}
Summary:        JavaScript command line from WebKit
Group:          Development/Tools/Other

%description -n webkit-jsc-%{_jscver}
jsc is a command-line utility that allows you to run JavaScript
programs outside of the context of a web browser. It is primarily
used as part of the test harness for validating the JavaScript
portions of WebKit, but can also be used as a scripting tool.

jsc can be run in an interactive mode to test out JavaScript
expressions, or it can be passed one or more files to run similar to
invoking a Perl or Python script.

%package minibrowser
Summary:        MiniBrowser from WebKit
Group:          Development/Tools/Other

%description minibrowser
A small test browswer from webkit, useful for testing features.

# Expand %%lang_package to Obsoletes its older-name counterpart
%if "%{flavor}" == "gtk3-soup2"
%package -n WebKit2GTK-%{_apiver}-lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       WebKit2GTK-%{_apiver} = %{version}
Provides:       WebKit2GTK-%{_apiver}-lang-all = %{version}
Obsoletes:      libwebkit2gtk3-lang < %{version}
BuildArch:      noarch

%description -n WebKit2GTK-%{_apiver}-lang
Provides translations for the "%{name}" package.
%else
%lang_package -n WebKit2GTK-%{_apiver}
%endif

%prep
%autosetup -p1 -n webkitgtk-%{version}

%build
# Here we must muzzle our dog so it doesn't eat all the memory
max_link_jobs="%{?jobs:%{jobs}}"
max_compile_jobs="%{?jobs:%{jobs}}"
echo "Available memory:"
cat /proc/meminfo
echo "System limits:"
ulimit -a
if test -n "$max_link_jobs" -a "$max_link_jobs" -gt 1 ; then
        mem_per_process=1500000
    max_mem=$(awk '/MemTotal/ { print $2 }' /proc/meminfo)
    max_jobs="$(($max_mem / $mem_per_process))"
    test "$max_link_jobs" -gt "$max_jobs" && max_link_jobs="$max_jobs" && echo "Warning: Reducing number of link jobs to $max_jobs because of memory limits"
    test "$max_link_jobs" -le 0 && max_link_jobs=1 && echo "Warning: Not linking in parallel at all becuse of memory limits"
fi

export PYTHON=%{_bindir}/python3
# Use linker flags to reduce memory consumption
%global optflags %(echo %{optflags} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads | sed 's/-g /-g1 /')
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DENABLE_DOCUMENTATION=OFF \
%if %usegcc10
  -DCMAKE_C_COMPILER=gcc-10 \
  -DCMAKE_CXX_COMPILER=g++-10 \
%endif
  -DLIBEXEC_INSTALL_DIR=%{_libexecdir}/libwebkit2gtk%{_wk2sover} \
  -DPORT=GTK \
%if "%{flavor}" == "gtk4"
  -DUSE_GTK4=ON \
%endif
  -DUSE_AVIF=ON \
  -DENABLE_MINIBROWSER=ON \
  -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -pthread" \
  -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -pthread" \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -pthread" \
  -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
%if %{_usesoup2}
  -DUSE_SOUP2=ON \
%endif
%ifarch aarch64
  -DENABLE_JIT=OFF \
  -DENABLE_C_LOOP=ON \
  -DENABLE_SAMPLING_PROFILER=OFF \
  -DUSE_SYSTEM_MALLOC=ON \
%endif

%ninja_build -j $max_link_jobs

%install
%ninja_install -C build
rm %{buildroot}%{_bindir}/WebKitWebDriver
%find_lang WebKit2GTK-%{_apiver}

%post -n libwebkit2gtk%{_wk2sover} -p /sbin/ldconfig
%postun -n libwebkit2gtk%{_wk2sover} -p /sbin/ldconfig
%post -n libjavascriptcoregtk%{_sover} -p /sbin/ldconfig
%postun -n libjavascriptcoregtk%{_sover} -p /sbin/ldconfig

%files -n libwebkit2gtk%{_wk2sover}
# Exclude jsc and MiniBrowser - we package them on their own
%exclude %{_libexecdir}/libwebkit2gtk%{_wk2sover}/jsc
%exclude %{_libexecdir}/libwebkit2gtk%{_wk2sover}/MiniBrowser
%{_libexecdir}/libwebkit2gtk%{_wk2sover}/
%{_libdir}/libwebkit2gtk-%{_apiver}.so.*

%files -n webkit2gtk-%{_sonameverpkg}-injected-bundles
%dir %{_libdir}/webkit2gtk-%{_apiver}
%dir %{_libdir}/webkit2gtk-%{_apiver}/injected-bundle
%{_libdir}/webkit2gtk-%{_apiver}/injected-bundle/libwebkit2gtkinjectedbundle.so

%files -n libjavascriptcoregtk%{_sover}
%license Source/JavaScriptCore/COPYING.LIB
%{_libdir}/libjavascriptcoregtk-%{_apiver}.so.*

%files -n typelib-1_0-WebKit2-%{_sonameverpkg}
%{_libdir}/girepository-1.0/WebKit2-%{_sonamever}.typelib

%files -n typelib-1_0-WebKit2WebExtension-%{_sonameverpkg}
%{_libdir}/girepository-1.0/WebKit2WebExtension-%{_sonamever}.typelib

%files -n typelib-1_0-JavaScriptCore-%{_sonameverpkg}
%{_libdir}/girepository-1.0/JavaScriptCore-%{_sonamever}.typelib

%files devel
%{_datadir}/gir-1.0/*.gir
%{_includedir}/webkitgtk-%{_apiver}/
%{_libdir}/libwebkit2gtk-%{_sonamever}.so
%{_libdir}/libjavascriptcoregtk-%{_sonamever}.so
%{_libdir}/pkgconfig/javascriptcoregtk-%{_apiver}.pc
%{_libdir}/pkgconfig/webkit2gtk-%{_apiver}.pc
%{_libdir}/pkgconfig/webkit2gtk-web-extension-%{_apiver}.pc

%files -n webkit-jsc-%{_jscver}
%{_libexecdir}/libwebkit2gtk%{_wk2sover}/jsc

%files minibrowser
%{_libexecdir}/libwebkit2gtk%{_wk2sover}/MiniBrowser

%files -n WebKit2GTK-%{_apiver}-lang -f WebKit2GTK-%{_apiver}.lang

%changelog
