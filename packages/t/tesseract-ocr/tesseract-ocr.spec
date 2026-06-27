#
# spec file for package tesseract-ocr
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define lname	libtesseract5
Name:           tesseract-ocr
Version:        5.5.2
Release:        0
Summary:        Open Source OCR Engine
License:        Apache-2.0 AND GPL-2.0-or-later
URL:            https://github.com/tesseract-ocr/tesseract
Source0:        https://github.com/tesseract-ocr/tesseract/archive/refs/tags/%{version}.tar.gz#/tesseract-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  plantuml
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(icu-i18n) >= 52.1
BuildRequires:  pkgconfig(icu-uc) >= 52.1
BuildRequires:  pkgconfig(lept) >= 1.74
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(pango) >= 1.38.0
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
Requires:       tesseract-ocr-common
%{?suse_build_hwcaps_libs}
%if 0%{?suse_version} > 1550
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc13-c++
%endif

%description
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005. From 2007 it is developed by Google.

%package common
Summary:        Tesseract Open Source OCR Engine Common files
Requires:       tesseract-ocr-traineddata-provider
Requires:       (%{name} = %{version} or %{lname} = %{version})
Recommends:     tesseract-ocr-traineddata-eng
BuildArch:      noarch

%description common
This package contains files common to the Tesseract Open Source OCR
Engine binaries and library.

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
Requires:       tesseract-ocr-common

%description -n %{lname}
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005. From 2007 it is developed by Google.

%prep
%autosetup -n tesseract-%{version} -p1

%build
%if 0%{?suse_version} < 1550
export CC=gcc-13
export CXX=g++-13
%endif

autoreconf -fiv
%configure \
    --disable-static

# Upstream mixes `all` and `training` in a single make invocation
# at its own peril (libtool race in convenience-library link rules).
# CI builds them in separate make invocations; do the same here so
# we can use parallel make.
%make_build all
%make_build training doc

%install
%make_install all training-install

rm -f %{buildroot}%{_libdir}/libtesseract.la

# Strip absolute -L paths injected via pkg-config (libarchive/libcurl);
# the system linker already searches /usr/lib(64), and -L/usr/lib in
# a lib64 build is an rpmlint error (pkgconfig-invalid-libs-dir).
sed -i -E 's| -L(/usr)?/lib(64)? | |g; s| -L(/usr)?/lib(64)?$||' \
    %{buildroot}%{_libdir}/pkgconfig/tesseract.pc

mkdir -p %{buildroot}%{_mandir}/{man1,man5}/
cp -a doc/*.1 %{buildroot}%{_mandir}/man1/
cp -a doc/*.5 %{buildroot}%{_mandir}/man5/
cp -a tessdata/pdf.ttf %{buildroot}/%{_datadir}/tessdata/

# Fix rpmlint warning "files-duplicate"
%fdupes -s %{buildroot}

%ldconfig_scriptlets -n %{lname}

%files
%doc AUTHORS ChangeLog README.md
%license LICENSE
%{_bindir}/ambiguous_words
%{_bindir}/classifier_tester
%{_bindir}/cntraining
%{_bindir}/combine_lang_model
%{_bindir}/combine_tessdata
%{_bindir}/dawg2wordlist
%{_bindir}/lstmeval
%{_bindir}/lstmtraining
%{_bindir}/merge_unicharsets
%{_bindir}/mftraining
%{_bindir}/set_unicharset_properties
%{_bindir}/shapeclustering
%{_bindir}/tesseract
%{_bindir}/text2image
%{_bindir}/unicharset_extractor
%{_bindir}/wordlist2dawg
%{_mandir}/man1/ambiguous_words.1%{?ext_man}
%{_mandir}/man1/classifier_tester.1%{?ext_man}
%{_mandir}/man1/cntraining.1%{?ext_man}
%{_mandir}/man1/combine_lang_model.1%{?ext_man}
%{_mandir}/man1/combine_tessdata.1%{?ext_man}
%{_mandir}/man1/dawg2wordlist.1%{?ext_man}
%{_mandir}/man1/lstmeval.1%{?ext_man}
%{_mandir}/man1/lstmtraining.1%{?ext_man}
%{_mandir}/man1/merge_unicharsets.1%{?ext_man}
%{_mandir}/man1/mftraining.1%{?ext_man}
%{_mandir}/man1/set_unicharset_properties.1%{?ext_man}
%{_mandir}/man1/shapeclustering.1%{?ext_man}
%{_mandir}/man1/tesseract.1%{?ext_man}
%{_mandir}/man1/text2image.1%{?ext_man}
%{_mandir}/man1/unicharset_extractor.1%{?ext_man}
%{_mandir}/man1/wordlist2dawg.1%{?ext_man}
%{_mandir}/man5/unicharambigs.5%{?ext_man}
%{_mandir}/man5/unicharset.5%{?ext_man}

%files common
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/configs/
%{_datadir}/tessdata/tessconfigs/
%{_datadir}/tessdata/pdf.ttf

%files devel
%{_includedir}/tesseract
%{_libdir}/libtesseract.so
%{_libdir}/pkgconfig/*.pc

%files -n %{lname}
%license LICENSE
%{_libdir}/libtesseract.so.*

%changelog
