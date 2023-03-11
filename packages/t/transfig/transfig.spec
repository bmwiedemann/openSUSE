#
# spec file for package transfig
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


Name:           transfig
Version:        3.2.8b
Release:        0
Summary:        Graphic Converter
#  www.xfig.org is dead
URL:            https://mcj.sourceforge.net/
License:        MIT
Group:          Productivity/Graphics/Convertors
#Source:        http://sourceforge.net/projects/mcj/files/fig2dev-%%{version}.tar.xz/download#/fig2dev-%%{version}.tar.xz
Source:         fig2dev-%{version}.tar.xz
Patch0:         transfig-3.2.8.dif
Patch1:         1b09a8.patch
Patch4:         transfig-fix-afl.patch
Patch43:        fig2dev-3.2.6-fig2mpdf.patch
Patch44:        fig2dev-3.2.6-fig2mpdf-doc.patch
Patch45:        fig2dev-3.2.6a-RGBFILE.patch
Patch46:        0001-Make-ModDate-and-CreationDate-in-PDF-reproducible.patch
BuildRequires:  fdupes
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  netpbm
BuildRequires:  sharutils
#!BuildIgnore:  texlive-tex4ht
BuildRequires:  texlive-courier
BuildRequires:  texlive-latex
%if 0%{?suse_version} > 1315
BuildRequires:  texlive-epstopdf
%endif
BuildRequires:  texlive-pdftex
BuildRequires:  texlive-times
BuildRequires:  tex(8r.enc)
BuildRequires:  tex(beamer.cls)
%if 0%{?suse_version} > 1315
BuildRequires:  tex(german.sty)
%endif
BuildRequires:  pkgconfig(xpm)
BuildRequires:  tex(multimedia.sty)
BuildRequires:  tex(times.sty)
BuildRequires:  tex(xmpmulti.sty)
Provides:       fig2dev
Recommends:     ghostscript-fonts-std
Recommends:     ghostscript-library
Requires:       netpbm
Recommends:     texlive-epstopdf
%if 0%{?suse_version} > 1315
Requires:       (texlive-epstopdf if texlive-latex)
%endif

%description
TransFig is a set of tools for creating TeX documents with graphics
that are portable in the sense that they can be printed in a wide
variety of environments.

The transfig directory contains the source for the transfig command
which generates a Makefile which translates Fig code to various
graphics description languages using the fig2dev program.  In previous
releases, this command was implemented as a shell script.

%prep
%setup -q -n fig2dev-%{version}
find -type f -exec chmod a-x,go-w '{}' \;
%patch0 -p0 -b .0
%patch1 -p0 -b .1
%patch4 -p1 -b .afl
%patch43 -p1 -b .mpdf
%patch44 -p1 -b .mpdfdoc
%patch45 -p1 -b .p45
%patch46 -p1 -b .pdfmark

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
%make_build CCOPTIONS="$CFLAGS"

pushd transfig/doc
    ../../fig2dev/fig2dev -L latex trans.fig > trans.tex
    pdflatex -draft manual.tex
    pdflatex -draft manual.tex
    pdflatex manual.tex
popd

pushd  fig2mpdf/doc
%if 0%{?suse_version} > 1315
    make
    while $(grep -q -i 'rerunfilecheck.*warning' sample-presentation.log); do
        pdflatex sample-presentation
    done
%endif
    mkdir htmlimg
    (cd htmlimg; uudecode ../*.uue)
popd

%install
#find -name '*.mpdfdoc' -o -name '*.mpdf' | xargs -r rm -vf
%make_install
install -m 0755 fig2mpdf/fig2mpdf %{buildroot}%{_bindir}
install -m 0644 fig2mpdf/fig2mpdf.1 %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
install -m 0644 [CLNR]* %{buildroot}%{_defaultdocdir}/%{name}
install -m 0644 transfig/doc/manual.pdf %{buildroot}%{_defaultdocdir}/%{name}/transfig.pdf

pushd fig2mpdf/doc
    mkdir %{buildroot}%{_defaultdocdir}/%{name}/fig2mpdf
    install -m 0644 *.{html,css,lfig} %{buildroot}%{_defaultdocdir}/%{name}/fig2mpdf/
    install -m 0644 htmlimg/*.{jpg,gif,pdf} %{buildroot}%{_defaultdocdir}/%{name}/fig2mpdf/
    install -m 0644 sample-presentation.tex Makefile %{buildroot}%{_defaultdocdir}/%{name}/fig2mpdf/
%if 0%{?suse_version} > 1315
    install -m 0644 sample-presentation.pdf %{buildroot}%{_defaultdocdir}/%{name}/fig2mpdf/
%endif
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
