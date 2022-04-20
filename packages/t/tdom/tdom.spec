#
# spec file for package tdom
#
# Copyright (c) 2022 SUSE LLC
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


Name:           tdom
%if 0%{!?tclscriptdir:1}
%define tclscriptdir %_libdir
%endif
Summary:        A XML/DOM/XPath/XSLT Implementation for Tcl
License:        MPL-2.0
Group:          Development/Libraries/Tcl
Version:        0.9.2
Release:        0
URL:            http://tdom.org
BuildRequires:  autoconf
BuildRequires:  libexpat-devel
BuildRequires:  tcl-devel
BuildRequires:  tcllib
Source0:        http://tdom.org/downloads/tdom-%{version}-src.tgz
Patch0:         install-libraries-libdir.patch

%description
tDOM combines high performance XML data processing with easy and
powerful Tcl scripting functionality. tDOM should be one of the fastest
ways to manipulate XML with a scripting language and uses very few
memory: for example, the DOM tree of the XML recommendation in XML
(160K) needs only about 450K of memory.

%package devel
Summary:        Development Files for tdom
Group:          Development/Libraries/Tcl
Requires:       tcl-devel
Requires:       tdom = %{version}

%description devel
This package contains files for developing software based on tdom.

%prep
%autosetup  -p1 -n %{name}-%{version}-src

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoreconf --force
mkdir build
cd build
CFLAGS="%optflags -DUSE_INTERP_ERRORLINE" ../configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--mandir=%_mandir \
	--with-tcl=%_libdir \
	--disable-tdomalloc \
	--with-expat
%make_build
cd ../extensions/tnc
autoreconf --force
CFLAGS="%optflags" ./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--mandir=%_mandir \
	--with-tcl=%_libdir \
	--with-tdom=../../build
%make_build

%check
cd build
make test
cd ../extensions/tnc
make test TCLLIBPATH=../../build EXTRA_PATH=../../build

%install
cd build
make DESTDIR=%buildroot pkglibdir=%tclscriptdir/%name%version install
chmod 644 %buildroot/%_libdir/*.a
cd ../extensions/tnc
make DESTDIR=%buildroot pkglibdir=%tclscriptdir/tnc0.3.0 install

%files
%license MPL_2.0.html LICENSE
%doc ChangeLog CHANGES README.md
%doc %_mandir/man*/*
%tclscriptdir/*
%_libdir/*.so

%files devel
%_libdir/tdomConfig.sh
%_libdir/*.a
%_includedir/tdom.h

%changelog
