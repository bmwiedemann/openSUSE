#
# spec file for package libao
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


%define sover  4
# Check configure.ac for the plugin versioning
%define plugver 4
%define my_provides /tmp/my-provides
Name:           libao
Version:        1.2.2+git20180114.d522165
Release:        0
Summary:        An Audio Output Library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://www.xiph.org/ao/
# Switched to git release as there are no releases for >3 years
#Source:         http://downloads.xiph.org/releases/ao/%{name}-%{version}.tar.gz
Source:         %{name}-%{version}.tar.xz
Source99:       baselibs.conf
Patch1:         libao-ocloexec.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libpulse-simple)
Obsoletes:      plugin4-esd

%description
Libao is an audio output library, supporting a number of
outputs, such as ALSA, PulseAudio, and PCM files.

%package -n libao%{sover}
Summary:        An Audio Output Library
Group:          System/Libraries
Requires:       libao-plugins%{plugver}
# libao was last used in openSUSE 11.3
Provides:       libao = 1.1.0
Obsoletes:      libao < 1.1.0

%description -n libao%{sover}
Libao is an audio output library, supporting a number of
outputs, such as ALSA, PulseAudio, and PCM files.

%package plugins%{plugver}
Summary:        Main output plugins for libao
Group:          System/Libraries

%description plugins%{plugver}
This package contains the main output plugins for libao.

%package devel
Summary:        Development files for libao, an audio outputl ibrary
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libao%{sover} = %{version}

%description devel
This package contains the headers for developing applications that
want to make use of libao.

%prep
%setup -q
%patch1

# setup libdir properly
sed -i "s:/lib:/%{_lib}:g" ao.m4

%build
autoreconf -fiv
%configure \
	--enable-alsa \
	--enable-alsa-mmap \
	--enable-nas \
	--enable-pulse \
	--disable-static \
	--disable-arts \
	--disable-esd
make %{?_smp_mflags}

%install
%make_install docdir=%{_docdir}/%{name}-devel
find %{buildroot} -type f -name "*.la" -delete -print
# exclude plugins from the provide-list
cat << EOF > %{my_provides}
grep -v %{_libdir}/ao/ | %{__find_provides}
EOF
chmod 755 %{my_provides}
%define _use_internal_dependency_generator 0
%define __find_provides %{my_provides}

%post -n libao%{sover} -p /sbin/ldconfig
%postun -n libao%{sover} -p /sbin/ldconfig

%files -n libao%{sover}
%doc AUTHORS CHANGES README TODO
%license COPYING
%{_libdir}/libao.so.%{sover}*
%dir %{_libdir}/ao
%dir %{_libdir}/ao/plugins-%{plugver}

%files plugins%{plugver}
%{_libdir}/ao/plugins-%{plugver}/libalsa.so
%{_libdir}/ao/plugins-%{plugver}/liboss.so
%{_libdir}/ao/plugins-%{plugver}/libpulse.so

%files devel
%{_docdir}/%{name}-devel
%{_mandir}/*/*
%{_includedir}/ao
%{_libdir}/libao.so
%{_libdir}/ckport
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc

%changelog
