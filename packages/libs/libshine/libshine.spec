#
# spec file for package libshine
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


%define oname   shine
%define libver  3
Name:           libshine
Version:        3.1.1
Release:        0
Summary:        MP3 encoding library
License:        LGPL-2.0-only
Group:          System/Libraries
URL:            https://github.com/toots/shine
Source0:        https://github.com/toots/shine/releases/download/%{version}/%{oname}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
Shine is an MP3 encoding library implemented in fixed-point
arithmetic. The library can be used to perform MP3 encoding on
architectures without a FPU, such as armel, etc., but likewise works
on systems with an FPU.

%package        devel
Summary:        Development files for %{name}, an MP3 encoding library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{libver} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n %{name}%{libver}
Summary:        MP3 encoding library
Group:          System/Libraries

%description -n %{name}%{libver}
Shine is an MP3 encoding library implemented in fixed-point
arithmetic. The library can be used to perform MP3 encoding on
architectures without a FPU, such as armel, etc., but likewise works
on systems with an FPU.

%package -n %{oname}
Summary:        MP3 encoding tool
Group:          Productivity/Multimedia/Sound/Utilities
Conflicts:      libshine3 <= 3.1.0

%description -n %{oname}
Shine is an MP3 encoding library implemented in fixed-point
arithmetic. This package contains the shineenc command line encoder.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{libver} -p /sbin/ldconfig
%postun -n %{name}%{libver} -p /sbin/ldconfig

%files -n %{oname}
%license COPYING
%{_bindir}/shineenc

%files -n %{name}%{libver}
%license COPYING
%{_libdir}/%{name}.so.%{libver}*

%files devel
%license COPYING
%doc ChangeLog README.md README.old
%dir %{_includedir}/%{oname}
%{_includedir}/%{oname}/layer3.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{oname}.pc

%changelog
