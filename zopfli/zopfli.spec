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
%define libversion 1.0.1
%define pnglibversion 1.0.0
%define libname lib%{name}1
%define libpngname lib%{name}png1
Name:           zopfli
Version:        1.0.1+git.20170707
Release:        0
Summary:        GZip compatible compression utlity
License:        Apache-2.0
Group:          Productivity/Archiving/Compression
URL:            https://github.com/google/zopfli
Source:         %{name}-%{version}.tar.xz
Source1:        Makefile
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make

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
%setup -q
cp %{SOURCE1} Makefile

%build
make CFLAGS="%{optflags}" %{?_smp_mflags} libzopfli libzopflipng zopfli zopflipng
# help2man since 1.47.1 respects SOURCE_DATE_EPOCH
export SOURCE_DATE_EPOCH=`echo %{version} | sed -e 's/.*git\.//' | date -f/dev/stdin +%%s`
help2man --help-option="-h" --version-string=%{version} --no-info --no-discard-stderr ./%{name} > %{name}.1
help2man --help-option="-h" --version-string=%{version} --no-info --no-discard-stderr ./%{pngname} > %{pngname}.1

%install
install -D -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -pm 0755 %{pngname} %{buildroot}%{_bindir}/%{pngname}
install -D -pm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -D -pm 0644 %{pngname}.1 %{buildroot}%{_mandir}/man1/%{pngname}.1
install -d -pm 0755 %{buildroot}%{_libdir}
install -pm 0755 libzopfli.so.%{libversion} %{buildroot}%{_libdir}/
install -pm 0755 libzopflipng.so.%{pnglibversion} %{buildroot}%{_libdir}/
install -d -pm 0755 %{buildroot}%{_includedir}/zopfli/
install -pm 0644 src/zopfli/*.h %{buildroot}%{_includedir}/zopfli/
install -pm 0644 src/zopflipng/*.h %{buildroot}%{_includedir}/zopfli/
ln -s libzopfli.so.%{libversion} %{buildroot}%{_libdir}/libzopfli.so
ln -s libzopfli.so.%{libversion} %{buildroot}%{_libdir}/libzopfli.so.1
ln -s libzopflipng.so.%{pnglibversion} %{buildroot}%{_libdir}/libzopflipng.so
ln -s libzopflipng.so.%{pnglibversion} %{buildroot}%{_libdir}/libzopflipng.so.1

%post -n %{libname} -p /sbin/ldconfig
%post -n %{libpngname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%postun -n %{libpngname} -p /sbin/ldconfig

%files
%doc README COPYING README.zopflipng
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
%{_includedir}/zopfli/

%changelog
