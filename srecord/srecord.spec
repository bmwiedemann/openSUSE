#
# spec file for package srecord
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


Name:           srecord
Version:        1.64
Release:        0
%define so_ver  0
Summary:        Hex/bin format conversion package
License:        GPL-3.0+
Group:          Development/Tools/Other
Url:            http://srecord.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  diffutils
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  groff
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  sharutils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The srecord package is a collection of powerful tools for manipulating EPROM
load files. It reads and writes numerous EPROM file formats, and can perform
many different manipulations.

%package     -n lib%{name}%{so_ver}
Summary:        Srecord libraries
Group:          System/Libraries

%description -n lib%{name}%{so_ver}
This package contains the shared libraries for programs that manipulate EPROM
load files.

%package        devel
Summary:        Srecord development files
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{so_ver} = %{version}

%description    devel
This package contains libraries and header files for compiling programs
that manipulate EPROM load files.

%package        doc
Summary:        Srecord PDF documentation
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
The srecord package is a collection of powerful tools for manipulating EPROM
load files. It reads and writes numerous EPROM file formats, and can perform
many different manipulations.

This package contains documentation in PDF format.

%prep
%setup -q

%build
%configure
make -j1

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_libdir}/libsrecord.a
mkdir %{buildroot}/%{_docdir}
mv %{buildroot}/%{_datadir}/doc/%{name} %{buildroot}/%{_docdir}/%{name}

%check
make sure

%post -n lib%{name}%{so_ver} -p /sbin/ldconfig

%postun -n lib%{name}%{so_ver} -p /sbin/ldconfig

%files
%defattr (-,root,root)
%doc AUTHORS LICENSE README
%{_bindir}/srec_cat
%{_bindir}/srec_cmp
%{_bindir}/srec_info
%{_mandir}/man1/srec_*.1.gz
%{_mandir}/man5/srec_*.5.gz
%exclude %{_docdir}/%{name}/*.pdf

%files -n lib%{name}%{so_ver}
%defattr (-,root,root,-)
%{_libdir}/libsrecord.so.%{so_ver}*

%files devel
%defattr (-,root,root)
%{_libdir}/libsrecord.so
%{_includedir}/srecord
%{_libdir}/pkgconfig/srecord.pc
%{_mandir}/man3/srecord.3.gz
%{_mandir}/man3/srecord_license.3.gz

%files doc
%defattr (-,root,root)
%{_docdir}/%{name}/*.pdf

%changelog
