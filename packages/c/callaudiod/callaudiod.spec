#
# spec file for package callaudiod
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


%define soname libcallaudio0_1-0
%define apiver 0.1

Name:           callaudiod
Version:        0.1.7
Release:        0
Summary:        Daemon for audio calls
License:        GPL-3.0-or-later AND MIT
URL:            https://gitlab.com/mobian1/callaudiod
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  gtkdoc
BuildRequires:  meson
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libebook-contacts-1.2)
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(mm-glib)

%description
A daemon for audio calls.

%package -n %{soname}
Summary:        Shared library files for %{name}

%description -n %{soname}
A daemon for audio calls.
This package contains the shared library files for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       %{soname} = %{version}

%description devel
A daemon for audio calls.
This package contains the development and header files for %{name}.

%package doc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description doc
A daemon for audio calls.
This package contains API documentation for %{name}.

%prep
%autosetup

%build
%meson \
	-Dgtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n %{soname}

%files
%license COPYING
%{_bindir}/callaudiocli
%{_bindir}/callaudiod
%{_datadir}/dbus-1/interfaces/org.mobian_project.CallAudio.xml
%{_datadir}/dbus-1/services/org.mobian_project.CallAudio.service

%files -n %{soname}
%{_libdir}/libcallaudio-%{apiver}.so.*

%files devel
%{_includedir}/libcallaudio-%{apiver}/
%{_libdir}/libcallaudio-%{apiver}.so
%{_libdir}/pkgconfig/libcallaudio-%{apiver}.pc

%files doc
%{_datadir}/gtk-doc/html/libcallaudio/

%changelog
