#
# spec file for package tesseract-ocr
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


%define so_ver 3
Name:           tesseract-ocr
Version:        3.05.01
Release:        0
Summary:        Open Source OCR Engine
License:        Apache-2.0 AND GPL-2.0+
Group:          Productivity/Graphics/Other
Url:            https://github.com/tesseract-ocr/tesseract
Source0:        https://github.com/tesseract-ocr/tesseract/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  liblept-devel >= 1.74
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
Recommends:     tesseract-ocr-traineddata-english

%description
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005. From 2007 it is developed by Google.

%package devel
Summary:        Tesseract Open Source OCR Engine Development files
Group:          Development/Libraries/Other
Requires:       liblept-devel
Requires:       libtesseract%{so_ver} = %{version}

%description devel
This package contains development files for the Tesseract Open Source OCR
Engine.

%package -n libtesseract%{so_ver}
Summary:        Open Source OCR Engine
Group:          System/Libraries

%description -n libtesseract%{so_ver}
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005. From 2007 it is developed by Google.

%prep
%setup -q -n tesseract-%{version}
autoreconf -fi

# Remove build time references so build-compare can do its work
echo "HTML_TIMESTAMP = NO" >> doc/Doxyfile

%build
export CXXFLAGS="%{optflags} -fno-strict-aliasing -fPIC"
%configure --disable-static
make %{?_smp_mflags}
make training %{?_smp_mflags}
make doc %{?_smp_mflags}

%install
%make_install
make DESTDIR=%{buildroot} training-install

# Remove libtool config files
rm -f %{buildroot}%{_libdir}/libtesseract.la

# Manually install the devel docs in order to fix rpmlint warnings "files-duplicate" and "doc-file-dependency"
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-devel
cp -a doc/html/ %{buildroot}%{_defaultdocdir}/%{name}-devel/
# Fix rpmlint warning "doc-file-dependency"
rm -f %{buildroot}%{_defaultdocdir}/%{name}-devel/html/installdox

# Fix rpmlint warning "files-duplicate"
%fdupes -s %{buildroot}

%post -n libtesseract%{so_ver} -p /sbin/ldconfig
%postun -n libtesseract%{so_ver} -p /sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog README.md
%{_bindir}/*
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/configs/
%{_datadir}/tessdata/tessconfigs/
%{_datadir}/tessdata/pdf.ttf
%{_mandir}/man1/*.1%{ext_man}
%{_mandir}/man5/*.5%{ext_man}

%files devel
%doc %{_defaultdocdir}/tesseract-ocr-devel/
%{_includedir}/tesseract/
%{_libdir}/libtesseract*.so
%{_libdir}/pkgconfig/*.pc

%files -n libtesseract%{so_ver}
%{_libdir}/libtesseract.so.%{so_ver}*

%changelog
