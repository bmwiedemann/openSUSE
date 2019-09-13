#
# spec file for package gnome-desktop-sharp2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%{s}\\n" "${filelist[@]}" | %{_libexecdir}/rpm/find-provides && printf "%{s}\\n" "${filelist[@]}" | %{_bindir}/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%{s}\\n" "${filelist[@]}" | %{_libexecdir}/rpm/find-requires && printf "%{s}\\n" "${filelist[@]}" | %{_bindir}/mono-find-requires ; } | sort | uniq'
Name:           gnome-desktop-sharp2
Version:        2.26.0
Release:        0
Summary:        Mono bindings for libgnome-desktop
License:        LGPL-2.1-only
Group:          Development/Languages/Mono
URL:            https://github.com/mono/gnome-desktop-sharp
Source:         gnome-desktop-sharp-%{version}.tar.bz2
Patch0:         gnome-desktop-version-11.3.patch
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(gnome-desktop-2.0)
BuildRequires:  pkgconfig(gnome-sharp-2.0)
BuildRequires:  pkgconfig(gtksourceview-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwnck-1.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(monodoc)
Requires:       libgnome-desktop-2-17

%description
Mono bindings for libgnome-desktop

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}
Requires:       gtksourceview2-sharp = %{version}
Requires:       rsvg2-sharp = %{version}
Requires:       wnck-sharp = %{version}
Provides:       gtksourceview2-sharp-devel = %{version}
Provides:       rsvg2-sharp-devel = %{version}
Provides:       wnck-sharp-devel = %{version}

%description devel
Development files (.pc) for %{name}.

%package -n gtksourceview2-sharp
Summary:        Mono bindings for gtksourceview2
Group:          Development/Languages/Mono
Requires:       libgtksourceview2sharpglue-2.so = %{version}
Provides:       gtksourceview-sharp2 = %{version}
Provides:       libgtksourceview2sharpglue-2.so = %{version}
Obsoletes:      gtksourceview-sharp2 < %{version}

%description -n gtksourceview2-sharp
Mono bindings for gtksourceview2

%package -n rsvg2-sharp
Summary:        Mono bindings for rsvg
Group:          Development/Languages/Mono

%description -n rsvg2-sharp
This package contains Mono bindings for librsvg.

%package -n wnck-sharp
Summary:        Mono bindings for wnck
Group:          Development/Languages/Mono
Requires:       libwnck-1-22
Requires:       libwncksharpglue-2.so = %{version}
Provides:       libwncksharpglue-2.so = %{version}

%description -n wnck-sharp
Mono bindings for wnck

%prep
%setup -q -n gnome-desktop-sharp-%{version}
%patch0

%build
# FIXME: windowmanager.c:*: warning: dereferencing type-punned pointer will break strict-aliasing rules
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure --libexecdir=%{_libexecdir} --enable-debug
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name "*.*a" -delete

%post -n gtksourceview2-sharp -p /sbin/ldconfig
%postun -n gtksourceview2-sharp -p /sbin/ldconfig
%post -n wnck-sharp -p /sbin/ldconfig
%postun -n wnck-sharp -p /sbin/ldconfig

%files
%{_libexecdir}/mono/gac/*gnomedesktop-sharp
%{_libexecdir}/mono/gnomedesktop-sharp-2.20
%dir %{_datadir}/gnomedesktop-sharp
%{_datadir}/gnomedesktop-sharp/2.20

%files devel
%{_libdir}/pkgconfig/gnome-desktop-sharp-2.0.pc
%{_libdir}/pkgconfig/gtksourceview2-sharp.pc
%{_libdir}/pkgconfig/rsvg2-sharp-2.0.pc
%{_libdir}/pkgconfig/wnck-sharp-1.0.pc

%files -n gtksourceview2-sharp
%{_libexecdir}/mono/gac/*gtksourceview2-sharp
%{_libexecdir}/mono/gtksourceview2-sharp-2.0
%dir %{_datadir}/gtksourceview2-sharp
%{_datadir}/gtksourceview2-sharp/2.0
%{_libdir}/libgtksourceview2sharpglue-2.so

%files -n rsvg2-sharp
%{_libexecdir}/mono/gac/*rsvg2-sharp
%{_libexecdir}/mono/rsvg2-sharp-2.0
%dir %{_datadir}/rsvg2-sharp
%{_datadir}/rsvg2-sharp/2.0

%files -n wnck-sharp
%{_libexecdir}/mono/gac/*wnck-sharp
%{_libexecdir}/mono/wnck-sharp-2.20
%dir %{_datadir}/wnck-sharp
%{_datadir}/wnck-sharp/2.20
%{_libdir}/libwncksharpglue-2.so

%changelog
