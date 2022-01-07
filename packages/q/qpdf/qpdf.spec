#
# spec file for package qpdf
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


%define so_version 28
Name:           qpdf
Version:        10.5.0
Release:        0
Summary:        Command-line tools and library for transforming PDF files
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://qpdf.sourceforge.io/
Source:         https://github.com/qpdf/qpdf/releases/download/release-qpdf-%{version}/qpdf-%{version}.tar.gz
Source1:        https://github.com/qpdf/qpdf/releases/download/release-qpdf-%{version}/qpdf-%{version}.tar.gz.asc
Source2:        qpdf.keyring
Patch1:         build-without-pdf.patch
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  libjpeg8-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  tiff
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(openssl)

%description
QPDF is a program that does structural, content-preserving
transformations on PDF files.  It could have been called something
like pdf-to-pdf.  It also provides many useful capabilities to
developers of PDF-producing software or for people who just want to
look at the innards of a PDF file to learn more about how they work.

QPDF offers many capabilities such as linearization (web
optimization), encrypt, and decryption of PDF files.  Note that QPDF
does not have the capability to create PDF files from scratch; it is
only used to create PDF files with special characteristics starting
from other PDF files or to inspect or extract information from
existing PDF files.

%package htmldoc
Summary:        Documentation files for qpdf
Group:          Documentation/HTML

%description htmldoc
This package contains the documentation for qpdf

%package devel
Summary:        Development files for qpdf PDF manipulation library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libstdc++-devel

%description devel
The qpdf-devel package contains header files and libraries necessary
for developing programs using the qpdf library.

%package -n libqpdf%{so_version}
Summary:        Shared libraries for qpdf
Group:          Development/Libraries/C and C++

%description -n libqpdf%{so_version}
This packages contains the shared libraries required for the qpdf
package.

%prep
%autosetup -p1

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure --disable-static \
           --enable-werror \
           --enable-crypto-openssl \
	   --enable-html-doc \
           --disable-implicit-crypto \
           --docdir='${datarootdir}'/doc/packages/%{name} \
           --enable-show-failed-test-output \
           --enable-test-compare-images
%make_build

%check
%make_build check
rm -rf qpdf/qtest # Unicode data can't be redistributed freely

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%make_build doc-dist DOC_DEST=%{buildroot}%{_docdir}/%{name}

%post -n libqpdf%{so_version} -p /sbin/ldconfig
%postun -n libqpdf%{so_version} -p /sbin/ldconfig

%files
%dir %{_docdir}/%{name}
%doc ChangeLog README-doc.txt
%license Artistic-2.0
%{_bindir}/*
%{_mandir}/man1/*

%files htmldoc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/singlehtml

%files -n libqpdf%{so_version}
%{_libdir}/libqpdf.so.%{so_version}*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/libqpdf.pc
%{_libdir}/libqpdf.so

%changelog
