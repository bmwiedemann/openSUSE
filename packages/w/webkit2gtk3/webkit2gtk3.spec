#
# spec file for package webkit2gtk3
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


%define _pkgname_no_slpp libwebkit2gtk3
%define _sover -4_0-18
%define _wk2sover -4_0-37
%define _sonamever 4.0
%define _sonameverpkg 4_0
%define _gtkver 3.0
%define _jscver 4
%define _pkgconfig_suffix gtk-3.0
%define _name webkitgtk
# gold linker not available on old s390/s390x
%define _gold_linker 1
%ifarch ppc s390
%define _gold_linker 0
%endif
Name:           webkit2gtk3
Version:        2.30.1
Release:        0
Summary:        Library for rendering web content, GTK+ Port
License:        LGPL-2.0-or-later AND BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://webkitgtk.org
Source0:        %{url}/releases/%{_name}-%{version}.tar.xz
Source1:        %{url}/releases/%{_name}-%{version}.tar.xz.asc
Source98:       baselibs.conf
Source99:       webkit2gtk3.keyring
# PATCH-FIX-OPENSUSE webkit2gtk3-fdo-soname.patch mgorse@suse.com -- don't call dlopen with an unversioned soname.
Patch0:         webkit2gtk3-fdo-soname.patch
# PATCH-FIX-OPENSUSE webkit-process.patch boo#1159329 mgorse@suse.com -- use single web process for evolution and geary.
Patch1:         webkit-process.patch
# PATCH-FIX-OPENSUSE no-forced-sse.patch jengelh@iani.de -- cure execution of illegal instruction in i586 firefox.
Patch2:         no-forced-sse.patch

BuildRequires:  Mesa-libEGL-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  Mesa-libGLESv1_CM-devel
BuildRequires:  Mesa-libGLESv2-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  bison >= 2.3
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  bubblewrap
%endif
BuildRequires:  cmake
BuildRequires:  enchant-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf >= 3.0.1
BuildRequires:  hyphen-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  ninja
BuildRequires:  perl >= 5.10.0
BuildRequires:  pkgconfig
BuildRequires:  ruby >= 1.8.7
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  xdg-dbus-proxy
%endif
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(atspi-2) >= 2.5.3
BuildRequires:  pkgconfig(cairo) >= 1.10.2
BuildRequires:  pkgconfig(fontconfig) >= 2.8.0
BuildRequires:  pkgconfig(freetype2) >= 2.4.2
BuildRequires:  pkgconfig(geoclue-2.0) >= 2.1.5
BuildRequires:  pkgconfig(glib-2.0) >= 2.36
BuildRequires:  pkgconfig(gnutls) >= 3.0.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.3
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
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(harfbuzz) >= 0.9.2
BuildRequires:  pkgconfig(libbrotlidec) >= 1.0.1
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.61.90
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.8.0
BuildRequires:  pkgconfig(libxslt) >= 1.1.7
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(upower-glib)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  pkgconfig(wpe-1.0) >= 1.3.0
BuildRequires:  pkgconfig(wpebackend-fdo-1.0) >= 1.3.0
%endif
BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1500
BuildRequires:  openjpeg2
BuildRequires:  openjpeg2-devel
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libwoff2dec)
%endif
BuildRequires:  python3
%if %{_gold_linker}
BuildRequires:  binutils-gold
%endif

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
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
Requires:       bubblewrap
%endif
Requires:       webkit2gtk-4_0-injected-bundles
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
Requires:       xdg-dbus-proxy
%endif
Provides:       %{_pkgname_no_slpp} = %{version}
Obsoletes:      webkit2gtk3-plugin-process-gtk2

%description -n libwebkit2gtk%{_wk2sover}
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser.  It is made to be
embedded in other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It
also supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and
more.

%package -n webkit2gtk-4_0-injected-bundles
Summary:        Injected bundles for %{name}
Group:          System/Libraries

%description -n webkit2gtk-4_0-injected-bundles
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

%lang_package -n %{_pkgname_no_slpp}

%prep
%setup -n webkitgtk-%{version}
%patch0 -p1
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} < 150200
%patch1 -p1
%endif
%patch2 -p1

%build
%define _lto_cflags %{nil}
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
%if %{_gold_linker}
%global optflags %(echo %{optflags} -Wl,--no-keep-memory | sed 's/-g /-g1 /')
%else
%global optflags %(echo %{optflags} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads | sed 's/-g /-g1 /')
%endif
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DLIBEXEC_INSTALL_DIR=%{_libexecdir}/libwebkit2gtk%{_wk2sover} \
  -DPORT=GTK \
  -DENABLE_MINIBROWSER=ON \
  -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -pthread" \
  -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -pthread" \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now -pthread" \
%if 0%{?suse_version} <= 1500
  -DUSE_WOFF2=false \
  -DENABLE_MEDIA_SOURCE=OFF \
%endif
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} < 150200
  -DUSE_WPE_RENDERER=OFF \
  -DENABLE_BUBBLEWRAP_SANDBOX=OFF \
%endif
  -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
%ifarch aarch64
  -DENABLE_JIT=OFF \
  -DENABLE_C_LOOP=ON \
  -DENABLE_SAMPLING_PROFILER=OFF \
  -DUSE_SYSTEM_MALLOC=ON \
%endif

%ninja_build -j $max_link_jobs

%install
%ninja_install -C build
%find_lang WebKit2GTK-4.0

%post -n libwebkit2gtk%{_wk2sover} -p /sbin/ldconfig
%postun -n libwebkit2gtk%{_wk2sover} -p /sbin/ldconfig
%post -n libjavascriptcoregtk%{_sover} -p /sbin/ldconfig
%postun -n libjavascriptcoregtk%{_sover} -p /sbin/ldconfig

%files -n libwebkit2gtk%{_wk2sover}
# Exclude jsc and MiniBrowser - we package them on their own
%exclude %{_libexecdir}/libwebkit2gtk%{_wk2sover}/jsc
%exclude %{_libexecdir}/libwebkit2gtk%{_wk2sover}/MiniBrowser
%{_libexecdir}/libwebkit2gtk%{_wk2sover}/
%{_libdir}/libwebkit2gtk-4.0.so.*
%{_bindir}/WebKitWebDriver

%files -n webkit2gtk-4_0-injected-bundles
%dir %{_libdir}/webkit2gtk-4.0
%dir %{_libdir}/webkit2gtk-4.0/injected-bundle
%{_libdir}/webkit2gtk-4.0/injected-bundle/libwebkit2gtkinjectedbundle.so

%files -n libjavascriptcoregtk%{_sover}
%license Source/JavaScriptCore/COPYING.LIB
%{_libdir}/libjavascriptcoregtk-4.0.so.*

%files -n typelib-1_0-WebKit2-%{_sonameverpkg}
%{_libdir}/girepository-1.0/WebKit2-%{_sonamever}.typelib

%files -n typelib-1_0-WebKit2WebExtension-%{_sonameverpkg}
%{_libdir}/girepository-1.0/WebKit2WebExtension-%{_sonamever}.typelib

%files -n typelib-1_0-JavaScriptCore-%{_sonameverpkg}
%{_libdir}/girepository-1.0/JavaScriptCore-%{_sonamever}.typelib

%files devel
%{_datadir}/gir-1.0/*.gir
%{_includedir}/webkitgtk-4.0/
%{_libdir}/libwebkit2gtk-4.0.so
%{_libdir}/libjavascriptcoregtk-4.0.so
%{_libdir}/pkgconfig/javascriptcoregtk-4.0.pc
%{_libdir}/pkgconfig/webkit2gtk-4.0.pc
%{_libdir}/pkgconfig/webkit2gtk-web-extension-4.0.pc

%files -n webkit-jsc-%{_jscver}
%{_libexecdir}/libwebkit2gtk%{_wk2sover}/jsc

%files minibrowser
%{_libexecdir}/libwebkit2gtk%{_wk2sover}/MiniBrowser

%files -n %{_pkgname_no_slpp}-lang -f WebKit2GTK-4.0.lang

%changelog
