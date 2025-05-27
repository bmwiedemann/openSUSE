#
# spec file for package libtheora
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           libtheora
Version:        1.2.0
Release:        0
Summary:        Theora video compression codec
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Other
URL:            https://www.theora.org/
Source0:        http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)

%description
Theora is a free and open video compression format. It is designed to scale
well from postage stamp to HD resolution, and is considered particularly
competitive at low bitrates.

%package -n libtheora1
Summary:        Theora video compression codec
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libtheora1
Theora is a free and open video compression format. It is designed to scale
well from postage stamp to HD resolution, and is considered particularly
competitive at low bitrates.

The package contains the library that can decode and encode Theora streams.
Theora is also able to playback VP3 streams.

%package -n libtheoradec2
Summary:        Theora video decompression library
Group:          System/Libraries

%description -n libtheoradec2
Theora is a free and open video compression format. It is designed to scale
well from postage stamp to HD resolution, and is considered particularly
competitive at low bitrates.

This subpackage contains the decoder library.

%package -n libtheoraenc2
Summary:        Theora video compression library
Group:          System/Libraries

%description -n libtheoraenc2
Theora is a free and open video compression format. It is designed to scale
well from postage stamp to HD resolution, and is considered particularly
competitive at low bitrates.

This subpackage contains the encoder library.

%package devel
Summary:        Theora video compression codec
Group:          Development/Libraries/C and C++
Requires:       libtheora1 = %{version}
Requires:       libtheoradec2 = %{version}
Requires:       libtheoraenc2 = %{version}

%description devel
Theora is a free and open video compression format. It is designed to scale
well from postage stamp to HD resolution, and is considered particularly
competitive at low bitrates.

The package contains the library that can decode and encode Theora streams.
Theora is also able to playback VP3 streams.

%prep
%autosetup -p1

%build
%configure \
	--disable-examples \
	--disable-static \
	--with-pic \
	%{nil}
%make_build docdir=%{_docdir}/%{name}

%install
%make_install docdir=%{_docdir}/%{name}

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "doxygen-build.stamp" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n libtheora1
%ldconfig_scriptlets -n libtheoradec2
%ldconfig_scriptlets -n libtheoraenc2

%files -n libtheora1
%license COPYING LICENSE
%{_libdir}/libtheora.so.1*

%files -n libtheoradec2
%license COPYING LICENSE
%{_libdir}/libtheoradec.so.2*

%files -n libtheoraenc2
%license COPYING LICENSE
%{_libdir}/libtheoraenc.so.2*

%files devel
%license COPYING LICENSE
%doc AUTHORS CHANGES README.md
%{_docdir}/%{name}
%{_includedir}/theora
%{_libdir}/libtheora.so
%{_libdir}/libtheoradec.so
%{_libdir}/libtheoraenc.so
%{_libdir}/pkgconfig/theora.pc
%{_libdir}/pkgconfig/theoradec.pc
%{_libdir}/pkgconfig/theoraenc.pc

%changelog
