#
# spec file for package psiconv
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           psiconv
Version:        0.9.9
Release:        0
Summary:        EPOC32 PSION 5(MX) File Format Data Conversion Utilities
License:        GPL-2.0-or-later
Group:          Hardware/Other
Url:            http://software.frodo.looijaard.name/psiconv/
Source:         http://www.frodo.looijaard.name/system/files/software/psiconv/%{name}-%{version}.tar.gz
BuildRequires:  ImageMagick-devel
BuildRequires:  bc
BuildRequires:  gcc-c++

%description
This package makes the Psion 5 series of PDAs, as well as other small
computers running EPOC 32, more usable to non-Windows users. The
package consists of several parts:

* Documentation about Psion 5 data formats

* A library that can be linked against applications that have to
  read and write Psion 5 files

* An example command line program that reads Psion files and writes
  more commonly used formats

%package -n libpsiconv6
Summary:        EPOC32 PSION 5(MX) file format data conversion library
Group:          System/Libraries

%description -n libpsiconv6
Library for the conversion of Psion files as produced by EPOC 32 Psion
5 series PDAs.

%package devel
Summary:        EPOC32 PSION 5(MX) File Format Data Conversion Utilities
Group:          Hardware/Psion
Requires:       glibc-devel
Requires:       libpsiconv6 = %{version}

%description devel
This package makes the Psion 5 series of PDAs, as well as other small
computers running EPOC 32, more usable to non-Windows users. The
package consists of several parts:

* Documentation about Psion 5 data formats

* A library which can be linked against application that have to
  read and write Psion 5 files

* An example command-line program which reads Psion files and writes
  more commonly used formats.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure --disable-static --enable-html4-docs
make %{?_smp_mflags} pkgdatadir=%{_docdir}/%{name}/formats

%install
make DESTDIR=%{buildroot} pkgdatadir=%{_docdir}/%{name}/formats install
cp AUTHORS ChangeLog INSTALL NEWS README TODO %{buildroot}/%{_docdir}/%{name}
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libpsiconv6 -p /sbin/ldconfig
%postun -n libpsiconv6 -p /sbin/ldconfig

%files
%doc %dir %{_docdir}/psiconv
%doc %{_docdir}/%{name}/AUTHORS
%license COPYING
%doc %{_docdir}/%{name}/ChangeLog
%doc %{_docdir}/%{name}/INSTALL
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/TODO
%dir %{_sysconfdir}/psiconv
%config %{_sysconfdir}/psiconv/psiconv.conf
%{_sysconfdir}/psiconv/psiconv.conf.eg
%{_bindir}/psiconv
%{_mandir}/man?/*%{ext_man}

%files -n libpsiconv6
%{_libdir}/*.so.*

%files devel
%doc %{_docdir}/%{name}/formats
%{_libdir}/*.so
%{_bindir}/*-config
%{_includedir}/*

%changelog
