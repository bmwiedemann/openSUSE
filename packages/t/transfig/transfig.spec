#
# spec file for package transfig
#
# Copyright (c) 2020 SUSE LLC
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
URL:            http://mcj.sourceforge.net/
Provides:       fig2dev
Provides:       transfig.3.2.3d
Requires:       ghostscript-fonts-std
Requires:       ghostscript-library
Requires:       netpbm
Requires:       texlive-epstopdf
Version:        3.2.7b
Release:        0
Summary:        Graphic Converter
#Source:        http://sourceforge.net/projects/mcj/files/fig2dev-%{version}.tar.xz/download#/fig2dev-%{version}.tar.xz
License:        MIT
Group:          Productivity/Graphics/Convertors
Source:         fig2dev-%{version}.tar.xz
Patch0:         transfig-3.2.6.dif
Patch1:         CVE-2019-19555.patch
Patch2:         transfig.3.2.5-binderman.dif
Patch3:         transfig.3.2.5d-mediaboxrealnb.dif
Patch4:         transfig-fix-afl.patch
Patch5:         CVE-2019-19746.patch
Patch6:         c379fe.patch
Patch7:         CVE-2019-19797.patch
Patch8:         00cded.patch
Patch9:         d70e4b.patch
Patch10:        d6a10d.patch
Patch11:        acccc8.patch
Patch12:        e3cee2.patch
Patch13:        421afa.patch
Patch14:        2f8d1a.patch
Patch15:        4d4e1f.patch
Patch16:        3165d8.patch
Patch17:        639c36.patch
Patch18:        100e27.patch
Patch19:        3065eb.patch
Patch20:        ca48cc.patch
Patch43:        fig2dev-3.2.6-fig2mpdf.patch
Patch44:        fig2dev-3.2.6-fig2mpdf-doc.patch
Patch45:        fig2dev-3.2.6a-RGBFILE.patch
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
%patch1 -p0 -b .sec
%patch2 -p0 -b .bm
%patch3 -p0 -b .mbox
%patch4 -p1 -b .afl
%patch5 -p0 -b .sec2
%patch6 -p0 -b .sec3
%patch7 -p0 -b .sec4
%patch8 -p0 -b .sec5
%patch9 -p0 -b .sec6
%patch10 -p0 -b .sec7
%patch11 -p0 -b .sec8
%patch12 -p0 -b .sec9
%patch13 -p0 -b .sec10
%patch14 -p0 -b .sec11
%patch15 -p0 -b .sec12
%patch16 -p0 -b .sec13
%patch17 -p0 -b .sec14
%patch18 -p0 -b .sec15
%patch19 -p0 -b .sec16
%patch20 -p0 -b .sec17
%patch43 -p2 -b .mpdf
%patch44 -p1 -b .mpdfdoc
%patch45 -p1 -b .p45

%build
ulimit -v unlimited || :
  #
  # Used for detection of hardening options of gcc and linker
  #
  cflags ()
  {
      local flag=$1; shift
      local var=$1; shift
      test -n "${flag}" -a -n "${var}" || return
      case "${!var}" in
      *${flag}*) return
      esac
      case "$flag" in
      -Wl,*)
	   set -o noclobber
	   echo 'int main () { return 0; }' > ldtest.c
	   if ${CC:-gcc} -Werror $flag -o /dev/null -xc ldtest.c > /dev/null 2>&1 ; then
	       eval $var=\${$var:+\$$var\ }$flag
	   fi
	   set +o noclobber
	   rm -f ldtest.c
	   ;;
      *)
	   if ${CC:-gcc} -Werror $flag -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
	       eval $var=\${$var:+\$$var\ }$flag
	   fi
	   if ${CXX:-g++} -Werror $flag -S -o /dev/null -xc++ /dev/null > /dev/null 2>&1 ; then
	       eval $var=\${$var:+\$$var\ }$flag
	   fi
      esac
  }

CC=gcc
CFLAGS="%{optflags} -fno-strict-aliasing -w -D_GNU_SOURCE -std=gnu99 $(getconf LFS_CFLAGS)"
cflags -D_FORTIFY_SOURCE=2       CFLAGS
cflags -fstack-protector         CFLAGS
cflags -fstack-protector-strong  CFLAGS
cflags -fstack-protector-all     CFLAGS
cflags -Wformat                  CFLAGS
cflags -Wformat-security         CFLAGS
cflags -Werror=format-security   CFLAGS
cflags -fPIE                     CFLAGS
cflags -pie                      LDFLAGS
cflags -Wl,-z,relro              LDFLAGS
cflags -Wl,-z,now                LDFLAGS
export CC CFLAGS LDFLAGS
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
