#
# spec file for package libkate
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2010 SUSE Dominique Leuenberger, Amsterdam, Netherlands
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


%define sover 1
Name:           libkate
Version:        0.4.3
Release:        0
Summary:        A karaoke and text codec for embedding in Ogg
License:        BSD-3-Clause
URL:            https://gitlab.xiph.org/xiph/kate
Source:         https://downloads.xiph.org/releases/kate/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)

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

%package -n %{name}%{sover}
Summary:        A karaoke and text codec for embedding in Ogg

%description -n %{name}%{sover}
Kate is a codec for karaoke and text encapsulation for Ogg. Most of the
time, this would be multiplexed with audio/video to carry subtitles,
song lyrics (with or without karaoke data), etc, but doesn't have to be.
A possible use of a lone Kate stream would be an e-book. Moreover, the
motion feature gives Kate a powerful means to describe arbitrary curves,
so hand drawing of shapes can be achieved.

This was originally meant for karaoke use, but can be used for any
purpose. Motions can be attached to various semantics, like position,
color, etc, so scrolling or fading text can be defined.

%package -n liboggkate%{sover}
Summary:        A karaoke and text codec for embedding in Ogg
Conflicts:      libkate1 < 0.4.1

%description -n liboggkate%{sover}
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
Requires:       %{name}%{sover} = %{version}
Requires:       liboggkate%{sover} = %{version}

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
%autosetup -p1

%build
echo 'HTML_TIMESTAMP=NO' >> doc/kate.doxygen.in
%configure \
        --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Remove files that we install with %%doc
rm -rf %{buildroot}%{_datadir}/doc/%{name}/{AUTHORS,COPYING,ChangeLog,README,THANKS,html}
%if %{with python2}
%fdupes %{buildroot}%{python_sitelib}/kdj
%else
# the py3 when found build system tries to compile and install it, and fails miserably
rm -rf %{buildroot}%{_bindir}/KateDJ
rm -rf %{buildroot}%{python3_sitelib}
rm -rf %{buildroot}%{_mandir}/man1/KateDJ.1*
%endif

%check
%make_build check

%ldconfig_scriptlets -n %{name}%{sover}
%ldconfig_scriptlets -n liboggkate%{sover}

%files -n %{name}%{sover}
%doc AUTHORS ChangeLog README THANKS
%license COPYING
%{_libdir}/%{name}.so.%{sover}
%{_libdir}/%{name}.so.%{sover}.*

%files -n liboggkate%{sover}
%license COPYING
%doc AUTHORS ChangeLog README THANKS
%{_libdir}/liboggkate.so.%{sover}
%{_libdir}/liboggkate.so.%{sover}.*

%files devel
%license COPYING
%doc doc/html/
%{_includedir}/kate/
%{_libdir}/%{name}.so
%{_libdir}/liboggkate.so
%{_libdir}/pkgconfig/kate.pc
%{_libdir}/pkgconfig/oggkate.pc

%files tools
%license COPYING
%{_bindir}/katedec
%{_bindir}/kateenc
%{_bindir}/katalyzer
%{_mandir}/man1/katalyzer.1%{?ext_man}
%{_mandir}/man1/katedec.1%{?ext_man}
%{_mandir}/man1/kateenc.1%{?ext_man}

%changelog
