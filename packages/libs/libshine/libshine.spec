#
# spec file for package libshine
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define oname   shine
%define libver  3
Name:           libshine
Version:        3.1.0
Release:        0
Summary:        MP3 encoding library
License:        LGPL-2.0
Group:          Productivity/Multimedia/Sound/Editors and Converters
Url:            https://github.com/toots/shine
Source0:        https://github.com/toots/shine/archive/3.1.0.tar.gz#/%{oname}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkg-config

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

%prep
%setup -q -n %{oname}-%{version}

%build
./bootstrap
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
dos2unix COPYING

%post -n %{name}%{libver} -p /sbin/ldconfig

%postun -n %{name}%{libver} -p /sbin/ldconfig

%files -n %{name}%{libver}
%defattr(-,root,root)
%{_bindir}/shineenc
%{_libdir}/%{name}.so.%{libver}*

%files devel
%defattr(-,root,root)
%doc ChangeLog COPYING README.md README.old
%dir %{_includedir}/%{oname}
%{_includedir}/%{oname}/layer3.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{oname}.pc

%changelog
