#
# spec file for package tdom
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
License:        MPL-1.1
Group:          Development/Libraries/Tcl
Version:        0.8.3
Release:        0
Url:            http://tdom.github.com/
BuildRequires:  autoconf
BuildRequires:  libexpat-devel
BuildRequires:  tcl-devel
BuildRequires:  tcllib
Source0:        https://github.com/downloads/tDOM/tdom/tDOM-%{version}.tgz
Patch0:         tdom.patch
Patch1:         tdom-expat.patch
Patch2:         tdom-tnc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -q -n tDOM-%version
%patch0
%patch1
%patch2

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
make
cd ../extensions/tnc
autoreconf --force
CFLAGS="%optflags" ./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--mandir=%_mandir \
	--with-tcl=%_libdir \
	--with-tdom=../../build
make

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

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc ChangeLog CHANGES README NPL-1_1Final.html LICENSE
%doc %_mandir/man*/*
%tclscriptdir/*
%_libdir/*.so

%files devel
%defattr(-,root,root,-)
%_libdir/tdomConfig.sh
%_libdir/*.a
%_includedir/tdom.h

%changelog
