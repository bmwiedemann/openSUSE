#
# spec file for package libofx
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


Name:           libofx
Version:        0.9.12
Release:        0
Summary:        OFX Command Parser and API
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            http://libofx.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/libofx/libofx/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM libofx-CVE-2017-14731.patch dimstar@opensuse.org -- Fix a buffer overflow
Patch0:         libofx-CVE-2017-14731.patch
BuildRequires:  curl-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  opensp-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml++-2.6) >= 2.6

%description
LibOFX is a parser and API for applications to support
OFX command responses, usually provided by financial institutions for
statement downloads.

%package -n libofx7
Summary:        OFX Command Parser and API
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libofx7
LibOFX is a parser and API for applications to support
OFX command responses, usually provided by financial institutions for
statement downloads.

%package devel
Summary:        Development files for libofx, an OFX Command Parser and API
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
LibOFX is a parser and API for applications to support
OFX command responses, usually provided by financial institutions for
statement downloads.

This subpackage contains the header files for the C API.

%prep
%setup -q
%patch0 -p1
chmod -x doc/ofx_sample_files/ofx_spec160_stmtrs_example.sgml

%build
%configure --disable-static --with-opensp-libs=%{_libdir}
make %{?_smp_mflags} docdir=%{_defaultdocdir}/%{name}

%install
%make_install
mkdir -p %{buildroot}%{_defaultdocdir}
mv %{buildroot}%{_datadir}/doc/libofx %{buildroot}%{_defaultdocdir}/%{name}
rm %{buildroot}%{_defaultdocdir}/%{name}/INSTALL
cp -a doc/ofx_sample_files/*.* %{buildroot}%{_defaultdocdir}/%{name}/
cp -a doc/html %{buildroot}%{_defaultdocdir}/%{name}/
%fdupes %{buildroot}%{_prefix}
rm -f %{buildroot}%{_libdir}/*.la

%post -n libofx7 -p /sbin/ldconfig

%postun -n libofx7 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc %dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/[ACNR]*
%doc %{_defaultdocdir}/%{name}/*.txt
%{_bindir}/*
%{_datadir}/libofx/
%{_mandir}/man1/*.1%{?ext_man}

%files -n libofx7
%defattr (-, root, root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}/html/
%doc %{_defaultdocdir}/%{name}/*.sgml
%doc %{_defaultdocdir}/%{name}/*.xml
%{_libdir}/*.so
%{_includedir}/libofx/
%{_libdir}/pkgconfig/libofx.pc

%changelog
