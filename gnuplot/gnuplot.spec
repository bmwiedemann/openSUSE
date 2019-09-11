#
# spec file for package gnuplot
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


%bcond_without  h3d_gridbox
%if 0%{suse_version} > 1310
%define qtver 5
%else
%define qtver 4
%endif
Name:           gnuplot
BuildRequires:  ImageMagick
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  emacs-nox
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  netpbm
BuildRequires:  pango-devel
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(x11)
%if %qtver >= 5
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
%else
BuildRequires:  libqt4-devel >= 4.5
%endif 
BuildRequires:  fdupes
BuildRequires:  latex2html
BuildRequires:  lua-devel
BuildRequires:  makeinfo
BuildRequires:  plotutils-devel
BuildRequires:  texlive-dvips
BuildRequires:  texlive-epstopdf
BuildRequires:  texlive-latex
BuildRequires:  texlive-latexconfig
BuildRequires:  texlive-tex
BuildRequires:  texlive-tex4ht
BuildRequires:  texlive-texinfo
BuildRequires:  texlive-ucs
BuildRequires:  texlive-ucs
BuildRequires:  zziplib
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libcerf)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(pdftex.def)
BuildRequires:  tex(subfigure.sty)
%if 0%{?suse_version} > 0 && 0%{?suse_version} <= 1310
BuildRequires:  wxWidgets-devel
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires
%else
BuildRequires:  wxWidgets-devel >= 3
%endif
Url:            http://www.gnuplot.info/
Version:        5.2.7
Release:        0
Summary:        Function Plotting Utility and more
License:        SUSE-Gnuplot AND GPL-2.0-or-later
Group:          Productivity/Graphics/Visualization/Graph
Source0:        http://downloads.sourceforge.net/project/gnuplot/gnuplot/%{version}/gnuplot-%{version}.tar.gz
Source2:        gnuplot-fr.doc.bz2
Source3:        README.whynot
# According to the gnuplot 5.0.0 release notes, the emacs .el should now be
# available at https://github.com/rudi/gnuplot-el but it doesn't exist anymore.
# Use the files from the lisp/ directory from gnuplot' CVS just before it was
# removed on 6 March 2014.
Source4:        gnuplot-el.tar.bz2
# http://mirrors.ctan.org/macros/latex209/contrib/picins/picins.sty
# That's a build requirement, not provided by Tex Live
Source5:        picins.sty
# Repair broken texi(nfo) file
Source6:        gnuplot-5.2.0-texi2info.patch
Patch0:         gnuplot-4.6.0.dif
Patch1:         gnuplot-4.4.0-x11ovf.dif
Patch2:         gnuplot-4.6.0-fonts.diff
Patch4:         gnuplot-4.6.0-demo.diff
Patch5:         gnuplot-wx3.diff
Patch6:         gnuplot-QtCore-PIC.dif
Patch7:         gnuplot-gd.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{expand: %%global _exec_prefix %(type -p pkg-config &>/dev/null && pkg-config --variable prefix x11 || echo /usr/X11R6)}
%if "%_exec_prefix" == "/usr/X11R6"
%define _x11lib     %{_exec_prefix}/%{_lib}
%define _x11data    %{_exec_prefix}/lib/X11
%define _libx11     %{_x11data}
%define _x11inc     %{_exec_prefix}/include
%define _appdef     %{_x11data}/app-defaults
%else
%define _x11lib     %{_libdir}
%define _x11data    %{_datadir}/X11
%define _libx11     %{_exec_prefix}/lib/X11
%define _x11inc     %{_includedir}
%define _appdef     %{_x11data}/app-defaults
%endif
%define _gnplttex   tex/latex/gnuplot

%description
GNUplot is a command line driven interactive function plotting utility.
 GNUplot supports many different types of terminals, plotters, and
printers (including many color devices and pseudodevices like LaTeX)
and can easily be extended to include new devices.

%package doc
Summary:        Documentation of GNUplot
Group:          Productivity/Graphics/Visualization/Graph
Requires:       %{name}
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
BuildArch:      noarch

%description doc
GNUplot documentation files including the man and info pages. GNUplot
is a command line driven interactive function plotting utility. 
GNUplot supports many different types of terminals, plotters, and
printers (including many color devices and pseudodevices like LaTeX)
and can easily be extended to include new devices.

%{name} documentation files including the man and info pages

%prep
%setup -qa 4
bunzip2 -dc %{_sourcedir}/gnuplot-fr.doc.bz2 > docs/gnuplot-fr.doc
test $? -eq 0 || exit 1
cp %{_sourcedir}/picins.sty docs
%patch2 -p0 -b .font
%patch4 -p0 -b .demo
%patch0 -p1 -b .0
%patch1 -p0 -b .x11ovf
%patch5 -p1 -b .w3x
%patch6 -p0 -b .pic
%patch7 -p1 -b .gd

%build
autoreconf -fi

    SECSVGA="-DSVGA_IS_SECURE=1"
    export  CPPFLAGS="-I%{_x11inc} -I%{_includedir}/gd -DAppDefDir=\\\"%{_appdef}\\\""
    export  CPPFLAGS="$CPPFLAGS -DGNUPLOT_LIB_DEFAULT=\\\"%{_docdir}/%{name}/demo\\\""
    export  CFLAGS="${RPM_OPT_FLAGS} -pipe ${SECSVGA} -D_GNU_SOURCE"
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
    for f in docs/makefile*; do
	test -e $f || continue
	mv $f $f.bak
    done

    autoreconf -fi
#    sed -i "s;bin/uic;bin/uic-qt5;g" ./configure
#    sed -i "s;bin/moc;bin/moc-qt5;g" ./configure
#    sed -i "s;bin/rcc;bin/rcc-qt5;g" ./configure
#    sed -i "s;bin/lrelease;bin/lrelease-qt5;g" ./configure
#    sed -i "s;UIC=uic;UIC=uic-qt5;g" ./configure
#    sed -i "s;MOC=moc;MOC=moc-qt5;g" ./configure
#    sed -i "s;RCC=rcc;RCC=rcc-qt5;g" ./configure
#    sed -i "s;LRELEASE=lrelease;LRELEASE=lrelease-qt5;g" ./configure

    %configure	\
	--enable-stats		\
	--with-x		\
	--with-x-dcop		\
	--x-includes=%{_x11inc}	\
	--x-libraries=%{_x11lib}\
	--with-x-app-defaultdir=%{_appdef}\
	--with-texdir=/usr/share/texmf/%{_gnplttex} \
	--with-readline=gnu	\
	--enable-history-file	\
	--with-linux-vga	\
	--with-bitmap-terminals	\
	--with-gpic		\
	--with-mif		\
	--enable-x11-mbfonts	\
%if ! %{with h3d_gridbox}
	--enable-h3d-quadtree	\
	--disable-h3d-gridbox	\
%else
	--disable-h3d-quadtree	\
	--enable-h3d-gridbox	\
%endif
	--enable-backwards-compatibility\
	--with-gd=%{_usr}		\
	--without-row-help	\
	--with-kpsexpand	\
	--with-caca		\
	--with-qt=qt%{qtver}

%if %{qtver} >= 5
  make %{?_smp_mflags} UIC=/usr/bin/uic-qt5  MOC=/usr/bin/moc-qt5 RCC=/usr/bin/rcc-qt5 LRELEASE=/usr/bin/lrelease-qt5 
%else
  make %{?_smp_mflags}
%endif

  pushd docs/
	make srcdir=. clean all html pdf
	make srcdir=. gnuplot.texi
	patch -p0 < %{S:6}
	make srcdir=. info
	pushd psdoc/
	    make srcdir=. pdf
	popd
  popd
  pushd tutorial/
	make srcdir=. clean pdf
  popd
  pushd lisp/
        for el_file in gnuplot.el gnuplot-gui.el; do
            emacs -batch -q -no-site-file -l "dot.el" -f batch-byte-compile \
                  "$el_file"
        done
 popd

%install
    rm -rf %{buildroot}
    make DESTDIR=%{buildroot} appdefaultdir=%{_appdef} install
    mkdir -p %{buildroot}/%{_infodir}
    mkdir -p %{buildroot}/%{_mandir}/ja/man1
    mkdir -p %{buildroot}/%{_docdir}/gnuplot/doc
    mkdir -p %{buildroot}/%{_docdir}/gnuplot/doc/html
    mkdir -p %{buildroot}/%{_docdir}/gnuplot/demo
    mkdir -p %{buildroot}/%{_datadir}/emacs/site-lisp
    rm  -vf docs/htmldocs/images.{aux,idx,log,out,tex}
    rm  -vf docs/htmldocs/*.pl
    rm  -vf docs/htmldocs/*.sty
    rm  -vf docs/htmldocs/WARNINGS
    rm  -vf docs/htmldocs/VERSION
    rm -rvf demo/html
    install -m 0444 docs/*.info*      %{buildroot}/%{_infodir}/
    install -m 0444 docs/*.pdf        %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 docs/htmldocs/*   %{buildroot}/%{_docdir}/gnuplot/doc/html
    install -m 0444 docs/psdoc/*.pdf  %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 docs/psdoc/*.ps   %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 docs/psdoc/*.gpi  %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 docs/psdoc/*.doc  %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 docs/psdoc/README %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 tutorial/*.pdf    %{buildroot}/%{_docdir}/gnuplot/doc/
    install -m 0444 demo/*.*          %{buildroot}/%{_docdir}/gnuplot/demo/
    install -m 0444 README*           %{buildroot}/%{_docdir}/gnuplot/
    install -m 0444 Copyright         %{buildroot}/%{_docdir}/gnuplot/
    install -m 0444 VERSION           %{buildroot}/%{_docdir}/gnuplot/
    install -m 0444 NEWS BUGS	      %{buildroot}/%{_docdir}/gnuplot/
    install -m 0444 %{SOURCE3}        %{buildroot}/%{_docdir}/gnuplot/
    install -m 0444 lisp/gnuplot*.el* %{buildroot}/%{_datadir}/emacs/site-lisp/
    mv %{buildroot}/%{_mandir}/man1/gnuplot-ja.1 %{buildroot}/%{_mandir}/ja/man1/gnuplot.1
    rm -f %{buildroot}/%{_docdir}/gnuplot/demo/Makefile*
    %fdupes -s %{buildroot}

%post doc
%install_info --info-dir=.%{_infodir} .%{_infodir}/%{name}.info.gz

%preun doc
%install_info_delete --info-dir=.%{_infodir} .%{_infodir}/%{name}.info.gz

%files
%defattr(-,root,root)
%{_bindir}/gnuplot
%{_libexecdir}/gnuplot
%{_datadir}/gnuplot
%{_datadir}/texmf/%{_gnplttex}/
%{_datadir}/emacs/site-lisp/
%{_appdef}/Gnuplot

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/gnuplot/
%doc %{_infodir}/%{name}.info.gz
%doc %{_mandir}/man1/gnuplot.1.gz
%doc %{_mandir}/ja/man1/gnuplot.1.gz

%changelog
