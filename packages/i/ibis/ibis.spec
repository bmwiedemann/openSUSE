#
# spec file for package ibis
#
# Copyright (c) 2025 SUSE LLC
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


%define         sover 0
Name:           ibis
Version:        0.11.2
Release:        0
Summary:        Gobject based library
License:        GPL-2.0-or-later
URL:            https://keep.imfreedom.org/ibis/ibis
Source0:        https://downloads.sf.net/pidgin/%{name}/%{name}-%{version}.tar.xz
Source1:        https://downloads.sf.net/pidgin/%{name}/%{name}-%{version}.tar.xz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x40de1dc7288fe3f50ab938c548f66affd9bdb729#/%{name}.keyring
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gi-docgen >= 2023.1
BuildRequires:  pkgconfig(birb)
BuildRequires:  pkgconfig(gio-2.0) >= 2.76
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gobject-2.0) >= 2.76
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(hasl)

%description
This parser originated out of an early version of purple-spasm. The library was
then adopted by the new IRCv3 protocol in purple 3 with the intent of being
able to subclass the protocol. However that proved to be very difficult and
thus Ibis was split out to its own library where others can use it.

Ibis is what we like to call an integration library. What that means is that it
is used to integrate the protocol into your application instead of bolting the
protocol onto your application in a highly opinionated way.

What this really means is that Ibis will do the heavy lifting for you of
handling the protocol specifics like parsing and serialization as well as any
building blocks the protocol requires.

However, this is where Ibis stops. Again, Ibis is meant for integration, so it
has zero opinion about how messages are handled, therefore it doesn't try to
handle them. Instead it makes the messages available to you, the integrator, to
do what you want with them.

%package devel
Summary:        Development files for %{name}
Requires:       typelib-1_0-Ibis-1_0 = %{version}

%description devel
%{summary}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%package -n typelib-1_0-Ibis-1_0
Summary:        Typelib for %{name}

%description -n typelib-1_0-Ibis-1_0
%{summary}.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}%{sover}
%{summary}.

%prep
%autosetup

%build
%meson \
  -Ddoc=true \
  -Dintrospection=true \
  -Dnls=true
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n lib%{name}%{sover}

%files devel
%license LICENSE
%doc AUTHORS README.md ChangeLog
%{_includedir}/%{name}-1.0
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Ibis-1.0.gir

%files -n typelib-1_0-Ibis-1_0
%{_libdir}/girepository-1.0/Ibis-1.0.typelib

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files doc
%{_datadir}/doc/%{name}

%changelog
