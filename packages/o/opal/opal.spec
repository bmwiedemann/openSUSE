#
# spec file for package opal
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%bcond_with ffmpeg
%bcond_with x264
%bcond_with capi4linux

Name:           opal
%if %{with capi4linux}
BuildRequires:  capi4linux-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  ilbc
BuildRequires:  libcelt-devel
BuildRequires:  libgsm-devel
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
%endif
BuildRequires:  libopenssl-devel
BuildRequires:  libpt-devel >= 2.10.1
BuildRequires:  libsamplerate-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtheora-devel
%if %{with x264}
BuildRequires:  libx264-devel
%endif
BuildRequires:  pkg-config
BuildRequires:  speex-devel
BuildRequires:  swig
# FIXME: ZRTP is implemented through libzrtp. Its webpage says it's AGPL, but I
# was unable to find a copy with that license. srtp is in Contrib, it should be
# moved back to support it here.
BuildRequires:  spandsp-devel
Summary:        Open Phone Abstraction Library
License:        MPL-1.0
Group:          System/Libraries
Url:            http://www.opalvoip.org/
Version:        3.10.10
Release:        0
# FIXME: we should probably list all plugins in %%files to make sure we don't lose some when updating the package.
%define _version 3_10_10
Source0:        http://download.gnome.org/sources/opal/3.10/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM opal-system-libgsm.patch vuntz@novell.com -- Fix detection of system libgsm
Patch1:         opal-system-libgsm.patch
# PATCH-FIX-UPSTREAM opal-fix-ambiguous.patch vuntz@novell.com -- Fix ambiguous code
Patch2:         opal-fix-ambiguous.patch
# PATCH-FIX-UPSTREAM opal-use-pkgconfig-for-PTLib.patch zaitor@opensuse.org  -- Use pkgconfig for PTLib, taken from upstream svn, fixes build.
Patch4:         opal-use-pkgconfig-for-PTLib.patch 
# PATCH-FIX-UPSTREAM bmwiedemann https://sourceforge.net/p/opalvoip/patches/333/
Patch5:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Requires:       libpt-devel
# opal-devel was last used in openSUSE 11.3
Provides:       opal-devel = %{version}
Obsoletes:      opal-devel < %{version}

%description -n lib%{name}-devel
Static libraries and header files for development with opal.



%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
# this subdir contains GPL - to avoid license issues delete it before build
rm -rf plugins/LID/VPB

%build
%if %{with ffmpeg} || %{with x264}
cd plugins
autoreconf -fi
cd ..
%endif
# Can support Voicetronix vpb
export CXXFLAGS="%optflags -fvisibility-inlines-hidden -std=gnu++98"
%configure --disable-static \
	--enable-sbc \
%if %{with capi4linux}
	--enable-capi \
%endif
	--disable-ixj

make %{?_smp_mflags} VERBOSE=1

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/lib%{name}_s.a

%post -n lib%{name}%{_version} -p /sbin/ldconfig

%postun -n lib%{name}%{_version} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n lib%{name}%{_version}
%defattr(-,root,root)
%doc  mpl-1.0.htm
%dir %{_libdir}/%{name}-%{version}/ 
%dir %{_libdir}/%{name}-%{version}/codecs
%dir %{_libdir}/%{name}-%{version}/codecs/audio
%dir %{_libdir}/%{name}-%{version}/codecs/video
%dir %{_libdir}/%{name}-%{version}/fax
%{_libdir}/libopal.so.%{version}
%{_libdir}/%{name}-%{version}/codecs/audio/celt_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/audio/g7221_ptplugin.so
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
%{_libdir}/%{name}-%{version}/codecs/video/h261_vic_ptplugin.so
%{_libdir}/%{name}-%{version}/codecs/video/theora_ptplugin.so
%{_libdir}/%{name}-%{version}/fax/spandsp_ptplugin.so

%files -n lib%{name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}/
%{_libdir}/libopal.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
