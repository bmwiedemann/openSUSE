#
# spec file for package adms
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


%define sover   0
Name:           adms
Version:        2.3.6
Release:        0
Summary:        An automatic device model synthesizer
License:        GPL-3.0-only
Group:          Productivity/Scientific/Electronics
URL:            http://sourceforge.net/projects/mot-adms/
Source0:        https://github.com/Qucs/ADMS/archive/release-%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE adms-no-build-time.patch -- remove build time from binary
Patch1:         adms-no-build-time.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl-XML-LibXML

%description
ADMS is a code generator that converts electrical compact device models
specified in high-level description language into ready-to-compile C code
for the API of SPICE simulators. Based on transformations specified in XML
language, ADMS transforms Verilog-AMS code into other target languages.

%package -n libadms%{sover}
Summary:        An automatic device model synthesizer
Group:          System/Libraries

%description -n libadms%{sover}
ADMS is a code generator that converts electrical compact device models
specified in high-level description language into ready-to-compile C code
for the API of SPICE simulators. Based on transformations specified in XML
language, ADMS transforms Verilog-AMS code into other target languages.

This package contains the libadms shared libraries.

%package devel
Summary:        C-Bindings development files for adms
Group:          Development/Languages/C and C++
Requires:       libadms%{sover} = %{version}

%description devel
This package contains all include files, libraries and configuration
files needed to develop programs that use adms.

%prep
%setup -q -n ADMS-release-%{version}
%patch1 -p1

%build
./bootstrap.sh
%configure --enable-maintainer-mode --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libadms0 -p /sbin/ldconfig
%postun -n libadms0 -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/admsCheck
%{_bindir}/admsXml
%{_mandir}/man1/admsCheck.1%{?ext_man}
%{_mandir}/man1/admsXml.1%{?ext_man}

%files -n libadms%{sover}
%{_libdir}/libadmsAdmstpath.so.%{sover}*
%{_libdir}/libadmsElement.so.%{sover}*
%{_libdir}/libadmsPreprocessor.so.%{sover}*
%{_libdir}/libadmsVeriloga.so.%{sover}*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/constants.vams
%{_includedir}/%{name}/disciplines.vams
%{_libdir}/libadmsAdmstpath.so
%{_libdir}/libadmsElement.so
%{_libdir}/libadmsPreprocessor.so
%{_libdir}/libadmsVeriloga.so

%changelog
