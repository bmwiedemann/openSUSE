#
# spec file for package wavpack
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


%define soname  1
Name:           wavpack
Version:        5.6.0
Release:        0
Summary:        Hybrid Lossless Audio Compression Format
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://www.wavpack.com/
Source0:        https://www.wavpack.com/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  pkgconfig

%description
WavPack is an open audio compression format providing lossless, high-quality
lossy, and unique hybrid compression modes.

Lossless mode is ideal for archiving audio material or any other situation
where quality is paramount. The compression ratio depends on the source
material, but generally is between 30%% and 70%%.

The hybrid mode creates both, a relatively small, high-quality lossy file that
can be used all by itself, and a "correction" file that (when combined with the
lossy file) provides full lossless restoration. For some users, this means
never having to choose between lossless and lossy compression.

%package -n libwavpack%{soname}
Summary:        Hybrid Lossless Audio Compression Format
Group:          System/Libraries

%description -n libwavpack%{soname}
WavPack is an open audio compression format providing lossless, high-quality
lossy, and unique hybrid compression modes.
Lossless mode is ideal for archiving audio material or any other situation
where quality is paramount. The compression ratio depends on the source
material, but generally is between 30%% and 70%%.

%package devel
Summary:        Development files for wavpack, an audio compression format
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
WavPack is an open audio compression format providing lossless, high-quality
lossy, and unique hybrid compression modes.

This subpackage contains libraries and header files for developing
applications that want to make use of wavpack.

%package doc
Summary:        Documentation files for wavpack, an audio compression format
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description doc
WavPack is an open audio compression format providing lossless, high-quality
lossy, and unique hybrid compression modes.

This subpackage contains development documentation for applications that
want to make use of wavpack.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

install -d -m 755 %{buildroot}%{_defaultdocdir}
mv %{buildroot}/usr/share/doc/%name %{buildroot}%{_defaultdocdir}

%check
%make_build check

%post   -n libwavpack%{soname} -p /sbin/ldconfig
%postun -n libwavpack%{soname} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/wavpack
%{_bindir}/wvgain
%{_bindir}/wvunpack
%{_bindir}/wvtag
%{_mandir}/man?/*

%files -n libwavpack%{soname}
%{_libdir}/libwavpack.so.%{soname}
%{_libdir}/libwavpack.so.%{soname}.*

%files devel
%{_includedir}/wavpack
%{_libdir}/libwavpack.so
%{_libdir}/pkgconfig/wavpack.pc

%files doc
%doc %_defaultdocdir/%name

%changelog
