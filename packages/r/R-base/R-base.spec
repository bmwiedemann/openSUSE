#
# spec file for package R-base
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


%if %{undefined _rpmmacrodir}
%define _rpmmacrodir %{_sysconfdir}/rpm/
%endif

%define release 1

Name:           R-base
Version:        4.4.1
Release:        %release
%define Rversion %{version}
Source0:        R-%{version}.tar.xz
Source10:       macros.R
#Source: http://cran.r-project.org/src/base/R-2/R-%%{version}.tar.gz

URL:            http://www.r-project.org/

Summary:        R - statistics package (S-Plus like)
License:        GPL-2.0-only OR GPL-3.0-only
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bzip2
BuildRequires:  cairo-devel
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  glib2-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pango-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl
BuildRequires:  readline-devel
BuildRequires:  shadow
BuildRequires:  tcl-devel
BuildRequires:  texlive-ae
BuildRequires:  texlive-bibtex
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-dvips
BuildRequires:  texlive-fancyvrb
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-latex
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-metafont
BuildRequires:  texlive-psnfss
BuildRequires:  texlive-tex
BuildRequires:  texlive-times
BuildRequires:  unzip
BuildRequires:  xdg-utils
BuildRequires:  xz-devel
BuildRequires:  zip
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1320
BuildRequires:  texinfo >= 5.1
BuildRequires:  tex(inconsolata.sty)
%endif
## > 1320
BuildRequires:  tk-devel
Requires:       R-base-devel = %{version}
Requires:       R-core = %{version}
Requires:       R-core-devel = %{version}
Requires:       R-core-doc = %{version}
Requires:       R-core-libs = %{version}
Requires:       R-core-packages = %{version}
Requires:       R-recommended-packages = %{version}
Requires:       fontconfig
Requires:       glibc-locale
#Requires:       libcairo2
#Requires:       libfreetype6
#Requires:       liblzma5
#Requires:       libreadline6
Requires:       make
Requires:       xdg-utils
Requires:       xorg-x11-fonts-100dpi
Requires:       xorg-x11-fonts-75dpi

Provides:       R = %{version}

%description
R is a language which is not entirely unlike the S language developed at
AT&T Bell Laboratories by Rick Becker, John Chambers and Allan Wilks.

%prep
%autosetup -n R-%{version}
#%%patch0 -p1

%build
#export R_BROWSER="xdg-open"
#export R_PDFVIEWER="xdg-open"
%configure --enable-R-shlib LIBnn=%{_lib}

make %{?_smp_mflags}
#make
make pdf
%if 0%{?suse_version} > 1320
make info
# Convert to UTF-8
for i in doc/manual/R-intro.info doc/manual/R-FAQ.info doc/FAQ doc/manual/R-admin.info doc/manual/R-exts.info-1; do
  iconv -f iso-8859-1 -t utf-8 -o $i{.utf8,}
  mv $i{.utf8,}
done
%endif

%install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install-pdf

# Installation of Info-files
%if 0%{?suse_version} > 1320
make DESTDIR=%{buildroot} INFODIR=%{buildroot}%{_infodir} install-info
%{__rm} -f %{buildroot}%{_infodir}/dir
%{__rm} -f %{buildroot}%{_infodir}/dir.old
%endif

chmod +x %{buildroot}%{_libdir}/R/share/sh/echo.sh

chmod -x %{buildroot}%{_libdir}/R/library/mgcv/CITATION

%fdupes -s $RPM_BUILD_ROOT

# Install ld.so.conf.d file to ensure other applications access the shared lib
mkdir -p %{buildroot}/etc/ld.so.conf.d
cat << EOF >%{buildroot}/etc/ld.so.conf.d/R.conf
%{_libdir}/R/lib
EOF

# Install RPM macros
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE10}
sed -i 's|@vers@|%{Rversion}|' %{buildroot}%{_rpmmacrodir}/macros.R

# Add noarch R library directory
mkdir -p %{buildroot}%{_datadir}/R/library

%files -n R-base

%package -n R-base-devel
Summary:        Metapackage, requires R-core-devel, R-core-libs
Version:        %{Rversion}
Release:        %release
#Requires:       R-Matrix-devel
Requires:       R-core-devel
Requires:       R-core-libs

%description -n R-base-devel
Metapackage to keep the same user experience as before the split of
the monolithic R-base-devel

%files -n R-base-devel

# R-core
%package -n R-core
Summary:        The core components of R
Version:        %{Rversion}
Release:        %release

%description -n R-core
This package provides the core of R, i.e. all that is in base.

%files -n R-core
%defattr(-, root, root)

# base
%dir %{_libdir}/R/library/base/
%{_libdir}/R/library/base/CITATION
%{_libdir}/R/library/base/demo/
%{_libdir}/R/library/base/DESCRIPTION
%{_libdir}/R/library/base/help/
%{_libdir}/R/library/base/html/
%{_libdir}/R/library/base/INDEX
%{_libdir}/R/library/base/Meta/
%{_libdir}/R/library/base/R/

# noarch

# translations
%dir %{_libdir}/R/library/translations/
%doc %{_libdir}/R/library/translations/DESCRIPTION

%dir %{_libdir}/R/library/translations/ar
%dir %{_libdir}/R/library/translations/ar/LC_MESSAGES
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/R-base.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/R-methods.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/R-parallel.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/R-splines.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/R-stats.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/R-stats4.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/R-tcltk.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/R-tools.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/R-utils.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/R.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/RGui.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/grDevices.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/graphics.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/methods.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/parallel.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/splines.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/stats.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/tcltk.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/tools.mo
%lang(ar) %{_libdir}/R/library/translations/ar/LC_MESSAGES/utils.mo

%dir %{_libdir}/R/library/translations/bn/
%dir %{_libdir}/R/library/translations/bn/LC_MESSAGES/
%lang(bn) %{_libdir}/R/library/translations/bn/LC_MESSAGES/R-base.mo
%lang(bn) %{_libdir}/R/library/translations/bn/LC_MESSAGES/RGui.mo
%lang(bn) %{_libdir}/R/library/translations/bn/LC_MESSAGES/tcltk.mo

%dir %{_libdir}/R/library/translations/ca/
%dir %{_libdir}/R/library/translations/ca/LC_MESSAGES/
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-base.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-compiler.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-grDevices.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-graphics.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-grid.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-methods.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-parallel.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-splines.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-stats.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-stats4.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-tcltk.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-tools.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R-utils.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/R.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/RGui.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/grDevices.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/graphics.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/grid.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/methods.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/parallel.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/splines.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/stats.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/tcltk.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/tools.mo
%lang(ca) %{_libdir}/R/library/translations/ca/LC_MESSAGES/utils.mo

%dir %{_libdir}/R/library/translations/da/
%dir %{_libdir}/R/library/translations/da/LC_MESSAGES/
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-base.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/de
%dir %{_libdir}/R/library/translations/de/LC_MESSAGES
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-base.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/en
%dir %{_libdir}/R/library/translations/en/LC_MESSAGES
%lang(en) %{_libdir}/R/library/translations/en/LC_MESSAGES/R.mo
%dir %{_libdir}/R/library/translations/en@quot
%dir %{_libdir}/R/library/translations/en@quot/LC_MESSAGES
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-base.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R.mo

%dir %{_libdir}/R/library/translations/en_GB
%dir %{_libdir}/R/library/translations/en_GB/LC_MESSAGES
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-base.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-compiler.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-graphics.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-grid.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-methods.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-parallel.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-splines.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-stats.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-stats4.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-tcltk.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-tools.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-utils.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/RGui.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/graphics.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/grid.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/methods.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/parallel.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/splines.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/stats.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/tcltk.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/tools.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/utils.mo

%dir %{_libdir}/R/library/translations/es
%dir %{_libdir}/R/library/translations/es/LC_MESSAGES
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R-base.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R-grDevices.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R-graphics.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R-grid.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R-methods.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R-parallel.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R-stats.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R-stats4.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R-tools.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/R-utils.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/RGui.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/grDevices.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/parallel.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/stats.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/tcltk.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/tools.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/utils.mo

%dir %{_libdir}/R/library/translations/fa
%dir %{_libdir}/R/library/translations/fa/LC_MESSAGES
%lang(fa) %{_libdir}/R/library/translations/fa/LC_MESSAGES/R-base.mo
%lang(fa) %{_libdir}/R/library/translations/fa/LC_MESSAGES/R.mo
%lang(fa) %{_libdir}/R/library/translations/fa/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/fr
%dir %{_libdir}/R/library/translations/fr/LC_MESSAGES
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-base.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/hi
%dir %{_libdir}/R/library/translations/hi/LC_MESSAGES
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/R-base.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/R-grDevices.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/R-graphics.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/R-parallel.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/R-stats.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/R-tools.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/R-utils.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/R.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/RGui.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/grDevices.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/graphics.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/parallel.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/stats.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/tools.mo
%lang(hi) %{_libdir}/R/library/translations/hi/LC_MESSAGES/utils.mo

%dir %{_libdir}/R/library/translations/hu
%dir %{_libdir}/R/library/translations/hu/LC_MESSAGES
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/R-base.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/R-graphics.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/R-parallel.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/R-splines.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/R-stats.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/R-tcltk.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/R-tools.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/R-utils.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/R.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/RGui.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/grDevices.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/graphics.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/grid.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/parallel.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/stats.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/tcltk.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/tools.mo
%lang(hu) %{_libdir}/R/library/translations/hu/LC_MESSAGES/utils.mo

%dir %{_libdir}/R/library/translations/id
%dir %{_libdir}/R/library/translations/id/LC_MESSAGES
%lang(id) %{_libdir}/R/library/translations/id/LC_MESSAGES/R-base.mo

%dir %{_libdir}/R/library/translations/it
%dir %{_libdir}/R/library/translations/it/LC_MESSAGES
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-base.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/ja
%dir %{_libdir}/R/library/translations/ja/LC_MESSAGES
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-base.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-parallel.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/RGui.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/parallel.mo

%dir %{_libdir}/R/library/translations/ko
%dir %{_libdir}/R/library/translations/ko/LC_MESSAGES
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-base.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/lt/
%dir %{_libdir}/R/library/translations/lt/LC_MESSAGES/
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-base.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/ne
%dir %{_libdir}/R/library/translations/ne/LC_MESSAGES
%lang(ne) %{_libdir}/R/library/translations/ne/LC_MESSAGES/R.mo
%lang(ne) %{_libdir}/R/library/translations/ne/LC_MESSAGES/R-compiler.mo
%lang(ne) %{_libdir}/R/library/translations/ne/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/nn
%dir %{_libdir}/R/library/translations/nn/LC_MESSAGES
%lang(nn) %{_libdir}/R/library/translations/nn/LC_MESSAGES/R.mo
%lang(nn) %{_libdir}/R/library/translations/nn/LC_MESSAGES/R-base.mo
%lang(nn) %{_libdir}/R/library/translations/nn/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/pl
%dir %{_libdir}/R/library/translations/pl/LC_MESSAGES
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-base.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/pt_BR
%dir %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-base.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-parallel.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/RGui.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/utils.mo

%dir %{_libdir}/R/library/translations/ru
%dir %{_libdir}/R/library/translations/ru/LC_MESSAGES
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-base.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/sq
%dir %{_libdir}/R/library/translations/sq/LC_MESSAGES
%lang(sq) %{_libdir}/R/library/translations/sq/LC_MESSAGES/R-base.mo
%lang(sq) %{_libdir}/R/library/translations/sq/LC_MESSAGES/R.mo

%dir %{_libdir}/R/library/translations/tr
%dir %{_libdir}/R/library/translations/tr/LC_MESSAGES
%lang(tr) %{_libdir}/R/library/translations/tr/LC_MESSAGES/R-base.mo
%lang(tr) %{_libdir}/R/library/translations/tr/LC_MESSAGES/R.mo
%lang(tr) %{_libdir}/R/library/translations/tr/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/ur
%dir %{_libdir}/R/library/translations/ur/LC_MESSAGES
%lang(ur) %{_libdir}/R/library/translations/ur/LC_MESSAGES/R-base.mo

%dir %{_libdir}/R/library/translations/zh_CN
%dir %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-base.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/RGui.mo

%dir %{_libdir}/R/library/translations/zh_TW
%dir %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-base.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/RGui.mo

# R-core main part
%dir %{_libdir}/R
%dir %{_datadir}/R
%{_bindir}/*
%{_libdir}/R/bin/
%{_libdir}/R/etc/
#%%{_libdir}/R/lib/
%{_libdir}/R/modules/
%dir %{_libdir}/R/share
%dir %{_libdir}/R/library
%dir %{_libdir}/R/library/grDevices/
%dir %{_libdir}/R/library/grDevices/fonts/
%dir %{_libdir}/R/library/grDevices/fonts/Montserrat
%dir %{_libdir}/R/library/grDevices/fonts/Montserrat/static
%{_libdir}/R/library/grDevices/fonts/Montserrat/static/Montserrat-BoldItalic.ttf
%{_libdir}/R/library/grDevices/fonts/Montserrat/static/Montserrat-Medium.ttf
%dir %{_libdir}/R/library/grDevices/fonts/Roboto
%{_libdir}/R/library/grDevices/fonts/Roboto/Roboto-Medium.ttf
%{_libdir}/R/library/grDevices/fonts/Roboto/LICENSE.txt

%dir %{_datadir}/R/library/
%{_libdir}/R/share/encodings/
%{_libdir}/R/share/java/

%dir %{_libdir}/R/share/dictionaries/
%{_libdir}/R/share/dictionaries/en_stats.rds
%{_libdir}/R/share/dictionaries/R_Rd_files.rds
%{_libdir}/R/share/dictionaries/R_manuals.rds
%{_libdir}/R/share/dictionaries/R_vignettes.rds
%license %{_libdir}/R/share/licenses/
%{_libdir}/R/share/make/
%{_libdir}/R/share/R/
%dir %{_libdir}/R/share/Rd/
%dir %{_libdir}/R/share/Rd/macros/
%{_libdir}/R/share/Rd/macros/system.Rd
%{_libdir}/R/share/sh/
%{_libdir}/R/share/texmf/

# ld.so.conf
#%%config /etc/ld.so.conf.d/R.conf

# R-core-devel
%package -n R-core-devel
Summary:        Libraries and include files for developing with R-base
Provides:       R-devel = %{version}
Provides:       R-devel-macros = %{version}
Requires:       R-base

%description -n R-core-devel
This package provides the necessary development headers and
libraries to allow you to devel with R-base.

%files -n R-core-devel
%defattr(-, root, root)
%dir %{_libdir}/R/include/
%{_libdir}/R/include/R.h
%{_libdir}/R/include/Rconfig.h
%{_libdir}/R/include/Rdefines.h
%{_libdir}/R/include/Rembedded.h
%{_libdir}/R/include/Rinterface.h
%{_libdir}/R/include/Rinternals.h
%{_libdir}/R/include/Rmath.h
%{_libdir}/R/include/Rversion.h
%dir %{_libdir}/R/include/R_ext
%{_libdir}/R/include/R_ext/Altrep.h
%{_libdir}/R/include/R_ext/Applic.h
%{_libdir}/R/include/R_ext/Arith.h
%{_libdir}/R/include/R_ext/BLAS.h
%{_libdir}/R/include/R_ext/Boolean.h
%{_libdir}/R/include/R_ext/Callbacks.h
%{_libdir}/R/include/R_ext/Complex.h
%{_libdir}/R/include/R_ext/Connections.h
%{_libdir}/R/include/R_ext/Constants.h
%{_libdir}/R/include/R_ext/Error.h
%{_libdir}/R/include/R_ext/GetX11Image.h
%{_libdir}/R/include/R_ext/GraphicsDevice.h
%{_libdir}/R/include/R_ext/GraphicsEngine.h
%{_libdir}/R/include/R_ext/Itermacros.h
%{_libdir}/R/include/R_ext/Lapack.h
%{_libdir}/R/include/R_ext/Linpack.h
%{_libdir}/R/include/R_ext/MathThreads.h
%{_libdir}/R/include/R_ext/Memory.h
%{_libdir}/R/include/R_ext/Parse.h
%{_libdir}/R/include/R_ext/Print.h
%{_libdir}/R/include/R_ext/PrtUtil.h
%{_libdir}/R/include/R_ext/QuartzDevice.h
%{_libdir}/R/include/R_ext/Rallocators.h
%{_libdir}/R/include/R_ext/RS.h
%{_libdir}/R/include/R_ext/RStartup.h
%{_libdir}/R/include/R_ext/Random.h
%{_libdir}/R/include/R_ext/Rdynload.h
%{_libdir}/R/include/R_ext/Riconv.h
%{_libdir}/R/include/R_ext/Utils.h
%{_libdir}/R/include/R_ext/Visibility.h
%{_libdir}/R/include/R_ext/eventloop.h
%{_libdir}/R/include/R_ext/libextern.h
%{_libdir}/R/include/R_ext/stats_package.h
%{_libdir}/R/include/R_ext/stats_stubs.h

%config %{_rpmmacrodir}/macros.R
%{_libdir}/pkgconfig/libR.pc

#R-core-libs
%package -n     R-core-libs
Summary:        R language libraries

%description -n R-core-libs
This package contains the files from R/lib to make their usage
possible without installing a complete R. (I.e. VTK uses this)

%files -n R-core-libs
%defattr(-, root, root)
%dir %{_libdir}/R
%{_libdir}/R/lib/

#ld.so.conf
%config /etc/ld.so.conf.d/R.conf

%post -n R-core-libs -p /sbin/ldconfig

%postun -n R-core-libs -p /sbin/ldconfig

%package -n R-core-doc
Summary:        Package provides all documentation of R base. PDFs, man pages, info pages

%description -n R-core-doc
This packages provides all documentation of R base. PDFs, man pages, info pages

%post -n R-core-doc
%if 0%{?suse_version} > 1320
%install_info --info-dir=%{_infodir} %{_infodir}/R-exts.info-1.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-FAQ.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-lang.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-admin.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-exts.info-2.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-intro.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-data.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-exts.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/R-ints.info.gz
%endif

%preun -n R-core-doc
%if 0%{?suse_version} > 1320
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-exts.info-1.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-FAQ.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-lang.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-admin.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-exts.info-2.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-intro.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-data.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-exts.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/R-ints.info.gz
%endif

%files -n R-core-doc
%defattr(-, root, root)
%doc README
%{_mandir}/man1/R.1*
%{_mandir}/man1/Rscript.1*
%doc %{_libdir}/R/COPYING
%doc %{_libdir}/R/SVN-REVISION
%if 0%{?suse_version} > 1320
%{_infodir}/*.gz
%endif
# this directory must *not* be marked as %%doc, as rstudio _requires_ the
# directory to be present even if rpm is invoked with --excludedocs
%{_libdir}/R/doc/

# R-core-packages

%package -n R-core-packages
Summary:        Metapackage, requires all core Packages
Version:        %{Rversion}
Release:        %release
Requires:       R-compiler
Requires:       R-datasets
Requires:       R-grDevices
Requires:       R-graphics
Requires:       R-grid
Requires:       R-methods
Requires:       R-parallel
Requires:       R-splines
Requires:       R-stats
Requires:       R-stats4
Requires:       R-tcltk
Requires:       R-tools
Requires:       R-utils

%description -n R-core-packages
Metapackage, Requires: all core Packages

%files -n R-core-packages

# compiler

%package -n R-compiler
Summary:        Package providing R-core packages R-compiler
Requires:       R-base = %{version}

%description -n R-compiler
This package provides R-compiler, one of the R-core packages.

%files -n R-compiler
%defattr(-, root, root)
%dir %{_libdir}/R/library/compiler/
%{_libdir}/R/library/compiler/DESCRIPTION
%{_libdir}/R/library/compiler/help/
%{_libdir}/R/library/compiler/html/
%{_libdir}/R/library/compiler/INDEX
%{_libdir}/R/library/compiler/Meta/
%{_libdir}/R/library/compiler/NAMESPACE
%{_libdir}/R/library/compiler/R/

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-compiler.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-compiler.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-compiler.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-compiler.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-compiler.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-compiler.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-compiler.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-compiler.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-compiler.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-compiler.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-compiler.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-compiler.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-compiler.mo

# datasets

%package -n R-datasets
Summary:        Package providing R-core datasets in R-datasets
Requires:       R-base = %{version}

%description -n R-datasets
This package provides R-datasets, one of R-core packages.

%files -n R-datasets
%defattr(-, root, root)
%dir %{_libdir}/R/library/datasets/
%{_libdir}/R/library/datasets/data/
%{_libdir}/R/library/datasets/DESCRIPTION
%{_libdir}/R/library/datasets/help/
%{_libdir}/R/library/datasets/html/
%{_libdir}/R/library/datasets/INDEX
%{_libdir}/R/library/datasets/Meta/
%{_libdir}/R/library/datasets/NAMESPACE

# grDevices

%package -n R-grDevices
Summary:        Package providing R-core graphics devices in R-grDevices
Requires:       R-base = %{version}

%description -n R-grDevices
This package provides R-grDevices, one of R-core packages.

%files -n R-grDevices
%defattr(-, root, root)

%dir %{_libdir}/R/library/grDevices
%{_libdir}/R/library/grDevices/afm/
%{_libdir}/R/library/grDevices/DESCRIPTION
%dir %{_libdir}/R/library/grDevices/demo/
%{_libdir}/R/library/grDevices/demo/colors.R
%{_libdir}/R/library/grDevices/demo/hclColors.R
%{_libdir}/R/library/grDevices/enc/
%{_libdir}/R/library/grDevices/help/
%{_libdir}/R/library/grDevices/html/
%{_libdir}/R/library/grDevices/icc/
%{_libdir}/R/library/grDevices/INDEX
%{_libdir}/R/library/grDevices/libs/
%{_libdir}/R/library/grDevices/Meta/
%{_libdir}/R/library/grDevices/NAMESPACE
%{_libdir}/R/library/grDevices/R/

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-grDevices.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/grDevices.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-grDevices.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/grDevices.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-grDevices.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/grDevices.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/R-grDevices.mo
%lang(en_GB) %{_libdir}/R/library/translations/en_GB/LC_MESSAGES/grDevices.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-grDevices.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/grDevices.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-grDevices.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/grDevices.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-grDevices.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/grDevices.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-grDevices.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/grDevices.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-grDevices.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/grDevices.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-grDevices.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/grDevices.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-grDevices.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/grDevices.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-grDevices.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/grDevices.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-grDevices.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/grDevices.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-grDevices.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/grDevices.mo

# graphics

%package -n R-graphics
Summary:        Package providing R-core graphics in R-graphics
Requires:       R-base = %{version}

%description -n R-graphics
This package provides R-graphics, one of R-core packages.

%files -n R-graphics
%defattr(-, root, root)

%dir %{_libdir}/R/library/graphics/
%{_libdir}/R/library/graphics/demo/
%{_libdir}/R/library/graphics/DESCRIPTION
%{_libdir}/R/library/graphics/help/
%{_libdir}/R/library/graphics/html/
%{_libdir}/R/library/graphics/INDEX
%{_libdir}/R/library/graphics/libs/
%{_libdir}/R/library/graphics/Meta/
%{_libdir}/R/library/graphics/NAMESPACE
%{_libdir}/R/library/graphics/R/

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-graphics.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/graphics.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-graphics.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/graphics.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-graphics.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/graphics.mo
%lang(es) %{_libdir}/R/library/translations/es/LC_MESSAGES/graphics.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-graphics.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/graphics.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-graphics.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/graphics.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-graphics.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/graphics.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-graphics.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/graphics.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-graphics.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/graphics.mo
%lang(nn) %{_libdir}/R/library/translations/nn/LC_MESSAGES/graphics.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-graphics.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/graphics.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-graphics.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/graphics.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-graphics.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/graphics.mo
%lang(tr) %{_libdir}/R/library/translations/tr/LC_MESSAGES/graphics.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-graphics.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/graphics.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-graphics.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/graphics.mo

# grid

%package -n R-grid
Summary:        Package providing R-grid graphics in R-grid
Requires:       R-base = %{version}

%description -n R-grid
This package provides R-grid, one of R-core packages.

%files -n R-grid
%defattr(-, root, root)

%dir %{_libdir}/R/library/grid/
%{_libdir}/R/library/grid/DESCRIPTION
%{_libdir}/R/library/grid/doc/
%{_libdir}/R/library/grid/help/
%{_libdir}/R/library/grid/html/
%{_libdir}/R/library/grid/INDEX
%{_libdir}/R/library/grid/libs/
%{_libdir}/R/library/grid/Meta/
%{_libdir}/R/library/grid/NAMESPACE
%{_libdir}/R/library/grid/R/

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-grid.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/grid.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-grid.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/grid.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-grid.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/grid.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-grid.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/grid.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-grid.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/grid.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-grid.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/grid.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-grid.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/grid.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-grid.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/grid.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-grid.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/grid.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-grid.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/grid.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-grid.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/grid.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-grid.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/grid.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-grid.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/grid.mo

# methods

%package -n R-methods
Summary:        Package providing R-methods
Requires:       R-base = %{version}

%description -n R-methods
This package provides R-methods, one of R-core packages.

%files -n R-methods
%defattr(-, root, root)

%dir %{_libdir}/R/library/methods/
%{_libdir}/R/library/methods/DESCRIPTION
%{_libdir}/R/library/methods/help/
%{_libdir}/R/library/methods/html/
%{_libdir}/R/library/methods/INDEX
%{_libdir}/R/library/methods/libs/
%{_libdir}/R/library/methods/Meta/
%{_libdir}/R/library/methods/NAMESPACE
%{_libdir}/R/library/methods/R/

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-methods.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/methods.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-methods.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/methods.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-methods.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/methods.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-methods.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/methods.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-methods.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/methods.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-methods.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/methods.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-methods.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/methods.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-methods.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/methods.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-methods.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/methods.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-methods.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/methods.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-methods.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/methods.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-methods.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/methods.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-methods.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/methods.mo

%package -n R-parallel
Summary:        Package providing R-parallel
Requires:       R-base = %{version}

%description -n R-parallel
This package provides R-parallel, one of R-core packages.

%files -n R-parallel
%defattr(-, root, root)

%dir %{_libdir}/R/library/parallel/
%{_libdir}/R/library/parallel/DESCRIPTION
%{_libdir}/R/library/parallel/INDEX
%dir %{_libdir}/R/library/parallel/doc
%{_libdir}/R/library/parallel/doc/index.html
%{_libdir}/R/library/parallel/doc/parallel.pdf
%{_libdir}/R/library/parallel/doc/parallel.R
%{_libdir}/R/library/parallel/doc/parallel.Rnw
%dir %{_libdir}/R/library/parallel/Meta
%{_libdir}/R/library/parallel/Meta/Rd.rds
%{_libdir}/R/library/parallel/Meta/features.rds
%{_libdir}/R/library/parallel/Meta/hsearch.rds
%{_libdir}/R/library/parallel/Meta/links.rds
%{_libdir}/R/library/parallel/Meta/nsInfo.rds
%{_libdir}/R/library/parallel/Meta/package.rds
%{_libdir}/R/library/parallel/Meta/vignette.rds
%{_libdir}/R/library/parallel/NAMESPACE
%dir %{_libdir}/R/library/parallel/R
%{_libdir}/R/library/parallel/R/parallel
%{_libdir}/R/library/parallel/R/parallel.rdb
%{_libdir}/R/library/parallel/R/parallel.rdx
%dir %{_libdir}/R/library/parallel/help
%{_libdir}/R/library/parallel/help/AnIndex
%{_libdir}/R/library/parallel/help/aliases.rds
%{_libdir}/R/library/parallel/help/parallel.rdb
%{_libdir}/R/library/parallel/help/parallel.rdx
%{_libdir}/R/library/parallel/help/paths.rds
%dir %{_libdir}/R/library/parallel/html
%{_libdir}/R/library/parallel/html/00Index.html
%{_libdir}/R/library/parallel/html/R.css
%dir %{_libdir}/R/library/parallel/libs
%{_libdir}/R/library/parallel/libs/parallel.so

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-parallel.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/parallel.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-parallel.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/parallel.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-parallel.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/parallel.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-parallel.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/parallel.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-parallel.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/parallel.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-parallel.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/parallel.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-parallel.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/parallel.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-parallel.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/parallel.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-parallel.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/parallel.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-parallel.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/parallel.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-parallel.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/parallel.mo

# splines

%package -n R-splines
Summary:        Package providing R-splines
Requires:       R-base = %{version}

%description -n R-splines
This package provides R-splines, one of R-core packages.

%files -n R-splines
%defattr(-, root, root)

%dir %{_libdir}/R/library/splines/
%{_libdir}/R/library/splines/DESCRIPTION
%{_libdir}/R/library/splines/help/
%{_libdir}/R/library/splines/html/
%{_libdir}/R/library/splines/INDEX
%{_libdir}/R/library/splines/libs/
%{_libdir}/R/library/splines/Meta/
%{_libdir}/R/library/splines/NAMESPACE
%{_libdir}/R/library/splines/R/

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-splines.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/splines.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-splines.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/splines.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-splines.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/splines.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-splines.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/splines.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-splines.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/splines.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-splines.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/splines.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-splines.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/splines.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-splines.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/splines.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-splines.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/splines.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-splines.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/splines.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-splines.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/splines.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-splines.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/splines.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-splines.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/splines.mo

# stats

%package -n R-stats
Summary:        Package providing R-stats
Requires:       R-base = %{version}

%description -n R-stats
This package provides R-stats, one of R-core packages.

%files -n R-stats
%defattr(-, root, root)

%dir %{_libdir}/R/library/stats/
%license %{_libdir}/R/library/stats/COPYRIGHTS.modreg
%{_libdir}/R/library/stats/demo/
%{_libdir}/R/library/stats/DESCRIPTION
%{_libdir}/R/library/stats/doc/
%{_libdir}/R/library/stats/help/
%{_libdir}/R/library/stats/html/
%{_libdir}/R/library/stats/INDEX
%{_libdir}/R/library/stats/libs/
%{_libdir}/R/library/stats/Meta/
%{_libdir}/R/library/stats/NAMESPACE
%{_libdir}/R/library/stats/R/
%{_libdir}/R/library/stats/SOURCES.ts

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-stats.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/stats.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-stats.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/stats.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-stats.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/stats.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-stats.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/stats.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-stats.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/stats.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-stats.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/stats.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-stats.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/stats.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-stats.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/stats.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-stats.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/stats.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-stats.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/stats.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-stats.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/stats.mo
%lang(tr) %{_libdir}/R/library/translations/tr/LC_MESSAGES/R-stats.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-stats.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/stats.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-stats.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/stats.mo

# stats4
%package -n R-stats4
Summary:        Package providing R-stats4
Requires:       R-base = %{version}

%description -n R-stats4
This package provides R-stats4, one of R-core packages.

%files -n R-stats4
%defattr(-, root, root)

%dir %{_libdir}/R/library/stats4/
%{_libdir}/R/library/stats4/DESCRIPTION
%{_libdir}/R/library/stats4/help/
%{_libdir}/R/library/stats4/html/
%{_libdir}/R/library/stats4/INDEX
%{_libdir}/R/library/stats4/Meta/
%{_libdir}/R/library/stats4/NAMESPACE
%{_libdir}/R/library/stats4/R/

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-stats4.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-stats4.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-stats4.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-stats4.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-stats4.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-stats4.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-stats4.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-stats4.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-stats4.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-stats4.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-stats4.mo
%lang(tr) %{_libdir}/R/library/translations/tr/LC_MESSAGES/R-stats4.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-stats4.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-stats4.mo

# tcltk

%package -n R-tcltk
Summary:        Package providing R-tcltk
Requires:       R-base = %{version}

%description -n R-tcltk
This package provides R-tcltk, one of R-core packages.

%files -n R-tcltk
%defattr(-, root, root)

%dir %{_libdir}/R/library/tcltk/
%{_libdir}/R/library/tcltk/demo/
%{_libdir}/R/library/tcltk/DESCRIPTION
%{_libdir}/R/library/tcltk/exec/
%{_libdir}/R/library/tcltk/help/
%{_libdir}/R/library/tcltk/html/
%{_libdir}/R/library/tcltk/INDEX
%{_libdir}/R/library/tcltk/libs/
%{_libdir}/R/library/tcltk/Meta/
%{_libdir}/R/library/tcltk/NAMESPACE
%{_libdir}/R/library/tcltk/R/

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-tcltk.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/tcltk.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-tcltk.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/tcltk.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-tcltk.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/tcltk.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-tcltk.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/tcltk.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-tcltk.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/tcltk.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-tcltk.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/tcltk.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-tcltk.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/tcltk.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-tcltk.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/tcltk.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-tcltk.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/tcltk.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-tcltk.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/tcltk.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-tcltk.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/tcltk.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-tcltk.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/tcltk.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-tcltk.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/tcltk.mo

# tools
%package -n R-tools
Summary:        Package providing R-tools
Requires:       R-base = %{version}

%description -n R-tools
This package provides R-tools, one of R-core packages.

%files -n R-tools
%defattr(-, root, root)

%dir %{_libdir}/R/library/tools/
%{_libdir}/R/library/tools/DESCRIPTION
%{_libdir}/R/library/tools/help/
%{_libdir}/R/library/tools/html/
%{_libdir}/R/library/tools/INDEX
%{_libdir}/R/library/tools/libs/
%{_libdir}/R/library/tools/Meta/
%{_libdir}/R/library/tools/NAMESPACE
%{_libdir}/R/library/tools/R/

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-tools.mo
%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/tools.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-tools.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/tools.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-tools.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/tools.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-tools.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/tools.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-tools.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/tools.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-tools.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/tools.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-tools.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/tools.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-tools.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/tools.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-tools.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/tools.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-tools.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/tools.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-tools.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/tools.mo
%lang(tr) %{_libdir}/R/library/translations/tr/LC_MESSAGES/R-tools.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-tools.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/tools.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-tools.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/tools.mo

# utils

%package -n R-utils
Summary:        Package providing R-utils
Requires:       R-base = %{version}

%description -n R-utils
This package provides R-utils, one of R-core packages.

%files -n R-utils
%defattr(-, root, root)

%dir %{_libdir}/R/library/utils/
%{_libdir}/R/library/utils/DESCRIPTION
%{_libdir}/R/library/utils/help/
%{_libdir}/R/library/utils/html/
%{_libdir}/R/library/utils/iconvlist
%{_libdir}/R/library/utils/INDEX
%{_libdir}/R/library/utils/libs/
%{_libdir}/R/library/utils/Meta/
%{_libdir}/R/library/utils/misc/
%{_libdir}/R/library/utils/NAMESPACE
%{_libdir}/R/library/utils/R/
%{_libdir}/R/library/utils/Sweave/
%{_libdir}/R/library/utils/doc/

%lang(da) %{_libdir}/R/library/translations/da/LC_MESSAGES/R-utils.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/R-utils.mo
%lang(de) %{_libdir}/R/library/translations/de/LC_MESSAGES/utils.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/R-utils.mo
%lang(en) %{_libdir}/R/library/translations/en@quot/LC_MESSAGES/utils.mo
%lang(fa) %{_libdir}/R/library/translations/fa/LC_MESSAGES/R-utils.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/R-utils.mo
%lang(fr) %{_libdir}/R/library/translations/fr/LC_MESSAGES/utils.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/R-utils.mo
%lang(it) %{_libdir}/R/library/translations/it/LC_MESSAGES/utils.mo
%lang(ja) %{_libdir}/R/library/translations/ja/LC_MESSAGES/R-utils.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/R-utils.mo
%lang(ko) %{_libdir}/R/library/translations/ko/LC_MESSAGES/utils.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/R-utils.mo
%lang(lt) %{_libdir}/R/library/translations/lt/LC_MESSAGES/utils.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/R-utils.mo
%lang(pl) %{_libdir}/R/library/translations/pl/LC_MESSAGES/utils.mo
%lang(pt_BR) %{_libdir}/R/library/translations/pt_BR/LC_MESSAGES/R-utils.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/R-utils.mo
%lang(ru) %{_libdir}/R/library/translations/ru/LC_MESSAGES/utils.mo
%lang(tr) %{_libdir}/R/library/translations/tr/LC_MESSAGES/R-utils.mo
%lang(zh_CN) %{_libdir}/R/library/translations/zh_CN/LC_MESSAGES/R-utils.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/R-utils.mo
%lang(zh_TW) %{_libdir}/R/library/translations/zh_TW/LC_MESSAGES/utils.mo

# Recommended Packages Section

%package -n R-recommended-packages
Summary:        Metapackage, requires all recommended Packages
Version:        %{Rversion}
Release:        %release
Requires:       R-KernSmooth
Requires:       R-MASS
Requires:       R-Matrix
Requires:       R-base
Requires:       R-boot
Requires:       R-class
Requires:       R-cluster
Requires:       R-codetools
Requires:       R-foreign
Requires:       R-lattice
Requires:       R-mgcv
Requires:       R-nlme
Requires:       R-nnet
Requires:       R-rpart
Requires:       R-spatial
Requires:       R-survival

%description -n R-recommended-packages
Metapackage, Requires: all recommended Packages

%files -n R-recommended-packages

%package -n R-boot
Summary:        Package provides recommended R-boot
Version:        1.3.30
Release:        %release
Requires:       R-base

%description -n R-boot
This packages provides R-boot, one of the recommended packages.

%files -n R-boot
%defattr(-, root, root)

%dir %{_libdir}/R/library/boot/
%{_libdir}/R/library/boot/bd.q
%{_libdir}/R/library/boot/CITATION
%{_libdir}/R/library/boot/data/
%{_libdir}/R/library/boot/DESCRIPTION
%{_libdir}/R/library/boot/help/
%{_libdir}/R/library/boot/html/
%{_libdir}/R/library/boot/INDEX
%{_libdir}/R/library/boot/Meta/
%{_libdir}/R/library/boot/NAMESPACE
%dir %{_libdir}/R/library/boot/po/
%lang(de) %{_libdir}/R/library/boot/po/de/
%lang(en) %{_libdir}/R/library/boot/po/en*/
%lang(fr) %{_libdir}/R/library/boot/po/fr/
%lang(fr) %{_libdir}/R/library/boot/po/it/
%lang(ko) %{_libdir}/R/library/boot/po/ko/
%lang(pl) %{_libdir}/R/library/boot/po/pl/
%lang(ru) %{_libdir}/R/library/boot/po/ru/
%{_libdir}/R/library/boot/R/

%package -n R-class
Summary:        Package provides recommended R-class
Version:        7.3.22
Release:        %release
Requires:       R-base

%description -n R-class
This packages provides R-class, one of the recommended packages.

%files -n R-class
%defattr(-, root, root)

%dir %{_libdir}/R/library/class/
%{_libdir}/R/library/class/CITATION
%{_libdir}/R/library/class/DESCRIPTION
%{_libdir}/R/library/class/help/
%{_libdir}/R/library/class/html/
%{_libdir}/R/library/class/INDEX
%{_libdir}/R/library/class/libs/
%{_libdir}/R/library/class/Meta/
%{_libdir}/R/library/class/NAMESPACE
%{_libdir}/R/library/class/NEWS

%dir %{_libdir}/R/library/class/po/
%lang(de) %{_libdir}/R/library/class/po/de/
%lang(en) %{_libdir}/R/library/class/po/en*/
%lang(fr) %{_libdir}/R/library/class/po/fr/
%lang(fr) %{_libdir}/R/library/class/po/it/
%lang(ko) %{_libdir}/R/library/class/po/ko/
%lang(pl) %{_libdir}/R/library/class/po/pl/
%{_libdir}/R/library/class/R/

%package -n R-cluster
Summary:        Package provides recommended R-cluster
Version:        2.1.6
Release:        %release
Requires:       R-base

%description -n R-cluster
This packages provides R-cluster, one of the recommended packages.

%files -n R-cluster
%defattr(-, root, root)

%dir %{_libdir}/R/library/cluster/
%{_libdir}/R/library/cluster/CITATION
%{_libdir}/R/library/cluster/data/
%{_libdir}/R/library/cluster/DESCRIPTION
%{_libdir}/R/library/cluster/help/
%{_libdir}/R/library/cluster/html/
%{_libdir}/R/library/cluster/INDEX
%{_libdir}/R/library/cluster/libs/
%{_libdir}/R/library/cluster/Meta/
%{_libdir}/R/library/cluster/NAMESPACE
%{_libdir}/R/library/cluster/NEWS.Rd
%{_libdir}/R/library/cluster/R/
%{_libdir}/R/library/cluster/test-tools.R
%dir %{_libdir}/R/library/cluster/po/
%lang(de) %{_libdir}/R/library/cluster/po/de/
%lang(en) %{_libdir}/R/library/cluster/po/en*/
%lang(fr) %{_libdir}/R/library/cluster/po/fr/
%lang(ko) %{_libdir}/R/library/cluster/po/it/
%lang(ko) %{_libdir}/R/library/cluster/po/ko/
%lang(ko) %{_libdir}/R/library/cluster/po/lt/
%lang(pl) %{_libdir}/R/library/cluster/po/pl/

%package -n R-codetools
Summary:        Package provides recommended R-codetools
Version:        0.2.20
Release:        %release
Requires:       R-base

%description -n R-codetools
This packages provides R-codetools, one of the recommended packages.

%files -n R-codetools
%defattr(-, root, root)

%dir %{_libdir}/R/library/codetools/
%{_libdir}/R/library/codetools/DESCRIPTION
%{_libdir}/R/library/codetools/help/
%{_libdir}/R/library/codetools/html/
%{_libdir}/R/library/codetools/INDEX
%{_libdir}/R/library/codetools/Meta/
%{_libdir}/R/library/codetools/NAMESPACE
%{_libdir}/R/library/codetools/R/

%package -n R-foreign
Summary:        Package provides recommended R-foreign
Version:        0.8.86
Release:        %release
Requires:       R-base

%description -n R-foreign
This packages provides R-foreign, one of the recommended packages.

%files -n R-foreign
%defattr(-, root, root)

%dir %{_libdir}/R/library/foreign/
%license %{_libdir}/R/library/foreign/COPYRIGHTS
%{_libdir}/R/library/foreign/DESCRIPTION
%{_libdir}/R/library/foreign/files/
%{_libdir}/R/library/foreign/help/
%{_libdir}/R/library/foreign/html/
%{_libdir}/R/library/foreign/INDEX
%{_libdir}/R/library/foreign/libs/
%{_libdir}/R/library/foreign/Meta/
%{_libdir}/R/library/foreign/NAMESPACE
%dir %{_libdir}/R/library/foreign/po/
%lang(de) %{_libdir}/R/library/foreign/po/de/
%lang(en) %{_libdir}/R/library/foreign/po/en*/
%lang(fr) %{_libdir}/R/library/foreign/po/fr/
%lang(fr) %{_libdir}/R/library/foreign/po/it/
%lang(pl) %{_libdir}/R/library/foreign/po/pl/
%{_libdir}/R/library/foreign/R/

%package -n R-KernSmooth
Summary:        Package provides recommended R-KernSmooth
Version:        2.23.24
Release:        %release
Requires:       R-base

%description -n R-KernSmooth
This packages provides R-KernSmooth, one of the recommended packages.

%files -n R-KernSmooth
%defattr(-, root, root)

%dir %{_libdir}/R/library/KernSmooth/
%{_libdir}/R/library/KernSmooth/DESCRIPTION
%{_libdir}/R/library/KernSmooth/help/
%{_libdir}/R/library/KernSmooth/html/
%{_libdir}/R/library/KernSmooth/INDEX
%{_libdir}/R/library/KernSmooth/libs/
%{_libdir}/R/library/KernSmooth/Meta/
%{_libdir}/R/library/KernSmooth/NAMESPACE
%dir %{_libdir}/R/library/KernSmooth/po/
%lang(de) %{_libdir}/R/library/KernSmooth/po/de/
%lang(en) %{_libdir}/R/library/KernSmooth/po/en*/
%lang(fr) %{_libdir}/R/library/KernSmooth/po/fr/
%lang(fr) %{_libdir}/R/library/KernSmooth/po/it/
%lang(pl) %{_libdir}/R/library/KernSmooth/po/pl/
%lang(ko) %{_libdir}/R/library/KernSmooth/po/ko/
%{_libdir}/R/library/KernSmooth/R/

%package -n R-lattice
Summary:        Package provides recommended R-lattice
Version:        0.22.6
Release:        %release
Requires:       R-base

%description -n R-lattice
This packages provides R-lattice, one of the recommended packages.

%files -n R-lattice
%defattr(-, root, root)

%dir %{_libdir}/R/library/lattice/
%{_libdir}/R/library/lattice/CITATION
%{_libdir}/R/library/lattice/data/
%{_libdir}/R/library/lattice/demo/
%{_libdir}/R/library/lattice/doc/
%{_libdir}/R/library/lattice/DESCRIPTION
%{_libdir}/R/library/lattice/help/
%{_libdir}/R/library/lattice/html/
%{_libdir}/R/library/lattice/INDEX
%{_libdir}/R/library/lattice/libs/
%{_libdir}/R/library/lattice/Meta/
%{_libdir}/R/library/lattice/NAMESPACE
%{_libdir}/R/library/lattice/NEWS.md
%dir %{_libdir}/R/library/lattice/po/
%lang(de) %{_libdir}/R/library/lattice/po/de/
%lang(en) %{_libdir}/R/library/lattice/po/en*/
%lang(fr) %{_libdir}/R/library/lattice/po/fr/
%lang(ko) %{_libdir}/R/library/lattice/po/it/
%lang(ko) %{_libdir}/R/library/lattice/po/ko/
%lang(pl) %{_libdir}/R/library/lattice/po/pl/
%{_libdir}/R/library/lattice/R/

%package -n R-MASS
Summary:        Package provides recommended R-MASS
Version:        7.3.60.2
Release:        %release
Requires:       R-base

%description -n R-MASS
This packages provides R-MASS, one of the recommended packages.

%files -n R-MASS
%defattr(-, root, root)

%dir %{_libdir}/R/library/MASS/
%{_libdir}/R/library/MASS/CITATION
%{_libdir}/R/library/MASS/data/
%{_libdir}/R/library/MASS/DESCRIPTION
%{_libdir}/R/library/MASS/help/
%{_libdir}/R/library/MASS/html/
%{_libdir}/R/library/MASS/INDEX
%{_libdir}/R/library/MASS/libs/
%{_libdir}/R/library/MASS/Meta/
%{_libdir}/R/library/MASS/NAMESPACE
%{_libdir}/R/library/MASS/NEWS
%dir %{_libdir}/R/library/MASS/po
%lang(de) %{_libdir}/R/library/MASS/po/de/
%lang(en) %{_libdir}/R/library/MASS/po/en*/
%lang(fr) %{_libdir}/R/library/MASS/po/fr/
%lang(fr) %{_libdir}/R/library/MASS/po/it/
%lang(ko) %{_libdir}/R/library/MASS/po/ko/
%lang(pl) %{_libdir}/R/library/MASS/po/pl/
%{_libdir}/R/library/MASS/R/
%{_libdir}/R/library/MASS/scripts/

%package -n R-Matrix
Summary:        Package provides recommended R-Matrix
Version:        1.7.0
Release:        %release
Requires:       R-base
Obsoletes:      R-Matrix-devel <= 1.3.2
Provides:       R-Matrix-devel
# This is for backwards-compatibility only. Nothing *should*
# (Build)Require R-Matrix-devel

%description -n R-Matrix
This packages provides R-Matrix, one of the recommended packages.

%files -n R-Matrix
%defattr(-, root, root)

%dir %{_libdir}/R/library/Matrix/
%{_libdir}/R/library/Matrix/data/
%{_libdir}/R/library/Matrix/doc/
%{_libdir}/R/library/Matrix/DESCRIPTION
%{_libdir}/R/library/Matrix/external/
%{_libdir}/R/library/Matrix/help/
%{_libdir}/R/library/Matrix/html/
%{_libdir}/R/library/Matrix/INDEX
%{_libdir}/R/library/Matrix/libs/
%license %{_libdir}/R/library/Matrix/LICENCE
%{_libdir}/R/library/Matrix/Meta/
%{_libdir}/R/library/Matrix/NAMESPACE
%{_libdir}/R/library/Matrix/NEWS.Rd
%dir %{_libdir}/R/library/Matrix/po/
%lang(de) %{_libdir}/R/library/Matrix/po/de/
%lang(en) %{_libdir}/R/library/Matrix/po/en*/
%lang(fr) %{_libdir}/R/library/Matrix/po/fr/
%lang(ko) %{_libdir}/R/library/Matrix/po/it/
%lang(ko) %{_libdir}/R/library/Matrix/po/ko/
%lang(ko) %{_libdir}/R/library/Matrix/po/lt/
%lang(pl) %{_libdir}/R/library/Matrix/po/pl/
%{_libdir}/R/library/Matrix/R/
%{_libdir}/R/library/Matrix/test-tools.R
%{_libdir}/R/library/Matrix/test-tools-1.R
%{_libdir}/R/library/Matrix/test-tools-Matrix.R
%dir %{_libdir}/R/library/Matrix/include/
%{_libdir}/R/library/Matrix/include/Matrix.h
%{_libdir}/R/library/Matrix/include/Matrix_stubs.c
%{_libdir}/R/library/Matrix/include/cholmod.h
%dir %{_libdir}/R/library/Matrix/include/Matrix/
%{_libdir}/R/library/Matrix/include/Matrix/Matrix.h
%{_libdir}/R/library/Matrix/include/Matrix/alloca.h
%{_libdir}/R/library/Matrix/include/Matrix/cholmod-utils.h
%{_libdir}/R/library/Matrix/include/Matrix/cholmod.h
%{_libdir}/R/library/Matrix/include/Matrix/remap.h
%{_libdir}/R/library/Matrix/include/Matrix/stubs.c
%{_libdir}/R/library/Matrix/include/Matrix/version.h
%dir %{_libdir}/R/library/Matrix/scripts/
%{_libdir}/R/library/Matrix/scripts/AMD.patch
%{_libdir}/R/library/Matrix/scripts/CAMD.patch
%{_libdir}/R/library/Matrix/scripts/CCOLAMD.patch
%{_libdir}/R/library/Matrix/scripts/CHOLMOD.patch
%{_libdir}/R/library/Matrix/scripts/COLAMD.patch
%{_libdir}/R/library/Matrix/scripts/CXSparse.patch
%{_libdir}/R/library/Matrix/scripts/SuiteSparse_config.patch
%{_libdir}/R/library/Matrix/scripts/api.patch
%{_libdir}/R/library/Matrix/scripts/disclaimer.txt
%{_libdir}/R/library/Matrix/scripts/rules.mk
%{_libdir}/R/library/Matrix/scripts/rules.sh
%{_libdir}/R/library/Matrix/scripts/sources.mk
%{_libdir}/R/library/Matrix/scripts/ssget.sh
%{_libdir}/R/library/Matrix/scripts/wall.patch

%package -n R-mgcv
Summary:        Package provides recommended R-mgcv
Version:        1.9.1
Release:        %release
Requires:       R-base

%description -n R-mgcv
This packages provides R-mgcv, one of the recommended packages.

%files -n R-mgcv
%defattr(-, root, root)

%dir %{_libdir}/R/library/mgcv/
%{_libdir}/R/library/mgcv/CITATION
%{_libdir}/R/library/mgcv/DESCRIPTION
%{_libdir}/R/library/mgcv/help/
%{_libdir}/R/library/mgcv/data
%{_libdir}/R/library/mgcv/html/
%{_libdir}/R/library/mgcv/INDEX
%{_libdir}/R/library/mgcv/libs/
%{_libdir}/R/library/mgcv/Meta/
%{_libdir}/R/library/mgcv/NAMESPACE
%{_libdir}/R/library/mgcv/R/
%dir %{_libdir}/R/library/mgcv/po/
%lang(de) %{_libdir}/R/library/mgcv/po/de/
%lang(en) %{_libdir}/R/library/mgcv/po/en*/
%lang(fr) %{_libdir}/R/library/mgcv/po/fr/
%lang(ko) %{_libdir}/R/library/mgcv/po/ko/
%lang(pl) %{_libdir}/R/library/mgcv/po/pl/

%package -n R-nlme
Summary:        Package provides recommended R-nlme
Version:        3.1.164
Release:        %release
Requires:       R-base

%description -n R-nlme
This packages provides R-nlme, one of the recommended packages.

%files -n R-nlme
%defattr(-, root, root)

%dir %{_libdir}/R/library/nlme/
%{_libdir}/R/library/nlme/CITATION
%{_libdir}/R/library/nlme/data/
%{_libdir}/R/library/nlme/DESCRIPTION
%{_libdir}/R/library/nlme/help/
%{_libdir}/R/library/nlme/html/
%{_libdir}/R/library/nlme/INDEX
%{_libdir}/R/library/nlme/libs/
%{_libdir}/R/library/nlme/Meta/
%{_libdir}/R/library/nlme/mlbook/
%{_libdir}/R/library/nlme/NAMESPACE
%dir %{_libdir}/R/library/nlme/po/
%lang(de) %{_libdir}/R/library/nlme/po/de/
%lang(en) %{_libdir}/R/library/nlme/po/en*/
%lang(fr) %{_libdir}/R/library/nlme/po/fr/
%lang(ko) %{_libdir}/R/library/nlme/po/ko/
%lang(pl) %{_libdir}/R/library/nlme/po/pl/
%{_libdir}/R/library/nlme/R/
%{_libdir}/R/library/nlme/scripts/

%package -n R-nnet
Summary:        Package provides recommended R-nnet
Version:        7.3.19
Release:        %release
Requires:       R-base

%description -n R-nnet
This packages provides R-nnet, one of the recommended packages.

%files -n R-nnet
%defattr(-, root, root)

%dir %{_libdir}/R/library/nnet/
%{_libdir}/R/library/nnet/CITATION
%{_libdir}/R/library/nnet/DESCRIPTION
%{_libdir}/R/library/nnet/help/
%{_libdir}/R/library/nnet/html/
%{_libdir}/R/library/nnet/INDEX
%{_libdir}/R/library/nnet/libs/
%{_libdir}/R/library/nnet/Meta/
%{_libdir}/R/library/nnet/NAMESPACE
%{_libdir}/R/library/nnet/NEWS
%dir %{_libdir}/R/library/nnet/po
%lang(de) %{_libdir}/R/library/nnet/po/de/
%lang(en) %{_libdir}/R/library/nnet/po/en*/
%lang(fr) %{_libdir}/R/library/nnet/po/fr/
%lang(fr) %{_libdir}/R/library/nnet/po/it/
%lang(ko) %{_libdir}/R/library/nnet/po/ko/
%lang(pl) %{_libdir}/R/library/nnet/po/pl/
%{_libdir}/R/library/nnet/R/

%package -n R-rpart
Summary:        Package provides recommended R-rpart
Version:        4.1.23
Release:        %release
Requires:       R-base

%description -n R-rpart
This packages provides R-rpart, one of the recommended packages.

%files -n R-rpart
%defattr(-, root, root)

%dir %{_libdir}/R/library/rpart/
%{_libdir}/R/library/rpart/data/
%{_libdir}/R/library/rpart/doc/
%{_libdir}/R/library/rpart/DESCRIPTION
%{_libdir}/R/library/rpart/help/
%{_libdir}/R/library/rpart/html/
%{_libdir}/R/library/rpart/INDEX
%{_libdir}/R/library/rpart/libs/
%{_libdir}/R/library/rpart/Meta/
%{_libdir}/R/library/rpart/NAMESPACE
%{_libdir}/R/library/rpart/NEWS.Rd
%dir %{_libdir}/R/library/rpart/po
%lang(de) %{_libdir}/R/library/rpart/po/de/
%lang(en) %{_libdir}/R/library/rpart/po/en*/
%lang(fr) %{_libdir}/R/library/rpart/po/fr/
%lang(ko) %{_libdir}/R/library/rpart/po/ko/
%lang(pl) %{_libdir}/R/library/rpart/po/pl/
%lang(ru) %{_libdir}/R/library/rpart/po/ru/
%{_libdir}/R/library/rpart/R/

%package -n R-spatial
Summary:        Package provides recommended R-spatial
Version:        7.3.17
Release:        %release
Requires:       R-base

%description -n R-spatial
This packages provides R-spatial, one of the recommended packages.

%files -n R-spatial
%defattr(-, root, root)

%dir %{_libdir}/R/library/spatial/
%{_libdir}/R/library/spatial/CITATION
%{_libdir}/R/library/spatial/DESCRIPTION
%{_libdir}/R/library/spatial/help/
%{_libdir}/R/library/spatial/html/
%{_libdir}/R/library/spatial/INDEX
%{_libdir}/R/library/spatial/libs/
%{_libdir}/R/library/spatial/Meta/
%{_libdir}/R/library/spatial/NAMESPACE
%{_libdir}/R/library/spatial/NEWS
%dir %{_libdir}/R/library/spatial/po
%lang(de) %{_libdir}/R/library/spatial/po/de/
%lang(en) %{_libdir}/R/library/spatial/po/en*/
%lang(fr) %{_libdir}/R/library/spatial/po/fr/
%lang(fr) %{_libdir}/R/library/spatial/po/it/
%lang(ko) %{_libdir}/R/library/spatial/po/ko/
%lang(pl) %{_libdir}/R/library/spatial/po/pl/
%{_libdir}/R/library/spatial/ppdata/
%{_libdir}/R/library/spatial/PP.files
%{_libdir}/R/library/spatial/R/

%package -n R-survival
Summary:        Package provides recommended R-survival
Version:        3.6.4
Release:        %release
Requires:       R-base

%description -n R-survival
This packages provides R-survival, one of the recommended packages.

%files -n R-survival
%defattr(-, root, root)

%dir %{_libdir}/R/library/survival/
%{_libdir}/R/library/survival/data/
%{_libdir}/R/library/survival/CITATION
%license %{_libdir}/R/library/survival/COPYRIGHTS
%{_libdir}/R/library/survival/doc/
%{_libdir}/R/library/survival/DESCRIPTION
%{_libdir}/R/library/survival/help/
%{_libdir}/R/library/survival/html/
%{_libdir}/R/library/survival/INDEX
%{_libdir}/R/library/survival/libs/
%{_libdir}/R/library/survival/Meta/
%{_libdir}/R/library/survival/NAMESPACE
%{_libdir}/R/library/survival/NEWS.Rd
%{_libdir}/R/library/survival/R/

%changelog
