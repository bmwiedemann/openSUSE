#
# spec file for package soup-sharp
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           soup-sharp
Version:        2.42.2+git.20141217.4404312
Release:        0
Summary:        Libsoup bindings for Mono
License:        LGPL-3.0
Group:          Development/Languages/Mono
Url:            http://www.go-mono.org/
Source:         %{name}-%{version}.tar.xz
Source99:       soup-sharp-rpmlintrc
BuildRequires:  libtool
BuildRequires:  mono-core
BuildRequires:  pkgconfig(gapi-3.0) >= 2.99.2
BuildRequires:  pkgconfig(glib-sharp-3.0) >= 2.99.2
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(mono) >= 1.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

This package provides the mono bindings for libsoup.

%package devel
Summary:        Libsoup bindings for Mono -- Development files
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}

%description devel
Libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

This package provides development files for the Mono bindings

%prep
%setup -q

%build
# We don't use autogen, as this forcibly launches configure
mkdir -p m4
autoreconf  -i --force --warnings=none -I . -I m4
%configure \
    --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%defattr(-,root,root)
%doc COPYING
%{_prefix}/lib/mono/soup-sharp/
%{_prefix}/lib/mono/gac/soup-sharp/
%{_libdir}/libsoupsharpglue-2.42.2.so

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/soup-sharp-2.4.pc

%changelog

