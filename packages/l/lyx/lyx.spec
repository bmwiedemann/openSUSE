#
# spec file for package lyx
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


%if 0%{?suse_version} >= 1600
%bcond_without qt6
%endif

Name:           lyx
Version:        2.4.0
Release:        0
Summary:        WYSIWYM (What You See Is What You Mean) document processor
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Frontends
URL:            http://www.lyx.org/
Source:         http://ftp.lyx.org/pub/lyx/stable/2.4.x/lyx-%{version}.tar.xz
Source1:        lyxrc.dist
Source2:        lyx.keyring
Source3:        http://ftp.lyx.org/pub/lyx/stable/2.4.x/lyx-%{version}.tar.xz.sig
Source4:        README.SUSE
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  enchant-devel
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  fontpackages-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  hunspell-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  mythes-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
%if %{with qt6}
BuildRequires:  qt6-gui-private-devel
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
%else
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
%endif
#!BuildIgnore: lyx
Requires:       %{name}-fonts
Requires:       ImageMagick
Requires:       ghostscript
# Goal is to require/recommends (roughly) everything that is supported in the GUI of LyX
# LyX can supoort everything of LaTeX in the preamble, but not everything is supported in the GUI
# I have ingored extra fonts and document classes
# Use "Recommends" so that expert users can have some control
Recommends:     texlive-algorithms
Recommends:     texlive-arabi
Recommends:     texlive-bezos
Recommends:     texlive-biber
Recommends:     texlive-bibtex8
Recommends:     texlive-bibtopic
Recommends:     texlive-braille
Recommends:     texlive-collection-fontsrecommended
Recommends:     texlive-collection-htmlxml
Recommends:     texlive-collection-latexrecommended
Recommends:     texlive-collection-luatex
Recommends:     texlive-collection-xetex
Recommends:     texlive-covington
Recommends:     texlive-endnotes
Recommends:     texlive-esint
Recommends:     texlive-esint-type1
Recommends:     texlive-fixme
Recommends:     texlive-forest
Recommends:     texlive-fragments
Recommends:     texlive-ifsym
Recommends:     texlive-mathdots
Recommends:     texlive-menukeys
Recommends:     texlive-mhchem
Recommends:     texlive-multirow
Recommends:     texlive-nomencl
Recommends:     texlive-pdfcomment
Recommends:     texlive-pdfsync
Recommends:     texlive-prettyref
Recommends:     texlive-refstyle
Recommends:     texlive-rotfloat
Recommends:     texlive-splitindex
Recommends:     texlive-tablefootnote
Recommends:     texlive-tcolorbox
Recommends:     texlive-textgreek
Recommends:     texlive-todonotes
Recommends:     texlive-units
Recommends:     texlive-wrapfig
Recommends:     texlive-zhmetrics
Recommends:     xindy
# Some stuff needed for LyX's documentation:
Recommends:     texlive-braket
Recommends:     texlive-cprotect
Recommends:     texlive-diagbox
Recommends:     texlive-doublestroke
Recommends:     texlive-picinpar
Recommends:     texlive-shapepar
Recommends:     texlive-sidecap

%description
LyX is a document processor that encourages an approach to writing
based on the structure of your documents, not their appearance. The
author can concentrate on the content (What You See Is What You Mean).
The formatting is done by the backends (like LaTeX) and the output can
have different formats, such as DVI, postscript, PDF, html.

LyX can check the LaTeX installation by opening the LaTeX Configuration
document under "Help" on the menubar.

LyX uses ImageMagick to deal with images. For security reasons
(open)SUSE limits the functionaly of ImageMagick. See README.SUSE
(in /usr/share/doc/packages/lyx/) for more information.

%package fonts
Summary:        Fonts for displaying math
Group:          System/X11/Fonts
BuildArch:      noarch
%reconfigure_fonts_prereq

%description fonts
A collection of Math symbol fonts for LyX.

%prep
%autosetup

%build
TEXMF=%{_datadir}/texmf
%configure \
    --enable-build-type=rel \
    --without-included-boost \
    --without-aspell \
    --with-hunspell \
    --with-enchant \
%if %{with qt6}
    --enable-qt6
%else
    --enable-qt5
%endif
make %{?_smp_mflags}

%install
TEXMF=%{_datadir}/texmf
%make_install TEXMF=$TEXMF
%python3_fix_shebang

# some defaults
install -p -m644 -D %{SOURCE1} %{buildroot}%{_datadir}/lyx/lyxrc.dist

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
pushd %{buildroot}%{_datadir}/lyx/doc/
    for i in *
    do
        ln -s %{_datadir}/lyx/doc/$i \
	      %{buildroot}/%{_defaultdocdir}/%{name}/
    done
popd

cp ANNOUNCE COPYING NEWS \
   README README.localization RELEASE-NOTES UPGRADING %{SOURCE4} \
   %{buildroot}/%{_defaultdocdir}/%{name}/

mkdir -p $RPM_BUILD_ROOT$TEXMF/tex/latex
ln -s %{_datadir}/lyx/tex $RPM_BUILD_ROOT$TEXMF/tex/latex/lyx

# fonts
install -m 0755 -d %{buildroot}%{_fontsdir}/lyx
mv %{buildroot}%{_datadir}/lyx/fonts/*.ttf %{buildroot}%{_fontsdir}/lyx/
rm -rf %{buildroot}%{_datadir}/lyx/fonts

install -p -D -m 0644 lib/scripts/bash_completion %{buildroot}%{_datadir}/bash-completion/completions/lyx

%suse_update_desktop_file lyx Office WordProcessor

%fdupes -s %{buildroot}%{_prefix}

%find_lang %{name}

%reconfigure_fonts_scriptlets -c -n %{name}-fonts

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files -f %{name}.lang
%docdir %{_datadir}/lyx/doc
%doc %{_defaultdocdir}/lyx
%{_bindir}/lyx
%{_bindir}/lyxclient
%{_bindir}/tex2lyx
%{_datadir}/applications/lyx.desktop
%{_datadir}/metainfo/org.lyx.LyX.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/texmf
%dir %{_datadir}/texmf/tex
%dir %{_datadir}/texmf/tex/latex
%{_datadir}/texmf/tex/latex/lyx
%{_datadir}/lyx
%{_mandir}/man1/lyx.1%{?ext_man}
%{_mandir}/man1/lyxclient.1%{?ext_man}
%{_mandir}/man1/tex2lyx.1%{?ext_man}
%{_datadir}/bash-completion/completions/lyx

%files fonts
%dir %{_fontsdir}/lyx
%{_fontsdir}/lyx/*.ttf
%doc lib/fonts/BaKoMaFontLicense.txt

%changelog
