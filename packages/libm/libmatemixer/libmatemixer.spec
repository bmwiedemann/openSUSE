#
# spec file for package libmatemixer
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   0
%define _version 1.23
Name:           libmatemixer
Version:        1.23.0
Release:        0
Summary:        Mixer library for MATE Desktop
License:        LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         http://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libpulse) >= 5.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
%glib2_gsettings_schema_requires

%description
libmatemixer is a mixer library for MATE desktop.

It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

%package -n %{name}%{sover}
Summary:        Mixer library for MATE Desktop
Group:          System/Libraries
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description -n %{name}%{sover}
libmatemixer is a mixer library for MATE desktop.

It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

%lang_package

%package devel
Summary:        MATE Desktop keyboard configuration development files
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
libmatemixer is a mixer library for MATE desktop.

It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static    \
  --enable-pulseaudio \
  --enable-alsa
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/%{name}.so.%{sover}*
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/libmatemixer-null.so
%{_libdir}/%{name}/libmatemixer-pulse.so
%{_libdir}/%{name}/libmatemixer-alsa.so

%files devel
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/gtk-doc/html
%{_includedir}/mate-mixer/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files lang -f %{name}.lang

%changelog
