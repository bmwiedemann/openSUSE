#
# spec file for package transfig
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


Name:           transfig
BuildRequires:  fdupes
BuildRequires:  libjpeg-devel
BuildRequires:  netpbm
BuildRequires:  texlive-latex
%if %suse_version > 1220
BuildRequires:  texlive-amsfonts
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-courier
BuildRequires:  texlive-dvips
BuildRequires:  texlive-epstopdf
BuildRequires:  texlive-pdftex
BuildRequires:  texlive-times
BuildRequires:  tex(beamer.cls)
BuildRequires:  tex(german.sty)
BuildRequires:  tex(multimedia.sty)
BuildRequires:  tex(times.sty)
BuildRequires:  tex(xmpmulti.sty)
%endif
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig(xpm)
#  www.xfig.org is dead
Url:            http://mcj.sourceforge.net/
Provides:       fig2dev
Provides:       transfig.3.2.3d
Requires:       ghostscript-fonts-std
Requires:       ghostscript-library
Requires:       netpbm
Requires:       texlive-epstopdf
Version:        3.2.7a
Release:        0
Summary:        Graphic Converter
#Source:        http://sourceforge.net/projects/mcj/files/fig2dev-%{version}.tar.xz/download#/fig2dev-%{version}.tar.xz
License:        MIT
Group:          Productivity/Graphics/Convertors
Source:         fig2dev-%{version}.tar.xz
Patch0:         transfig-3.2.6.dif
Patch2:         transfig.3.2.5-binderman.dif
Patch3:         transfig.3.2.5d-mediaboxrealnb.dif
Patch4:         transfig-fix-afl.patch
Patch5:         transfig-e0c4b024.patch
Patch6:         transfig-03ea4578.patch
Patch43:        fig2dev-3.2.6-fig2mpdf.patch
Patch44:        fig2dev-3.2.6-fig2mpdf-doc.patch
Patch45:        fig2dev-3.2.6a-RGBFILE.patch
Patch46:        fig2dev-3.2.6a-man-typo.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{expand: %%global _exec_prefix %(type -p pkg-config &>/dev/null && pkg-config --variable prefix x11 || echo /usr/X11R6)}
%if "%_exec_prefix" == "/usr/X11R6"
%global _mandir     %{_exec_prefix}/man
%define _x11data    %{_exec_prefix}/lib/X11
%define _data       $(LIBDIR)
%else
%define _x11data    %{_datadir}/X11
%define _data       $(SHAREDIR)
%endif

%description
TransFig is a set of tools for creating TeX documents with graphics
that are portable in the sense that they can be printed in a wide
variety of environments.

The transfig directory contains the source for the transfig command
which generates a Makefile which translates Fig code to various
graphics description languages using the fig2dev program.  In previous
releases, this command was implemented as a shell script.

Documentation: man transfig



Authors:
--------
    Anthony Starks     <ajs@merck.com>
    George Ferguson    <ferguson@cs.rochester.edu>
    Herbert Bauer      <heb@regent.e-technik.tu-muenchen.de>
    Micah Beck         <supoj@sally.utexas.edu>
    Supoj Sutantavibul <beck@cs.utk.ecu>

%prep
%setup -q -n fig2dev-%{version}
find -type f | xargs -r chmod a-x,go-w
%patch0 -p0 -b .0
%patch2 -p0 -b .bm
%patch3 -p0 -b .mbox
%patch4 -p1 -b .afl
%patch5 -p0 -b .e0c4b024
%patch6 -p0 -b .03ea4578
%patch43 -p2 -b .mpdf
%patch44 -p1 -b .mpdfdoc
%patch45 -p1 -b .p45
%patch46 -p1 -b .p46

%build
CC=gcc
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -w -D_GNU_SOURCE -std=gnu99"
CFLAGS="$CFLAGS -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
export CC CFLAGS
chmod 755 configure
%configure \
    --docdir=%{_defaultdocdir}/%{name} \
    --enable-transfig \
    --enable-scale-pic2t2e
make %{?_smp_mflags} CCOPTIONS="$CFLAGS"

%install
find -name '*.mpdfdoc' -o -name '*.mpdf' | xargs -r rm -vf
make DESTDIR=%{buildroot} install
install -m 0755 fig2mpdf/fig2mpdf %{buildroot}%{_bindir}
install -m 0644 fig2mpdf/fig2mpdf.1 %{buildroot}%{_mandir}/man1/
gzip -9 %{buildroot}%{_mandir}/man1/fig2mpdf.1

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
install -m 0644 [CLNR]* %{buildroot}%{_defaultdocdir}/%{name}
pushd fig2mpdf/doc
    make
    mkdir %{buildroot}%{_defaultdocdir}/%{name}/fig2mpdf
    rm -f overlay-sample-?.pdf 
    rm -f *.aux *.log *.nav *.out *.snm *.toc
    install -m 0644 * %{buildroot}%{_defaultdocdir}/%{name}/fig2mpdf/
popd
pushd transfig/doc
    ../../fig2dev/fig2dev -L latex trans.fig > trans.tex
    pdflatex manual.tex
    pdflatex manual.tex
    pdflatex manual.tex
    install -m 0644 manual.pdf %{buildroot}%{_defaultdocdir}/%{name}/transfig.pdf
popd

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/fig2dev
%{_bindir}/fig2mpdf
%{_bindir}/fig2ps2tex
%{_bindir}/pic2tpic
%{_bindir}/transfig
%{_datadir}/fig2dev/
%doc %{_defaultdocdir}/%{name}
%doc %{_mandir}/man1/*.1*.gz

%changelog
