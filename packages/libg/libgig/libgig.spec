# vim: set sw=4 ts=4 et:
#
# spec file for package libgig
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define sover_gig  9
%define sover_akai 0
Name:           libgig
Version:        4.2.0
Release:        0
Summary:        Library for loading Gigasampler and DLS Level 1/2 files
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://linuxsampler.org/
ExclusiveArch:  %ix86 x86_64
Source0:        http://download.linuxsampler.org/packages/libgig-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sndfile) >= 1.0.2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
C++ library for loading Gigasampler and DLS Level 1/2 files.

%package -n libgig%{sover_gig}
Summary:        Library for loading Gigasampler and DLS Level 1/2 files
Group:          System/Libraries

%description -n libgig%{sover_gig}
C++ library for loading Gigasampler and DLS Level 1/2 files.

%package -n libakai%{sover_akai}
Summary:        Library for accessing AKAI disk images
Group:          System/Libraries

%description -n libakai%{sover_akai}
C++ library for accessing AKAI disk images

%package -n libgig-devel
Summary:        Library for loading Gigasampler and DLS Level 1/2 files
Group:          Development/Languages/C and C++
Requires:       libgig%{sover_gig} = %{version}

%description -n libgig-devel
C++ library for loading Gigasampler and DLS Level 1/2 files.

%package -n libgig-tools
Summary:        Example applications for libgig
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       libgig%{sover_gig} = %{version}-%{release}
Provides:       libgig6-tools = %{version}-%{release}
Obsoletes:      libgig6-tools < %{version}

%description -n libgig-tools
Some example applications for the libgig package.

* gigdump: demo app that prints out the content of a .gig file
* gigextract: extracts samples from a .gig file
* dlsdump: demo app that prints out the content of a DLS file
* rifftree: tool that prints out the RIFF tree of an arbitrary RIFF file

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo "%{_libdir}/libgig"  > "%{buildroot}%{_sysconfdir}/ld.so.conf.d/libgig%{sover_gig}.conf"
echo "%{_libdir}/libakai" > "%{buildroot}%{_sysconfdir}/ld.so.conf.d/libakai%{sover_akai}.conf"

%post   -n libgig%{sover_gig} -p /sbin/ldconfig
%postun -n libgig%{sover_gig} -p /sbin/ldconfig

%files -n libgig%{sover_gig}
%defattr(-,root,root)
%license  COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_libdir}/libgig/
%{_libdir}/libgig/libgig.so.%{sover_gig}
%{_libdir}/libgig/libgig.so.%{sover_gig}.*
%config %{_sysconfdir}/ld.so.conf.d/libgig%{sover_gig}.conf

%post   -n libakai%{sover_akai} -p /sbin/ldconfig
%postun -n libakai%{sover_akai} -p /sbin/ldconfig

%files -n libakai%{sover_akai}
%defattr(-,root,root)
%license  COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/libgig/libakai.so.%{sover_akai}
%{_libdir}/libgig/libakai.so.%{sover_akai}.*
%config %{_sysconfdir}/ld.so.conf.d/libakai%{sover_akai}.conf

%files -n libgig-devel
%defattr(-,root,root)
%dir %{_libdir}/libgig/
%dir %{_includedir}/libgig/
%{_libdir}/libgig/libgig.so
%{_includedir}/libgig/Akai.h
%{_includedir}/libgig/DLS.h
%{_includedir}/libgig/Korg.h
%{_includedir}/libgig/RIFF.h
%{_includedir}/libgig/SF.h
%{_includedir}/libgig/Serialization.h
%{_includedir}/libgig/gig.h
%{_libdir}/libgig/libakai.so
%{_libdir}/pkgconfig/akai.pc
%{_libdir}/pkgconfig/gig.pc

%files -n libgig-tools
%defattr(-,root,root)
%license  COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/akaidump
%{_bindir}/akaiextract
%{_bindir}/dlsdump
%{_bindir}/gig2mono
%{_bindir}/gig2stereo
%{_bindir}/gigdump
%{_bindir}/gigextract
%{_bindir}/gigmerge
%{_bindir}/korg2gig
%{_bindir}/korgdump
%{_bindir}/rifftree
%{_bindir}/sf2dump
%{_bindir}/sf2extract
%{_mandir}/man1/*.1*

%changelog
