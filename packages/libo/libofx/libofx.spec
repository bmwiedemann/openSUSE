#
# spec file for package libofx
#
# Copyright (c) 2025 SUSE LLC
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


Name:           libofx
Version:        0.10.9
Release:        0
Summary:        OFX Command Parser and API
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            https://github.com/libofx/libofx
Source:         https://github.com/libofx/libofx/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Remove-handling-for-obsolete-partner-server.patch
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  help2man
BuildRequires:  opensp-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
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
Requires:       libofx7 = %{version}
Requires:       opensp-devel

%description devel
LibOFX is a parser and API for applications to support
OFX command responses, usually provided by financial institutions for
statement downloads.

This subpackage contains the header files for the C API.

%prep
%autosetup -p1

chmod -x doc/ofx_sample_files/ofx_spec160_stmtrs_example.sgml
dos2unix doc/ofx_sample_files/*.ofx

%build
# CMake build system doesn't currently handle docs, create them manually
cd doc
# E: file-contains-date-and-time /usr/share/doc/packages/libofx/html/doxygen.css
sed -i '/HTML_TIMESTAMP/d' doxygen.cfg

doxygen -u doxygen.cfg
doxygen doxygen.cfg
cd ..

# lto causes build issues on leap and armv7l
%define _lto_cflags %{nil}

%cmake

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp -a doc/ofx_sample_files/*.* %{buildroot}%{_defaultdocdir}/%{name}/
cp -a doc/html %{buildroot}%{_defaultdocdir}/%{name}/

# man pages
mkdir -p %{buildroot}%{_mandir}/man1
for prog in ofxconnect ofxdump; do
help2man -N --output=${prog}.1 %__builddir/${prog}/${prog}
install -m 0644 ${prog}.1 %{buildroot}%{_mandir}/man1
done

%fdupes %{buildroot}

%ldconfig_scriptlets -n libofx7

%files
%doc AUTHORS ChangeLog NEWS README
%doc %dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/*.ofx
%{_bindir}/ofx2qif
%{_bindir}/ofxconnect
%{_bindir}/ofxdump
%{_datadir}/libofx/
%{_mandir}/man1/*.1%{?ext_man}

%files -n libofx7
%license COPYING
%{_libdir}/libofx.so.7*

%files devel
%doc %{_defaultdocdir}/%{name}/html/
%doc %{_defaultdocdir}/%{name}/*.sgml
%doc %{_defaultdocdir}/%{name}/*.xml
%{_libdir}/libofx.so
%{_includedir}/libofx/
%{_libdir}/cmake/libofx/
%{_libdir}/pkgconfig/libofx.pc

%changelog
