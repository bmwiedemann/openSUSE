#
# spec file for package libkate
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 SUSE Dominique Leuenberger, Amsterdam, Netherlands
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


# python2_sitelib isn't defined in Leap:42.3
%if 0%{?suse_version} <= 1315
%define python2_sitelib %{python_sitelib}
%endif
%bcond_without python2
Name:           libkate
Version:        0.4.1
Release:        0
Summary:        A karaoke and text codec for embedding in Ogg
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Other
URL:            http://libkate.googlecode.com
Source:         http://libkate.googlecode.com/files/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
Patch0:         disable-namespace-test.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)
%if %{with python2}
BuildRequires:  python2-base
%endif

%description
Kate is a codec for karaoke and text encapsulation for Ogg. Most of the
time, this would be multiplexed with audio/video to carry subtitles,
song lyrics (with or without karaoke data), etc, but doesn't have to be.
A possible use of a lone Kate stream would be an e-book. Moreover, the
motion feature gives Kate a powerful means to describe arbitrary curves,
so hand drawing of shapes can be achieved.

This was originally meant for karaoke use, but can be used for any
purpose. Motions can be attached to various semantics, like position,
color, etc, so scrolling or fading text can be defined.

%package -n %{name}1
Summary:        A karaoke and text codec for embedding in Ogg
Group:          System/Libraries

%description -n %{name}1
Kate is a codec for karaoke and text encapsulation for Ogg. Most of the
time, this would be multiplexed with audio/video to carry subtitles,
song lyrics (with or without karaoke data), etc, but doesn't have to be.
A possible use of a lone Kate stream would be an e-book. Moreover, the
motion feature gives Kate a powerful means to describe arbitrary curves,
so hand drawing of shapes can be achieved.

This was originally meant for karaoke use, but can be used for any
purpose. Motions can be attached to various semantics, like position,
color, etc, so scrolling or fading text can be defined.

%package -n liboggkate1
Summary:        A karaoke and text codec for embedding in Ogg
Group:          System/Libraries
Conflicts:      libkate1 < 0.4.1

%description -n liboggkate1
Kate is a codec for karaoke and text encapsulation for Ogg. Most of the
time, this would be multiplexed with audio/video to carry subtitles,
song lyrics (with or without karaoke data), etc, but doesn't have to be.
A possible use of a lone Kate stream would be an e-book. Moreover, the
motion feature gives Kate a powerful means to describe arbitrary curves,
so hand drawing of shapes can be achieved.

This was originally meant for karaoke use, but can be used for any
purpose. Motions can be attached to various semantics, like position,
color, etc, so scrolling or fading text can be defined.

%package devel
Summary:        A karaoke and text codec for embedding in Ogg - Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name}1 = %{version}
Requires:       glibc-devel
Requires:       liboggkate1 = %{version}
Requires:       pkgconfig(ogg)

%description devel
Kate is a codec for karaoke and text encapsulation for Ogg. Most of the
time, this would be multiplexed with audio/video to carry subtitles,
song lyrics (with or without karaoke data), etc, but doesn't have to be.
A possible use of a lone Kate stream would be an e-book. Moreover, the
motion feature gives Kate a powerful means to describe arbitrary curves,
so hand drawing of shapes can be achieved.

This was originally meant for karaoke use, but can be used for any
purpose. Motions can be attached to various semantics, like position,
color, etc, so scrolling or fading text can be defined.

This package contains files for developers.

%package tools
Summary:        A karaoke and text codec for embedding in Ogg
Group:          Productivity/Multimedia/Other

%description tools
Kate is a codec for karaoke and text encapsulation for Ogg. Most of the
time, this would be multiplexed with audio/video to carry subtitles,
song lyrics (with or without karaoke data), etc, but doesn't have to be.
A possible use of a lone Kate stream would be an e-book. Moreover, the
motion feature gives Kate a powerful means to describe arbitrary curves,
so hand drawing of shapes can be achieved.

This was originally meant for karaoke use, but can be used for any
purpose. Motions can be attached to various semantics, like position,
color, etc, so scrolling or fading text can be defined.

%package -n python-katedj
Summary:        Editor and remixer for Kate streams in Ogg
Group:          Productivity/Multimedia/Other
Requires:       %{name}-tools = %{version}
Requires:       oggz-tools
Requires:       python-wxWidgets
Provides:       katedj = 0.4.1
Obsoletes:      katedj < 0.4.1
BuildArch:      noarch

%description -n python-katedj
KateDJ allows extracting Kate tracks embedded in an Ogg stream, editing
them, and rebuilding the Ogg stream after the Kate tracks are modified.

%prep
%setup -q
%patch0 -p1

%build
echo 'HTML_TIMESTAMP=NO' >> doc/kate.doxygen.in
%configure \
        --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Remove files that we install with %%doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}/{AUTHORS,COPYING,ChangeLog,README,THANKS,html}
%if %{with python2}
%fdupes %{buildroot}%{python_sitelib}/kdj
%else
rm -rf %{buildroot}%{_mandir}/man1/KateDJ.1*
%endif

%check
make %{?_smp_mflags} check

%post -n %{name}1 -p /sbin/ldconfig
%postun -n %{name}1 -p /sbin/ldconfig

%files -n %{name}1
%doc AUTHORS ChangeLog README THANKS
%license COPYING
%{_libdir}/%{name}.so.1*

%post -n liboggkate1 -p /sbin/ldconfig
%postun -n liboggkate1 -p /sbin/ldconfig

%files -n liboggkate1
%license COPYING
%doc AUTHORS ChangeLog README THANKS
%{_libdir}/liboggkate.so.1*

%files devel
%doc doc/html/
%{_includedir}/kate/
%{_libdir}/%{name}.so
%{_libdir}/liboggkate.so
%{_libdir}/pkgconfig/kate.pc
%{_libdir}/pkgconfig/oggkate.pc

%files tools
%{_bindir}/katedec
%{_bindir}/kateenc
%{_bindir}/katalyzer
%{_mandir}/man1/katalyzer.1%{?ext_man}
%{_mandir}/man1/katedec.1%{?ext_man}
%{_mandir}/man1/kateenc.1%{?ext_man}

%if %{with python2}
%files -n python-katedj
%{_bindir}/KateDJ
%{_mandir}/man1/KateDJ.1%{?ext_man}
%{python2_sitelib}/kdj/
%endif

%changelog
