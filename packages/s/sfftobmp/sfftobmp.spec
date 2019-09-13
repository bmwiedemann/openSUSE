#
# spec file for package sfftobmp
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


Name:           sfftobmp
Summary:        Tool to convert Structured Fax Files (.sff) to other image formats
License:        MIT
Group:          Hardware/ISDN
Version:        3.1.4
Release:        0
Url:            http://sf.net/projects/sfftools/

#SVN-Clone:	svn://svn.code.sf.net/p/sfftools/code-0/sfftobmp3/tags/REL_3_1_4
# Source tarballs no longer provided; have to generate them from SVN
Source:         %name-%version.tar.xz
Source2:        sanitize_source.sh
Patch1:         boost_library.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  unix2dos
BuildRequires:  xz

%description
The CAPI interface for programming ISDN hardware expects and gives
faxes in the "Structured Fax File" (SFF) format.

SffToBmp is a converter tool, written in C++, to transform SFF files to
BMP, JPEG or multipage TIFF format. In addition generation of PBM files
(Portable Bitmap) is also possible which can be transformed into nearby
all other graphics formats using the PBMPLUS tools that are included in
almost every Linux distribution nowadays.

%prep
%setup -qn REL_3_1_4
%patch1 -p1
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
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT/%{_defaultdocdir}/sfftobmp/getopt
install -m 644 doc/getopt/* $RPM_BUILD_ROOT/%{_defaultdocdir}/sfftobmp/getopt
rm -rf doc/getopt
install -m 644 doc/* $RPM_BUILD_ROOT/%{_defaultdocdir}/sfftobmp

%files
%defattr(-,root,root)
%{_bindir}/sfftobmp
%doc %{_defaultdocdir}/sfftobmp

%changelog
