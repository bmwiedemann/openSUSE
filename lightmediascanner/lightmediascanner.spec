#
# spec file for package lightmediascanner
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 0
Name:           lightmediascanner
Version:        0.5.1
Release:        0
Summary:        Lightweight media scanner
License:        LGPL-2.1
Group:          Productivity/Multimedia/Other
Url:            https://github.com/profusion/lightmediascanner
Source:         https://github.com/profusion/lightmediascanner/archive/release_%{version}.tar.gz#/%{name}-release_%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  file-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)

%description
Lightweight media scanner meant to be used in not-so-powerful devices,
like embedded systems or old machines.

%package -n     lib%{name}%{sover}
Summary:        The core library for %{name}
Group:          System/Libraries

%description -n lib%{name}%{sover}
Lightweight media scanner.

This package contains the shared library.

%package        devel
Summary:        Development files of %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description    devel
Lightweight media scanner.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%setup -q -n %{name}-release_%{version}

sed -i 's/CODEC_ID_MP3/AV_CODEC_ID_MP3/' $(grep -rl CODEC_ID_MP3)

%build
export CFLAGS="%{optflags} -I$(pkg-config --variable=includedir libavformat)"
NOCONFIGURE=yes
./autogen.sh
%configure \
        --disable-static \
        --enable-daemon
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%doc AUTHORS COPYING* README NEWS
%{_bindir}/lightmediascannerctl
%{_bindir}/lightmediascannerd
%{_libdir}/%{name}/
%{_datadir}/dbus-1/services/org.%{name}.service

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}_charset_conv.h
%{_includedir}/%{name}_db.h
%{_includedir}/%{name}_plugin.h
%{_includedir}/%{name}_utils.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
