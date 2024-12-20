#
# spec file for package java-atk-wrapper
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


%global major_version 0.40
Name:           java-atk-wrapper
Version:        %{major_version}.0
Release:        0
Summary:        Java ATK Wrapper
License:        LGPL-2.0-or-later
Group:          Development/Libraries/Java
URL:            https://gitlab.gnome.org/GNOME/java-atk-wrapper/
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
Source1:        HOWTO
Source2:        https://gitlab.gnome.org/GNOME/%{name}/-/raw/%{version}/autogen.sh
Patch0:         jaw-dependencies.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  java-devel >= 9
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xprop
BuildRequires:  xz
BuildRequires:  pkgconfig(atk) >= 2.14.0
BuildRequires:  pkgconfig(atk-bridge-2.0) >= 2.33.1
BuildRequires:  pkgconfig(atspi-2) >= 2.14.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  strip-nondeterminism
Requires:       java >= 1.8
Requires:       xprop

%description
Java ATK Wrapper is a implementation of ATK by using JNI technic. It
converts Java Swing events into ATK events, and send these events to
ATK-Bridge.

JAW is part of the Bonobo deprecation project. It will replaces the
former java-access-bridge.
By talking to ATK-Bridge, it keeps itself from being affected by the
change of underlying communication mechanism.

%prep
%setup -q
%patch -P 0 -p1
cp %{SOURCE1} %{SOURCE2} .

%build
chmod +x autogen.sh
./autogen.sh
%configure --libdir=%{_libdir}/%{name} --enable-modular-jar
make %{?_smp_mflags}

%install
make -C jni install DESTDIR=%{buildroot}
install wrapper/java-atk-wrapper.jar %{buildroot}%{_libdir}/%{name}/
find %{buildroot} -type f -name "*.la" -delete -print
cd %{buildroot}%{_libdir}/%{name}/
%?strip_all_nondeterminism

%files
%doc AUTHORS
%license COPYING.LESSER
%doc NEWS
%doc README
%doc HOWTO
%{_libdir}/%{name}/

%changelog
