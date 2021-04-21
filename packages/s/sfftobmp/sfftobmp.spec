#
# spec file for package sfftobmp
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


%define rname sfftobmp3
Name:           sfftobmp
Version:        3.1.4
Release:        0
Summary:        Tool to convert Structured Fax Files (.sff) to other image formats
License:        MIT
Group:          Hardware/ISDN
URL:            https://sf.net/projects/sfftools/
Source:         %{rname}-%{version}.tar.xz
Patch0:         boost_library.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  unix2dos

%description
The CAPI interface for programming ISDN hardware expects and gives
faxes in the "Structured Fax File" (SFF) format.

SffToBmp is a converter tool, written in C++, to transform SFF files to
BMP, JPEG or multipage TIFF format. In addition generation of PBM files
(Portable Bitmap) is also possible which can be transformed into nearby
all other graphics formats using the PBMPLUS tools that are included in
almost every Linux distribution nowadays.

%prep
%autosetup -p1 -n %{rname}-%{version}

chmod a+x configure
dos2unix -c mac src/output.h

%build
# This needs updating time and again
export CPPFLAGS="-DBOOST_FILESYSTEM_VERSION=3"

touch INSTALL NEWS README AUTHORS ChangeLog COPYING
autoreconf --force --install
%configure

#
# There will be a warning,
# 	main.cpp:303:16: warning: deleting object of abstract class
#	type 'COutputFilter' which has non-virtual destructor will
#	cause undefined behaviour [-Wdelete-non-virtual-dtor]
# which is - so far - however harmless, because there are no destructors
# *at all* in the derived classes.
#
%make_build

%install
%make_install
install -d %{buildroot}/%{_defaultdocdir}/sfftobmp/getopt
install -m 644 doc/getopt/* %{buildroot}/%{_defaultdocdir}/sfftobmp/getopt
rm -rf doc/getopt
install -m 644 doc/* %{buildroot}/%{_defaultdocdir}/sfftobmp

%files
%{_bindir}/sfftobmp
%doc %{_defaultdocdir}/sfftobmp

%changelog
