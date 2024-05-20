#
# spec file for package spiel
#
# Copyright (c) 2024 SUSE LLC
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


Name:           spiel
Version:        1.0.1
Release:        0
Summary:        Speech synthesis API and framework for free desktops
License:        LGPL-2.1-or-later
URL:            https://eeejay.github.io/spiel/
Source:         %{name}-%{version}.tar.zst
BuildRequires:  meson >= 0.64.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.76
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.76
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)

%description
Spiel provides a speech synthesis API for desktop Linux and beyond.

It consists of two parts, a speech provider interface specification and a client library.

%package devel
Summary:        Header files for libspiel
Requires:       libspeech-provider-1_0 = %{version}
Requires:       libspiel-1_0 = %{version}
Requires:       typelib-1_0-SpeechProvider-1_0 = %{version}
Requires:       typelib-1_0-Spiel-1_0 = %{version}

%description devel
Spiel provides a speech synthesis API for desktop Linux and beyond.

It consists of two parts, a speech provider interface specification and a client library.

%package -n typelib-1_0-SpeechProvider-1_0
Summary:        Speech synthesis API and framework for free desktops

%description -n typelib-1_0-SpeechProvider-1_0
Spiel provides a speech synthesis API for desktop Linux and beyond.

It consists of two parts, a speech provider interface specification and a client library.

%package -n typelib-1_0-Spiel-1_0
Summary:        Speech synthesis API and framework for free desktops

%description -n typelib-1_0-Spiel-1_0
Spiel provides a speech synthesis API for desktop Linux and beyond.

It consists of two parts, a speech provider interface specification and a client library.

%package -n libspeech-provider-1_0
Summary:        Speech synthesis API and framework for free desktops

%description -n libspeech-provider-1_0
Spiel provides a speech synthesis API for desktop Linux and beyond.

It consists of two parts, a speech provider interface specification and a client library.

%package -n libspiel-1_0
Summary:        Speech synthesis API and framework for free desktops

%description -n libspiel-1_0
Spiel provides a speech synthesis API for desktop Linux and beyond.

It consists of two parts, a speech provider interface specification and a client library.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/spiel
%{_datadir}/glib-2.0/schemas/org.monotonous.libspiel.gschema.xml

%files devel
%{_includedir}/speech-provider/
%{_includedir}/spiel/
%{_libdir}/pkgconfig/speech-provider-1.0.pc
%{_libdir}/pkgconfig/spiel-1.0.pc
%{_datadir}/gir-1.0/SpeechProvider-1.0.gir
%{_datadir}/gir-1.0/Spiel-1.0.gir

%files -n typelib-1_0-SpeechProvider-1_0
%{_libdir}/girepository-1.0/SpeechProvider-1.0.typelib

%files -n typelib-1_0-Spiel-1_0
%{_libdir}/girepository-1.0/Spiel-1.0.typelib

%files -n libspeech-provider-1_0
%{_libdir}/libspeech-provider-1.0.so

%files -n libspiel-1_0
%{_libdir}/libspiel-1.0.so

%changelog
