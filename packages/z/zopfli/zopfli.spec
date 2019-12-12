#
# spec file for package zopfli
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


%define pngname zopflipng
%define libversion 1.0.3
%define pnglibversion 1.0.3
%define libname lib%{name}1
%define libpngname lib%{name}png1
%define releasedateepoch 1574898960
Name:           zopfli
Version:        1.0.3
Release:        0
Summary:        GZip compatible compression utlity
License:        Apache-2.0
Group:          Productivity/Archiving/Compression
URL:            https://github.com/google/zopfli
Source:         https://github.com/google/zopfli/archive/zopfli-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  cmake >= 2.8.11

%description
Example program for libzopfli to create gzip compatible files. Files can be
decompressed with e.g. gzip.

%package -n %{libname}
Summary:        Deflate/zlib compatible compression library
Group:          System/Libraries

%description -n %{libname}
Zopfli Compression Algorithm is a compression library programmed in C to
perform very good, but slow, deflate or zlib compression.

%package -n %{libpngname}
Summary:        Deflate/zlib compatible compression library
Group:          System/Libraries

%description -n %{libpngname}
This package contain the libzopflipng PNG optimizer library.

%package -n libzopfli-devel
Summary:        Header files for libzopfli, a gzip-compatible compressor
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{libpngname} = %{version}

%description -n libzopfli-devel
The basic function to compress data is ZopfliCompress in zopfli.h. Use the
ZopfliOptions object to set parameters that affect the speed and compression.
Use the ZopfliInitOptions function to place the default values in the
ZopfliOptions first.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
%cmake
%cmake_build
# help2man since 1.47.1 respects SOURCE_DATE_EPOCH
export SOURCE_DATE_EPOCH=%{releasedateepoch}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$RPM_BUILD_DIR/%{name}-%{name}-%{version}/build
help2man --help-option="-h" --version-string=%{version} --no-info --no-discard-stderr ./%{name} > %{name}.1
help2man --help-option="-h" --version-string=%{version} --no-info --no-discard-stderr ./%{pngname} > %{pngname}.1

%install
%cmake_install
install -D -pm 0644 build/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -D -pm 0644 build/%{pngname}.1 %{buildroot}%{_mandir}/man1/%{pngname}.1

%post -n %{libname} -p /sbin/ldconfig
%post -n %{libpngname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%postun -n %{libpngname} -p /sbin/ldconfig

%files
%doc README README.zopflipng
%license COPYING
%{_bindir}/%{name}
%{_bindir}/zopflipng
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man1/zopflipng.1%{ext_man}

%files -n %{libname}
%{_libdir}/libzopfli.so.*

%files -n %{libpngname}
%{_libdir}/libzopflipng.so.*

%files -n libzopfli-devel
%{_libdir}/libzopfli*.so
%{_includedir}/zopfli.h
%{_includedir}/zopflipng_lib.h
%{_libdir}/cmake/Zopfli

%changelog
