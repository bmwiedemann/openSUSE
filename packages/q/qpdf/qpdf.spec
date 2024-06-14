#
# spec file for package qpdf
#
# Copyright (c) 2024 SUSE LLC
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


%define so_version 29
Name:           qpdf
Version:        11.9.1
Release:        0
Summary:        Command-line tools and library for transforming PDF files
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://qpdf.sourceforge.io/
Source:         https://github.com/qpdf/qpdf/releases/download/v%{version}/qpdf-%{version}.tar.gz
Source1:        https://github.com/qpdf/qpdf/releases/download/v%{version}/qpdf-%{version}.tar.gz.asc
Source2:        qpdf.keyring
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python3-Sphinx
BuildRequires:  python3-Sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  texlive-latex
BuildRequires:  texlive-latexmk
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(zlib)

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

%if 0%{?suse_version} > 1500
%package htmldoc
Summary:        Documentation files for qpdf
Group:          Documentation/HTML
BuildArch:      noarch

%description htmldoc
This package contains the documentation for qpdf
%endif

%package devel
Summary:        Development files for qpdf PDF manipulation library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libqpdf%{so_version} = %{version}
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
%global optflags %optflags -fexcess-precision=fast
%cmake \
%if 0%{?suse_version} > 1500
  -DBUILD_DOC=ON \
  -DBUILD_DOC_DIST=ON \
  -DBUILD_DOC_HTML=ON \
  -DBUILD_DOC_PDF=ON \
%endif
  -DCMAKE_INSTALL_DOCDIR='${datarootdir}'share/doc/packages/%{name}
%cmake_build

%check
make -C build test

%install
%cmake_install
%if 0%{?suse_version} > 1500
mkdir -m755 -p %{buildroot}%{_docdir}/%{name}/html
mkdir -m755 -p %{buildroot}%{_docdir}/%{name}/singlehtml
pushd build/manual/doc-dist
  cp -a manual-html/* %{buildroot}%{_docdir}/%{name}/html/
  cp -a manual-single-page-html/* %{buildroot}%{_docdir}/%{name}/singlehtml/
  install -Dm644 qpdf-manual.pdf %{buildroot}%{_docdir}/%{name}/qpdf-manual.pdf
popd
%endif

# create symlinks for html and singlehtml duplicate docs
%fdupes -s %{buildroot}%{_docdir}/%{name}

%post -n libqpdf%{so_version} -p /sbin/ldconfig
%postun -n libqpdf%{so_version} -p /sbin/ldconfig

%files
%if 0%{?suse_version} > 1500
%doc qpdf-manual.pdf
%endif
%dir %{_docdir}/%{name}
%doc ChangeLog README-doc.txt
%if 0%{?suse_version} > 1500
%doc qpdf-manual.pdf
%endif
%license Artistic-2.0 LICENSE.txt
%{_bindir}/*
%{_mandir}/man1/*

%if 0%{?suse_version} > 1500
%files htmldoc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/singlehtml
%endif

%files -n libqpdf%{so_version}
%{_libdir}/libqpdf.so.%{so_version}*

%files devel
%doc %{_docdir}/%{name}/examples
%{_includedir}/*
%{_libdir}/pkgconfig/libqpdf.pc
%{_libdir}/libqpdf.so
%{_libdir}/cmake/qpdf

%changelog
