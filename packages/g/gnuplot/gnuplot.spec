#
# spec file
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


#################################################################
###    Please call "./pre_checkin.sh" prior to submitting.    ###
###    (This will regenerate gnuplot-doc.changes)             ###
#################################################################

%global flavor @BUILD_FLAVOR@%{nil}
%global sname gnuplot
%if "%{flavor}" == ""
%else
%global psuffix -%{flavor}
%endif

Name:           gnuplot%{?psuffix}
BuildRequires:  ImageMagick
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  lua-devel
BuildRequires:  netpbm
BuildRequires:  openspecfun-devel
BuildRequires:  pango-devel
BuildRequires:  plotutils-devel
BuildRequires:  readline-devel
BuildRequires:  wxGTK3-devel >= 3
BuildRequires:  zziplib
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libcerf)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(x11)
%if "%{flavor}" == "doc"
BuildRequires:  emacs-nox
BuildRequires:  gnuplot
BuildRequires:  latex2html
BuildRequires:  makeinfo
BuildRequires:  texlive-epstopdf
BuildRequires:  texlive-latex
BuildRequires:  texlive-latexconfig
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-pdftex
BuildRequires:  texlive-tex
BuildRequires:  texlive-tex4ht
BuildRequires:  texlive-texinfo
BuildRequires:  texlive-ucs
BuildRequires:  tex(booktabs.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(gttn1000.tfm)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(imakeidx.sty)
BuildRequires:  tex(lgrcmr.fd)
BuildRequires:  tex(nicefrac.sty)
BuildRequires:  tex(pdftex.def)
BuildRequires:  tex(subfigure.sty)
BuildRequires:  tex(textgreek.sty)
BuildRequires:  tex(upquote.sty)
%endif
URL:            https://www.gnuplot.info/
Version:        6.0.1
Release:        0
%global         underscore 6
%if "%{flavor}" == ""
Summary:        Function Plotting Utility and more
License:        GPL-2.0-or-later AND SUSE-Gnuplot
Group:          Documentation/Other
%else
Summary:        Documentation of GNUplot
License:        GPL-2.0-or-later AND SUSE-Gnuplot
Group:          Documentation/Other
%endif
Source0:        https://downloads.sourceforge.net/project/gnuplot/gnuplot/%{version}/gnuplot-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/project/gnuplot/gnuplot/%{version}/Gnuplot%{underscore}.pdf
Source2:        gnuplot-fr.doc.bz2
Source3:        README.whynot
Source4:        webp_figures.gnu
# https://mirrors.ctan.org/macros/latex209/contrib/picins/picins.sty
# That's a build requirement, not provided by Tex Live
Source5:        picins.sty
# Repair broken texi(nfo) file
Source6:        gnuplot-5.2.0-texi2info.patch
Patch0:         gnuplot-4.6.0.dif
Patch1:         gnuplot-4.4.0-x11ovf.dif
Patch2:         gnuplot-4.6.0-fonts.diff
Patch3:         gnuplot-doc2tex.patch
Patch4:         gnuplot-4.6.0-demo.diff
Patch5:         gnuplot-wx3.diff
Patch6:         gnuplot-QtCore-PIC.dif
Patch7:         gnuplot-PIE.patch
%define _x11lib     %{_libdir}
%define _x11data    %{_datadir}/X11
%define _x11inc     %{_includedir}/X11
%define _appdef     %{_x11data}/app-defaults
%define _gnplttex   tex/latex/gnuplot
%if "%{flavor}" == "doc"
Requires:       %{sname}
Requires(post): %install_info_prereq
Requires(preun):%install_info_prereq
BuildArch:      noarch
%endif

%description
GNUplot is a command line driven interactive function plotting utility.
GNUplot supports many different types of terminals, plotters, and
printers (including many color devices and pseudodevices like LaTeX)
and can easily be extended to include new devices.

%if "%{flavor}" == "doc"
%{sname} documentation files including the info pages.
%endif

%prep
%setup -q -n %{sname}-%{version}
bunzip2 -dc %{_sourcedir}/gnuplot-fr.doc.bz2 > docs/gnuplot-fr.doc
test $? -eq 0 || exit 1
cp %{_sourcedir}/picins.sty docs
%patch -P2 -p0 -b .font
%patch -P3 -p0 -b .overscan
%patch -P4 -p0 -b .demo
%patch -P0 -p1 -b .0
%patch -P1 -p0 -b .x11ovf
%patch -P5 -p1 -b .w3x
%patch -P6 -p0 -b .pic
%patch -P7 -p1 -b .pie

%build
autoreconf -fi

    export  CPPFLAGS="-I%{_includedir}/gd -DAppDefDir=\\\"%{_appdef}\\\""
    export  CPPFLAGS="$CPPFLAGS -DGNUPLOT_LIB_DEFAULT=\\\"%{_docdir}/%{sname}/demo\\\""
    export  CFLAGS="${RPM_OPT_FLAGS} -pipe -D_GNU_SOURCE -fpic"
    export  CXXFLAGS="$CFLAGS -fno-strict-aliasing"
    export  LDFLAGS="-L%{_x11lib} -Wl,--as-needed"
    export  ARCHLIB=%_lib
%if 0%{?suse_version}
%if !0%{?sle_version}
    export  CFLAGS="$CFLAGS -DDIST_CONTACT='https://bugs.opensuse.org/'"
%else
    export  CFLAGS="$CFLAGS -DDIST_CONTACT='https://bugzilla.suse.com/'"
%endif
%endif

%if "%{flavor}" == ""
    mkdir bin
    ln -sf /bin/true bin/dvips
    ln -sf /bin/true bin/emacs
    ln -sf /bin/true bin/kpsewhich
    ln -sf /bin/true bin/texhash
    PATH=${PATH}:${PWD}/bin
%endif

    %configure	\
	--with-x		\
	--x-includes=%{_x11inc}	\
	--x-libraries=%{_x11lib}\
	--with-x-app-defaultdir=%{_appdef}\
	--with-texdir=%{_datadir}/texmf/%{_gnplttex} \
	--with-kpsexpand=%{_bindir}/kpsexpand \
%if "%{flavor}" == "doc"
	--with-latex=yes \
%else
	--with-latex=force \
%endif
	--with-readline=gnu	\
	--enable-history-file	\
	--with-bitmap-terminals	\
	--with-gpic		\
	--with-mif		\
	--enable-x11-mbfonts	\
	--enable-stats		\
	--enable-stable-sort    \
	--enable-polar-grid     \
	--enable-watchpoints    \
	--enable-function-blocks \
	--enable-backward-compatibility \
	--with-gd=yes		\
	--with-caca		\
	--with-tgif		\
	--with-metafont		\
	--with-metapost		\
	--with-regis		\
        --with-amos=%{_libdir}  \
	--with-qt=qt5

%if "%{flavor}" == ""
  make %{?_smp_mflags} UIC=/usr/bin/uic-qt5  MOC=/usr/bin/moc-qt5 RCC=/usr/bin/rcc-qt5 LRELEASE=/usr/bin/lrelease-qt5
%endif

%if "%{flavor}" == "doc"
  mv src/Makefile{,_INACESSIBLE}
  pushd docs/
	cp -p %{S:4} webp_figures.gnu
	make GNUPLOT_EXE=%{_bindir}/gnuplot srcdir=. clean
	make GNUPLOT_EXE=%{_bindir}/gnuplot srcdir=. allterm.h allterm-ja.h
	make GNUPLOT_EXE=%{_bindir}/gnuplot srcdir=. html pdf
	make srcdir=. gnuplot.texi
	patch -p0 < %{S:6}
	make srcdir=. info
	pushd psdoc/
	    make srcdir=. pdf
	popd
  popd
  if test -d tutorial/
  then
     pushd tutorial/
	make srcdir=. clean pdf
     popd
  fi
%endif

%install
    rm -rf %{buildroot}

%if "%{flavor}" == ""
    make DESTDIR=%{buildroot} appdefaultdir=%{_appdef} install
    mkdir -p %{buildroot}/%{_mandir}/ja/man1
    install -m 0644 man/ja/man1/gnuplot.1 %{buildroot}/%{_mandir}/ja/man1/gnuplot.1
%endif

%if "%{flavor}" == "doc"
    mkdir -p %{buildroot}/%{_infodir}
    mkdir -p %{buildroot}/%{_docdir}/gnuplot/doc
    mkdir -p %{buildroot}/%{_docdir}/gnuplot/doc/html
    mkdir -p %{buildroot}/%{_docdir}/gnuplot/demo
    rm  -vf docs/htmldocs/images.{aux,idx,log,out,tex}
    rm  -vf docs/htmldocs/*.pl
    rm  -vf docs/htmldocs/*.aux
    rm  -vf docs/htmldocs/*.sty
    rm  -vf docs/htmldocs/WARNINGS
    rm  -vf docs/htmldocs/VERSION
    rm  -vf docs/figure_*.pdf
    rm  -vf tutorial/eg7.pdf
    rm -rvf demo/html
    install -m 0444 docs/*.info*      %{buildroot}/%{_infodir}/
    install -m 0444 docs/html/*       %{buildroot}/%{_docdir}/gnuplot/doc/html
    install -m 0444 docs/psdoc/*.pdf  %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 docs/psdoc/*.ps   %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 docs/psdoc/*.gpi  %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 docs/psdoc/*.doc  %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 docs/psdoc/README %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 demo/*.*          %{buildroot}/%{_docdir}/gnuplot/demo/
    install -m 0444 README*           %{buildroot}/%{_docdir}/gnuplot/
    install -m 0444 NEWS BUGS	      %{buildroot}/%{_docdir}/gnuplot/
    install -m 0444 %{SOURCE3}        %{buildroot}/%{_docdir}/gnuplot/
    rm -f %{buildroot}/%{_docdir}/gnuplot/demo/Makefile*
    install -m 0444 %{S:1}            %{buildroot}/%{_docdir}/gnuplot/
    %fdupes %{buildroot}/%{_docdir}
%endif

%if "%{flavor}" == "doc"
%post
%install_info --info-dir=.%{_infodir} .%{_infodir}/%{sname}.info.gz

%preun
%install_info_delete --info-dir=.%{_infodir} .%{_infodir}/%{sname}.info.gz
%endif

%if "%{flavor}" == ""
%files
%license Copyright
%{_bindir}/gnuplot
%{_libexecdir}/gnuplot
%{_datadir}/gnuplot
%dir %{_datadir}/texmf
%{_datadir}/texmf/*
%dir %{_appdef}
%{_appdef}/Gnuplot
%doc %{_mandir}/man1/gnuplot.1.gz
%doc %{_mandir}/ja/man1/gnuplot.1.gz
%endif

%if "%{flavor}" == "doc"
%files
%{_docdir}/gnuplot/
%{_infodir}/%{sname}.info.gz
%endif

%changelog
