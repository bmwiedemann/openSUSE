#
# spec file for package libtheora
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libtheora
Summary:        Theora video compression codec
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Other
Version:        1.1.1
Release:        0
%define pkg_version %version
Url:            http://www.theora.org/

Source:         http://downloads.xiph.org/releases/theora/%{name}-%{pkg_version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  pkg-config
BuildRequires:  python
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# bug437293
%ifarch ppc64
Obsoletes:      libtheora-64bit
%endif

%description
Theora is a free and open video compression format from the Xiph.org Foundation. Like all our 
multimedia technology it can be used to distribute film and video online and on disc without 
the licensing and royalty fees or vendor lock-in associated with other formats.

%package -n libtheora0
Summary:        Theora video compression codec
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} <= %{version}
# bug437293
%ifarch ppc64
Obsoletes:      libtheora-64bit
%endif
#

%description -n libtheora0
Theora is a free and open video compression format from the Xiph.org Foundation. Like all our 
multimedia technology it can be used to distribute film and video online and on disc without 
the licensing and royalty fees or vendor lock-in associated with other formats.

Theora scales from postage stamp to HD resolution, and is considered particularly competitive 
at low bitrates. It is in the same class as MPEG-4/DiVX, and like the Vorbis audio codec it 
has lots of room for improvement as encoder technology develops.

Theora is in full public release as of November 3, 2008. The bitstream format for Theora I 
was frozen Thursday, 2004 July 1. All bitstreams encoded since that date will remain compatible 
with future releases.

The package contains the library that can decode and encode Theora streams. Theora is also 
able to playback VP3 streams.

Authors:
--------
    the Xiph.Org Foundation http://www.xiph.org/

%package -n libtheoradec1
Summary:        Theora video decompression library
Group:          System/Libraries

%description -n libtheoradec1
Theora is a free and open video compression format from the Xiph.org Foundation. Like all our 
multimedia technology it can be used to distribute film and video online and on disc without 
the licensing and royalty fees or vendor lock-in associated with other formats.

This subpackage contains the decoder library.

%package -n libtheoraenc1
Summary:        Theora video compression library
Group:          System/Libraries

%description -n libtheoraenc1
Theora is a free and open video compression format from the Xiph.org Foundation. Like all our 
multimedia technology it can be used to distribute film and video online and on disc without 
the licensing and royalty fees or vendor lock-in associated with other formats.

This subpackage contains the encoder library.

%package devel
Summary:        Theora video compression codec
Group:          Development/Libraries/C and C++
Requires:       libogg-devel
Requires:       libtheora0 = %{version}
Requires:       libtheoradec1 = %{version}
Requires:       libtheoraenc1 = %{version}
# bug437293
%ifarch ppc64
Obsoletes:      libtheora-devel-64bit
%endif
#

%description devel
Theora is a free and open video compression format from the Xiph.org Foundation. Like all our 
multimedia technology it can be used to distribute film and video online and on disc without 
the licensing and royalty fees or vendor lock-in associated with other formats.

Theora scales from postage stamp to HD resolution, and is considered particularly competitive 
at low bitrates. It is in the same class as MPEG-4/DiVX, and like the Vorbis audio codec it 
has lots of room for improvement as encoder technology develops.

Theora is in full public release as of November 3, 2008. The bitstream format for Theora I 
was frozen Thursday, 2004 July 1. All bitstreams encoded since that date will remain compatible 
with future releases.

The package contains the library that can decode and encode Theora streams. Theora is also 
able to playback VP3 streams.

Authors:
--------
    the Xiph.Org Foundation http://www.xiph.org/

%prep
%setup -q -n %{name}-%{pkg_version}

%build
ACLOCAL="aclocal -I m4" autoreconf -f -i
%configure --disable-examples \
    --disable-static \
    --with-pic
make %{?_smp_mflags} docdir=%{_docdir}/%{name}

%install
%make_install docdir=%{_docdir}/%{name}
%{__install} -d $RPM_BUILD_ROOT%{_bindir}
# Install remaining parts of documentation.
%{__cp} -a AUTHORS CHANGES COPYING LICENSE README $RPM_BUILD_ROOT%{_docdir}/%{name}

%check
%{__make} check

%post   -n libtheora0 -p /sbin/ldconfig
%postun -n libtheora0 -p /sbin/ldconfig
%post   -n libtheoradec1 -p /sbin/ldconfig
%postun -n libtheoradec1 -p /sbin/ldconfig
%post   -n libtheoraenc1 -p /sbin/ldconfig
%postun -n libtheoraenc1 -p /sbin/ldconfig

%files -n libtheora0
%defattr(-,root,root)
%{_libdir}/libtheora.so.0*

%files -n libtheoradec1
%defattr(-,root,root)
%{_libdir}/libtheoradec.so.1*

%files -n libtheoraenc1
%defattr(-,root,root)
%{_libdir}/libtheoraenc.so.1*

%files devel
%defattr(-,root,root)
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%{_includedir}/theora
%{_libdir}/*.so
%{_libdir}/pkgconfig/theoradec.pc
%{_libdir}/pkgconfig/theoraenc.pc
%{_libdir}/pkgconfig/theora.pc
%exclude %{_libdir}/*.la

%changelog
