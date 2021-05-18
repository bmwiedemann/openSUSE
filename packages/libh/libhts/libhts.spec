#
# spec file for package libhts
#
# Copyright (c) 2021 SUSE LLC
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


Name:           libhts
Version:        1.12
Release:        0
%define   sonum 3
Summary:        C library for high-throughput sequencing data formats
License:        MIT
Group:          Productivity/Scientific/Other
URL:            https://github.com/samtools/htslib/
Source0:        https://github.com/samtools/htslib/releases/download/%{version}/htslib-%{version}.tar.bz2
Source100:      baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)

%description
HTSlib is an implementation of a unified C library for accessing common file formats, such as
SAM, CRAM and VCF, used for high-throughput sequencing data, and is the core library used by
samtools and bcftools.
HTSlib implements a generalized BAM index, with file extension .csi (coordinate-sorted index).
The HTSlib file reader first looks for the new index and then for the old if the new index is absent.
This project also includes the popular tabix indexer, which indexes both .tbi and .csi formats, and
the bgzip compression utility.

%package -n libhts%{sonum}
Summary:        C library for high-throughput sequencing data formats
Group:          System/Libraries

%description -n libhts%{sonum}
HTSlib is an implementation of a unified C library for accessing common file formats, such as
SAM, CRAM and VCF, used for high-throughput sequencing data, and is the core library used by
samtools and bcftools.
HTSlib implements a generalized BAM index, with file extension .csi (coordinate-sorted index).
The HTSlib file reader first looks for the new index and then for the old if the new index is absent.

%package -n bgzip
Summary:        Block compression/decompression utility from the HTSlib project
Group:          Productivity/Scientific/Other
Requires:       libhts%{sonum} = %{version}
Requires:       tabix = %{version}

%description -n bgzip
HTSlib is an implementation of a unified C library for accessing common file formats, such as
SAM, CRAM and VCF, used for high-throughput sequencing data, and is the core library used by
samtools and bcftools.
HTSlib implements a generalized BAM index, with file extension .csi (coordinate-sorted index).
The HTSlib file reader first looks for the new index and then for the old if the new index is absent.
This project also includes the popular tabix indexer, which indexes both .tbi and .csi formats, and
the bgzip compression utility.

%package -n tabix
Summary:        Generic indexer for TAB-delimited genome position files from the HTSlib project
Group:          Productivity/Scientific/Other
Requires:       bgzip = %{version}
Requires:       libhts%{sonum} = %{version}

%description -n tabix
HTSlib is an implementation of a unified C library for accessing common file formats, such as
SAM, CRAM and VCF, used for high-throughput sequencing data, and is the core library used by
samtools and bcftools.
HTSlib implements a generalized BAM index, with file extension .csi (coordinate-sorted index).
The HTSlib file reader first looks for the new index and then for the old if the new index is absent.
This project also includes the popular tabix indexer, which indexes both .tbi and .csi formats, and
the bgzip compression utility.

%package -n htsfile
Summary:        Identify high-throughput sequencing data files from the HTSlib project
Group:          Productivity/Scientific/Other
Requires:       libhts%{sonum} = %{version}

%description -n htsfile
HTSlib is an implementation of a unified C library for accessing common file formats, such as
SAM, CRAM and VCF, used for high-throughput sequencing data, and is the core library used by
samtools and bcftools.
HTSlib implements a generalized BAM index, with file extension .csi (coordinate-sorted index).
The HTSlib file reader first looks for the new index and then for the old if the new index is absent.
This project also includes the popular tabix indexer, which indexes both .tbi and .csi formats, and
the bgzip compression utility.

%package devel
Summary:        Header files and libraries for compiling against %{name}
Group:          Development/Libraries/C and C++
Requires:       libhts%{sonum} = %{version}
Provides:       libhts1-devel = %{version}
Obsoletes:      libhts1-devel < 1.5
Requires:       pkgconfig(bzip2)
Requires:       pkgconfig(libcurl)
Requires:       pkgconfig(liblzma)
Requires:       pkgconfig(zlib)

%description devel
Header files and libraries of the HTSlib project for compiling against %{name}.

%prep
%setup -q -n htslib-%{version}

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/libhts.a

%post   -n libhts%{sonum} -p /sbin/ldconfig
%postun -n libhts%{sonum} -p /sbin/ldconfig
%post   devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files -n libhts%{sonum}
%{_libdir}/libhts.so.*

%files -n bgzip
%{_bindir}/bgzip
%{_mandir}/man1/bgzip*

%files -n tabix
%{_bindir}/tabix
%{_mandir}/man1/tabix*

%files -n htsfile
%license LICENSE
%doc NEWS README
%{_bindir}/htsfile
%{_mandir}/man1/htsfile*
%{_mandir}/man5/*
%{_mandir}/man7/*

%files devel
%{_includedir}/htslib/.
%{_includedir}/htslib/*.h
%{_libdir}/libhts.so
%{_libdir}/pkgconfig/htslib.pc

%changelog
