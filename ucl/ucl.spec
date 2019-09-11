#
# spec file for package ucl
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


%define         sover 1
%define libname lib%{name}%{sover}
Name:           ucl
Version:        1.03
Release:        0
Summary:        The UCL Compression Library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://www.oberhumer.com/opensource/ucl/
Source0:        http://www.oberhumer.com/opensource/ucl/download/ucl-%{version}.tar.gz
Source1:        %{name}.changes
BuildRequires:  gcc-c++

%description
This package contains a lossless data compression library written in
ANSI C. UCL implements the NRV compression algorithms. Compared to
LZO, decompression time is traded for compression ratio.

%package -n %{libname}
Summary:        The UCL compression library
Group:          System/Libraries

%description -n %{libname}
This package contains a lossless data compression library written in
ANSI C. UCL implements the NRV compression algorithms. Compared to
LZO, decompression time is traded for compression ratio.

%package devel
Summary:        Development files for the UCL library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       %{libname}-devel = %{version}
Obsoletes:      %{libname}-devel < %{version}

%description devel
Headers and other development files for UCL library.

%prep
%setup -q
# remove _DATE_ and _TIME_ macros
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE1}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.[ch]' |\
    xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

%build
export CFLAGS="%{optflags} -std=c90"
export CXXFLAGS="%{optflags} -std=c90"
export LDFLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now"
%configure \
  --disable-static \
  --enable-shared
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc COPYING NEWS README THANKS TODO
%{_libdir}/libucl.so.%{sover}*

%files devel
%doc COPYING
%{_includedir}/ucl
%{_libdir}/libucl.so

%changelog
