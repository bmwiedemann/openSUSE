#
# spec file for package libskk
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


%define sover 0
%define real_version 1.0.5
Name:           libskk
# Note this is 1.0.5 release version
# Some package maintainer once specified wrong version number
# so we have to keep 1.2.0
Version:        1.2.0+git20180916+%{real_version}
Release:        0
Summary:        A statistical language model based Japanese input method engine
License:        GPL-3.0-or-later
Group:          System/I18n/Japanese
URL:            https://github.com/ueno/libskk
Source0:        %{name}-%{real_version}.tar.xz
Source1:        %{name}-%{real_version}.tar.xz.sig
Source99:       baselibs.conf
Patch0:         libskk-typlib-dependencies.patch
# PATCH-FIX-UPSTREAM fix-build-on-gcc14+.patch hillwood@opensuse.org - Support gcc 14+
Patch1:         fix-build-on-gcc14+.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  sqlite3-devel
BuildRequires:  vala-devel >= 0.14
BuildRequires:  xz
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(xkbcommon)

%description
SKK is a statistical language model based Japanese input method engine.
to model the Japanese language, it use a backoff bigram and trigram

%package -n %{name}%{sover}
Summary:        A statistical language model based Japanese input method engine
Group:          System/Libraries
Requires:       skkdic
Requires:       skkdic-extra

%description -n %{name}%{sover}
SKK is a statistical language model based Japanese input method engine.
to model the Japanese language, it use a backoff bigram and trigram

This package provides GObject-based library to deal with Japanese
kana-to-kanji conversion method.

%package -n typelib-1_0-Skk-1_0
Summary:        Introspection bindings for libskk, a Japanese IME
Group:          System/I18n/Japanese
Requires:       girepository-1_0

%description -n typelib-1_0-Skk-1_0
SKK is a statistical language model based Japanese input method engine.
to model the Japanese language, it use a backoff bigram and trigram

This package provides the introspection bindings for the libskk library.

%package -n libskk-devel
Summary:        Development Files for libskk
Group:          Development/Libraries/Other
Requires:       %{name}%{sover} = %{version}

%description -n libskk-devel
SKK is a statistical language model based Japanese input method engine.
to model the Japanese language, it use a backoff bigram and trigram

This package provides C/Vala headers for the libskk library.

%prep
%autosetup -p1 -n %{name}-%{real_version}

%build
autoreconf -f
%configure --disable-static \
           --enable-introspection=yes
%make_build

%install
%make_install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%find_lang %{name}

%fdupes %{buildroot}/%{_prefix}

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover} -f %{name}.lang
%license COPYING
%doc README NEWS
%{_mandir}/man1/skk.1%{?ext_man}
%{_bindir}/skk
%{_libdir}/%{name}.so.*
%{_datadir}/%{name}

%files -n typelib-1_0-Skk-1_0
%{_libdir}/girepository-1.0/Skk-1.0.typelib

%files -n libskk-devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libskk.pc
%{_datadir}/gir-1.0/Skk-1.0.gir
%{_datadir}/vala/vapi/skk-1.0.deps
%{_datadir}/vala/vapi/skk-1.0.vapi

%changelog
