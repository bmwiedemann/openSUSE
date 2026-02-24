#
# spec file for package qpdf
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without doc
%else
%bcond_with doc
%endif

%define so_version 30
%bcond_without zopfli
Name:           qpdf
Version:        12.3.2
Release:        0
Summary:        Command-line tools and library for transforming PDF files
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://qpdf.sourceforge.io
Source:         https://github.com/qpdf/qpdf/releases/download/v%{version}/qpdf-%{version}.tar.gz
Source1:        https://github.com/qpdf/qpdf/releases/download/v%{version}/qpdf-%{version}.tar.gz.asc
Source2:        qpdf.keyring
BuildRequires:  cmake >= 3.16
BuildRequires:  fdupes
%if 0%{suse_version} > 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc15-c++
%endif
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-Sphinx-latex
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  texlive-latex
BuildRequires:  texlive-latexmk
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(zlib)
%if %{with zopfli}
BuildRequires:  cmake(Zopfli)
%endif

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

%package doc
Summary:        Documentation files for qpdf
Group:          Documentation/HTML
Obsoletes:      %{name}-htmldoc
BuildArch:      noarch

%description doc
This package contains the documentation for qpdf

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
%if 0%{suse_version} == 1500
export CXX=g++-15
%endif
%global optflags %{optflags} -fexcess-precision=fast
%cmake \
  -DSHOW_FAILED_TEST_OUTPUT=ON \
  -DWERROR=ON \
%if %{with doc}
  -DBUILD_DOC=ON \
  -DBUILD_DOC_DIST=ON \
  -DBUILD_DOC_HTML=ON \
  -DBUILD_DOC_PDF=ON \
%else
   -DBUILD_DOC=OFF \
%endif
%if %{with zopfli}
  -DZOPFLI=ON \
%endif
  %{?nil}
%cmake_build

%check
%ifarch s390x
rm qpdf/qtest/specific-bugs.test
rm qpdf/qtest/inline-images.test
%endif
%ctest

%install
%cmake_install
%if %{with doc}
mkdir -m755 -p %{buildroot}%{_docdir}/%{name}/html
mkdir -m755 -p %{buildroot}%{_docdir}/%{name}/singlehtml
pushd build/manual/doc-dist
  cp -a manual-html/* %{buildroot}%{_docdir}/%{name}/html/
  cp -a manual-single-page-html/* %{buildroot}%{_docdir}/%{name}/singlehtml/
  install -Dm644 qpdf-manual.pdf %{buildroot}%{_docdir}/%{name}/qpdf-manual.pdf
popd
%endif
install -D -m 0644 completions/bash/qpdf %{buildroot}%{_datadir}/bash-completion/completions/qpdf
install -D -m 0644 completions/zsh/_qpdf %{buildroot}%{_datadir}/zsh/site-functions/_qpdf

# create symlinks for html and singlehtml duplicate docs
%fdupes -s %{buildroot}%{_docdir}/%{name}

%post -n libqpdf%{so_version} -p /sbin/ldconfig
%postun -n libqpdf%{so_version} -p /sbin/ldconfig

%files
%doc ChangeLog README-doc.txt
%license Artistic-2.0 LICENSE.txt
%{_bindir}/{fix-qdf,qpdf,zlib-flate}
%{_mandir}/man1/{fix-qdf,qpdf,zlib-flate}.1%{?ext_man}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/bash-completion/completions/qpdf
%{_datadir}/zsh/site-functions/_qpdf

%if %{with doc}
%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/singlehtml
%doc %{_docdir}/%{name}/qpdf-manual.pdf
%endif

%files -n libqpdf%{so_version}
%license Artistic-2.0 LICENSE.txt
%{_libdir}/libqpdf.so.%{so_version}*

%files devel
%doc %{_docdir}/%{name}/examples
%license Artistic-2.0 LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/libqpdf.pc
%{_libdir}/libqpdf.so
%{_libdir}/cmake/qpdf

%changelog
