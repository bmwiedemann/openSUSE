#
# spec file for package libass
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


%define sover   9
Name:           libass
Version:        0.17.0
Release:        0
Summary:        Library for SSA/ASS-formatted subtitle rendering
License:        ISC
Group:          Development/Libraries/C and C++
URL:            https://github.com/libass/libass
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig) >= 2.10.92
BuildRequires:  pkgconfig(freetype2) >= 9.10.3
BuildRequires:  pkgconfig(fribidi) >= 0.19.0
BuildRequires:  pkgconfig(harfbuzz) >= 1.2.3

%description
libass is a subtitle renderer for the ASS/SSA
(Advanced Substation Alpha/Substation Alpha) subtitle
format. It is mostly compatible with VSFilter.

%package -n libass%{sover}
Summary:        Library for SSA/ASS-formatted subtitle rendering
Group:          System/Libraries

%description -n libass%{sover}
libass is a subtitle renderer for the ASS/SSA
(Advanced Substation Alpha/Substation Alpha) subtitle
format. It is mostly compatible with VSFilter.

%package devel
Summary:        Development files for libass, a subtitle rendering library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libass%{sover} = %{version}
Requires:       pkgconfig(fontconfig) >= 2.10.92
Requires:       pkgconfig(freetype2) >= 9.10.3
Requires:       pkgconfig(fribidi) >= 0.19.0
Requires:       pkgconfig(harfbuzz) >= 1.2.3

%description devel
This package is needed if you want to develop / compile against libass.

%prep
%autosetup

%build
%configure \
  --disable-silent-rules \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n libass%{sover} -p /sbin/ldconfig
%postun -n libass%{sover} -p /sbin/ldconfig

%files -n libass%{sover}
%{_libdir}/libass.so.%{sover}*

%files devel
%{_includedir}/ass
%{_libdir}/libass.so
%{_libdir}/pkgconfig/libass.pc

%changelog
