#
# spec file for package libgig
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover_gig  11
%define sover_akai 0
Name:           libgig
Version:        4.4.1
Release:        0
Summary:        Library for loading Gigasampler and DLS Level 1/2 files
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://linuxsampler.org/
Source0:        http://download.linuxsampler.org/packages/libgig-%{version}.tar.bz2
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sndfile) >= 1.0.2
BuildRequires:  pkgconfig(uuid)

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
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo "%{_libdir}/libgig"  > "%{buildroot}%{_sysconfdir}/ld.so.conf.d/libgig%{sover_gig}.conf"
echo "%{_libdir}/libakai" > "%{buildroot}%{_sysconfdir}/ld.so.conf.d/libakai%{sover_akai}.conf"

%check
%make_build check

%ldconfig_scriptlets -n libgig%{sover_gig}
%ldconfig_scriptlets -n libakai%{sover_akai}

%files -n libgig%{sover_gig}
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_libdir}/libgig/
%{_libdir}/libgig/libgig.so.%{sover_gig}
%{_libdir}/libgig/libgig.so.%{sover_gig}.*
%config %{_sysconfdir}/ld.so.conf.d/libgig%{sover_gig}.conf

%files -n libakai%{sover_akai}
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/libgig/libakai.so.%{sover_akai}
%{_libdir}/libgig/libakai.so.%{sover_akai}.*
%config %{_sysconfdir}/ld.so.conf.d/libakai%{sover_akai}.conf

%files -n libgig-devel
%license COPYING
%dir %{_libdir}/libgig/
%{_libdir}/libgig/*.so
%{_includedir}/libgig/
%{_libdir}/pkgconfig/*.pc

%files -n libgig-tools
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
