#
# spec file for package tesseract-ocr
#
# Copyright (c) 2023 SUSE LLC
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


%define lname	libtesseract-5_3_0
Name:           tesseract-ocr
Version:        5.3.0
Release:        0
Summary:        Open Source OCR Engine
License:        Apache-2.0 AND GPL-2.0-or-later
URL:            https://github.com/tesseract-ocr/tesseract
Source0:        https://github.com/tesseract-ocr/tesseract/archive/refs/tags/%{version}.tar.gz#/tesseract-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxslt-tools
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  plantuml
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(icu-i18n) >= 52.1
BuildRequires:  pkgconfig(icu-uc) >= 52.1
BuildRequires:  pkgconfig(lept) >= 1.74
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(pango) >= 1.22.0
BuildRequires:  pkgconfig(pangocairo) >= 1.22.0
BuildRequires:  pkgconfig(pangoft2) >= 1.22.0
Recommends:     tesseract-ocr-traineddata-english

%description
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005. From 2007 it is developed by Google.

%package devel
Summary:        Tesseract Open Source OCR Engine Development files
Requires:       %{lname} = %{version}
Requires:       pkgconfig(lept) >= 1.74
Requires:       pkgconfig(libarchive)

%description devel
This package contains development files for the Tesseract Open Source OCR
Engine.

%package -n %{lname}
Summary:        Open Source OCR Engine

%description -n %{lname}
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005. From 2007 it is developed by Google.

%prep
%autosetup -n tesseract-%{version} -p1

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DTESSDATA_PREFIX=%{_datadir}/%{name}
%cmake_build

chrpath --delete src/training/libpango_training.so

# Manually build manfiles, cmake does not build them
cd ../doc
sh generate_manpages.sh
ls -alh

%install
%cmake_install
install -D build/src/training/libpango_training.so \
	%{buildroot}%{_libdir}/libpango_training.so
mkdir -p %{buildroot}%{_mandir}/{man1,man5}/
cp -a doc/*.1 %{buildroot}%{_mandir}/man1/
cp -a doc/*.5 %{buildroot}%{_mandir}/man5/
cp -a tessdata/pdf.ttf %{buildroot}/%{_datadir}/tessdata/

# Fix rpmlint warning "files-duplicate"
%fdupes -s %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/libcommon_training.so
%{_libdir}/libpango_training.so
%{_libdir}/libunicharset_training.so
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/configs/
%{_datadir}/tessdata/tessconfigs/
%{_datadir}/tessdata/pdf.ttf
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}

%files devel
%{_includedir}/tesseract
%{_libdir}/libtesseract.so
%{_libdir}/cmake/tesseract/
%{_libdir}/pkgconfig/*.pc

%files -n %{lname}
%license LICENSE
%{_libdir}/libtesseract.so.*

%changelog
