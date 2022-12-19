#
# spec file for package gsequencer
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


%define libagssonumber 4
%define libgsequencersonumber 0
# The condition is run functional tests; defaulted off and needs to be
# activated with --with run_functional_tests command line switch.
%bcond_with run_functional_tests
Name:           gsequencer
Version:        4.4.3
Release:        0
Summary:        Audio processing engine
License:        AGPL-3.0-or-later AND GPL-3.0-or-later AND GFDL-1.3-only
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://nongnu.org/gsequencer
Source0:        https://download.savannah.gnu.org/releases/gsequencer/4.4.x/%{name}-%{version}.tar.gz
# improve glib-2.0 compatibility to version 2.54
Patch1:         gsequencer.1-improved-glib-compatibility.patch
BuildRequires:  cunit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  dssi-devel
BuildRequires:  fluid-soundfont-gm
BuildRequires:  fop
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel >= 0.19.8
BuildRequires:  gstreamer-plugins-base
BuildRequires:  gstreamer-plugins-good
BuildRequires:  gtk-doc
BuildRequires:  hydrogen
BuildRequires:  ladspa-cmt
BuildRequires:  ladspa-devel
BuildRequires:  libtool
BuildRequires:  lv2-devel
BuildRequires:  lv2-swh-plugins
BuildRequires:  pkgconfig
BuildRequires:  pulseaudio
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-fancybox
BuildRequires:  texlive-jknapltx
BuildRequires:  texlive-latex
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libinstpatch-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(uuid)

%description
Advanced Gtk+ Sequencer is an audio
sequencer application supporting the LADPSA, DSSI and Lv2 plugin
formats. It can output to Pulseaudio server, JACK and ALSA.

You may add multiple sinks, mix different sources by producing
sound with different sequencers. Furthermore, it features a pattern
and piano roll and there is an editor to automate ports.

%prep
%setup -q
%patch1 -p0

%build
autoreconf -fi
export LIBAGS_CPPFLAGS='-D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security'
export LIBAGS_THREAD_CPPFLAGS='-D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security'
export LIBAGS_SERVER_CPPFLAGS='-D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security'
#export LIBAGS_VST3_RELEASE_TYPE="-DRELEASE"
#export LIBAGS_VST3_CPPFLAGS='-D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security'
#export LIBAGS_VST3_CXXFLAGS="-I/usr/include/vst3sdk"
#export LIBAGS_VST3_LIBS="-L/usr/%{_lib}/vst3sdk"
export LIBAGS_AUDIO_CPPFLAGS='-D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security'
export LIBAGS_GUI_CPPFLAGS='-D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security'
export LIBGSEQUENCER_CPPFLAGS='-DAGS_CSS_FILENAME=\"'%{_datadir}'/gsequencer/styles/ags.css\" -DAGS_ANIMATION_FILENAME=\"'%{_datadir}'/gsequencer/images/gsequencer-800x450.png\" -DAGS_LOGO_FILENAME=\"'%{_datadir}'/gsequencer/images/ags.png\" -DAGS_LICENSE_FILENAME=\"'%{_datadir}'/licenses/gsequencer/COPYING\" -DAGS_ONLINE_HELP_A4_PDF_FILENAME=\"'%{_docdir}'/gsequencer/pdf/user-manual-a4.pdf\" -DAGS_ONLINE_HELP_LETTER_PDF_FILENAME=\"'%{_docdir}'/gsequencer/pdf/user-manual-letter.pdf\" -DAGS_REDUCE_RT_EVENTS=1 -DAGS_LIBRARY_SUFFIX=\".so\" -D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security'
#NOTE:JK: no --enable-vst3 passed to configure
%configure \
%if %{with run_functional_tests}
    --enable-run-functional-tests \
%endif
    FO_XSL=/usr/share/xml/docbook/stylesheet/nwalsh/current/fo/docbook.xsl HTMLHELP_XSL="/usr/share/xml/docbook/stylesheet/nwalsh/current/htmlhelp/htmlhelp.xsl" --disable-upstream-gtk-doc --enable-introspection --disable-oss --with-poppler --with-gtk-unix-print --enable-gtk-doc --enable-gtk-doc-html

%make_build all
%make_build html
%make_build fix-local-html
%make_build pdf

%install
%make_install
%make_install install-compress-changelog
%make_install install-html-mkdir
%make_install install-html-mkdir-links
%make_install install-html
%make_install install-pdf-mkdir
%make_install install-pdf
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_datadir}/doc-base/
mkdir -p %{buildroot}%{_datadir}/doc/packages
mv %{buildroot}%{_datadir}/doc/gsequencer  %{buildroot}%{_docdir}
%find_lang %name

%check
xvfb-run --server-args="-screen 0 1920x1080x24" -a make check
desktop-file-validate %{buildroot}/%{_datadir}/applications/gsequencer.desktop

%files -f %name.lang
%license COPYING
%{_bindir}/gsequencer
%{_bindir}/midi2xml
%{_mandir}/man1/gsequencer.1*
%{_mandir}/man1/midi2xml.1*
%{_datadir}/gsequencer/
%{_datadir}/xml/gsequencer/
%{_docdir}/gsequencer/
%{_docdir}/gsequencer/pdf/user-manual-a4.pdf
%{_docdir}/gsequencer/pdf/user-manual-letter.pdf
%{_datadir}/applications/gsequencer.desktop
%{_datadir}/icons/hicolor/*/apps/gsequencer.png
%{_datadir}/icons/hicolor/scalable/apps/gsequencer.svg
%{_datadir}/metainfo/*
%{_datadir}/mime/packages/*

%package -n libags%{libagssonumber}
Summary:        GSequencer core libraries
Group:          System/Libraries

%description -n libags%{libagssonumber}
Advanced Gtk+ Sequencer is an audio sequencer application.
This subpackage contains part of its library set.

%package -n typelib-1_0-Libags-4_0
Summary:        GSequencer core libraries -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Libags-4_0
Advanced Gtk+ Sequencer is an audio sequencer application.
This package provides the GObject Introspection bindings for Libags.

%package -n libgsequencer%{libgsequencersonumber}
Summary:        GSequencer core libraries
Group:          System/Libraries

%description -n libgsequencer%{libgsequencersonumber}
Advanced Gtk+ Sequencer is an audio sequencer application.
This subpackage contains part of its library set.

%package devel
Summary:        Advanced Gtk+ Sequencer library development files
Group:          Development/Libraries/C and C++
Requires:       libags%{libagssonumber} = %{version}
Requires:       libgsequencer%{libgsequencersonumber} = %{version}

%description devel
Advanced Gtk+ Sequencer library development files.

%files devel
%{_includedir}/ags/
%{_libdir}/libags.so
%{_libdir}/libags_thread.so
%{_libdir}/libags_server.so
%{_libdir}/libags_gui.so
#%{_libdir}/libags_vst.so
%{_libdir}/libags_audio.so
%{_libdir}/libgsequencer.so
%{_datadir}/gir-1.0/*.gir
%{_libdir}/pkgconfig/libags.pc
%{_libdir}/pkgconfig/libags_audio.pc
%{_libdir}/pkgconfig/libags_gui.pc
%{_libdir}/pkgconfig/libgsequencer.pc

%package -n gsequencer-devel-doc
Summary:        Documentation for Advanced Gtk+ Sequencer
Group:          Documentation/HTML
BuildArch:      noarch

%description -n gsequencer-devel-doc
Advanced Gtk+ Sequencer library development documentation.

%post   -n libags%{libagssonumber} -p /sbin/ldconfig
%postun -n libags%{libagssonumber} -p /sbin/ldconfig
%post   -n libgsequencer%{libgsequencersonumber} -p /sbin/ldconfig
%postun -n libgsequencer%{libgsequencersonumber} -p /sbin/ldconfig

%files -n libags%{libagssonumber}
%defattr(-,root,root)
%{_libdir}/libags.so.%{libagssonumber}*
%{_libdir}/libags_thread.so.%{libagssonumber}*
%{_libdir}/libags_server.so.%{libagssonumber}*
%{_libdir}/libags_gui.so.%{libagssonumber}*
#%{_libdir}/libags_vst.so.%{libagssonumber}*
%{_libdir}/libags_audio.so.%{libagssonumber}*

%files -n typelib-1_0-Libags-4_0
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Ags-4.0.typelib
%{_libdir}/girepository-1.0/AgsGui-4.0.typelib
%{_libdir}/girepository-1.0/AgsAudio-4.0.typelib

%files -n libgsequencer%{libgsequencersonumber}
%defattr(-,root,root)
%{_libdir}/libgsequencer.so.%{libgsequencersonumber}*

%files -n gsequencer-devel-doc
%{_datadir}/gtk-doc/
%{_datadir}/doc/libags-audio-doc/

%changelog
