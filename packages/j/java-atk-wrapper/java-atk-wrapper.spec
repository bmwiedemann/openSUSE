#
# spec file for package java-atk-wrapper
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


%global major_version 0.33
Name:           java-atk-wrapper
Version:        0.33.2
Release:        0
Summary:        Java ATK Wrapper
License:        LGPL-2.0+
Group:          Development/Libraries/Java
Url:            http://git.gnome.org/browse/java-atk-wrapper/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
Source1:        HOWTO
Source2:        https://git.gnome.org/browse/java-atk-wrapper/plain/wrapper/manifest.txt
Source3:        https://git.gnome.org/browse/java-atk-wrapper/plain/autogen.sh
# Avoid libtool versioning; this library is dynamically loaded from Java code
Patch0:         jaw-avoid-version.patch
Patch1:         jaw-java_required.patch
Patch2:         jaw-quotes.patch
Patch3:         jaw-gdk.patch
Patch4:         jaw-javah.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  java-devel >= 1.7
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xprop
BuildRequires:  xz
BuildRequires:  pkgconfig(atk) >= 2.14.0
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(atspi-2) >= 2.14.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
Requires:       java >= 1.7
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
cp %{SOURCE1} .
cp %{SOURCE2} wrapper/
cp %{SOURCE3} .
rm -f wrapper/org/GNOME/Accessibility/AtkWrapper.java

%build
chmod +x autogen.sh
./autogen.sh
%configure JAVACFLAGS="-source 1.7 -target 1.7" --libdir=%{_libdir}/%{name}
make %{?_smp_mflags}

%install
make -C jni install DESTDIR=%{buildroot}
install wrapper/java-atk-wrapper.jar %{buildroot}%{_libdir}/%{name}/
find %{buildroot} -type f -name "*.la" -delete -print

%files
%doc AUTHORS
%doc COPYING.LESSER
%doc NEWS
%doc README
%doc HOWTO
%{_libdir}/%{name}/

%changelog
