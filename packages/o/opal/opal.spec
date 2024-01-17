#
# spec file for package opal
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_with ffmpeg
%bcond_with x264
%bcond_with capi4linux

Name:           opal
Version:        3.18.8
Release:        0
Summary:        Open Phone Abstraction Library
License:        MPL-1.0
Group:          Development/Libraries/C and C++
#Git-Clone:      https://git.code.sf.net/p/opalvoip/opal
URL:            https://sf.net/projects/opalvoip/
# FIXME: we should probably list all plugins in %%files to make sure we don't lose some when updating the package.
%define _version 3_18_8
Source0:        https://download.sf.net/opalvoip/%{name}-%{version}.tar.bz2
Patch1:         arches.patch
%if %{with capi4linux}
BuildRequires:  capi4linux-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  ilbc
BuildRequires:  libcelt-devel
BuildRequires:  libgsm-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(opus)
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
%endif
BuildRequires:  libopenssl-devel
BuildRequires:  libpt-devel >= 2.18.5
BuildRequires:  libsamplerate-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtheora-devel
%if %{with x264}
BuildRequires:  libx264-devel
%endif
BuildRequires:  pkg-config
BuildRequires:  speex-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(libsrtp2)
# FIXME: ZRTP is implemented through libzrtp. Its webpage says it's AGPL, but I
# was unable to find a copy with that license. srtp is in Contrib, it should be
# moved back to support it here.
BuildRequires:  spandsp-devel

%description
Open Phone Abstraction Library, implementation of the ITU H.323
teleconferencing protocol, and successor of the openh323 library. It
supports the H.323 protocol as well as SIP and IAX2.

%package -n lib%{name}%{_version}
Summary:        Open Phone Abstraction Library
Group:          System/Libraries

%description -n lib%{name}%{_version}
Open Phone Abstraction Library, implementation of the ITU H.323
teleconferencing protocol, and successor of the openh323 library. It
supports the H.323 protocol as well as SIP and IAX2.

%package -n lib%{name}-devel
Summary:        Development package for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{_version} = %{version}
Requires:       pkgconfig(libsrtp2)
Requires:       pkgconfig(ptlib)
Requires:       pkgconfig(speexdsp)
# opal-devel was last used in openSUSE 11.3
Provides:       opal-devel = %{version}
Obsoletes:      opal-devel < %{version}

%description -n lib%{name}-devel
Static libraries and header files for development with opal.

%prep
%autosetup -p1
# this subdir contains GPL - to avoid license issues delete it before build
rm -rf plugins/LID/VPB

%build
%if %{with ffmpeg} || %{with x264}
cd plugins
autoreconf -fi
cd ..
%endif
# Can support Voicetronix vpb
export CPPFLAGS="-I/usr/include/gsm"
export CXXFLAGS="%optflags -fvisibility-inlines-hidden"
%configure --disable-static \
	--enable-sbc \
%if %{with capi4linux}
	--enable-capi \
%endif
	--disable-ixj --enable-cpp17

%make_build OS="" CPU="" VERBOSE=1 DSYMUTIL=/bin/true

%install
%make_install OS="" CPU=""
rm -f %{buildroot}%{_libdir}/lib%{name}_s.a

%post -n lib%{name}%{_version} -p /sbin/ldconfig

%postun -n lib%{name}%{_version} -p /sbin/ldconfig

%files -n lib%{name}%{_version}
%doc  mpl-1.0.htm
%dir %{_libdir}/%{name}-%{version}/
%dir %{_libdir}/%{name}-%{version}/codecs
%dir %{_libdir}/%{name}-%{version}/codecs/audio
%dir %{_libdir}/%{name}-%{version}/codecs/video
%dir %{_libdir}/%{name}-%{version}/fax
%{_libdir}/libopal.so.%{version}
%{_libdir}/%{name}-%{version}/codecs/audio/g7222_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/g722_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/g726_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/gsm0610_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/gsmamrcodec_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/iLBC_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/ima_adpcm_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/lpc10_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/silk_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/speex_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/opus_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/iSAC_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/video/h261_vic_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/video/theora_ptplugin.so
%{_libdir}/%{name}-%{version}/fax/spandsp_ptplugin.so

%files -n lib%{name}-devel
%{_includedir}/%{name}/
%{_libdir}/libopal.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/opal/

%changelog
