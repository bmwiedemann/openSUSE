#
# spec file for package rlog
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2010 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define soname 5
Name:           rlog
Version:        1.4
Release:        0
Summary:        C++ Logging Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            http://www.arg0.net/rlog
# http://rlog.googlecode.com/files/rlog-%%{version}.tar.gz
Source:         rlog-%{version}.tar.bz2
Source99:       rlog-rpmlintrc
Patch0:         include_fix.patch
Patch1:         0002-Fix-FTBFS-with-autoconf-2.70.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
RLOG is a C++ library to manage message logging.

%package -n librlog%{soname}
Summary:        C++ Logging Library
Group:          System/Libraries
Provides:       rlog = %{version}
Obsoletes:      rlog < %{version}

%description -n librlog%{soname}
RLOG is a C++ library to manage message logging.

%package -n librlog%{soname}-doc
Summary:        C++ Logging Library - Documentation
Group:          System/Libraries

%description -n librlog%{soname}-doc
RLOG is a C++ library to manage message logging.
This subpackage contains the developer/API documentation.

%package -n librlog-devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       librlog%{soname} = %{version}
Requires:       libstdc++-devel
Provides:       rlog-devel = %{version}
Obsoletes:      rlog-devel < %{version}

%description -n librlog-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q
%patch0
%patch1 -p1

%build
autoreconf -fiv
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure --disable-static --with-pic
%make_build

%install
%make_install
rm -rf "%{buildroot}%{_datadir}/doc"
find %{buildroot} -type f -name "*.la" -delete -print

install -d "%{buildroot}%{_docdir}/librlog%{soname}"

FILES_MAIN="$PWD/files.main.lst"
echo "%doc %dir %{_docdir}/librlog%{soname}" >"$FILES_MAIN"
for f in AUTHORS COPYING* ChangeLog README*; do
    ff=$(basename "$f")
    cp -a "$f" "%{buildroot}%{_docdir}/librlog%{soname}/"
    echo "%doc %{_docdir}/librlog%{soname}/$ff" >>"$FILES_MAIN"
done

FILES_DOC="$PWD/files.doc.lst"
for f in docs/html docs/latex/*.pdf; do
    ff=$(basename "$f")
    cp -a "$f" "%{buildroot}%{_docdir}/librlog%{soname}/"
    echo "%doc %{_docdir}/librlog%{soname}/$ff" >>"$FILES_DOC"
done

%post   -n librlog%{soname} -p /sbin/ldconfig
%postun -n librlog%{soname} -p /sbin/ldconfig

%files -n librlog%{soname} -f files.main.lst
%{_libdir}/librlog.so.%{soname}
%{_libdir}/librlog.so.%{soname}.*

%files -n librlog%{soname}-doc -f files.doc.lst

%files -n librlog-devel
%{_libdir}/librlog.so
%{_includedir}/rlog
%{_libdir}/pkgconfig/librlog.pc

%changelog
