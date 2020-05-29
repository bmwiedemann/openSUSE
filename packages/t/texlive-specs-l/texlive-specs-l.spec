#
# spec file for package texlive-specs-l
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


%bcond_with	zypper_posttrans

%define texlive_version  2020
%define texlive_previous 2019
%define texlive_release  20200327
%define texlive_noarch   176

#!BuildIgnore:          texlive
#!BuildIgnore:          texlive-scripts
#!BuildIgnore:          texlive-scripts-extra
#!BuildIgnore:          texlive-scripts-bin
#!BuildIgnore:          texlive-scripts-extra-bin
#!BuildIgnore:          texlive-gsftopk
#!BuildIgnore:          texlive-gsftopk-bin
#!BuildIgnore:          texlive-kpathsea
#!BuildIgnore:          texlive-kpathsea-bin

%global _varlib         %{_localstatedir}/lib
%global _libexecdir     %{_prefix}/lib

%define _texmfdistdir   %{_datadir}/texmf
%if 0%{texlive_version} >= 2013
%define _texmfmaindir   %{_texmfdistdir}
%define _texmfdirs      %{_texmfdistdir}
%else
%define _texmfmaindir   %{_libexecdir}/texmf
%define _texmfdirs      \{%{_texmfdistdir},%{_texmfmaindir}\}
%endif

%define _texmfconfdir   %{_sysconfdir}/texmf
%define _texmfvardir    %{_varlib}/texmf
%define _texmfcache     %{_localstatedir}/cache/texmf
%define _fontcache      %{_texmfcache}/fonts
#
%define _x11bin         %{_prefix}/bin
%define _x11lib         %{_libdir}
%define _x11data        %{_datadir}/X11
%define _x11inc         %{_includedir}
%define _appdefdir      %{_x11data}/app-defaults

Name:           texlive-specs-l
Version:        2020
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for l
License:        GFDL-1.2 and GPL-2.0+ and LGPL-2.1+ and LPPL-1.0 and OFL-1.1 and SUSE-Public-Domain and SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Source0:        texlive-specs-l-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-hrlatex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.23svn18020
Release:        0
Summary:        LaTeX support for Croatian documents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hrlatex-doc >= %{texlive_version}
Provides:       tex(fsbispit.cls)
Provides:       tex(fsbmath.sty)
Provides:       tex(hrlatex.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amsopn.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(babel.sty)
Requires:       tex(calc.sty)
Requires:       tex(cancel.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(framed.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(multicol.sty)
Requires:       tex(optional.sty)
Requires:       tex(paralist.sty)
Requires:       tex(txfonts.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source1:        hrlatex.tar.xz
Source2:        hrlatex.doc.tar.xz

%description -n texlive-hrlatex
This package simplifies creation of new documents for the
(average) Croatian user. As an example, a class file hrdipl.cls
(designed for the graduation thesis at the University of
Zagreb) and sample thesis documents are included.

%package -n texlive-hrlatex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.23svn18020
Release:        0
Summary:        Documentation for texlive-hrlatex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hrlatex-doc:hr)

%description -n texlive-hrlatex-doc
This package includes the documentation for texlive-hrlatex

%post -n texlive-hrlatex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hrlatex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hrlatex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hrlatex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hrlatex/README
%{_texmfdistdir}/doc/latex/hrlatex/hrlatex.pdf
%{_texmfdistdir}/doc/latex/hrlatex/sample.fsbispit.tex
%{_texmfdistdir}/doc/latex/hrlatex/sample.minimal.cp1250.tex
%{_texmfdistdir}/doc/latex/hrlatex/sample.minimal.latin2.tex
%{_texmfdistdir}/doc/latex/hrlatex/sample.minimal.utf8.tex
%{_texmfdistdir}/doc/latex/hrlatex/sample.prezentacija.tex

%files -n texlive-hrlatex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hrlatex/fsbispit.cls
%{_texmfdistdir}/tex/latex/hrlatex/fsbmath.sty
%{_texmfdistdir}/tex/latex/hrlatex/hrlatex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hrlatex-%{texlive_version}.%{texlive_noarch}.0.0.23svn18020-%{release}-zypper
%endif

%package -n texlive-hu-berlin-bundle
Version:        %{texlive_version}.%{texlive_noarch}.1.0.4svn54512
Release:        0
Summary:        LaTeX classes for the Humboldt-Universitat zu Berlin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hu-berlin-bundle-doc >= %{texlive_version}
Provides:       tex(hu-berlin-base.sty)
Provides:       tex(hu-berlin-bundle-style.sty)
Provides:       tex(hu-berlin-letter.cls)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(calc.sty)
Requires:       tex(ccicons.sty)
Requires:       tex(dirtree.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(hyperxmp.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(libertine.sty)
Requires:       tex(listings.sty)
Requires:       tex(luatex85.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(markdown.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(microtype.sty)
Requires:       tex(newfile.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source3:        hu-berlin-bundle.tar.xz
Source4:        hu-berlin-bundle.doc.tar.xz

%description -n texlive-hu-berlin-bundle
This package provides files according to the corporate design
of the Humboldt-Universitat zu Berlin. This is not an official
package by the university itself, and not officially approved
by it. More information can be found in the Humboldt
University's corporate design guideline and on the website
https://www.hu-berlin.de/de/hu-intern/design. At present, the
bundle contains a letter class based on scrlttr2 and a package
hu-berlin-base.sty which contains all relevant code for
documents and documentclasses of the bundle.

%package -n texlive-hu-berlin-bundle-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.4svn54512
Release:        0
Summary:        Documentation for texlive-hu-berlin-bundle
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hu-berlin-bundle-doc
This package includes the documentation for texlive-hu-berlin-bundle

%post -n texlive-hu-berlin-bundle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hu-berlin-bundle 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hu-berlin-bundle
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hu-berlin-bundle-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/README.md
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/_markdown_hu-berlin-bundle/5743ba341396e7047e5a76bfb9c28dcd.md.tex
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/hu-berlin-bundle-bibliography.bib
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/hu-berlin-bundle.markdown.in
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/hu-berlin-bundle.pdf
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/hu-berlin-bundle.pkglist
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/hu-berlin-letter-example-lualatex.tex
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/hu-berlin-letter-example-markdown.md
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/hu-berlin-letter-example.lco
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/hu-berlin-letter-template.latex
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/img/hu-berlin-logo.jpg
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/img/texografie.png
%{_texmfdistdir}/doc/latex/hu-berlin-bundle/makefile

%files -n texlive-hu-berlin-bundle
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hu-berlin-bundle/hu-berlin-base.sty
%{_texmfdistdir}/tex/latex/hu-berlin-bundle/hu-berlin-bundle-style.sty
%{_texmfdistdir}/tex/latex/hu-berlin-bundle/hu-berlin-letter.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hu-berlin-bundle-%{texlive_version}.%{texlive_noarch}.1.0.4svn54512-%{release}-zypper
%endif

%package -n texlive-hulipsum
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn46803
Release:        0
Summary:        Hungarian dummy text (Lorum ipse)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hulipsum-doc >= %{texlive_version}
Provides:       tex(hulipsum.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source5:        hulipsum.tar.xz
Source6:        hulipsum.doc.tar.xz

%description -n texlive-hulipsum
Lorem ipsum is an improper Latin filler dummy text, cf. the
lipsum package. It is commonly used for demonstrating the
textual elements of a document template. Lorum ipse is a
Hungarian variation of Lorem ipsum. (Lorum is a Hungarian card
game, and ipse is a Hungarian slang word meaning bloke.) With
this package you can typeset 150 paragraphs of Lorum ipse. All
paragraphs are taken with permission from
http://www.lorumipse.hu. Thanks to Lorum Ipse Lab (Viktor Nagy
and David Takacs) for their work.

%package -n texlive-hulipsum-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn46803
Release:        0
Summary:        Documentation for texlive-hulipsum
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hulipsum-doc
This package includes the documentation for texlive-hulipsum

%post -n texlive-hulipsum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hulipsum 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hulipsum
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hulipsum-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hulipsum/README
%{_texmfdistdir}/doc/latex/hulipsum/hulipsum.pdf

%files -n texlive-hulipsum
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hulipsum/hulipsum.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hulipsum-%{texlive_version}.%{texlive_noarch}.1.0svn46803-%{release}-zypper
%endif

%package -n texlive-hustthesis
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn42547
Release:        0
Summary:        Unofficial thesis template for Huazhong University
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hustthesis-doc >= %{texlive_version}
Provides:       tex(hustthesis.cls)
Requires:       tex(afterpage.sty)
Requires:       tex(algorithm2e.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(appendix.sty)
Requires:       tex(array.sty)
Requires:       tex(book.cls)
Requires:       tex(caption.sty)
Requires:       tex(color.sty)
Requires:       tex(datenumber.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fancynum.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(listings.sty)
Requires:       tex(ltxtable.sty)
Requires:       tex(luatexja-fontspec.sty)
Requires:       tex(multirow.sty)
Requires:       tex(natbib.sty)
Requires:       tex(ntheorem.sty)
Requires:       tex(overpic.sty)
Requires:       tex(perpage.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(tocvsec2.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xeCJK.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Requires:       tex(xunicode.sty)
Requires:       tex(zhnumber.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source7:        hustthesis.tar.xz
Source8:        hustthesis.doc.tar.xz

%description -n texlive-hustthesis
The package provides an Unofficial Thesis Template in LaTeX for
Huazhong University of Science and Technology.

%package -n texlive-hustthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn42547
Release:        0
Summary:        Documentation for texlive-hustthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hustthesis-doc
This package includes the documentation for texlive-hustthesis

%post -n texlive-hustthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hustthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hustthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hustthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hustthesis/README.md
%{_texmfdistdir}/doc/latex/hustthesis/fig-example.pdf
%{_texmfdistdir}/doc/latex/hustthesis/hustthesis-en-example.pdf
%{_texmfdistdir}/doc/latex/hustthesis/hustthesis-zh-example.pdf
%{_texmfdistdir}/doc/latex/hustthesis/hustthesis.pdf
%{_texmfdistdir}/doc/latex/hustthesis/ref-example.bib

%files -n texlive-hustthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/hustthesis/hustthesis.bst
%{_texmfdistdir}/tex/latex/hustthesis/hust-title.eps
%{_texmfdistdir}/tex/latex/hustthesis/hust-title.pdf
%{_texmfdistdir}/tex/latex/hustthesis/hustthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hustthesis-%{texlive_version}.%{texlive_noarch}.1.4svn42547-%{release}-zypper
%endif

%package -n texlive-hvfloat
Version:        %{texlive_version}.%{texlive_noarch}.2.16svn52010
Release:        0
Summary:        Rotating caption and object of floats independently
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hvfloat-doc >= %{texlive_version}
Provides:       tex(hvfloat-fps.sty)
Provides:       tex(hvfloat.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(caption.sty)
Requires:       tex(expl3.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifoddpage.sty)
Requires:       tex(multido.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source9:        hvfloat.tar.xz
Source10:       hvfloat.doc.tar.xz

%description -n texlive-hvfloat
This package defines a macro to place objects (tables and
figures) and their captions in different positions with
different rotating angles within a float. All objects and
captions can be framed. The main command is \hvFloat{float
type}{floating object}{caption}{label}; a simple example is
\hvFloat{figure}{\includegraphics{rose}}{Caption}{fig:0}.
Options are provided to place captions to the right or left,
and rotated. Setting nonFloat=true results in placing the float
here.

%package -n texlive-hvfloat-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.16svn52010
Release:        0
Summary:        Documentation for texlive-hvfloat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hvfloat-doc
This package includes the documentation for texlive-hvfloat

%post -n texlive-hvfloat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hvfloat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hvfloat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hvfloat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hvfloat/CTAN.png
%{_texmfdistdir}/doc/latex/hvfloat/Changes
%{_texmfdistdir}/doc/latex/hvfloat/README
%{_texmfdistdir}/doc/latex/hvfloat/README.exa
%{_texmfdistdir}/doc/latex/hvfloat/after1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/after1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/after2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/after2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/default1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/default1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/default1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/default1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/default2s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/default2s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/default2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/default2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/even1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/even1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/even1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/even1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/even2s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/even2s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/even2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/even2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/frose.png
%{_texmfdistdir}/doc/latex/hvfloat/fullpage1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/fullpage1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/hvfloat.pdf
%{_texmfdistdir}/doc/latex/hvfloat/hvfloat.tex
%{_texmfdistdir}/doc/latex/hvfloat/inner1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/inner1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/inner2s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/inner2s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/inner2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/inner2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/left2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/left2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/multi-after1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/multi-after1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/multi-default1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/multi-default1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/multi-default1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/multi-default1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/multi-default2s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/multi-default2s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/multi-default2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/multi-default2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/multi-inner2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/multi-inner2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/multi-outer2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/multi-outer2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/multi-right1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/multi-right1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/odd1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/odd1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/odd1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/odd1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/odd2s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/odd2s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/odd2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/odd2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/outer1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/outer1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/outer2s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/outer2s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/outer2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/outer2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/paper-after1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/paper-after1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/paper-default1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/paper-default1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/paper-default1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/paper-default1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/paper-default2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/paper-default2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/paper-inner2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/paper-inner2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/paper-right1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/paper-right1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/preamble.ltx
%{_texmfdistdir}/doc/latex/hvfloat/right1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/right1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/right1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/right1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/right2s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/right2s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/right2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/right2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/rose.png
%{_texmfdistdir}/doc/latex/hvfloat/runAll.sh
%{_texmfdistdir}/doc/latex/hvfloat/runEXA.sh
%{_texmfdistdir}/doc/latex/hvfloat/sub-after1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/sub-after1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/sub-after2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/sub-after2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/sub-default1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/sub-default1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/sub-default1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/sub-default1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/sub-default2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/sub-default2s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/sub-right1s1c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/sub-right1s1c.tex
%{_texmfdistdir}/doc/latex/hvfloat/sub-right1s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/sub-right1s2c.tex
%{_texmfdistdir}/doc/latex/hvfloat/sub-right2s2c.pdf
%{_texmfdistdir}/doc/latex/hvfloat/sub-right2s2c.tex

%files -n texlive-hvfloat
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hvfloat/hvfloat-fps.sty
%{_texmfdistdir}/tex/latex/hvfloat/hvfloat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hvfloat-%{texlive_version}.%{texlive_noarch}.2.16svn52010-%{release}-zypper
%endif

%package -n texlive-hvindex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.04svn46051
Release:        0
Summary:        Support for indexing
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hvindex-doc >= %{texlive_version}
Provides:       tex(hvindex.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source11:       hvindex.tar.xz
Source12:       hvindex.doc.tar.xz

%description -n texlive-hvindex
The package simplifies the indexing of words using the \index
command of makeidx. With the package, to index a word in a
text, you only have to type it once; the package makes sure it
is both typeset and indexed.

%package -n texlive-hvindex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.04svn46051
Release:        0
Summary:        Documentation for texlive-hvindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hvindex-doc
This package includes the documentation for texlive-hvindex

%post -n texlive-hvindex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hvindex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hvindex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hvindex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hvindex/Changes
%{_texmfdistdir}/doc/latex/hvindex/README
%{_texmfdistdir}/doc/latex/hvindex/hvindex-doc.pdf
%{_texmfdistdir}/doc/latex/hvindex/hvindex-doc.tex

%files -n texlive-hvindex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hvindex/hvindex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hvindex-%{texlive_version}.%{texlive_noarch}.0.0.04svn46051-%{release}-zypper
%endif

%package -n texlive-hvqrurl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01asvn52993
Release:        0
Summary:        Insert a QR code in the margin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hvqrurl-doc >= %{texlive_version}
Provides:       tex(hvqrurl.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(qrcode.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source13:       hvqrurl.tar.xz
Source14:       hvqrurl.doc.tar.xz

%description -n texlive-hvqrurl
This package allows to draw an URL as a QR code into the margin
of a one- or twosided document. The following packages are
loaded by default: qrcode, marginnote, url, xcolor and xkeyval.

%package -n texlive-hvqrurl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01asvn52993
Release:        0
Summary:        Documentation for texlive-hvqrurl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hvqrurl-doc
This package includes the documentation for texlive-hvqrurl

%post -n texlive-hvqrurl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hvqrurl 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hvqrurl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hvqrurl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hvqrurl/Changes
%{_texmfdistdir}/doc/latex/hvqrurl/README
%{_texmfdistdir}/doc/latex/hvqrurl/hvqrurl.pdf
%{_texmfdistdir}/doc/latex/hvqrurl/hvqrurl.tex

%files -n texlive-hvqrurl
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hvqrurl/hvqrurl.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hvqrurl-%{texlive_version}.%{texlive_noarch}.0.0.01asvn52993-%{release}-zypper
%endif

%package -n texlive-hycolor
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn53584
Release:        0
Summary:        Implements colour for packages hyperref and bookmark
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hycolor-doc >= %{texlive_version}
Provides:       tex(hycolor.sty)
Provides:       tex(xcolor-patch.sty)
Requires:       tex(hopatch.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source15:       hycolor.tar.xz
Source16:       hycolor.doc.tar.xz

%description -n texlive-hycolor
This package provides the code for the color option that is
used by packages hyperref and bookmark. It is not intended as
package for the user.

%package -n texlive-hycolor-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn53584
Release:        0
Summary:        Documentation for texlive-hycolor
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hycolor-doc:en)

%description -n texlive-hycolor-doc
This package includes the documentation for texlive-hycolor

%post -n texlive-hycolor
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hycolor 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hycolor
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hycolor-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hycolor/README.md
%{_texmfdistdir}/doc/latex/hycolor/hycolor.pdf

%files -n texlive-hycolor
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hycolor/hycolor.sty
%{_texmfdistdir}/tex/latex/hycolor/xcolor-patch.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hycolor-%{texlive_version}.%{texlive_noarch}.1.10svn53584-%{release}-zypper
%endif

%package -n texlive-hypdvips
Version:        %{texlive_version}.%{texlive_noarch}.3.03svn53197
Release:        0
Summary:        Hyperref extensions for use with dvips
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hypdvips-doc >= %{texlive_version}
Provides:       tex(hypdvips.sty)
Requires:       tex(atveryend.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(hypcap.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source17:       hypdvips.tar.xz
Source18:       hypdvips.doc.tar.xz

%description -n texlive-hypdvips
The hypdvips package fixes some problems when using hyperref
with dvips. It also adds support for breaking links, file
attachments, embedded documents and different types of
GoTo-links. The cooperation of hyperref with cleveref is
improved, which in addition allows an enhanced back-referencing
system.

%package -n texlive-hypdvips-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.03svn53197
Release:        0
Summary:        Documentation for texlive-hypdvips
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hypdvips-doc
This package includes the documentation for texlive-hypdvips

%post -n texlive-hypdvips
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hypdvips 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hypdvips
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hypdvips-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hypdvips/README
%{_texmfdistdir}/doc/latex/hypdvips/hypdvips.pdf
%{_texmfdistdir}/doc/latex/hypdvips/images/example1.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/example2.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/example3.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/example4.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/example5.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/example6.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/example7.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/graph.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/icon_draft.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/ids.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/logfile.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/openmsg_six.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/openmsg_sixinbrowser.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/paperclip.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/pushpin.eps
%{_texmfdistdir}/doc/latex/hypdvips/images/tag.eps
%{_texmfdistdir}/doc/latex/hypdvips/manifest.txt

%files -n texlive-hypdvips
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hypdvips/hypdvips.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hypdvips-%{texlive_version}.%{texlive_noarch}.3.03svn53197-%{release}-zypper
%endif

%package -n texlive-hyper
Version:        %{texlive_version}.%{texlive_noarch}.4.2dsvn17357
Release:        0
Summary:        Hypertext cross referencing
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyper-doc >= %{texlive_version}
Provides:       tex(hxt-bc.sty)
Provides:       tex(hyper.sty)
Requires:       tex(color.sty)
Requires:       tex(defpattern.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source19:       hyper.tar.xz
Source20:       hyper.doc.tar.xz

%description -n texlive-hyper
Redefines LaTeX cross-referencing commands to insert \special
commands for HyperTeX dvi viewers, such as recent versions of
xdvi. The package is now largely superseded by hyperref.

%package -n texlive-hyper-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.2dsvn17357
Release:        0
Summary:        Documentation for texlive-hyper
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hyper-doc
This package includes the documentation for texlive-hyper

%post -n texlive-hyper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hyper 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hyper
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyper-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hyper/README
%{_texmfdistdir}/doc/latex/hyper/TODO
%{_texmfdistdir}/doc/latex/hyper/contrib/README
%{_texmfdistdir}/doc/latex/hyper/contrib/harvard-to.hyp
%{_texmfdistdir}/doc/latex/hyper/defpattern.sty
%{_texmfdistdir}/doc/latex/hyper/hyper.pdf
%{_texmfdistdir}/doc/latex/hyper/scontrib/README
%{_texmfdistdir}/doc/latex/hyper/scontrib/harvard.hyp

%files -n texlive-hyper
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hyper/amsart.hyp
%{_texmfdistdir}/tex/latex/hyper/amsbook.hyp
%{_texmfdistdir}/tex/latex/hyper/amsdtx.hyp
%{_texmfdistdir}/tex/latex/hyper/amsldoc.hyp
%{_texmfdistdir}/tex/latex/hyper/amsmath.hyp
%{_texmfdistdir}/tex/latex/hyper/amsproc.hyp
%{_texmfdistdir}/tex/latex/hyper/amstex.hyp
%{_texmfdistdir}/tex/latex/hyper/amsthm.hyp
%{_texmfdistdir}/tex/latex/hyper/article.hyp
%{_texmfdistdir}/tex/latex/hyper/book.hyp
%{_texmfdistdir}/tex/latex/hyper/cweb.hyp
%{_texmfdistdir}/tex/latex/hyper/doc.hyp
%{_texmfdistdir}/tex/latex/hyper/fancyheadings.hyp
%{_texmfdistdir}/tex/latex/hyper/ftnright.hyp
%{_texmfdistdir}/tex/latex/hyper/hxt-bc.sty
%{_texmfdistdir}/tex/latex/hyper/hyper.sty
%{_texmfdistdir}/tex/latex/hyper/leqno.hyp
%{_texmfdistdir}/tex/latex/hyper/letter.hyp
%{_texmfdistdir}/tex/latex/hyper/longtable.hyp
%{_texmfdistdir}/tex/latex/hyper/ltnews.hyp
%{_texmfdistdir}/tex/latex/hyper/ltxdoc.hyp
%{_texmfdistdir}/tex/latex/hyper/ltxguide.hyp
%{_texmfdistdir}/tex/latex/hyper/natbib.hyp
%{_texmfdistdir}/tex/latex/hyper/proc.hyp
%{_texmfdistdir}/tex/latex/hyper/report.hyp
%{_texmfdistdir}/tex/latex/hyper/slides.hyp
%{_texmfdistdir}/tex/latex/hyper/subeqnarray.hyp
%{_texmfdistdir}/tex/latex/hyper/theorem.hyp
%{_texmfdistdir}/tex/latex/hyper/upref.hyp
%{_texmfdistdir}/tex/latex/hyper/xr.hyp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyper-%{texlive_version}.%{texlive_noarch}.4.2dsvn17357-%{release}-zypper
%endif

%package -n texlive-hyperbar
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn48147
Release:        0
Summary:        Add interactive Barcode fields to PDF forms
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyperbar-doc >= %{texlive_version}
Provides:       tex(hyperbar.sty)
Requires:       tex(hyperref.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source21:       hyperbar.tar.xz
Source22:       hyperbar.doc.tar.xz

%description -n texlive-hyperbar
The package extends the hyperref functionality for creating
interactive forms to allow adding Barcode form fields supported
by some modern PDF readers. Currently, only pdfTeX is
supported.

%package -n texlive-hyperbar-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn48147
Release:        0
Summary:        Documentation for texlive-hyperbar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hyperbar-doc
This package includes the documentation for texlive-hyperbar

%post -n texlive-hyperbar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hyperbar 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hyperbar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyperbar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hyperbar/README.md
%{_texmfdistdir}/doc/latex/hyperbar/example.pdf
%{_texmfdistdir}/doc/latex/hyperbar/example.tex
%{_texmfdistdir}/doc/latex/hyperbar/hyperbar.pdf

%files -n texlive-hyperbar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hyperbar/hyperbar.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyperbar-%{texlive_version}.%{texlive_noarch}.0.0.1svn48147-%{release}-zypper
%endif

%package -n texlive-hypernat
Version:        %{texlive_version}.%{texlive_noarch}.1.0bsvn17358
Release:        0
Summary:        Allow hyperref and natbib to work together
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hypernat-doc >= %{texlive_version}
Provides:       tex(hypernat.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source23:       hypernat.tar.xz
Source24:       hypernat.doc.tar.xz

%description -n texlive-hypernat
Allows hyperref package and the natbib package with options
'numbers' and 'sort&compress' to work together. This means that
multiple sequential citations (e.g [3,2,1]) will be compressed
to [1-3], where the '1' and the '3' are (color-)linked to the
bibliography.

%package -n texlive-hypernat-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0bsvn17358
Release:        0
Summary:        Documentation for texlive-hypernat
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hypernat-doc
This package includes the documentation for texlive-hypernat

%post -n texlive-hypernat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hypernat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hypernat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hypernat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hypernat/hypernat.pdf
%{_texmfdistdir}/doc/latex/hypernat/hypernat.tex

%files -n texlive-hypernat
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hypernat/hypernat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hypernat-%{texlive_version}.%{texlive_noarch}.1.0bsvn17358-%{release}-zypper
%endif

%package -n texlive-hyperref
Version:        %{texlive_version}.%{texlive_noarch}.7.00dsvn53837
Release:        0
Summary:        Extensive support for hypertext in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-atbegshi >= %{texlive_version}
#!BuildIgnore: texlive-atbegshi
Requires:       texlive-bitset >= %{texlive_version}
#!BuildIgnore: texlive-bitset
Requires:       texlive-etexcmds >= %{texlive_version}
#!BuildIgnore: texlive-etexcmds
Requires:       texlive-gettitlestring >= %{texlive_version}
#!BuildIgnore: texlive-gettitlestring
Requires:       texlive-intcalc >= %{texlive_version}
#!BuildIgnore: texlive-intcalc
Requires:       texlive-kvdefinekeys >= %{texlive_version}
#!BuildIgnore: texlive-kvdefinekeys
Requires:       texlive-kvsetkeys >= %{texlive_version}
#!BuildIgnore: texlive-kvsetkeys
Requires:       texlive-letltxmacro >= %{texlive_version}
#!BuildIgnore: texlive-letltxmacro
Requires:       texlive-ltxcmds >= %{texlive_version}
#!BuildIgnore: texlive-ltxcmds
Requires:       texlive-pdfescape >= %{texlive_version}
#!BuildIgnore: texlive-pdfescape
Requires:       texlive-refcount >= %{texlive_version}
#!BuildIgnore: texlive-refcount
Requires:       texlive-rerunfilecheck >= %{texlive_version}
#!BuildIgnore: texlive-rerunfilecheck
Requires:       texlive-stringenc >= %{texlive_version}
#!BuildIgnore: texlive-stringenc
Requires:       texlive-url >= %{texlive_version}
#!BuildIgnore: texlive-url
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyperref-doc >= %{texlive_version}
Provides:       tex(backref.sty)
Provides:       tex(hdvipdfm.def)
Provides:       tex(hdvips.def)
Provides:       tex(hdvipson.def)
Provides:       tex(hdviwind.def)
Provides:       tex(hluatex.def)
Provides:       tex(hpdftex.def)
Provides:       tex(htex4ht.cfg)
Provides:       tex(htex4ht.def)
Provides:       tex(htexture.def)
Provides:       tex(hvtex.def)
Provides:       tex(hvtexhtm.def)
Provides:       tex(hvtexmrk.def)
Provides:       tex(hxetex.def)
Provides:       tex(hyperref.sty)
Provides:       tex(hypertex.def)
Provides:       tex(minitoc-hyper.sty)
Provides:       tex(nameref.sty)
Provides:       tex(nohyperref.sty)
Provides:       tex(ntheorem-hyper.sty)
Provides:       tex(pd1enc.def)
Provides:       tex(pdfmark.def)
Provides:       tex(psdextra.def)
Provides:       tex(puarenc.def)
Provides:       tex(puenc.def)
Provides:       tex(puvnenc.def)
Provides:       tex(xr-hyper.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(atveryend.sty)
Requires:       tex(auxhook.sty)
Requires:       tex(bitset.sty)
Requires:       tex(color.sty)
Requires:       tex(etexcmds.sty)
Requires:       tex(gettitlestring.sty)
Requires:       tex(hycolor.sty)
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(intcalc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvdefinekeys.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(memhfixc.sty)
Requires:       tex(minitoc.sty)
Requires:       tex(pdf14.sty)
Requires:       tex(pdfescape.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(refcount.sty)
Requires:       tex(rerunfilecheck.sty)
Requires:       tex(stringenc.sty)
Requires:       tex(tex4ht.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source25:       hyperref.tar.xz
Source26:       hyperref.doc.tar.xz

%description -n texlive-hyperref
The hyperref package is used to handle cross-referencing
commands in LaTeX to produce hypertext links in the document.
The package provides backends for the \special set defined for
HyperTeX DVI processors; for embedded pdfmark commands for
processing by Acrobat Distiller (dvips and Y&Y's dvipsone); for
Y&Y's dviwindo; for PDF control within pdfTeX and dvipdfm; for
TeX4ht; and for VTeX's pdf and HTML backends. The package is
distributed with the backref and nameref packages, which make
use of the facilities of hyperref. The package depends on the
author's kvoptions, ltxcmds and refcount packages.

%package -n texlive-hyperref-doc
Version:        %{texlive_version}.%{texlive_noarch}.7.00dsvn53837
Release:        0
Summary:        Documentation for texlive-hyperref
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hyperref-doc:en)

%description -n texlive-hyperref-doc
This package includes the documentation for texlive-hyperref

%post -n texlive-hyperref
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hyperref 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hyperref
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyperref-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hyperref/ChangeLog.txt
%{_texmfdistdir}/doc/latex/hyperref/README.md
%{_texmfdistdir}/doc/latex/hyperref/backref.pdf
%{_texmfdistdir}/doc/latex/hyperref/cmmi10-22.gif
%{_texmfdistdir}/doc/latex/hyperref/cmsy10-21.gif
%{_texmfdistdir}/doc/latex/hyperref/hyperref.pdf
%{_texmfdistdir}/doc/latex/hyperref/manifest.txt
%{_texmfdistdir}/doc/latex/hyperref/manual.css
%{_texmfdistdir}/doc/latex/hyperref/manual.html
%{_texmfdistdir}/doc/latex/hyperref/manual.pdf
%{_texmfdistdir}/doc/latex/hyperref/manual2.html
%{_texmfdistdir}/doc/latex/hyperref/manual3.html
%{_texmfdistdir}/doc/latex/hyperref/manual4.html
%{_texmfdistdir}/doc/latex/hyperref/manual5.html
%{_texmfdistdir}/doc/latex/hyperref/manual6.html
%{_texmfdistdir}/doc/latex/hyperref/manual7.html
%{_texmfdistdir}/doc/latex/hyperref/nameref.pdf
%{_texmfdistdir}/doc/latex/hyperref/paper.pdf
%{_texmfdistdir}/doc/latex/hyperref/slides.pdf

%files -n texlive-hyperref
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hyperref/backref.sty
%{_texmfdistdir}/tex/latex/hyperref/hdvipdfm.def
%{_texmfdistdir}/tex/latex/hyperref/hdvips.def
%{_texmfdistdir}/tex/latex/hyperref/hdvipson.def
%{_texmfdistdir}/tex/latex/hyperref/hdviwind.def
%{_texmfdistdir}/tex/latex/hyperref/hluatex.def
%{_texmfdistdir}/tex/latex/hyperref/hpdftex.def
%{_texmfdistdir}/tex/latex/hyperref/htex4ht.cfg
%{_texmfdistdir}/tex/latex/hyperref/htex4ht.def
%{_texmfdistdir}/tex/latex/hyperref/htexture.def
%{_texmfdistdir}/tex/latex/hyperref/hvtex.def
%{_texmfdistdir}/tex/latex/hyperref/hvtexhtm.def
%{_texmfdistdir}/tex/latex/hyperref/hvtexmrk.def
%{_texmfdistdir}/tex/latex/hyperref/hxetex.def
%{_texmfdistdir}/tex/latex/hyperref/hyperref.sty
%{_texmfdistdir}/tex/latex/hyperref/hypertex.def
%{_texmfdistdir}/tex/latex/hyperref/minitoc-hyper.sty
%{_texmfdistdir}/tex/latex/hyperref/nameref.sty
%{_texmfdistdir}/tex/latex/hyperref/nohyperref.sty
%{_texmfdistdir}/tex/latex/hyperref/ntheorem-hyper.sty
%{_texmfdistdir}/tex/latex/hyperref/pd1enc.def
%{_texmfdistdir}/tex/latex/hyperref/pdfmark.def
%{_texmfdistdir}/tex/latex/hyperref/psdextra.def
%{_texmfdistdir}/tex/latex/hyperref/puarenc.def
%{_texmfdistdir}/tex/latex/hyperref/puenc.def
%{_texmfdistdir}/tex/latex/hyperref/puvnenc.def
%{_texmfdistdir}/tex/latex/hyperref/xr-hyper.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyperref-%{texlive_version}.%{texlive_noarch}.7.00dsvn53837-%{release}-zypper
%endif

%package -n texlive-hyperxmp
Version:        %{texlive_version}.%{texlive_noarch}.5.1svn54758
Release:        0
Summary:        Embed XMP metadata within a LaTeX document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyperxmp-doc >= %{texlive_version}
Provides:       tex(hyperxmp.sty)
Requires:       tex(atenddvi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifdraft.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifmtarg.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(intcalc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdfescape.sty)
Requires:       tex(stringenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source27:       hyperxmp.tar.xz
Source28:       hyperxmp.doc.tar.xz

%description -n texlive-hyperxmp
XMP (eXtensible Metadata Platform) is a mechanism proposed by
Adobe for embedding document metadata within the document
itself. The metadata is designed to be easy to extract, even by
programs that are oblivious to the document's file format. Most
of Adobe's applications store XMP metadata when saving files.
Now, with the hyperxmp package, it is trivial for LaTeX
document authors to store XMP metadata in their documents as
well. Version 2.2 of the package added support for the IPTC
Photo Metadata schema. It allows \xmpcomma and \xmpquote to be
used in any hyperxmp option, not only those that require
special treatment of commas. And it introduces an \xmplinesep
macro that controls how multiline fields are represented in the
XMP packet. The package integrates seamlessly with hyperref and
requires virtually no modifications to documents that already
exploit hyperref's mechanisms for specifying PDF metadata. The
current version of hyperxmp can embed the following metadata as
XMP: title, authors, primary author's title or position,
metadata writer, subject/summary, keywords, copyright, license
URL, document base URL, document identifier and instance
identifier, language, source file name, PDF generating tool,
PDF version, and contact telephone number/postal address/email
address/URL. Hyperxmp currently embeds XMP only within PDF
documents; it is compatible with pdfLaTeX, XeLaTeX,
LaTeX+dvipdfm, and LaTeX+dvips+ps2pdf.

%package -n texlive-hyperxmp-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.1svn54758
Release:        0
Summary:        Documentation for texlive-hyperxmp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hyperxmp-doc
This package includes the documentation for texlive-hyperxmp

%post -n texlive-hyperxmp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hyperxmp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hyperxmp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyperxmp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hyperxmp/README
%{_texmfdistdir}/doc/latex/hyperxmp/hyperxmp.pdf

%files -n texlive-hyperxmp
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hyperxmp/hyperxmp.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyperxmp-%{texlive_version}.%{texlive_noarch}.5.1svn54758-%{release}-zypper
%endif

%package -n texlive-hyph-utf8
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Hyphenation patterns expressed in UTF-8
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyph-utf8-doc >= %{texlive_version}
Provides:       tex(conv-utf8-ec.tex)
Provides:       tex(conv-utf8-il2.tex)
Provides:       tex(conv-utf8-il3.tex)
Provides:       tex(conv-utf8-l7x.tex)
Provides:       tex(conv-utf8-lmc.tex)
Provides:       tex(conv-utf8-lth.tex)
Provides:       tex(conv-utf8-qx.tex)
Provides:       tex(conv-utf8-t2a.tex)
Provides:       tex(conv-utf8-t8m.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source29:       hyph-utf8.tar.xz
Source30:       hyph-utf8.doc.tar.xz

%description -n texlive-hyph-utf8
Modern native UTF-8 engines such as XeTeX and LuaTeX need
hyphenation patterns in UTF-8 format, whereas older systems
require hyphenation patterns in the 8-bit encoding of the font
in use (such encodings are codified in the LaTeX scheme with
names like OT1, T2A, TS1, OML, LY1, etc). The present package
offers a collection of conversions of existing patterns to
UTF-8 format, together with converters for use with 8-bit fonts
in older systems. Since hyphenation patterns for Knuthian-style
TeX systems are only read at iniTeX time, it is hoped that the
UTF-8 patterns, with their converters, will completely supplant
the older patterns.

%package -n texlive-hyph-utf8-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Documentation for texlive-hyph-utf8
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hyph-utf8-doc:en)

%description -n texlive-hyph-utf8-doc
This package includes the documentation for texlive-hyph-utf8

%post -n texlive-hyph-utf8
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hyph-utf8 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hyph-utf8
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyph-utf8-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/hyph-utf8/CHANGES
%{_texmfdistdir}/doc/generic/hyph-utf8/HISTORY
%{_texmfdistdir}/doc/generic/hyph-utf8/README.md
%{_texmfdistdir}/doc/generic/hyph-utf8/hyph-utf8.pdf
%{_texmfdistdir}/doc/generic/hyph-utf8/hyph-utf8.tex
%{_texmfdistdir}/doc/generic/hyph-utf8/hyphenation-distribution.pdf
%{_texmfdistdir}/doc/generic/hyph-utf8/hyphenation-distribution.tex
%{_texmfdistdir}/doc/generic/hyph-utf8/img/miktex-languages.png
%{_texmfdistdir}/doc/generic/hyph-utf8/img/texlive-collection.png
%{_texmfdistdir}/doc/luatex/hyph-utf8/README
%{_texmfdistdir}/doc/luatex/hyph-utf8/luatex-hyphen.pdf

%files -n texlive-hyph-utf8
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-il2.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-il3.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-l7x.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-lmc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-lth.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-qx.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/conversions/conv-utf8-t8m.tex
%{_texmfdistdir}/tex/luatex/hyph-utf8/etex.src
%{_texmfdistdir}/tex/luatex/hyph-utf8/luatex-hyphen.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyph-utf8-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-afrikaans
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Afrikaans hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-af.ec.tex)
Provides:       tex(hyph-af.tex)
Provides:       tex(hyph-quote-af.tex)
Provides:       tex(loadhyph-af.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source31:       hyphen-afrikaans.tar.xz

%description -n texlive-hyphen-afrikaans
Hyphenation patterns for Afrikaans in T1/EC and UTF-8
encodings. OpenOffice includes older patterns created by a
different author, but the patterns packaged with TeX are
considered superior in quality.
%post -n texlive-hyphen-afrikaans
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-afrikaans 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-afrikaans
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-afrikaans
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-af.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-af.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-af.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-af.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-af.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-af.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-afrikaans.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-afrikaans.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-afrikaans.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-afrikaans-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-ancientgreek
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Ancient Greek hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(grahyph5.tex)
Provides:       tex(hyph-grc.tex)
Provides:       tex(ibyhyph.tex)
Provides:       tex(loadhyph-grc.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source32:       hyphen-ancientgreek.tar.xz

%description -n texlive-hyphen-ancientgreek
Hyphenation patterns for Ancient Greek in LGR and UTF-8
encodings, including support for (obsolete) Ibycus font
encoding. Patterns in UTF-8 use two code positions for each of
the vowels with acute accent (a.k.a tonos, oxia), e.g., U+03AE,
U+1F75 for eta.
%post -n texlive-hyphen-ancientgreek
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-ancientgreek 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-ancientgreek
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-ancientgreek
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-grc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-grc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-grc.pat.txt
%{_texmfdistdir}/tex/generic/hyphen/grahyph5.tex
%{_texmfdistdir}/tex/generic/hyphen/ibyhyph.tex
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ancientgreek.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ancientgreek.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ancientgreek.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-ancientgreek-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-arabic
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        (No) Arabic hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source33:       hyphen-arabic.tar.xz

%description -n texlive-hyphen-arabic
Prevent hyphenation in Arabic.
%post -n texlive-hyphen-arabic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-arabic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-arabic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-arabic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-arabic.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-arabic.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-arabic.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-arabic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-armenian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Armenian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-hy.tex)
Provides:       tex(loadhyph-hy.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source34:       hyphen-armenian.tar.xz

%description -n texlive-hyphen-armenian
Hyphenation patterns for Armenian for Unicode engines.
Auto-generated from a script included in hyph-utf8.
%post -n texlive-hyphen-armenian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-armenian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-armenian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-armenian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-hy.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-hy.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hy.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-armenian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-armenian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-armenian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-armenian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-base
Version:        %{texlive_version}.%{texlive_noarch}.svn54763
Release:        0
Summary:        Core hyphenation support files
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(dumyhyph.tex)
Provides:       tex(hyphen.tex)
Provides:       tex(hypht1.tex)
Provides:       tex(language.dat)
Provides:       tex(language.dat.lua)
Provides:       tex(language.def)
Provides:       tex(language.us.def)
Provides:       tex(zerohyph.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source35:       hyphen-base.tar.xz

%description -n texlive-hyphen-base
Includes Knuth's original hyphen.tex, zerohyph.tex to disable
hyphenation, language.us which starts the autogenerated files
language.dat and language.def (and default versions of those),
etc.
%post -n texlive-hyphen-base
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr

%postun -n texlive-hyphen-base 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hyphen-base
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-base
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/tex/generic/config/language.dat
%verify(link) %{_texmfdistdir}/tex/generic/config/language.dat.lua
%verify(link) %{_texmfdistdir}/tex/generic/config/language.def
%{_texmfdistdir}/tex/generic/config/language.us
%{_texmfdistdir}/tex/generic/config/language.us.def
%{_texmfdistdir}/tex/generic/config/language.us.lua
%{_texmfdistdir}/tex/generic/hyphen/dumyhyph.tex
%{_texmfdistdir}/tex/generic/hyphen/hyphen.tex
%{_texmfdistdir}/tex/generic/hyphen/hypht1.tex
%{_texmfdistdir}/tex/generic/hyphen/zerohyph.tex
%config %verify(not md5 mtime size) %{_texmfconfdir}/tex/generic/config/language.dat
%config %verify(not md5 mtime size) %{_texmfconfdir}/tex/generic/config/language.dat.lua
%config %verify(not md5 mtime size) %{_texmfconfdir}/tex/generic/config/language.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-base-%{texlive_version}.%{texlive_noarch}.svn54763-%{release}-zypper
%endif

%package -n texlive-hyphen-basque
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Basque hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-eu.ec.tex)
Provides:       tex(hyph-eu.tex)
Provides:       tex(loadhyph-eu.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source36:       hyphen-basque.tar.xz

%description -n texlive-hyphen-basque
Hyphenation patterns for Basque in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-basque
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-basque 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-basque
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-basque
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-eu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-eu.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-eu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-eu.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-basque.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-basque.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-basque.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-basque-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-belarusian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Belarusian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-be.t2a.tex)
Provides:       tex(hyph-be.tex)
Provides:       tex(hyph-quote-be.tex)
Provides:       tex(loadhyph-be.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source37:       hyphen-belarusian.tar.xz

%description -n texlive-hyphen-belarusian
Belarusian hyphenation patterns in T2A and UTF-8 encodings
%post -n texlive-hyphen-belarusian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-belarusian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-belarusian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-belarusian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-be.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-be.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-be.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-be.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-be.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-belarusian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-belarusian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-belarusian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-belarusian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-bulgarian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Bulgarian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-bg.t2a.tex)
Provides:       tex(hyph-bg.tex)
Provides:       tex(loadhyph-bg.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source38:       hyphen-bulgarian.tar.xz

%description -n texlive-hyphen-bulgarian
Hyphenation patterns for Bulgarian in T2A and UTF-8 encodings.
%post -n texlive-hyphen-bulgarian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-bulgarian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-bulgarian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-bulgarian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-bg.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-bg.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-bg.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-bg.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-bulgarian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-bulgarian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-bulgarian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-bulgarian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-catalan
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Catalan hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-ca.ec.tex)
Provides:       tex(hyph-ca.tex)
Provides:       tex(loadhyph-ca.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source39:       hyphen-catalan.tar.xz

%description -n texlive-hyphen-catalan
Hyphenation patterns for Catalan in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-catalan
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-catalan 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-catalan
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-catalan
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ca.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-ca.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ca.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ca.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ca.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-catalan.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-catalan.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-catalan.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-catalan-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-chinese
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Chinese pinyin hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-zh-latn-pinyin.ec.tex)
Provides:       tex(hyph-zh-latn-pinyin.tex)
Provides:       tex(loadhyph-zh-latn-pinyin.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source40:       hyphen-chinese.tar.xz

%description -n texlive-hyphen-chinese
Hyphenation patterns for transliterated Mandarin Chinese
(pinyin) in T1/EC and UTF-8 encodings. The latter can hyphenate
pinyin with or without tone markers; the former only without.
%post -n texlive-hyphen-chinese
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-chinese 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-chinese
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-chinese
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-zh-latn-pinyin.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-zh-latn-pinyin.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-zh-latn-pinyin.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-zh-latn-pinyin.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-chinese.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-chinese.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-chinese.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-chinese-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-churchslavonic
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Church Slavonic hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-cu.tex)
Provides:       tex(loadhyph-cu.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source41:       hyphen-churchslavonic.tar.xz

%description -n texlive-hyphen-churchslavonic
Hyphenation patterns for Church Slavonic in UTF-8 encoding
%post -n texlive-hyphen-churchslavonic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-churchslavonic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-churchslavonic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-churchslavonic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-cu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-cu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cu.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cu.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-churchslavonic.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-churchslavonic.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-churchslavonic.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-churchslavonic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-coptic
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Coptic hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(copthyph.tex)
Provides:       tex(hyph-cop.tex)
Provides:       tex(loadhyph-cop.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source42:       hyphen-coptic.tar.xz

%description -n texlive-hyphen-coptic
Hyphenation patterns for Coptic in UTF-8 encoding as well as in
ASCII-based encoding for 8-bit engines. The latter can only be
used with special Coptic fonts (like CBcoptic). The patterns
are considered experimental.
%post -n texlive-hyphen-coptic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-coptic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-coptic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-coptic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-cop.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex-8bit/copthyph.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-cop.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cop.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-coptic.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-coptic.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-coptic.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-coptic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-croatian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Croatian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-hr.ec.tex)
Provides:       tex(hyph-hr.tex)
Provides:       tex(loadhyph-hr.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source43:       hyphen-croatian.tar.xz

%description -n texlive-hyphen-croatian
Hyphenation patterns for Croatian in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-croatian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-croatian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-croatian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-croatian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-hr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-hr.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-hr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hr.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-croatian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-croatian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-croatian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-croatian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-czech
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Czech hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-cs.ec.tex)
Provides:       tex(hyph-cs.tex)
Provides:       tex(loadhyph-cs.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source44:       hyphen-czech.tar.xz

%description -n texlive-hyphen-czech
Hyphenation patterns for Czech in T1/EC and UTF-8 encodings.
Original patterns 'czhyphen' are still distributed in the
'csplain' package and loaded with ISO Latin 2 encoding (IL2).
%post -n texlive-hyphen-czech
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-czech 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-czech
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-czech
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-cs.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-cs.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-cs.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cs.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cs.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-czech.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-czech.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-czech.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-czech-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-danish
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Danish hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-da.ec.tex)
Provides:       tex(hyph-da.tex)
Provides:       tex(loadhyph-da.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source45:       hyphen-danish.tar.xz

%description -n texlive-hyphen-danish
Hyphenation patterns for Danish in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-danish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-danish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-danish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-danish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-da.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-da.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-da.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-da.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-danish.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-danish.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-danish.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-danish-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-dutch
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn54568
Release:        0
Summary:        Dutch hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-nl.ec.tex)
Provides:       tex(hyph-nl.tex)
Provides:       tex(loadhyph-nl.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source46:       hyphen-dutch.tar.xz

%description -n texlive-hyphen-dutch
Hyphenation patterns for Dutch in T1/EC and UTF-8 encodings.
These patterns don't handle cases like 'menuutje' > 'menu-tje',
and don't hyphenate words that have different hyphenations
according to their meaning.
%post -n texlive-hyphen-dutch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-dutch 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-dutch
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-dutch
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-nl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-nl.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-nl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nl.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-dutch.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-dutch.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-dutch.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-dutch-%{texlive_version}.%{texlive_noarch}.1.1svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-english
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        English hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-en-gb.tex)
Provides:       tex(hyph-en-us.tex)
Provides:       tex(loadhyph-en-gb.tex)
Provides:       tex(loadhyph-en-us.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source47:       hyphen-english.tar.xz

%description -n texlive-hyphen-english
Additional hyphenation patterns for American and British
English in ASCII encoding. The American English patterns
(usenglishmax) greatly extend the standard patterns from Knuth
to find many additional hyphenation points. British English
hyphenation is completely different from US English, so has its
own set of patterns.
%post -n texlive-hyphen-english
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-english 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-english
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-english
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-en-gb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-en-us.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-en-gb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-en-us.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-gb.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-en-us.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-english.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-english.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-english.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-english-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-esperanto
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Esperanto hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-eo.il3.tex)
Provides:       tex(hyph-eo.tex)
Provides:       tex(loadhyph-eo.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source48:       hyphen-esperanto.tar.xz

%description -n texlive-hyphen-esperanto
Hyphenation patterns for Esperanto ISO Latin 3 and UTF-8
encodings. Note that TeX distributions don't ship any suitable
fonts in Latin 3 encoding, so unless you create your own font
support or want to use MlTeX, using native Unicode engines is
highly recommended.
%post -n texlive-hyphen-esperanto
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-esperanto 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-esperanto
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-esperanto
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-eo.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-eo.il3.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-eo.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-eo.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-esperanto.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-esperanto.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-esperanto.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-esperanto-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-estonian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Estonian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-et.ec.tex)
Provides:       tex(hyph-et.tex)
Provides:       tex(loadhyph-et.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source49:       hyphen-estonian.tar.xz

%description -n texlive-hyphen-estonian
Hyphenation patterns for Estonian in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-estonian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-estonian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-estonian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-estonian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-et.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-et.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-et.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-et.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-estonian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-estonian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-estonian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-estonian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-ethiopic
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Hyphenation patterns for Ethiopic scripts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-mul-ethi.tex)
Provides:       tex(loadhyph-mul-ethi.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source50:       hyphen-ethiopic.tar.xz

%description -n texlive-hyphen-ethiopic
Hyphenation patterns for languages written using the Ethiopic
script for Unicode engines. They are not supposed to be
linguistically relevant in all cases and should, for proper
typography, be replaced by files tailored to individual
languages.
%post -n texlive-hyphen-ethiopic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-ethiopic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-ethiopic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-ethiopic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-mul-ethi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-mul-ethi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mul-ethi.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ethiopic.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ethiopic.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ethiopic.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-ethiopic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-farsi
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        (No) Persian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source51:       hyphen-farsi.tar.xz

%description -n texlive-hyphen-farsi
Prevent hyphenation in Persian.
%post -n texlive-hyphen-farsi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-farsi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-farsi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-farsi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-farsi.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-farsi.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-farsi.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-farsi-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-finnish
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Finnish hyphenation patterns
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-fi.ec.tex)
Provides:       tex(hyph-fi.tex)
Provides:       tex(loadhyph-fi.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source52:       hyphen-finnish.tar.xz

%description -n texlive-hyphen-finnish
Hyphenation patterns for Finnish in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-finnish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-finnish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-finnish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-finnish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-fi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-fi.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-fi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fi.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-finnish.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-finnish.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-finnish.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-finnish-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-french
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        French hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-fr.ec.tex)
Provides:       tex(hyph-fr.tex)
Provides:       tex(hyph-quote-fr.tex)
Provides:       tex(loadhyph-fr.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source53:       hyphen-french.tar.xz

%description -n texlive-hyphen-french
Hyphenation patterns for French in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-french
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-french 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-french
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-french
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-fr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-fr.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-fr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-fr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fr.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-french.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-french.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-french.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-french-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-friulan
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Friulan hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-fur.ec.tex)
Provides:       tex(hyph-fur.tex)
Provides:       tex(hyph-quote-fur.tex)
Provides:       tex(loadhyph-fur.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source54:       hyphen-friulan.tar.xz

%description -n texlive-hyphen-friulan
Hyphenation patterns for Friulan in ASCII encoding. They are
supposed to comply with the common spelling of the Friulan
(Furlan) language as fixed by the Regional Law N.15/96 dated
November 6, 1996 and its following amendments.
%post -n texlive-hyphen-friulan
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-friulan 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-friulan
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-friulan
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-fur.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-fur.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-fur.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-fur.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-fur.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-friulan.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-friulan.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-friulan.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-friulan-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-galician
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Galician hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-gl.ec.tex)
Provides:       tex(hyph-gl.tex)
Provides:       tex(loadhyph-gl.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source55:       hyphen-galician.tar.xz

%description -n texlive-hyphen-galician
Hyphenation patterns for Galician in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-galician
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-galician 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-galician
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-galician
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-gl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-gl.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-gl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-gl.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-galician.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-galician.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-galician.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-galician-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-georgian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Georgian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-ka.t8m.tex)
Provides:       tex(hyph-ka.tex)
Provides:       tex(loadhyph-ka.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source56:       hyphen-georgian.tar.xz

%description -n texlive-hyphen-georgian
Hyphenation patterns for Georgian in T8M, T8K and UTF-8
encodings.
%post -n texlive-hyphen-georgian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-georgian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-georgian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-georgian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ka.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-ka.t8m.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ka.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ka.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-georgian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-georgian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-georgian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-georgian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-german
Version:        %{texlive_version}.%{texlive_noarch}.svn54758
Release:        0
Summary:        German hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-dehyph >= %{texlive_version}
#!BuildIgnore: texlive-dehyph
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-de-1901.ec.tex)
Provides:       tex(hyph-de-1901.tex)
Provides:       tex(hyph-de-1996.ec.tex)
Provides:       tex(hyph-de-1996.tex)
Provides:       tex(hyph-de-ch-1901.ec.tex)
Provides:       tex(hyph-de-ch-1901.tex)
Provides:       tex(loadhyph-de-1901.tex)
Provides:       tex(loadhyph-de-1996.tex)
Provides:       tex(loadhyph-de-ch-1901.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source57:       hyphen-german.tar.xz

%description -n texlive-hyphen-german
Hyphenation patterns for German in T1/EC and UTF-8 encodings,
for traditional and reformed spelling, including Swiss German.
The package includes the latest patterns from dehyph-exptl
(known to TeX under names 'german', 'ngerman' and
'swissgerman'), however 8-bit engines still load old versions
of patterns for 'german' and 'ngerman' for
backward-compatibility reasons. Swiss German patterns are
suitable for Swiss Standard German (Hochdeutsch) not the
Alemannic dialects spoken in Switzerland (Schwyzerduetsch).
There are no known patterns for written Schwyzerduetsch.
%post -n texlive-hyphen-german
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-german 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-german
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-german
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-de-1901.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-de-1996.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-de-ch-1901.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-de-1901.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-de-1996.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-de-ch-1901.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-de-1901.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-de-1996.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-de-ch-1901.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-1901.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-1996.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-de-ch-1901.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-german.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-german.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-german.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-german-%{texlive_version}.%{texlive_noarch}.svn54758-%{release}-zypper
%endif

%package -n texlive-hyphen-greek
Version:        %{texlive_version}.%{texlive_noarch}.5svn54568
Release:        0
Summary:        Modern Greek hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyphen-greek-doc >= %{texlive_version}
Provides:       tex(grmhyph5.tex)
Provides:       tex(grphyph5.tex)
Provides:       tex(hyph-el-monoton.tex)
Provides:       tex(hyph-el-polyton.tex)
Provides:       tex(loadhyph-el-monoton.tex)
Provides:       tex(loadhyph-el-polyton.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source58:       hyphen-greek.tar.xz
Source59:       hyphen-greek.doc.tar.xz

%description -n texlive-hyphen-greek
Hyphenation patterns for Modern Greek in monotonic and
polytonic spelling in LGR and UTF-8 encodings. Patterns in
UTF-8 use two code positions for each of the vowels with acute
accent (a.k.a tonos, oxia), e.g., U+03AC, U+1F71 for alpha.

%package -n texlive-hyphen-greek-doc
Version:        %{texlive_version}.%{texlive_noarch}.5svn54568
Release:        0
Summary:        Documentation for texlive-hyphen-greek
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hyphen-greek-doc
This package includes the documentation for texlive-hyphen-greek

%post -n texlive-hyphen-greek
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-greek 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-greek
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-greek-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/elhyphen/README
%{_texmfdistdir}/doc/generic/elhyphen/anc-test.ltx
%{_texmfdistdir}/doc/generic/elhyphen/anc-test.pdf
%{_texmfdistdir}/doc/generic/elhyphen/ancient.pdf
%{_texmfdistdir}/doc/generic/elhyphen/compound.ltx
%{_texmfdistdir}/doc/generic/elhyphen/compound.pdf
%{_texmfdistdir}/doc/generic/elhyphen/copyrite.txt
%{_texmfdistdir}/doc/generic/elhyphen/modern.pdf

%files -n texlive-hyphen-greek
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-el-monoton.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-el-polyton.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-el-monoton.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-el-polyton.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-el-monoton.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-el-polyton.pat.txt
%{_texmfdistdir}/tex/generic/hyphen/grmhyph5.tex
%{_texmfdistdir}/tex/generic/hyphen/grphyph5.tex
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-greek.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-greek.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-greek.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-greek-%{texlive_version}.%{texlive_noarch}.5svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-hungarian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Hungarian hyphenation patterns
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyphen-hungarian-doc >= %{texlive_version}
Provides:       tex(hyph-hu.ec.tex)
Provides:       tex(hyph-hu.tex)
Provides:       tex(loadhyph-hu.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source60:       hyphen-hungarian.tar.xz
Source61:       hyphen-hungarian.doc.tar.xz

%description -n texlive-hyphen-hungarian
Hyphenation patterns for Hungarian in T1/EC and UTF-8
encodings.

%package -n texlive-hyphen-hungarian-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Documentation for texlive-hyphen-hungarian
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hyphen-hungarian-doc
This package includes the documentation for texlive-hyphen-hungarian

%post -n texlive-hyphen-hungarian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-hungarian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-hungarian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-hungarian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/huhyphen/huhyphn.pdf
%{_texmfdistdir}/doc/generic/huhyphen/hyph_hu.dic
%{_texmfdistdir}/doc/generic/huhyphen/searchforerrors.rb
%{_texmfdistdir}/doc/generic/huhyphen/testhyphenation.rb
%{_texmfdistdir}/doc/generic/hyph-utf8/languages/hu/huhyphn.pdf

%files -n texlive-hyphen-hungarian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-hu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-hu.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-hu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hu.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-hungarian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-hungarian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-hungarian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-hungarian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-icelandic
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Icelandic hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-is.ec.tex)
Provides:       tex(hyph-is.tex)
Provides:       tex(loadhyph-is.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source62:       hyphen-icelandic.tar.xz

%description -n texlive-hyphen-icelandic
Hyphenation patterns for Icelandic in T1/EC and UTF-8
encodings.
%post -n texlive-hyphen-icelandic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-icelandic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-icelandic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-icelandic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-is.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-is.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-is.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-is.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-icelandic.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-icelandic.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-icelandic.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-icelandic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-indic
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Indic hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-as.tex)
Provides:       tex(hyph-bn.tex)
Provides:       tex(hyph-gu.tex)
Provides:       tex(hyph-hi.tex)
Provides:       tex(hyph-kn.tex)
Provides:       tex(hyph-ml.tex)
Provides:       tex(hyph-mr.tex)
Provides:       tex(hyph-or.tex)
Provides:       tex(hyph-pa.tex)
Provides:       tex(hyph-pi.tex)
Provides:       tex(hyph-ta.tex)
Provides:       tex(hyph-te.tex)
Provides:       tex(loadhyph-as.tex)
Provides:       tex(loadhyph-bn.tex)
Provides:       tex(loadhyph-gu.tex)
Provides:       tex(loadhyph-hi.tex)
Provides:       tex(loadhyph-kn.tex)
Provides:       tex(loadhyph-ml.tex)
Provides:       tex(loadhyph-mr.tex)
Provides:       tex(loadhyph-or.tex)
Provides:       tex(loadhyph-pa.tex)
Provides:       tex(loadhyph-pi.tex)
Provides:       tex(loadhyph-ta.tex)
Provides:       tex(loadhyph-te.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source63:       hyphen-indic.tar.xz

%description -n texlive-hyphen-indic
Hyphenation patterns for Assamese, Bengali, Gujarati, Hindi,
Kannada, Malayalam, Marathi, Oriya, Panjabi, Tamil and Telugu
for Unicode engines.
%post -n texlive-hyphen-indic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-indic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-indic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-indic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-as.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-bn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-gu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-hi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-kn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ml.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-mr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-or.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-pa.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-pi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ta.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-te.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-as.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-bn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-gu.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-hi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-kn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ml.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-mr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-or.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-pa.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-pi.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ta.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-te.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-as.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-bn.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-gu.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hi.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-kn.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ml.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mr.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-or.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pa.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pi.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ta.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-te.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indic.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indic.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indic.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-indic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-indonesian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Indonesian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-id.tex)
Provides:       tex(loadhyph-id.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source64:       hyphen-indonesian.tar.xz

%description -n texlive-hyphen-indonesian
Hyphenation patterns for Indonesian (Bahasa Indonesia) in ASCII
encoding. They are probably also usable for Malay (Bahasa
Melayu).
%post -n texlive-hyphen-indonesian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-indonesian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-indonesian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-indonesian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-id.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-id.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-id.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-id.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indonesian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indonesian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indonesian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-indonesian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-interlingua
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Interlingua hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-ia.tex)
Provides:       tex(loadhyph-ia.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source65:       hyphen-interlingua.tar.xz

%description -n texlive-hyphen-interlingua
Hyphenation patterns for Interlingua in ASCII encoding.
%post -n texlive-hyphen-interlingua
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-interlingua 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-interlingua
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-interlingua
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ia.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ia.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ia.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ia.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-interlingua.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-interlingua.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-interlingua.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-interlingua-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-irish
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Irish hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-ga.ec.tex)
Provides:       tex(hyph-ga.tex)
Provides:       tex(loadhyph-ga.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source66:       hyphen-irish.tar.xz

%description -n texlive-hyphen-irish
Hyphenation patterns for Irish (Gaeilge) in T1/EC and UTF-8
encodings.
%post -n texlive-hyphen-irish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-irish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-irish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-irish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ga.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-ga.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ga.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ga.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ga.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-irish.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-irish.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-irish.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-irish-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-italian
Version:        %{texlive_version}.%{texlive_noarch}.4.8gsvn54568
Release:        0
Summary:        Italian hyphenation patterns
License:        LGPL-2.1-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-it.tex)
Provides:       tex(hyph-quote-it.tex)
Provides:       tex(loadhyph-it.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source67:       hyphen-italian.tar.xz

%description -n texlive-hyphen-italian
Hyphenation patterns for Italian in ASCII encoding. Compliant
with the Recommendation UNI 6461 on hyphenation issued by the
Italian Standards Institution (Ente Nazionale di Unificazione
UNI).
%post -n texlive-hyphen-italian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-italian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-italian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-italian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-it.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-it.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-it.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-it.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-italian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-italian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-italian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-italian-%{texlive_version}.%{texlive_noarch}.4.8gsvn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-kurmanji
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Kurmanji hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-kmr.ec.tex)
Provides:       tex(hyph-kmr.tex)
Provides:       tex(loadhyph-kmr.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source68:       hyphen-kurmanji.tar.xz

%description -n texlive-hyphen-kurmanji
Hyphenation patterns for Kurmanji (Northern Kurdish) as spoken
in Turkey and by the Kurdish diaspora in Europe, in T1/EC and
UTF-8 encodings.
%post -n texlive-hyphen-kurmanji
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-kurmanji 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-kurmanji
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-kurmanji
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-kmr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-kmr.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-kmr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-kmr.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-kurmanji.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-kurmanji.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-kurmanji.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-kurmanji-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-latin
Version:        %{texlive_version}.%{texlive_noarch}.3.1svn54568
Release:        0
Summary:        Latin hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-la-x-classic.ec.tex)
Provides:       tex(hyph-la-x-classic.tex)
Provides:       tex(hyph-la-x-liturgic.ec.tex)
Provides:       tex(hyph-la-x-liturgic.tex)
Provides:       tex(hyph-la.ec.tex)
Provides:       tex(hyph-la.tex)
Provides:       tex(loadhyph-la-x-classic.tex)
Provides:       tex(loadhyph-la-x-liturgic.tex)
Provides:       tex(loadhyph-la.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source69:       hyphen-latin.tar.xz

%description -n texlive-hyphen-latin
Hyphenation patterns for Latin in T1/EC and UTF-8 encodings,
mainly in modern spelling (u when u is needed and v when v is
needed), medieval spelling with the ligatures \ae and \oe and
the (uncial) lowercase 'v' written as a 'u' is also supported.
Apparently there is no conflict between the patterns of modern
Latin and those of medieval Latin. Hyphenation patterns for the
Classical Latin in T1/EC and UTF-8 encodings. Classical Latin
hyphenation patterns are different from those of 'plain' Latin,
the latter being more adapted to modern Latin. Hyphenation
patterns for the Liturgical Latin in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-latin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-latin 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-latin
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-latin
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-la-x-classic.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-la-x-liturgic.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-la.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-la-x-liturgic.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-la.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex-8bit/hyph-la-x-classic.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-la-x-classic.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-la-x-liturgic.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-la.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-la-x-classic.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-la-x-liturgic.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-la.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latin.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latin.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latin.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-latin-%{texlive_version}.%{texlive_noarch}.3.1svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-latvian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Latvian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-lv.l7x.tex)
Provides:       tex(hyph-lv.tex)
Provides:       tex(loadhyph-lv.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source70:       hyphen-latvian.tar.xz

%description -n texlive-hyphen-latvian
Hyphenation patterns for Latvian in L7X and UTF-8 encodings.
%post -n texlive-hyphen-latvian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-latvian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-latvian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-latvian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-lv.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-lv.l7x.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-lv.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-lv.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latvian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latvian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latvian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-latvian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-lithuanian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Lithuanian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-lt.l7x.tex)
Provides:       tex(hyph-lt.tex)
Provides:       tex(loadhyph-lt.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source71:       hyphen-lithuanian.tar.xz

%description -n texlive-hyphen-lithuanian
Hyphenation patterns for Lithuanian in L7X and UTF-8 encodings.
\lefthyphenmin and \righthyphenmin have to be at least 2.
%post -n texlive-hyphen-lithuanian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-lithuanian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-lithuanian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-lithuanian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-lt.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-lt.l7x.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-lt.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-lt.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-lithuanian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-lithuanian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-lithuanian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-lithuanian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-macedonian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Macedonian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-mk.tex)
Provides:       tex(loadhyph-mk.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source72:       hyphen-macedonian.tar.xz

%description -n texlive-hyphen-macedonian
Hyphenation patterns for Macedonian
%post -n texlive-hyphen-macedonian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-macedonian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-macedonian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-macedonian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-mk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-mk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mk.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-macedonian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-macedonian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-macedonian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-macedonian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-mongolian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Mongolian hyphenation patterns in Cyrillic script
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-mn-cyrl-x-lmc.lmc.tex)
Provides:       tex(hyph-mn-cyrl-x-lmc.tex)
Provides:       tex(hyph-mn-cyrl.t2a.tex)
Provides:       tex(hyph-mn-cyrl.tex)
Provides:       tex(loadhyph-mn-cyrl-x-lmc.tex)
Provides:       tex(loadhyph-mn-cyrl.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source73:       hyphen-mongolian.tar.xz

%description -n texlive-hyphen-mongolian
Hyphenation patterns for Mongolian in T2A, LMC and UTF-8
encodings. LMC encoding is used in MonTeX. The package includes
two sets of patterns that will hopefully be merged in future.
%post -n texlive-hyphen-mongolian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-mongolian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-mongolian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-mongolian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-mn-cyrl-x-lmc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-mn-cyrl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-mn-cyrl-x-lmc.lmc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-mn-cyrl.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-mn-cyrl-x-lmc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-mn-cyrl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-mn-cyrl.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-mongolian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-mongolian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-mongolian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-mongolian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-norwegian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Norwegian Bokmal and Nynorsk hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-nb.ec.tex)
Provides:       tex(hyph-nb.tex)
Provides:       tex(hyph-nn.ec.tex)
Provides:       tex(hyph-nn.tex)
Provides:       tex(hyph-no.tex)
Provides:       tex(loadhyph-nb.tex)
Provides:       tex(loadhyph-nn.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source74:       hyphen-norwegian.tar.xz

%description -n texlive-hyphen-norwegian
Hyphenation patterns for Norwegian Bokmal and Nynorsk in T1/EC
and UTF-8 encodings.
%post -n texlive-hyphen-norwegian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-norwegian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-norwegian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-norwegian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-nb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-nn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-nb.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-nn.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-nb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-nn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-no.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nb.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nb.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nn.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-nn.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-norwegian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-norwegian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-norwegian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-norwegian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-occitan
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Occitan hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-oc.ec.tex)
Provides:       tex(hyph-oc.tex)
Provides:       tex(hyph-quote-oc.tex)
Provides:       tex(loadhyph-oc.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source75:       hyphen-occitan.tar.xz

%description -n texlive-hyphen-occitan
Hyphenation patterns for Occitan in T1/EC and UTF-8 encodings.
They are supposed to be valid for all the Occitan variants
spoken and written in the wide area called 'Occitanie' by the
French. It ranges from the Val d'Aran within Catalunya, to the
South Western Italian Alps encompassing the southern half of
the French pentagon.
%post -n texlive-hyphen-occitan
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-occitan 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-occitan
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-occitan
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-oc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-oc.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-oc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-oc.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-oc.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-occitan.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-occitan.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-occitan.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-occitan-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-piedmontese
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Piedmontese hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-pms.tex)
Provides:       tex(hyph-quote-pms.tex)
Provides:       tex(loadhyph-pms.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source76:       hyphen-piedmontese.tar.xz

%description -n texlive-hyphen-piedmontese
Hyphenation patterns for Piedmontese in ASCII encoding.
Compliant with 'Gramatica dla lengua piemonteisa' by Camillo
Brero.
%post -n texlive-hyphen-piedmontese
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-piedmontese 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-piedmontese
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-piedmontese
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-pms.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-pms.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-pms.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pms.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-piedmontese.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-piedmontese.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-piedmontese.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-piedmontese-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-polish
Version:        %{texlive_version}.%{texlive_noarch}.3.0asvn54568
Release:        0
Summary:        Polish hyphenation patterns
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-pl.qx.tex)
Provides:       tex(hyph-pl.tex)
Provides:       tex(loadhyph-pl.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source77:       hyphen-polish.tar.xz

%description -n texlive-hyphen-polish
Hyphenation patterns for Polish in QX and UTF-8 encodings.
These patterns are also used by Polish TeX formats MeX and
LaMeX.
%post -n texlive-hyphen-polish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-polish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-polish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-polish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-pl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-pl.qx.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-pl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pl.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-polish.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-polish.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-polish.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-polish-%{texlive_version}.%{texlive_noarch}.3.0asvn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-portuguese
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Portuguese hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-pt.ec.tex)
Provides:       tex(hyph-pt.tex)
Provides:       tex(loadhyph-pt.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source78:       hyphen-portuguese.tar.xz

%description -n texlive-hyphen-portuguese
Hyphenation patterns for Portuguese in T1/EC and UTF-8
encodings.
%post -n texlive-hyphen-portuguese
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-portuguese 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-portuguese
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-portuguese
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-pt.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-pt.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-pt.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pt.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-pt.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-portuguese.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-portuguese.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-portuguese.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-portuguese-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-romanian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Romanian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-ro.ec.tex)
Provides:       tex(hyph-ro.tex)
Provides:       tex(loadhyph-ro.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source79:       hyphen-romanian.tar.xz

%description -n texlive-hyphen-romanian
Hyphenation patterns for Romanian in T1/EC and UTF-8 encodings.
The UTF-8 patterns use U+0219 for the character 's with comma
accent' and U+021B for 't with comma accent', but we may
consider using U+015F and U+0163 as well in the future.
Generated by PatGen2-output hyphen-level 9.
%post -n texlive-hyphen-romanian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-romanian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-romanian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-romanian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ro.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-ro.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ro.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ro.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romanian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romanian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romanian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-romanian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-romansh
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Romansh hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-quote-rm.tex)
Provides:       tex(hyph-rm.tex)
Provides:       tex(loadhyph-rm.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source80:       hyphen-romansh.tar.xz

%description -n texlive-hyphen-romansh
Hyphenation patterns for Romansh in ASCII encoding. They are
supposed to comply with the rules indicated by the Lia
Rumantscha (Romansh language society).
%post -n texlive-hyphen-romansh
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-romansh 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-romansh
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-romansh
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-rm.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-rm.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-rm.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-rm.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romansh.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romansh.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romansh.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-romansh-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-russian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Russian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires:       texlive-ruhyphen >= %{texlive_version}
#!BuildIgnore: texlive-ruhyphen
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-ru.t2a.tex)
Provides:       tex(hyph-ru.tex)
Provides:       tex(loadhyph-ru.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source81:       hyphen-russian.tar.xz

%description -n texlive-hyphen-russian
Hyphenation patterns for Russian in T2A and UTF-8 encodings.
For 8-bit engines, the 'ruhyphen' package provides a number of
different pattern sets, as well as different (8-bit) encodings,
that can be chosen at format-generation time. The UTF-8 version
only provides the default pattern set. A mechanism similar to
the one used for 8-bit patterns may be implemented in the
future.
%post -n texlive-hyphen-russian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-russian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-russian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-russian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-ru.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-ru.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-ru.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ru.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-ru.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-russian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-russian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-russian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-russian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-sanskrit
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Sanskrit hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyphen-sanskrit-doc >= %{texlive_version}
Provides:       tex(hyph-sa.tex)
Provides:       tex(loadhyph-sa.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source82:       hyphen-sanskrit.tar.xz
Source83:       hyphen-sanskrit.doc.tar.xz

%description -n texlive-hyphen-sanskrit
Hyphenation patterns for Sanskrit and Prakrit in
transliteration, and in Devanagari, Bengali, Kannada, Malayalam
and Telugu scripts for Unicode engines.

%package -n texlive-hyphen-sanskrit-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Documentation for texlive-hyphen-sanskrit
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hyphen-sanskrit-doc
This package includes the documentation for texlive-hyphen-sanskrit

%post -n texlive-hyphen-sanskrit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-sanskrit 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-sanskrit
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-sanskrit-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/hyph-utf8/languages/sa/hyphenmin.txt

%files -n texlive-hyphen-sanskrit
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sa.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sa.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sa.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-sanskrit.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-sanskrit.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-sanskrit.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-sanskrit-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-serbian
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn54568
Release:        0
Summary:        Serbian hyphenation patterns
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-sh-cyrl.t2a.tex)
Provides:       tex(hyph-sh-cyrl.tex)
Provides:       tex(hyph-sh-latn.ec.tex)
Provides:       tex(hyph-sh-latn.tex)
Provides:       tex(hyph-sr-cyrl.tex)
Provides:       tex(loadhyph-sr-cyrl.tex)
Provides:       tex(loadhyph-sr-latn.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source84:       hyphen-serbian.tar.xz

%description -n texlive-hyphen-serbian
Hyphenation patterns for Serbian in T1/EC, T2A and UTF-8
encodings. For 8-bit engines the patterns are available
separately as 'serbian' in T1/EC encoding for Latin script and
'serbianc' in T2A encoding for Cyrillic script. Unicode engines
should only use 'serbian' which has patterns in both scripts
combined.
%post -n texlive-hyphen-serbian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-serbian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-serbian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-serbian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sr-cyrl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sr-latn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-sh-cyrl.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-sh-latn.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sh-cyrl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sh-latn.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sr-cyrl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-cyrl.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sh-latn.pat.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sr-cyrl.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-serbian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-serbian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-serbian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-serbian-%{texlive_version}.%{texlive_noarch}.1.0asvn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-slovak
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Slovak hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-sk.ec.tex)
Provides:       tex(hyph-sk.tex)
Provides:       tex(loadhyph-sk.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source85:       hyphen-slovak.tar.xz

%description -n texlive-hyphen-slovak
Hyphenation patterns for Slovak in T1/EC and UTF-8 encodings.
Original patterns 'skhyphen' are still distributed in the
'csplain' package and loaded with ISO Latin 2 encoding (IL2).
%post -n texlive-hyphen-slovak
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-slovak 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-slovak
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-slovak
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-sk.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sk.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sk.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovak.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovak.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovak.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-slovak-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-slovenian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Slovenian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-sl.ec.tex)
Provides:       tex(hyph-sl.tex)
Provides:       tex(loadhyph-sl.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source86:       hyphen-slovenian.tar.xz

%description -n texlive-hyphen-slovenian
Hyphenation patterns for Slovenian in T1/EC and UTF-8
encodings.
%post -n texlive-hyphen-slovenian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-slovenian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-slovenian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-slovenian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-sl.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sl.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sl.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovenian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovenian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovenian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-slovenian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-spanish
Version:        %{texlive_version}.%{texlive_noarch}.4.5svn54568
Release:        0
Summary:        Spanish hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyphen-spanish-doc >= %{texlive_version}
Provides:       tex(hyph-es.ec.tex)
Provides:       tex(hyph-es.tex)
Provides:       tex(loadhyph-es.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source87:       hyphen-spanish.tar.xz
Source88:       hyphen-spanish.doc.tar.xz

%description -n texlive-hyphen-spanish
Hyphenation patterns for Spanish in T1/EC and UTF-8 encodings.

%package -n texlive-hyphen-spanish-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.5svn54568
Release:        0
Summary:        Documentation for texlive-hyphen-spanish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hyphen-spanish-doc:es)

%description -n texlive-hyphen-spanish-doc
This package includes the documentation for texlive-hyphen-spanish

%post -n texlive-hyphen-spanish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-spanish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-spanish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-spanish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/hyph-utf8/languages/es/README
%{_texmfdistdir}/doc/generic/hyph-utf8/languages/es/division.pdf

%files -n texlive-hyphen-spanish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-es.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-es.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-es.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-es.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-spanish.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-spanish.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-spanish.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-spanish-%{texlive_version}.%{texlive_noarch}.4.5svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-swedish
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Swedish hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-sv.ec.tex)
Provides:       tex(hyph-sv.tex)
Provides:       tex(loadhyph-sv.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source89:       hyphen-swedish.tar.xz

%description -n texlive-hyphen-swedish
Hyphenation patterns for Swedish in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-swedish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-swedish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-swedish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-swedish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-sv.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-sv.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-sv.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-sv.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-swedish.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-swedish.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-swedish.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-swedish-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-thai
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Thai hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-th.lth.tex)
Provides:       tex(hyph-th.tex)
Provides:       tex(loadhyph-th.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source90:       hyphen-thai.tar.xz

%description -n texlive-hyphen-thai
Hyphenation patterns for Thai in LTH and UTF-8 encodings.
%post -n texlive-hyphen-thai
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-thai 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-thai
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-thai
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-th.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-th.lth.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-th.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-th.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-thai.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-thai.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-thai.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-thai-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-turkish
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Turkish hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-tr.ec.tex)
Provides:       tex(hyph-tr.tex)
Provides:       tex(loadhyph-tr.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source91:       hyphen-turkish.tar.xz

%description -n texlive-hyphen-turkish
Hyphenation patterns for Turkish in T1/EC and UTF-8 encodings.
Auto-generated from a script included in the distribution. The
patterns for Turkish were first produced for the Ottoman Texts
Project in 1987 and were suitable for both Modern Turkish and
Ottoman Turkish in Latin script, however the required character
set didn't fit into EC encoding, so support for Ottoman Turkish
had to be dropped to keep compatibility with 8-bit engines.
%post -n texlive-hyphen-turkish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-turkish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-turkish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-turkish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-tr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-tr.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-tr.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-tr.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkish.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkish.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkish.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-turkish-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-turkmen
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Turkmen hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-tk.ec.tex)
Provides:       tex(hyph-tk.tex)
Provides:       tex(loadhyph-tk.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source92:       hyphen-turkmen.tar.xz

%description -n texlive-hyphen-turkmen
Hyphenation patterns for Turkmen in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-turkmen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-turkmen 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-turkmen
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-turkmen
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-tk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-tk.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-tk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-tk.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkmen.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkmen.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkmen.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-turkmen-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-ukrainian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Ukrainian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires:       texlive-ukrhyph >= %{texlive_version}
#!BuildIgnore: texlive-ukrhyph
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-quote-uk.tex)
Provides:       tex(hyph-uk.t2a.tex)
Provides:       tex(hyph-uk.tex)
Provides:       tex(loadhyph-uk.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source93:       hyphen-ukrainian.tar.xz

%description -n texlive-hyphen-ukrainian
Hyphenation patterns for Ukrainian in T2A and UTF-8 encodings.
For 8-bit engines, the 'ukrhyph' package provides a number of
different pattern sets, as well as different (8-bit) encodings,
that can be chosen at format-generation time. The UTF-8 version
only provides the default pattern set. A mechanism similar to
the one used for 8-bit patterns may be implemented in the
future.
%post -n texlive-hyphen-ukrainian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-ukrainian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-ukrainian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-ukrainian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-uk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-uk.t2a.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/quote/hyph-quote-uk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-uk.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-uk.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ukrainian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ukrainian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ukrainian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-ukrainian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-uppersorbian
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Upper Sorbian hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-hsb.ec.tex)
Provides:       tex(hyph-hsb.tex)
Provides:       tex(loadhyph-hsb.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source94:       hyphen-uppersorbian.tar.xz

%description -n texlive-hyphen-uppersorbian
Hyphenation patterns for Upper Sorbian in T1/EC and UTF-8
encodings.
%post -n texlive-hyphen-uppersorbian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-uppersorbian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-uppersorbian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-uppersorbian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-hsb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-hsb.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-hsb.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.hyp.txt
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-hsb.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-uppersorbian.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-uppersorbian.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-uppersorbian.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-uppersorbian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphen-welsh
Version:        %{texlive_version}.%{texlive_noarch}.svn54568
Release:        0
Summary:        Welsh hyphenation patterns
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(hyph-cy.ec.tex)
Provides:       tex(hyph-cy.tex)
Provides:       tex(loadhyph-cy.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source95:       hyphen-welsh.tar.xz

%description -n texlive-hyphen-welsh
Hyphenation patterns for Welsh in T1/EC and UTF-8 encodings.
%post -n texlive-hyphen-welsh
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-hyphen-welsh 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-hyphen-welsh
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphen-welsh
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/loadhyph-cy.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/ptex/hyph-cy.ec.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/tex/hyph-cy.tex
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/txt/hyph-cy.pat.txt
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-welsh.dat
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-welsh.def
%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-welsh.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphen-welsh-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif

%package -n texlive-hyphenat
Version:        %{texlive_version}.%{texlive_noarch}.2.3csvn15878
Release:        0
Summary:        Disable/enable hypenation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyphenat-doc >= %{texlive_version}
Provides:       tex(hyphenat.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source96:       hyphenat.tar.xz
Source97:       hyphenat.doc.tar.xz

%description -n texlive-hyphenat
This package can disable all hyphenation or enable hyphenation
of non-alphabetics or monospaced fonts. The package can also
enable hyphenation within 'words' that contain non-alphabetic
characters (e.g., that include underscores), and hyphenation of
text typeset in monospaced (e.g., cmtt) fonts.

%package -n texlive-hyphenat-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3csvn15878
Release:        0
Summary:        Documentation for texlive-hyphenat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hyphenat-doc
This package includes the documentation for texlive-hyphenat

%post -n texlive-hyphenat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hyphenat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hyphenat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphenat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hyphenat/README
%{_texmfdistdir}/doc/latex/hyphenat/hyphenat.pdf

%files -n texlive-hyphenat
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hyphenat/hyphenat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphenat-%{texlive_version}.%{texlive_noarch}.2.3csvn15878-%{release}-zypper
%endif

%package -n texlive-hyphenex
Version:        %{texlive_version}.%{texlive_noarch}.svn37354
Release:        0
Summary:        US English hyphenation exceptions file
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(ushyphex.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source98:       hyphenex.tar.xz

%description -n texlive-hyphenex
Exceptions for American English hyphenation patterns are
occasionally published in the TeX User Group journal TUGboat.
This bundle provides alternative Perl and Bourne shell scripts
to convert the source of such an article into an exceptions
file, together with a recent copy of the article and
machine-readable files.
%post -n texlive-hyphenex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hyphenex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hyphenex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyphenex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hyphenex/ushyphex.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyphenex-%{texlive_version}.%{texlive_noarch}.svn37354-%{release}-zypper
%endif

%package -n texlive-hyplain
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Basic support for multiple languages in Plain TeX
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-hyplain-doc >= %{texlive_version}
Provides:       tex(hylang.tex)
Provides:       tex(hyplain.tex)
Provides:       tex(hyrules.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source99:       hyplain.tar.xz
Source100:      hyplain.doc.tar.xz

%description -n texlive-hyplain
The package offers a means to set up hyphenation suitable for
several languages and/or dialects, and to select them or switch
between them while typesetting.

%package -n texlive-hyplain-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-hyplain
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hyplain-doc
This package includes the documentation for texlive-hyplain

%post -n texlive-hyplain
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hyplain 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hyplain
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hyplain-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/hyplain/README
%{_texmfdistdir}/doc/plain/hyplain/hydoc.pdf
%{_texmfdistdir}/doc/plain/hyplain/hydoc.tex

%files -n texlive-hyplain
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/hyplain/hylang.tex
%{_texmfdistdir}/tex/plain/hyplain/hypdfplain.ini
%{_texmfdistdir}/tex/plain/hyplain/hyplain.tex
%{_texmfdistdir}/tex/plain/hyplain/hyrules.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hyplain-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-ibycus-babel
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn15878
Release:        0
Summary:        Use the Ibycus 4 Greek font with Babel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ibycus-babel-doc >= %{texlive_version}
Provides:       tex(ibycus.ldf)
Provides:       tex(lgienc.def)
Provides:       tex(lgifib.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source101:      ibycus-babel.tar.xz
Source102:      ibycus-babel.doc.tar.xz

%description -n texlive-ibycus-babel
The package allows you to use the Ibycus 4 font for ancient
Greek with Babel. It uses a Perl script to generate hyphenation
patterns for Ibycus from those for the ordinary Babel encoding,
cbgreek. It sets up ibycus as a pseudo-language you can specify
in the normal Babel manner. For proper hyphenation of Greek
quoted in mid-paragraph, you should use it with elatex (all
current distributions of LaTeX are built with e-TeX, so the
constraint should not be onerous).

%package -n texlive-ibycus-babel-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn15878
Release:        0
Summary:        Documentation for texlive-ibycus-babel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ibycus-babel-doc
This package includes the documentation for texlive-ibycus-babel

%post -n texlive-ibycus-babel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ibycus-babel 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ibycus-babel
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ibycus-babel-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ibycus-babel/README
%{_texmfdistdir}/doc/latex/ibycus-babel/ibycus-babel-test.tex
%{_texmfdistdir}/doc/latex/ibycus-babel/ibycus-babel.pdf
%{_texmfdistdir}/doc/latex/ibycus-babel/ibyhyph.pl

%files -n texlive-ibycus-babel
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ibycus-babel/ibycus.ldf
%{_texmfdistdir}/tex/latex/ibycus-babel/lgienc.def
%{_texmfdistdir}/tex/latex/ibycus-babel/lgifib.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ibycus-babel-%{texlive_version}.%{texlive_noarch}.3.0svn15878-%{release}-zypper
%endif

%package -n texlive-ibygrk
Version:        %{texlive_version}.%{texlive_noarch}.4.5svn15878
Release:        0
Summary:        Fonts and macros to typeset ancient Greek
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-ibygrk-fonts >= %{texlive_version}
Recommends:     texlive-ibygrk-doc >= %{texlive_version}
Provides:       tex(IbycusHTG.enc)
Provides:       tex(Uibycus.fd)
Provides:       tex(Uibycus4.fd)
Provides:       tex(fibb84.tfm)
Provides:       tex(fibb848.tfm)
Provides:       tex(fibb849.tfm)
Provides:       tex(fibo84.tfm)
Provides:       tex(fibo848.tfm)
Provides:       tex(fibo849.tfm)
Provides:       tex(fibr84.tfm)
Provides:       tex(fibr848.tfm)
Provides:       tex(fibr849.tfm)
Provides:       tex(iby.map)
Provides:       tex(iby4extr.tex)
Provides:       tex(ibycus4.map)
Provides:       tex(ibycus4.map)
Provides:       tex(ibycus4.sty)
Provides:       tex(ibycus4.tex)
Provides:       tex(ibycusps.tex)
Provides:       tex(psibycus.sty)
Provides:       tex(pssetiby.tex)
Provides:       tex(setiby4.tex)
Provides:       tex(tlgsqq.tex)
Provides:       tex(version4.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source103:      ibygrk.tar.xz
Source104:      ibygrk.doc.tar.xz

%description -n texlive-ibygrk
Ibycus is a Greek typeface, based on Silvio Levy's realisation
of a classic Didot cut of Greek type from around 1800. The
fonts are available both as Metafont source and in Adobe Type 1
format. This distribution of ibycus is accompanied by a set of
macro packages to use it with Plain TeX or LaTeX, but for use
with Babel, see the ibycus-babel package.

%package -n texlive-ibygrk-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.5svn15878
Release:        0
Summary:        Documentation for texlive-ibygrk
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ibygrk-doc
This package includes the documentation for texlive-ibygrk


%package -n texlive-ibygrk-fonts
Version:        %{texlive_version}.%{texlive_noarch}.4.5svn15878
Release:        0
Summary:        Severed fonts for texlive-ibygrk
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-ibygrk-fonts
The  separated fonts package for texlive-ibygrk
%post -n texlive-ibygrk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap iby.map' >> /var/run/texlive/run-updmap

%postun -n texlive-ibygrk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap iby.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-ibygrk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-ibygrk-fonts
%files -n texlive-ibygrk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/ibygrk/COPYING
%{_texmfdistdir}/doc/fonts/ibygrk/NEWS
%{_texmfdistdir}/doc/fonts/ibygrk/README
%{_texmfdistdir}/doc/fonts/ibygrk/README.ibycus4
%{_texmfdistdir}/doc/fonts/ibygrk/iby4text.tex
%{_texmfdistdir}/doc/fonts/ibygrk/ibycus3.RME
%{_texmfdistdir}/doc/fonts/ibygrk/ibycus4.ltx
%{_texmfdistdir}/doc/fonts/ibygrk/psibycus.ltx
%{_texmfdistdir}/doc/fonts/ibygrk/psibycus.tex

%files -n texlive-ibygrk
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/ibygrk/fibb84.afm
%{_texmfdistdir}/fonts/afm/public/ibygrk/fibr84.afm
%{_texmfdistdir}/fonts/enc/dvips/ibygrk/IbycusHTG.enc
%{_texmfdistdir}/fonts/map/dvips/ibygrk/iby.map
%{_texmfdistdir}/fonts/source/public/ibygrk/abary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/cigma4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/digamma4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ebary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibb84.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibb848.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibb849.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibo84.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibo848.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibo849.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibr84.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibr848.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/fibr849.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/hbary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibyacc4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibycus4.map
%{_texmfdistdir}/fonts/source/public/ibygrk/ibycus4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibylig4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibylwr4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibypnct4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ibyupr4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/koppa4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/obary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/sampi4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/ubary4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/version4.mf
%{_texmfdistdir}/fonts/source/public/ibygrk/wbary4.mf
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibb84.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibb848.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibb849.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibo84.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibo848.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibo849.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibr84.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibr848.tfm
%{_texmfdistdir}/fonts/tfm/public/ibygrk/fibr849.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/ibygrk/fibb84.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/ibygrk/fibr84.pfb
%{_texmfdistdir}/tex/generic/ibygrk/Uibycus.fd
%{_texmfdistdir}/tex/generic/ibygrk/Uibycus4.fd
%{_texmfdistdir}/tex/generic/ibygrk/iby4extr.tex
%{_texmfdistdir}/tex/generic/ibygrk/ibycus4.map
%{_texmfdistdir}/tex/generic/ibygrk/ibycus4.sty
%{_texmfdistdir}/tex/generic/ibygrk/ibycus4.tex
%{_texmfdistdir}/tex/generic/ibygrk/ibycusps.tex
%{_texmfdistdir}/tex/generic/ibygrk/psibycus.sty
%{_texmfdistdir}/tex/generic/ibygrk/pssetiby.tex
%{_texmfdistdir}/tex/generic/ibygrk/setiby4.tex
%{_texmfdistdir}/tex/generic/ibygrk/tlgsqq.tex
%{_texmfdistdir}/tex/generic/ibygrk/version4.tex

%files -n texlive-ibygrk-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-ibygrk
%{_datadir}/fontconfig/conf.avail/58-texlive-ibygrk.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-ibygrk/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-ibygrk/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-ibygrk/fonts.scale
%{_datadir}/fonts/texlive-ibygrk/fibb84.pfb
%{_datadir}/fonts/texlive-ibygrk/fibr84.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ibygrk-fonts-%{texlive_version}.%{texlive_noarch}.4.5svn15878-%{release}-zypper
%endif

%package -n texlive-icite
Version:        %{texlive_version}.%{texlive_noarch}.1.3asvn54512
Release:        0
Summary:        Indices locorum citatorum
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-icite-doc >= %{texlive_version}
Provides:       tex(icite.sty)
Requires:       tex(datatool.sty)
Requires:       tex(usebib.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source105:      icite.tar.xz
Source106:      icite.doc.tar.xz

%description -n texlive-icite
The package is designed to produce from BibTeX or BibLaTeX
bibliographical databases the different indices of authors and
works cited which are called indices locorum citatorum. It
relies on a specific \icite command and can operate with either
BibTeX or BibLaTeX.

%package -n texlive-icite-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3asvn54512
Release:        0
Summary:        Documentation for texlive-icite
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-icite-doc
This package includes the documentation for texlive-icite

%post -n texlive-icite
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-icite 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-icite
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-icite-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/icite/README.md
%{_texmfdistdir}/doc/latex/icite/icite.pdf
%{_texmfdistdir}/doc/latex/icite/samples/bibsample.bib
%{_texmfdistdir}/doc/latex/icite/samples/icite-biblatex.pdf
%{_texmfdistdir}/doc/latex/icite/samples/icite-biblatex.tex
%{_texmfdistdir}/doc/latex/icite/samples/icite-minimal.pdf
%{_texmfdistdir}/doc/latex/icite/samples/icite-minimal.tex
%{_texmfdistdir}/doc/latex/icite/samples/icite-nobiblatex.pdf
%{_texmfdistdir}/doc/latex/icite/samples/icite-nobiblatex.tex

%files -n texlive-icite
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/icite/icite.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-icite-%{texlive_version}.%{texlive_noarch}.1.3asvn54512-%{release}-zypper
%endif

%package -n texlive-icsv
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Class for typesetting articles for the ICSV conference
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-icsv-doc >= %{texlive_version}
Provides:       tex(icsv.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(bm.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fix-cm.sty)
Requires:       tex(fixltx2e.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(helvet.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(textcomp.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source107:      icsv.tar.xz
Source108:      icsv.doc.tar.xz

%description -n texlive-icsv
This is an ad-hoc class for typesetting articles for the ICSV
conference, based on the earler active-conf by the same author.

%package -n texlive-icsv-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Documentation for texlive-icsv
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-icsv-doc
This package includes the documentation for texlive-icsv

%post -n texlive-icsv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-icsv 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-icsv
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-icsv-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/icsv/README
%{_texmfdistdir}/doc/latex/icsv/icsv-example.tex
%{_texmfdistdir}/doc/latex/icsv/icsv.pdf

%files -n texlive-icsv
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/icsv/icsv.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-icsv-%{texlive_version}.%{texlive_noarch}.0.0.2svn15878-%{release}-zypper
%endif

%package -n texlive-identkey
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.0svn49018
Release:        0
Summary:        Typesetting bracketed dichotomous identification keys
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-identkey-doc >= %{texlive_version}
Provides:       tex(identkey.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source109:      identkey.tar.xz
Source110:      identkey.doc.tar.xz

%description -n texlive-identkey
The package is for typesetting bracketed dichotomous
identification keys.

%package -n texlive-identkey-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.0svn49018
Release:        0
Summary:        Documentation for texlive-identkey
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-identkey-doc
This package includes the documentation for texlive-identkey

%post -n texlive-identkey
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-identkey 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-identkey
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-identkey-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/identkey/README.md

%files -n texlive-identkey
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/identkey/identkey.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-identkey-%{texlive_version}.%{texlive_noarch}.0.0.1.0svn49018-%{release}-zypper
%endif

%package -n texlive-idxcmds
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2csvn54554
Release:        0
Summary:        Semantic commands for adding formatted index entries
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-idxcmds-doc >= %{texlive_version}
Provides:       tex(idxcmds.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pgfopts.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source111:      idxcmds.tar.xz
Source112:      idxcmds.doc.tar.xz

%description -n texlive-idxcmds
The package provides commands for adding formatted index
entries; it arises from the author's work on large documents.

%package -n texlive-idxcmds-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2csvn54554
Release:        0
Summary:        Documentation for texlive-idxcmds
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-idxcmds-doc
This package includes the documentation for texlive-idxcmds

%post -n texlive-idxcmds
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-idxcmds 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-idxcmds
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-idxcmds-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/idxcmds/README
%{_texmfdistdir}/doc/latex/idxcmds/idxcmds_en.pdf
%{_texmfdistdir}/doc/latex/idxcmds/idxcmds_en.tex

%files -n texlive-idxcmds
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/idxcmds/idxcmds.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-idxcmds-%{texlive_version}.%{texlive_noarch}.0.0.2csvn54554-%{release}-zypper
%endif

%package -n texlive-idxlayout
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4dsvn25821
Release:        0
Summary:        Configurable index layout, responsive to KOMA-Script and memoir
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-idxlayout-doc >= %{texlive_version}
Provides:       tex(idxlayout.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(multicol.sty)
Requires:       tex(ragged2e.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source113:      idxlayout.tar.xz
Source114:      idxlayout.doc.tar.xz

%description -n texlive-idxlayout
The idxlayout package offers a key-value interface to configure
index layout parameters, e.g. allowing for three-column indexes
or for "parent" items and their affiliated subitems being
typeset as a single paragraph. The package is responsive to the
index-related options and commands of the KOMA-Script and
memoir classes.

%package -n texlive-idxlayout-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4dsvn25821
Release:        0
Summary:        Documentation for texlive-idxlayout
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-idxlayout-doc:en)

%description -n texlive-idxlayout-doc
This package includes the documentation for texlive-idxlayout

%post -n texlive-idxlayout
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-idxlayout 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-idxlayout
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-idxlayout-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/idxlayout/README
%{_texmfdistdir}/doc/latex/idxlayout/idxlayout.pdf

%files -n texlive-idxlayout
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/idxlayout/idxlayout.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-idxlayout-%{texlive_version}.%{texlive_noarch}.0.0.4dsvn25821-%{release}-zypper
%endif

%package -n texlive-ieeepes
Version:        %{texlive_version}.%{texlive_noarch}.4.0svn17359
Release:        0
Summary:        IEEE Power Engineering Society Transactions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ieeepes-doc >= %{texlive_version}
Provides:       tex(ieeepes.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(mathptm.sty)
Requires:       tex(times.sty)
Requires:       tex(vmargin.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source115:      ieeepes.tar.xz
Source116:      ieeepes.doc.tar.xz

%description -n texlive-ieeepes
Supports typesetting of transactions, as well as discussions
and closures, for the IEEE Power Engineering Society
Transactions journals.

%package -n texlive-ieeepes-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.0svn17359
Release:        0
Summary:        Documentation for texlive-ieeepes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ieeepes-doc
This package includes the documentation for texlive-ieeepes

%post -n texlive-ieeepes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ieeepes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ieeepes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ieeepes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ieeepes/README
%{_texmfdistdir}/doc/latex/ieeepes/ieeepes_check.bib
%{_texmfdistdir}/doc/latex/ieeepes/ieeepes_check.tex
%{_texmfdistdir}/doc/latex/ieeepes/ieeepes_doc.pdf
%{_texmfdistdir}/doc/latex/ieeepes/ieeepes_doc.tex
%{_texmfdistdir}/doc/latex/ieeepes/ieeepes_skel.tex
%{_texmfdistdir}/doc/latex/ieeepes/vk.eps

%files -n texlive-ieeepes
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/ieeepes/ieeepes.bst
%{_texmfdistdir}/tex/latex/ieeepes/ieeepes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ieeepes-%{texlive_version}.%{texlive_noarch}.4.0svn17359-%{release}-zypper
%endif

%package -n texlive-ietfbibs
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn41332
Release:        0
Summary:        Generate BibTeX entries for various IETF index files
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source117:      ietfbibs.doc.tar.xz

%description -n texlive-ietfbibs
The package provides scripts to translate IETF index files to
BibTeX files.
%post -n texlive-ietfbibs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ietfbibs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ietfbibs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ietfbibs
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/ietfbibs/CHANGELOG.md
%{_texmfdistdir}/doc/bibtex/ietfbibs/LICENSE.md
%{_texmfdistdir}/doc/bibtex/ietfbibs/Makefile
%{_texmfdistdir}/doc/bibtex/ietfbibs/README.md
%{_texmfdistdir}/doc/bibtex/ietfbibs/id2bib
%{_texmfdistdir}/doc/bibtex/ietfbibs/id2bib.awk
%{_texmfdistdir}/doc/bibtex/ietfbibs/ids.tex
%{_texmfdistdir}/doc/bibtex/ietfbibs/rfc2bib
%{_texmfdistdir}/doc/bibtex/ietfbibs/rfc2bib.awk
%{_texmfdistdir}/doc/bibtex/ietfbibs/rfcs.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ietfbibs-%{texlive_version}.%{texlive_noarch}.1.0.0svn41332-%{release}-zypper
%endif

%package -n texlive-iffont
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn38823
Release:        0
Summary:        Conditionally load fonts with fontspec
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-iffont-doc >= %{texlive_version}
Provides:       tex(iffont.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source118:      iffont.tar.xz
Source119:      iffont.doc.tar.xz

%description -n texlive-iffont
This package provides a macro to select the first font XeLaTeX
or LuaTeX can find in a comma separated list and, additionally,
a number of macro tests.

%package -n texlive-iffont-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn38823
Release:        0
Summary:        Documentation for texlive-iffont
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-iffont-doc
This package includes the documentation for texlive-iffont

%post -n texlive-iffont
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-iffont 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-iffont
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-iffont-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/iffont/README.md
%{_texmfdistdir}/doc/latex/iffont/iffont.pdf

%files -n texlive-iffont
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/iffont/iffont.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-iffont-%{texlive_version}.%{texlive_noarch}.1.0.0svn38823-%{release}-zypper
%endif

%package -n texlive-ifmslide
Version:        %{texlive_version}.%{texlive_noarch}.0.0.47svn20727
Release:        0
Summary:        Presentation slides for screen and printouts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ifmslide-doc >= %{texlive_version}
Provides:       tex(ifmslide.cfg)
Provides:       tex(ifmslide.sty)
Requires:       tex(amsbsy.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(fixseminar.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(texpower.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source120:      ifmslide.tar.xz
Source121:      ifmslide.doc.tar.xz

%description -n texlive-ifmslide
This package is used to produce printed slides with LaTeX and
online presentations with pdfLaTeX. It is provided by the
'Institute of Mechanics' (ifm) Univ. of Technology Darmstadt,
Germany. It is based on ideas of pdfslide, but completely
rewritten for compatibility with texpower and seminar. The
manual describes all functions and provides a sample.

%package -n texlive-ifmslide-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.47svn20727
Release:        0
Summary:        Documentation for texlive-ifmslide
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ifmslide-doc
This package includes the documentation for texlive-ifmslide

%post -n texlive-ifmslide
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ifmslide 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ifmslide
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ifmslide-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ifmslide/README
%{_texmfdistdir}/doc/latex/ifmslide/genbutton
%{_texmfdistdir}/doc/latex/ifmslide/ifmman.pdf
%{_texmfdistdir}/doc/latex/ifmslide/ifmman.tex

%files -n texlive-ifmslide
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ifmslide/aqua_ravines.eps
%{_texmfdistdir}/tex/latex/ifmslide/aqua_ravines.jpg
%{_texmfdistdir}/tex/latex/ifmslide/button1c.eps
%{_texmfdistdir}/tex/latex/ifmslide/button1c.pdf
%{_texmfdistdir}/tex/latex/ifmslide/button1e.eps
%{_texmfdistdir}/tex/latex/ifmslide/button1e.pdf
%{_texmfdistdir}/tex/latex/ifmslide/buttonec.eps
%{_texmfdistdir}/tex/latex/ifmslide/buttonec.pdf
%{_texmfdistdir}/tex/latex/ifmslide/buttonee.eps
%{_texmfdistdir}/tex/latex/ifmslide/buttonee.pdf
%{_texmfdistdir}/tex/latex/ifmslide/buttongc.eps
%{_texmfdistdir}/tex/latex/ifmslide/buttongc.pdf
%{_texmfdistdir}/tex/latex/ifmslide/buttonge.eps
%{_texmfdistdir}/tex/latex/ifmslide/buttonge.pdf
%{_texmfdistdir}/tex/latex/ifmslide/ifmlogoc.eps
%{_texmfdistdir}/tex/latex/ifmslide/ifmlogoc.pdf
%{_texmfdistdir}/tex/latex/ifmslide/ifmlogog.eps
%{_texmfdistdir}/tex/latex/ifmslide/ifmlogog.pdf
%{_texmfdistdir}/tex/latex/ifmslide/ifmslide.cfg
%{_texmfdistdir}/tex/latex/ifmslide/ifmslide.sty
%{_texmfdistdir}/tex/latex/ifmslide/liquid_helium.eps
%{_texmfdistdir}/tex/latex/ifmslide/liquid_helium.jpg
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ifmslide-%{texlive_version}.%{texlive_noarch}.0.0.47svn20727-%{release}-zypper
%endif

%package -n texlive-ifmtarg
Version:        %{texlive_version}.%{texlive_noarch}.1.2bsvn47544
Release:        0
Summary:        If-then-else command for processing potentially empty arguments
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ifmtarg-doc >= %{texlive_version}
Provides:       tex(ifmtarg.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source122:      ifmtarg.tar.xz
Source123:      ifmtarg.doc.tar.xz

%description -n texlive-ifmtarg
This package provides a command for the LaTeX programmer for
testing whether an argument is empty.

%package -n texlive-ifmtarg-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2bsvn47544
Release:        0
Summary:        Documentation for texlive-ifmtarg
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ifmtarg-doc
This package includes the documentation for texlive-ifmtarg

%post -n texlive-ifmtarg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ifmtarg 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ifmtarg
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ifmtarg-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ifmtarg/README
%{_texmfdistdir}/doc/latex/ifmtarg/ifmtarg.pdf

%files -n texlive-ifmtarg
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ifmtarg/ifmtarg.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ifmtarg-%{texlive_version}.%{texlive_noarch}.1.2bsvn47544-%{release}-zypper
%endif

%package -n texlive-ifnextok
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn23379
Release:        0
Summary:        Utility macro: peek ahead without ignoring spaces
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ifnextok-doc >= %{texlive_version}
Provides:       tex(ifnextok.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source124:      ifnextok.tar.xz
Source125:      ifnextok.doc.tar.xz

%description -n texlive-ifnextok
The package deals with the behaviour of the LaTeX internal
command \@ifnextchar, which skips blank spaces. This has the
potential to surprise users, since it can produce really
unwanted effects. A common example occurs with brackets
starting a line following \\: the command looks for an optional
argument, whereas the user wants the brackets to be printed.
The package offers commands and options for modifying this
behaviour, maybe limited to certain parts of the document
source.

%package -n texlive-ifnextok-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn23379
Release:        0
Summary:        Documentation for texlive-ifnextok
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ifnextok-doc
This package includes the documentation for texlive-ifnextok

%post -n texlive-ifnextok
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ifnextok 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ifnextok
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ifnextok-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ifnextok/README
%{_texmfdistdir}/doc/latex/ifnextok/RELEASEs.txt
%{_texmfdistdir}/doc/latex/ifnextok/SRCFILEs.txt
%{_texmfdistdir}/doc/latex/ifnextok/ifnextok.pdf
%{_texmfdistdir}/doc/latex/ifnextok/testIfNT.pdf

%files -n texlive-ifnextok
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ifnextok/ifnextok.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ifnextok-%{texlive_version}.%{texlive_noarch}.0.0.3svn23379-%{release}-zypper
%endif

%package -n texlive-ifoddpage
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn40726
Release:        0
Summary:        Determine if the current page is odd or even
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ifoddpage-doc >= %{texlive_version}
Provides:       tex(ifoddpage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source126:      ifoddpage.tar.xz
Source127:      ifoddpage.doc.tar.xz

%description -n texlive-ifoddpage
The package provides an \ifoddpage conditional to determine if
the current page is odd or even. The macro \checkoddpage must
be used direct before to check the page number using a label.
Two compiler runs are therefore required to achieve correct
results. In addition, the conditional \ifoddpageoronside is
provided which is also true in oneside mode where all pages use
the odd page layout.

%package -n texlive-ifoddpage-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn40726
Release:        0
Summary:        Documentation for texlive-ifoddpage
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ifoddpage-doc
This package includes the documentation for texlive-ifoddpage

%post -n texlive-ifoddpage
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ifoddpage 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ifoddpage
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ifoddpage-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ifoddpage/README
%{_texmfdistdir}/doc/latex/ifoddpage/ifoddpage.pdf

%files -n texlive-ifoddpage
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ifoddpage/ifoddpage.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ifoddpage-%{texlive_version}.%{texlive_noarch}.1.1svn40726-%{release}-zypper
%endif

%package -n texlive-ifplatform
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4asvn45533
Release:        0
Summary:        Conditionals to test which platform is being used
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ifplatform-doc >= %{texlive_version}
Provides:       tex(ifplatform.sty)
Requires:       tex(catchfile.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(shellesc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source128:      ifplatform.tar.xz
Source129:      ifplatform.doc.tar.xz

%description -n texlive-ifplatform
This package uses the (La)TeX extension -shell-escape to
establish whether the document is being processed on a Windows
or on a Unix-like system (Mac OS X, Linux, etc.), or on Cygwin
(Unix environment over a windows system). Booleans provided
are: \ifwindows, \iflinux, \ifmacosx and \ifcygwin. The package
also preserves the output of uname on a Unix-like system, which
may be used to distinguish between various classes of Unix
systems.

%package -n texlive-ifplatform-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4asvn45533
Release:        0
Summary:        Documentation for texlive-ifplatform
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ifplatform-doc
This package includes the documentation for texlive-ifplatform

%post -n texlive-ifplatform
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ifplatform 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ifplatform
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ifplatform-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ifplatform/README
%{_texmfdistdir}/doc/latex/ifplatform/ifplatform.pdf

%files -n texlive-ifplatform
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ifplatform/ifplatform.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ifplatform-%{texlive_version}.%{texlive_noarch}.0.0.4asvn45533-%{release}-zypper
%endif

%package -n texlive-ifptex
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn52626
Release:        0
Summary:        Check if the engine is pTeX or one of its derivatives
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ifptex-doc >= %{texlive_version}
Provides:       tex(ifptex.sty)
Provides:       tex(ifuptex.sty)
Requires:       tex(iftex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source130:      ifptex.tar.xz
Source131:      ifptex.doc.tar.xz

%description -n texlive-ifptex
The ifptex package is a counterpart of ifxetex, ifluatex, etc.
for the ptex engine. The ifuptex package is an alias to ifptex
provided for backward compatibility.

%package -n texlive-ifptex-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn52626
Release:        0
Summary:        Documentation for texlive-ifptex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-ifptex-doc:ja)

%description -n texlive-ifptex-doc
This package includes the documentation for texlive-ifptex

%post -n texlive-ifptex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ifptex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ifptex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ifptex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/ifptex/LICENSE
%{_texmfdistdir}/doc/generic/ifptex/README-ja.md
%{_texmfdistdir}/doc/generic/ifptex/README.md

%files -n texlive-ifptex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/ifptex/ifptex.sty
%{_texmfdistdir}/tex/generic/ifptex/ifuptex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ifptex-%{texlive_version}.%{texlive_noarch}.2.0svn52626-%{release}-zypper
%endif

%package -n texlive-ifsym
Version:        %{texlive_version}.%{texlive_noarch}.svn24868
Release:        0
Summary:        A collection of symbols
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ifsym-doc >= %{texlive_version}
Provides:       tex(ifclk10.tfm)
Provides:       tex(ifclkb10.tfm)
Provides:       tex(ifgeo10.tfm)
Provides:       tex(ifgeob10.tfm)
Provides:       tex(ifgeobn10.tfm)
Provides:       tex(ifgeobw10.tfm)
Provides:       tex(ifgeon10.tfm)
Provides:       tex(ifgeow10.tfm)
Provides:       tex(ifsym.sty)
Provides:       tex(ifsym10.tfm)
Provides:       tex(ifsymb10.tfm)
Provides:       tex(ifsymbi10.tfm)
Provides:       tex(ifsymi10.tfm)
Provides:       tex(ifwea10.tfm)
Provides:       tex(ifweab10.tfm)
Provides:       tex(uifblk.fd)
Provides:       tex(uifclk.fd)
Provides:       tex(uifgeo.fd)
Provides:       tex(uifsym.fd)
Provides:       tex(uifwea.fd)
Requires:       tex(calc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source132:      ifsym.tar.xz
Source133:      ifsym.doc.tar.xz

%description -n texlive-ifsym
A set of symbol fonts, written in Metafont, offering
(respectively) clock-face symbols, geometrical symbols, weather
symbols, mountaineering symbols, electronic circuit symbols and
a set of miscellaneous symbols. A LaTeX package is provided,
that allows the user to load only those symbols needed in a
document.

%package -n texlive-ifsym-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn24868
Release:        0
Summary:        Documentation for texlive-ifsym
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-ifsym-doc:de)

%description -n texlive-ifsym-doc
This package includes the documentation for texlive-ifsym

%post -n texlive-ifsym
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ifsym 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ifsym
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ifsym-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/ifsym/ifsym.ps

%files -n texlive-ifsym
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/ifsym/ifclk.gen
%{_texmfdistdir}/fonts/source/public/ifsym/ifclk10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifclkb10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeo.gen
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeo10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeob10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeobn10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeobw10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeon10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeow10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifsym.gen
%{_texmfdistdir}/fonts/source/public/ifsym/ifsym10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifsymb10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifsymbi10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifsymi10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifwea.gen
%{_texmfdistdir}/fonts/source/public/ifsym/ifwea10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifweab10.mf
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifclk10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifclkb10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeo10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeob10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeobn10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeobw10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeon10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeow10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifsym10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifsymb10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifsymbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifsymi10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifwea10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifweab10.tfm
%{_texmfdistdir}/tex/latex/ifsym/ifsym.sty
%{_texmfdistdir}/tex/latex/ifsym/uifblk.fd
%{_texmfdistdir}/tex/latex/ifsym/uifclk.fd
%{_texmfdistdir}/tex/latex/ifsym/uifgeo.fd
%{_texmfdistdir}/tex/latex/ifsym/uifsym.fd
%{_texmfdistdir}/tex/latex/ifsym/uifwea.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ifsym-%{texlive_version}.%{texlive_noarch}.svn24868-%{release}-zypper
%endif

%package -n texlive-iftex
Version:        %{texlive_version}.%{texlive_noarch}.1.0dsvn54159
Release:        0
Summary:        Am I running under pdfTeX, XeTeX or LuaTeX?
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-iftex-doc >= %{texlive_version}
Provides:       tex(ifetex.sty)
Provides:       tex(ifluatex.sty)
Provides:       tex(ifpdf.sty)
Provides:       tex(iftex.sty)
Provides:       tex(ifvtex.sty)
Provides:       tex(ifxetex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source134:      iftex.tar.xz
Source135:      iftex.doc.tar.xz

%description -n texlive-iftex
The package, which works both for Plain TeX and for LaTeX,
defines the \ifPDFTeX, \ifXeTeX, and \ifLuaTeX conditionals for
testing which engine is being used for typesetting. The package
also provides the \RequirePDFTeX, \RequireXeTeX, and
\RequireLuaTeX commands which throw an error if pdfTeX, XeTeX
or LuaTeX (respectively) is not the engine in use.

%package -n texlive-iftex-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0dsvn54159
Release:        0
Summary:        Documentation for texlive-iftex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-iftex-doc
This package includes the documentation for texlive-iftex

%post -n texlive-iftex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-iftex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-iftex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-iftex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/iftex/README.md
%{_texmfdistdir}/doc/generic/iftex/iftex.pdf
%{_texmfdistdir}/doc/generic/iftex/iftex.tex

%files -n texlive-iftex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/iftex/ifetex.sty
%{_texmfdistdir}/tex/generic/iftex/ifluatex.sty
%{_texmfdistdir}/tex/generic/iftex/ifpdf.sty
%{_texmfdistdir}/tex/generic/iftex/iftex.sty
%{_texmfdistdir}/tex/generic/iftex/ifvtex.sty
%{_texmfdistdir}/tex/generic/iftex/ifxetex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-iftex-%{texlive_version}.%{texlive_noarch}.1.0dsvn54159-%{release}-zypper
%endif

%package -n texlive-ifthenx
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1asvn25819
Release:        0
Summary:        Extra tests for \ifthenelse
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ifthenx-doc >= %{texlive_version}
Provides:       tex(ifthenx.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source136:      ifthenx.tar.xz
Source137:      ifthenx.doc.tar.xz

%description -n texlive-ifthenx
The package extends the ifthen package, providing extra
predicates for the package's \ifthenelse command. The package
is complementary to xifthen, in that they provide different
facilities; the two may be loaded in the same document, as long
as xifthen is loaded first.

%package -n texlive-ifthenx-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1asvn25819
Release:        0
Summary:        Documentation for texlive-ifthenx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ifthenx-doc
This package includes the documentation for texlive-ifthenx

%post -n texlive-ifthenx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ifthenx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ifthenx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ifthenx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ifthenx/README

%files -n texlive-ifthenx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ifthenx/ifthenx.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ifthenx-%{texlive_version}.%{texlive_noarch}.0.0.1asvn25819-%{release}-zypper
%endif

%package -n texlive-ifxptex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn46153
Release:        0
Summary:        Detect pTeX and its derivatives
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ifxptex-doc >= %{texlive_version}
Provides:       tex(ifxptex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source138:      ifxptex.tar.xz
Source139:      ifxptex.doc.tar.xz

%description -n texlive-ifxptex
The package provides commands for detecting pTeX and its
derivatives (e-pTeX, upTeX, e-upTeX, and ApTeX). Both LaTeX and
plain TeX are supported.

%package -n texlive-ifxptex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn46153
Release:        0
Summary:        Documentation for texlive-ifxptex
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ifxptex-doc
This package includes the documentation for texlive-ifxptex

%post -n texlive-ifxptex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ifxptex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ifxptex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ifxptex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/ifxptex/README
%{_texmfdistdir}/doc/generic/ifxptex/ifxptex-doc.pdf
%{_texmfdistdir}/doc/generic/ifxptex/ifxptex-doc.tex

%files -n texlive-ifxptex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/ifxptex/ifxptex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ifxptex-%{texlive_version}.%{texlive_noarch}.0.0.2svn46153-%{release}-zypper
%endif

%package -n texlive-iitem
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn29613
Release:        0
Summary:        Multiple level of lists in one list-like environment
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-iitem-doc >= %{texlive_version}
Provides:       tex(iitem.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source140:      iitem.tar.xz
Source141:      iitem.doc.tar.xz

%description -n texlive-iitem
The package defines multiple level lists within one list-like
environment. instead of writing \begin{enumerate} \item 1
\begin{enumerate} \item 2 \begin{enumerate} \item 3
\begin{enumerate} \item 4 \end{enumerate} \end{enumerate} \item
2.1 \end{enumerate} \item 1.1 \begin{enumerate} \item 2
\end{enumerate} \end{enumerate} this package allows you to
write \begin{enumerate} \item 1 \iitem 2 \iiitem 3 \ivtem 4
\iitem 2.1 \item 1.1 \iitem 2 \end{enumerate}

%package -n texlive-iitem-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn29613
Release:        0
Summary:        Documentation for texlive-iitem
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-iitem-doc
This package includes the documentation for texlive-iitem

%post -n texlive-iitem
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-iitem 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-iitem
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-iitem-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/iitem/README
%{_texmfdistdir}/doc/latex/iitem/iitem.pdf

%files -n texlive-iitem
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/iitem/iitem.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-iitem-%{texlive_version}.%{texlive_noarch}.1.0svn29613-%{release}-zypper
%endif

%package -n texlive-ijmart
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn30958
Release:        0
Summary:        LaTeX Class for the Israel Journal of Mathematics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ijmart-doc >= %{texlive_version}
Provides:       tex(ijmart.cls)
Requires:       tex(amsart.cls)
Requires:       tex(fancyhdr.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(lastpage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source142:      ijmart.tar.xz
Source143:      ijmart.doc.tar.xz

%description -n texlive-ijmart
The Israel Journal of Mathematics is published by The Hebrew
University Magnes Press. This class provides LaTeX support for
its authors and editors. It strives to achieve the distinct
"look and feel" of the journal, while having the interface
similar to that of the amsart document class. This will help
authors already familiar with amsart to easily submit
manuscripts for The Israel Journal of Mathematics or to put the
preprints in arXiv with minimal changes in the LaTeX source.

%package -n texlive-ijmart-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn30958
Release:        0
Summary:        Documentation for texlive-ijmart
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ijmart-doc
This package includes the documentation for texlive-ijmart

%post -n texlive-ijmart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ijmart 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ijmart
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ijmart-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ijmart/Makefile
%{_texmfdistdir}/doc/latex/ijmart/README
%{_texmfdistdir}/doc/latex/ijmart/ijmart.bib
%{_texmfdistdir}/doc/latex/ijmart/ijmart.pdf
%{_texmfdistdir}/doc/latex/ijmart/ijmsample.bib
%{_texmfdistdir}/doc/latex/ijmart/ijmsample.pdf
%{_texmfdistdir}/doc/latex/ijmart/ijmsample.tex

%files -n texlive-ijmart
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/ijmart/ijmart.bst
%{_texmfdistdir}/tex/latex/ijmart/ijmart.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ijmart-%{texlive_version}.%{texlive_noarch}.1.7svn30958-%{release}-zypper
%endif

%package -n texlive-ijqc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn15878
Release:        0
Summary:        BibTeX style file for the Intl. J. Quantum Chem
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ijqc-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source144:      ijqc.tar.xz
Source145:      ijqc.doc.tar.xz

%description -n texlive-ijqc
ijqc.bst is a BibTeX style file to support publication in
Wiley's International Journal of Quantum Chemistry. It is not
in any way officially endorsed by the publisher or editors, and
is provided without any warranty one could ever think of.

%package -n texlive-ijqc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn15878
Release:        0
Summary:        Documentation for texlive-ijqc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ijqc-doc
This package includes the documentation for texlive-ijqc

%post -n texlive-ijqc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ijqc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ijqc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ijqc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/ijqc/README
%{_texmfdistdir}/doc/bibtex/ijqc/makefile
%{_texmfdistdir}/doc/bibtex/ijqc/mybib.bib
%{_texmfdistdir}/doc/bibtex/ijqc/xampl.pdf
%{_texmfdistdir}/doc/bibtex/ijqc/xampl.tex

%files -n texlive-ijqc
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/ijqc/ijqc.bst
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ijqc-%{texlive_version}.%{texlive_noarch}.1.2svn15878-%{release}-zypper
%endif

%package -n texlive-ijsra
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn44886
Release:        0
Summary:        LaTeX document class for the International Journal of Student Research in Archaeology
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ijsra-doc >= %{texlive_version}
Provides:       tex(ijsra.cls)
Requires:       tex(abbrevs.sty)
Requires:       tex(alertmessage.sty)
Requires:       tex(babel.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(chngcntr.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(currfile-abspath.sty)
Requires:       tex(currfile.sty)
Requires:       tex(draftfigure.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(filecontents.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifvtex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(lettrine.sty)
Requires:       tex(listings.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multirow.sty)
Requires:       tex(nth.sty)
Requires:       tex(paralist.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(scrhack.sty)
Requires:       tex(setspace.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(url.sty)
Requires:       tex(wrapfig.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source146:      ijsra.tar.xz
Source147:      ijsra.doc.tar.xz

%description -n texlive-ijsra
This is a document class called ijsra which is used for the
International Journal of Student Research in Archaeology.

%package -n texlive-ijsra-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn44886
Release:        0
Summary:        Documentation for texlive-ijsra
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ijsra-doc
This package includes the documentation for texlive-ijsra

%post -n texlive-ijsra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ijsra 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ijsra
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ijsra-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ijsra/README.md
%{_texmfdistdir}/doc/latex/ijsra/ijsra.pdf
%{_texmfdistdir}/doc/latex/ijsra/ijsra.tex

%files -n texlive-ijsra
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ijsra/ijsra.cls
%{_texmfdistdir}/tex/latex/ijsra/ijsra_logo.png
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ijsra-%{texlive_version}.%{texlive_noarch}.1.1svn44886-%{release}-zypper
%endif

%package -n texlive-imac
Version:        %{texlive_version}.%{texlive_noarch}.svn17347
Release:        0
Summary:        International Modal Analysis Conference format
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-imac-doc >= %{texlive_version}
Provides:       tex(imac.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(cite.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source148:      imac.tar.xz
Source149:      imac.doc.tar.xz

%description -n texlive-imac
A set of files for producing correctly formatted documents for
the International Modal Analysis Conference. The bundle
provides a LaTeX package and a BibTeX style file.

%package -n texlive-imac-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn17347
Release:        0
Summary:        Documentation for texlive-imac
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-imac-doc
This package includes the documentation for texlive-imac

%post -n texlive-imac
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-imac 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-imac
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-imac-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/imac/imac.bib
%{_texmfdistdir}/doc/latex/imac/imac.pdf
%{_texmfdistdir}/doc/latex/imac/imac.tex
%{_texmfdistdir}/doc/latex/imac/readme.txt

%files -n texlive-imac
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/imac/imac.bst
%{_texmfdistdir}/tex/latex/imac/imac.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-imac-%{texlive_version}.%{texlive_noarch}.svn17347-%{release}-zypper
%endif

%package -n texlive-image-gallery
Version:        %{texlive_version}.%{texlive_noarch}.1.0jsvn15878
Release:        0
Summary:        Create an overview of pictures from a digital camera or from other sources
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-image-gallery-doc >= %{texlive_version}
Provides:       tex(image-gallery.cls)
Requires:       tex(article.cls)
Requires:       tex(color.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source150:      image-gallery.tar.xz
Source151:      image-gallery.doc.tar.xz

%description -n texlive-image-gallery
The class may be used to create an overview of pictures from a
digital camera or from other sources. It is possible to adjust
the size of the pictures and all the margins. The example file
shows the usage.

%package -n texlive-image-gallery-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0jsvn15878
Release:        0
Summary:        Documentation for texlive-image-gallery
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-image-gallery-doc
This package includes the documentation for texlive-image-gallery

%post -n texlive-image-gallery
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-image-gallery 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-image-gallery
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-image-gallery-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/image-gallery/README
%{_texmfdistdir}/doc/latex/image-gallery/gallery-example.pdf
%{_texmfdistdir}/doc/latex/image-gallery/gallery-example.tex
%{_texmfdistdir}/doc/latex/image-gallery/mypics.txt
%{_texmfdistdir}/doc/latex/image-gallery/pic001.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic002.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic003.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic004.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic005.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic006.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic007.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic008.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic009.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic010.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic011.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic012.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic013.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic014.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic015.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic016.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic017.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic018.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic019.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic020.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic021.jpg
%{_texmfdistdir}/doc/latex/image-gallery/pic022.jpg

%files -n texlive-image-gallery
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/image-gallery/image-gallery.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-image-gallery-%{texlive_version}.%{texlive_noarch}.1.0jsvn15878-%{release}-zypper
%endif

%package -n texlive-imakeidx
Version:        %{texlive_version}.%{texlive_noarch}.1.3esvn42287
Release:        0
Summary:        A package for producing multiple indexes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-imakeidx-doc >= %{texlive_version}
Provides:       tex(imakeidx.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(multicol.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source152:      imakeidx.tar.xz
Source153:      imakeidx.doc.tar.xz

%description -n texlive-imakeidx
The package enables the user to produce and typeset one or more
indexes simultaneously with a document. The package is known to
work in LaTeX documents processed with pdfLaTeX, XeLaTeX and
LuaLaTeX. If makeindex is used for processing the index
entries, no particular setting up is needed when TeX Live is
used. Using xindy or other programs it is necessary to enable
shell escape; shell escape is also needed if splitindex is
used.

%package -n texlive-imakeidx-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3esvn42287
Release:        0
Summary:        Documentation for texlive-imakeidx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-imakeidx-doc
This package includes the documentation for texlive-imakeidx

%post -n texlive-imakeidx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-imakeidx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-imakeidx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-imakeidx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/imakeidx/README
%{_texmfdistdir}/doc/latex/imakeidx/imakeidx.pdf
%{_texmfdistdir}/doc/latex/imakeidx/manifest.txt

%files -n texlive-imakeidx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/imakeidx/imakeidx.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-imakeidx-%{texlive_version}.%{texlive_noarch}.1.3esvn42287-%{release}-zypper
%endif

%package -n texlive-imfellenglish
Version:        %{texlive_version}.%{texlive_noarch}.svn38547
Release:        0
Summary:        IM Fell English fonts with LaTeX support
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-imfellenglish-fonts >= %{texlive_version}
Recommends:     texlive-imfellenglish-doc >= %{texlive_version}
Provides:       tex(IM_FELL_English_Italic-tlf-ly1--base.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-ly1--lcdfj.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-ly1.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-ly1.vf)
Provides:       tex(IM_FELL_English_Italic-tlf-ot1--base.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-ot1--lcdfj.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-ot1.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-ot1.vf)
Provides:       tex(IM_FELL_English_Italic-tlf-t1--base.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-t1--lcdfj.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-t1.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-t1.vf)
Provides:       tex(IM_FELL_English_Italic-tlf-ts1--base.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-ts1.tfm)
Provides:       tex(IM_FELL_English_Italic-tlf-ts1.vf)
Provides:       tex(IM_FELL_English_Roman-tlf-ly1--base.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-ly1--lcdfj.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-ly1.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-ly1.vf)
Provides:       tex(IM_FELL_English_Roman-tlf-ot1--base.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-ot1--lcdfj.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-ot1.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-ot1.vf)
Provides:       tex(IM_FELL_English_Roman-tlf-t1--base.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-t1--lcdfj.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-t1.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-t1.vf)
Provides:       tex(IM_FELL_English_Roman-tlf-ts1--base.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-ts1.tfm)
Provides:       tex(IM_FELL_English_Roman-tlf-ts1.vf)
Provides:       tex(IM_FELL_English_SC-tlf-ly1--base.tfm)
Provides:       tex(IM_FELL_English_SC-tlf-ly1.tfm)
Provides:       tex(IM_FELL_English_SC-tlf-ly1.vf)
Provides:       tex(IM_FELL_English_SC-tlf-ot1--base.tfm)
Provides:       tex(IM_FELL_English_SC-tlf-ot1.tfm)
Provides:       tex(IM_FELL_English_SC-tlf-ot1.vf)
Provides:       tex(IM_FELL_English_SC-tlf-t1--base.tfm)
Provides:       tex(IM_FELL_English_SC-tlf-t1.tfm)
Provides:       tex(IM_FELL_English_SC-tlf-t1.vf)
Provides:       tex(IM_FELL_English_SC-tlf-ts1--base.tfm)
Provides:       tex(IM_FELL_English_SC-tlf-ts1.tfm)
Provides:       tex(IM_FELL_English_SC-tlf-ts1.vf)
Provides:       tex(LY1IMFELLEnglish-TLF.fd)
Provides:       tex(OT1IMFELLEnglish-TLF.fd)
Provides:       tex(T1IMFELLEnglish-TLF.fd)
Provides:       tex(TS1IMFELLEnglish-TLF.fd)
Provides:       tex(imfe_5cupvv.enc)
Provides:       tex(imfe_cycd4j.enc)
Provides:       tex(imfe_dc7pev.enc)
Provides:       tex(imfe_fhc46f.enc)
Provides:       tex(imfe_qauovj.enc)
Provides:       tex(imfe_s6atnx.enc)
Provides:       tex(imfe_uut767.enc)
Provides:       tex(imfe_wnjo6u.enc)
Provides:       tex(imfe_zxj6gt.enc)
Provides:       tex(imfellEnglish.map)
Provides:       tex(imfellEnglish.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source154:      imfellenglish.tar.xz
Source155:      imfellenglish.doc.tar.xz

%description -n texlive-imfellenglish
Igino Marini has implemented digital revivals of fonts
bequeathed to Oxford University by Dr. John Fell, Bishop of
Oxford and Dean of Christ Church in 1686. This package provides
the English family, consisting of Roman, Italic and Small-Cap
fonts.

%package -n texlive-imfellenglish-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn38547
Release:        0
Summary:        Documentation for texlive-imfellenglish
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-imfellenglish-doc
This package includes the documentation for texlive-imfellenglish


%package -n texlive-imfellenglish-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn38547
Release:        0
Summary:        Severed fonts for texlive-imfellenglish
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-imfellenglish-fonts
The  separated fonts package for texlive-imfellenglish
%post -n texlive-imfellenglish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap imfellEnglish.map' >> /var/run/texlive/run-updmap

%postun -n texlive-imfellenglish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap imfellEnglish.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-imfellenglish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-imfellenglish-fonts
%files -n texlive-imfellenglish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/imfellenglish/COPYING
%{_texmfdistdir}/doc/fonts/imfellenglish/README
%{_texmfdistdir}/doc/fonts/imfellenglish/imfellEnglish.pdf
%{_texmfdistdir}/doc/fonts/imfellenglish/imfellEnglish.tex

%files -n texlive-imfellenglish
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/imfellenglish/imfe_5cupvv.enc
%{_texmfdistdir}/fonts/enc/dvips/imfellenglish/imfe_cycd4j.enc
%{_texmfdistdir}/fonts/enc/dvips/imfellenglish/imfe_dc7pev.enc
%{_texmfdistdir}/fonts/enc/dvips/imfellenglish/imfe_fhc46f.enc
%{_texmfdistdir}/fonts/enc/dvips/imfellenglish/imfe_qauovj.enc
%{_texmfdistdir}/fonts/enc/dvips/imfellenglish/imfe_s6atnx.enc
%{_texmfdistdir}/fonts/enc/dvips/imfellenglish/imfe_uut767.enc
%{_texmfdistdir}/fonts/enc/dvips/imfellenglish/imfe_wnjo6u.enc
%{_texmfdistdir}/fonts/enc/dvips/imfellenglish/imfe_zxj6gt.enc
%{_texmfdistdir}/fonts/map/dvips/imfellenglish/imfellEnglish.map
%verify(link) %{_texmfdistdir}/fonts/opentype/iginomarini/imfellenglish/IMFeENit28P.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/iginomarini/imfellenglish/IMFeENrm28P.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/iginomarini/imfellenglish/IMFeENsc28P.otf
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/iginomarini/imfellenglish/IM_FELL_English_Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/iginomarini/imfellenglish/IM_FELL_English_ItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/iginomarini/imfellenglish/IM_FELL_English_Roman.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/iginomarini/imfellenglish/IM_FELL_English_RomanLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/iginomarini/imfellenglish/IM_FELL_English_SC.pfb
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_Roman-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/iginomarini/imfellenglish/IM_FELL_English_SC-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/imfellenglish/LY1IMFELLEnglish-TLF.fd
%{_texmfdistdir}/tex/latex/imfellenglish/OT1IMFELLEnglish-TLF.fd
%{_texmfdistdir}/tex/latex/imfellenglish/T1IMFELLEnglish-TLF.fd
%{_texmfdistdir}/tex/latex/imfellenglish/TS1IMFELLEnglish-TLF.fd
%{_texmfdistdir}/tex/latex/imfellenglish/imfellEnglish.sty

%files -n texlive-imfellenglish-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-imfellenglish
%{_datadir}/fontconfig/conf.avail/58-texlive-imfellenglish.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-imfellenglish.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-imfellenglish.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-imfellenglish/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-imfellenglish/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-imfellenglish/fonts.scale
%{_datadir}/fonts/texlive-imfellenglish/IMFeENit28P.otf
%{_datadir}/fonts/texlive-imfellenglish/IMFeENrm28P.otf
%{_datadir}/fonts/texlive-imfellenglish/IMFeENsc28P.otf
%{_datadir}/fonts/texlive-imfellenglish/IM_FELL_English_Italic.pfb
%{_datadir}/fonts/texlive-imfellenglish/IM_FELL_English_ItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-imfellenglish/IM_FELL_English_Roman.pfb
%{_datadir}/fonts/texlive-imfellenglish/IM_FELL_English_RomanLCDFJ.pfb
%{_datadir}/fonts/texlive-imfellenglish/IM_FELL_English_SC.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-imfellenglish-fonts-%{texlive_version}.%{texlive_noarch}.svn38547-%{release}-zypper
%endif

%package -n texlive-impatient
Version:        %{texlive_version}.%{texlive_noarch}.2020svn54080
Release:        0
Summary:        Free edition of the book "TeX for the Impatient"
License:        GFDL-1.2-only
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source156:      impatient.doc.tar.xz

%description -n texlive-impatient
"TeX for the Impatient" is a book (of around 350 pages) on TeX,
Plain TeX and Eplain. The book is also available in French and
Chinese translations.
%post -n texlive-impatient
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-impatient 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-impatient
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-impatient
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/impatient/ChangeLog
%{_texmfdistdir}/doc/plain/impatient/Makefile
%{_texmfdistdir}/doc/plain/impatient/NEWS
%{_texmfdistdir}/doc/plain/impatient/README
%{_texmfdistdir}/doc/plain/impatient/backm.tex
%{_texmfdistdir}/doc/plain/impatient/book.ccs
%{_texmfdistdir}/doc/plain/impatient/book.pdf
%{_texmfdistdir}/doc/plain/impatient/book.sdx
%{_texmfdistdir}/doc/plain/impatient/book.tex
%{_texmfdistdir}/doc/plain/impatient/capsule.tex
%{_texmfdistdir}/doc/plain/impatient/concepts.tex
%{_texmfdistdir}/doc/plain/impatient/config.tex
%{_texmfdistdir}/doc/plain/impatient/copyrght.tex
%{_texmfdistdir}/doc/plain/impatient/diffs/impatient-2.0-2.3.diff.gz
%{_texmfdistdir}/doc/plain/impatient/diffs/impatient-2.3-2.4.diff.gz
%{_texmfdistdir}/doc/plain/impatient/diffs/impatient-2.4-2020.diff.gz
%{_texmfdistdir}/doc/plain/impatient/eplain.tex
%{_texmfdistdir}/doc/plain/impatient/errata.future
%{_texmfdistdir}/doc/plain/impatient/errors.tex
%{_texmfdistdir}/doc/plain/impatient/examples.tex
%{_texmfdistdir}/doc/plain/impatient/fdl.tex
%{_texmfdistdir}/doc/plain/impatient/fonts.tex
%{_texmfdistdir}/doc/plain/impatient/frontm.tex
%{_texmfdistdir}/doc/plain/impatient/genops.tex
%{_texmfdistdir}/doc/plain/impatient/index.tex
%{_texmfdistdir}/doc/plain/impatient/index1.icn
%{_texmfdistdir}/doc/plain/impatient/index2.icn
%{_texmfdistdir}/doc/plain/impatient/macros.tex
%{_texmfdistdir}/doc/plain/impatient/math.tex
%{_texmfdistdir}/doc/plain/impatient/modes.tex
%{_texmfdistdir}/doc/plain/impatient/pages.tex
%{_texmfdistdir}/doc/plain/impatient/paras.tex
%{_texmfdistdir}/doc/plain/impatient/preface.tex
%{_texmfdistdir}/doc/plain/impatient/read1st.tex
%{_texmfdistdir}/doc/plain/impatient/tips.tex
%{_texmfdistdir}/doc/plain/impatient/usebook.tex
%{_texmfdistdir}/doc/plain/impatient/usermacs.tex
%{_texmfdistdir}/doc/plain/impatient/usingtex.tex
%{_texmfdistdir}/doc/plain/impatient/xmptext.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-impatient-%{texlive_version}.%{texlive_noarch}.2020svn54080-%{release}-zypper
%endif

%package -n texlive-impatient-cn
Version:        %{texlive_version}.%{texlive_noarch}.2020svn54080
Release:        0
Summary:        Free edition of the book "TeX for the Impatient"
License:        GFDL-1.2-only
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source157:      impatient-cn.doc.tar.xz

%description -n texlive-impatient-cn
"TeX for the Impatient" is a book (of around 350 pages) on TeX,
Plain TeX and Eplain. The book is also available in French and
Chinese translations.
%post -n texlive-impatient-cn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-impatient-cn 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-impatient-cn
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-impatient-cn
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/impatient-cn/Makefile
%{_texmfdistdir}/doc/plain/impatient-cn/backm.tex
%{_texmfdistdir}/doc/plain/impatient-cn/book.tex
%{_texmfdistdir}/doc/plain/impatient-cn/capsule.tex
%{_texmfdistdir}/doc/plain/impatient-cn/cnbook.pdf
%{_texmfdistdir}/doc/plain/impatient-cn/concepts.tex
%{_texmfdistdir}/doc/plain/impatient-cn/config.tex
%{_texmfdistdir}/doc/plain/impatient-cn/copyrght.tex
%{_texmfdistdir}/doc/plain/impatient-cn/eplain.tex
%{_texmfdistdir}/doc/plain/impatient-cn/eplain3.tex
%{_texmfdistdir}/doc/plain/impatient-cn/errors.tex
%{_texmfdistdir}/doc/plain/impatient-cn/examples.tex
%{_texmfdistdir}/doc/plain/impatient-cn/fdl.tex
%{_texmfdistdir}/doc/plain/impatient-cn/fonts.tex
%{_texmfdistdir}/doc/plain/impatient-cn/frontm.tex
%{_texmfdistdir}/doc/plain/impatient-cn/genops.tex
%{_texmfdistdir}/doc/plain/impatient-cn/index.tex
%{_texmfdistdir}/doc/plain/impatient-cn/macros.tex
%{_texmfdistdir}/doc/plain/impatient-cn/math.tex
%{_texmfdistdir}/doc/plain/impatient-cn/modes.tex
%{_texmfdistdir}/doc/plain/impatient-cn/pages.tex
%{_texmfdistdir}/doc/plain/impatient-cn/paras.tex
%{_texmfdistdir}/doc/plain/impatient-cn/preface.tex
%{_texmfdistdir}/doc/plain/impatient-cn/read1st.tex
%{_texmfdistdir}/doc/plain/impatient-cn/tips.tex
%{_texmfdistdir}/doc/plain/impatient-cn/usebook.tex
%{_texmfdistdir}/doc/plain/impatient-cn/usermacs.tex
%{_texmfdistdir}/doc/plain/impatient-cn/usingtex.tex
%{_texmfdistdir}/doc/plain/impatient-cn/xeCJK-base.tex
%{_texmfdistdir}/doc/plain/impatient-cn/xmptext.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-impatient-cn-%{texlive_version}.%{texlive_noarch}.2020svn54080-%{release}-zypper
%endif

%package -n texlive-impatient-fr
Version:        %{texlive_version}.%{texlive_noarch}.2020svn54080
Release:        0
Summary:        Free edition of the book "TeX for the Impatient"
License:        GFDL-1.2-only
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source158:      impatient-fr.doc.tar.xz

%description -n texlive-impatient-fr
"TeX for the Impatient" is a book (of around 350 pages) on TeX,
Plain TeX and Eplain. The book is also available in French and
Chinese translations.
%post -n texlive-impatient-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-impatient-fr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-impatient-fr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-impatient-fr
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/impatient-fr/README
%{_texmfdistdir}/doc/plain/impatient-fr/config.tex
%{_texmfdistdir}/doc/plain/impatient-fr/eplain.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fbackm.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fbook.pdf
%{_texmfdistdir}/doc/plain/impatient-fr/fbook.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fcapsule.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fconcept.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fcopyrgh.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fdl.tex
%{_texmfdistdir}/doc/plain/impatient-fr/ferrors.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fexamples.tex
%{_texmfdistdir}/doc/plain/impatient-fr/ffrontm.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fgenops.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fmacros.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fmath.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fmodes.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fonts.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fpages.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fparas.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fpreface.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fread1st.tex
%{_texmfdistdir}/doc/plain/impatient-fr/ftips.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fusebook.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fusermacs.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fusingtex.tex
%{_texmfdistdir}/doc/plain/impatient-fr/fxmptext.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-impatient-fr-%{texlive_version}.%{texlive_noarch}.2020svn54080-%{release}-zypper
%endif

%package -n texlive-impnattypo
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn50227
Release:        0
Summary:        Support typography of l'Imprimerie Nationale Francaise
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-impnattypo-doc >= %{texlive_version}
Provides:       tex(impnattypo.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source159:      impnattypo.tar.xz
Source160:      impnattypo.doc.tar.xz

%description -n texlive-impnattypo
The package provides useful macros implementing recommendations
by the French Imprimerie Nationale.

%package -n texlive-impnattypo-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn50227
Release:        0
Summary:        Documentation for texlive-impnattypo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-impnattypo-doc:fr;en)

%description -n texlive-impnattypo-doc
This package includes the documentation for texlive-impnattypo

%post -n texlive-impnattypo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-impnattypo 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-impnattypo
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-impnattypo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/impnattypo/README.md
%{_texmfdistdir}/doc/latex/impnattypo/impnattypo-fr.pdf
%{_texmfdistdir}/doc/latex/impnattypo/impnattypo.pdf

%files -n texlive-impnattypo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/impnattypo/impnattypo.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-impnattypo-%{texlive_version}.%{texlive_noarch}.1.5svn50227-%{release}-zypper
%endif

%package -n texlive-import
Version:        %{texlive_version}.%{texlive_noarch}.6.2svn54683
Release:        0
Summary:        Establish input relative to a directory
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-import-doc >= %{texlive_version}
Provides:       tex(import.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source161:      import.tar.xz
Source162:      import.doc.tar.xz

%description -n texlive-import
The commands \import{full_path}{file} and
\subimport{path_extension}{file} set up input through standard
LaTeX mechanisms (\input, \include and \includegraphics) to
load files relative to the \import-ed directory. There are also
\includefrom, \subincludefrom, and * variants of the commands.

%package -n texlive-import-doc
Version:        %{texlive_version}.%{texlive_noarch}.6.2svn54683
Release:        0
Summary:        Documentation for texlive-import
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-import-doc
This package includes the documentation for texlive-import

%post -n texlive-import
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-import 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-import
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-import-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/import/README
%{_texmfdistdir}/doc/latex/import/import.pdf
%{_texmfdistdir}/doc/latex/import/import.tex

%files -n texlive-import
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/import/import.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-import-%{texlive_version}.%{texlive_noarch}.6.2svn54683-%{release}-zypper
%endif

%package -n texlive-imsproc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn29803
Release:        0
Summary:        Typeset IMS conference proceedings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-imsproc-doc >= %{texlive_version}
Provides:       tex(imsproc.cls)
Requires:       tex(amsfonts.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source163:      imsproc.tar.xz
Source164:      imsproc.doc.tar.xz

%description -n texlive-imsproc
The class typesets papers for IMS (Iranian Mathematical
Society) conference proceedings. The class uses the XePersian
package.

%package -n texlive-imsproc-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn29803
Release:        0
Summary:        Documentation for texlive-imsproc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-imsproc-doc
This package includes the documentation for texlive-imsproc

%post -n texlive-imsproc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-imsproc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-imsproc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-imsproc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/imsproc/README
%{_texmfdistdir}/doc/xelatex/imsproc/logo.JPG
%{_texmfdistdir}/doc/xelatex/imsproc/sample-imsproc.tex

%files -n texlive-imsproc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/imsproc/imsproc.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-imsproc-%{texlive_version}.%{texlive_noarch}.0.0.1svn29803-%{release}-zypper
%endif

%package -n texlive-imtekda
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn17667
Release:        0
Summary:        IMTEK thesis class
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-imtekda-doc >= %{texlive_version}
Provides:       tex(IMTEKda.cls)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(scrbook.cls)
Requires:       tex(textpos.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source165:      imtekda.tar.xz
Source166:      imtekda.doc.tar.xz

%description -n texlive-imtekda
The class permits typesetting of diploma, bachelor's and
master's theses for the Institute of Microsystem Technology
(IMTEK) at the University of Freiburg (Germany). The class is
based on the KOMA-Script class scrbook. Included in the
documentation is a large collection of useful tips for
typesetting theses and a list of recommended packages.

%package -n texlive-imtekda-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn17667
Release:        0
Summary:        Documentation for texlive-imtekda
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-imtekda-doc:de)

%description -n texlive-imtekda-doc
This package includes the documentation for texlive-imtekda

%post -n texlive-imtekda
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-imtekda 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-imtekda
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-imtekda-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/imtekda/IMTEKda.pdf
%{_texmfdistdir}/doc/latex/imtekda/README
%{_texmfdistdir}/doc/latex/imtekda/diplarb.bib
%{_texmfdistdir}/doc/latex/imtekda/diplarb.tex
%{_texmfdistdir}/doc/latex/imtekda/figures/bild.eps
%{_texmfdistdir}/doc/latex/imtekda/figures/bild.pdf

%files -n texlive-imtekda
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/imtekda/IMTEKda.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-imtekda-%{texlive_version}.%{texlive_noarch}.1.7svn17667-%{release}-zypper
%endif

%package -n texlive-incgraph
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn36500
Release:        0
Summary:        Sophisticated graphics inclusion in a PDF document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-incgraph-doc >= %{texlive_version}
Provides:       tex(incgraph.sty)
Requires:       tex(pgfkeys.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source167:      incgraph.tar.xz
Source168:      incgraph.doc.tar.xz

%description -n texlive-incgraph
The package provides tools for including graphics at the full
size of the output medium, or for creating "pages" whose size
is that of the graphic they contain. A principal use case is
documents that require inclusion of (potentially many) scans or
photographs. Bookmarking is especially supported. The tool box
has basic macros and a 'convenience' user interface that wraps
\includegraphics.

%package -n texlive-incgraph-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn36500
Release:        0
Summary:        Documentation for texlive-incgraph
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-incgraph-doc
This package includes the documentation for texlive-incgraph

%post -n texlive-incgraph
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-incgraph 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-incgraph
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-incgraph-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/incgraph/CHANGES
%{_texmfdistdir}/doc/latex/incgraph/README
%{_texmfdistdir}/doc/latex/incgraph/exaimage-0001.png
%{_texmfdistdir}/doc/latex/incgraph/exaimage-0037.png
%{_texmfdistdir}/doc/latex/incgraph/exaimage-0123.png
%{_texmfdistdir}/doc/latex/incgraph/example.jpg
%{_texmfdistdir}/doc/latex/incgraph/incgraph-example-a.pdf
%{_texmfdistdir}/doc/latex/incgraph/incgraph-example-a.tex
%{_texmfdistdir}/doc/latex/incgraph/incgraph-example-b.pdf
%{_texmfdistdir}/doc/latex/incgraph/incgraph-example-b.tex
%{_texmfdistdir}/doc/latex/incgraph/incgraph-example-c.pdf
%{_texmfdistdir}/doc/latex/incgraph/incgraph-example-c.tex
%{_texmfdistdir}/doc/latex/incgraph/incgraph.pdf
%{_texmfdistdir}/doc/latex/incgraph/incgraph.tex

%files -n texlive-incgraph
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/incgraph/incgraph.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-incgraph-%{texlive_version}.%{texlive_noarch}.1.12svn36500-%{release}-zypper
%endif

%package -n texlive-includernw
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.0svn47557
Release:        0
Summary:        Include .Rnw inside .tex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-includernw-doc >= %{texlive_version}
Provides:       tex(includeRnw.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source169:      includernw.tar.xz
Source170:      includernw.doc.tar.xz

%description -n texlive-includernw
This package is for including .Rnw (knitr/sweave)-files inside
.tex-files. It requires that you have R and the R-package knitr
installed. Note: This package will probably not work on
Windows. It is tested only on OS X, and will probably also work
on standard Linux distros.

%package -n texlive-includernw-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.0svn47557
Release:        0
Summary:        Documentation for texlive-includernw
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-includernw-doc
This package includes the documentation for texlive-includernw

%post -n texlive-includernw
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-includernw 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-includernw
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-includernw-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/includernw/README.txt
%{_texmfdistdir}/doc/latex/includernw/includeRnw-doc.pdf
%{_texmfdistdir}/doc/latex/includernw/includeRnw-doc.tex

%files -n texlive-includernw
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/includernw/includeRnw.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-includernw-%{texlive_version}.%{texlive_noarch}.0.0.1.0svn47557-%{release}-zypper
%endif

%package -n texlive-inconsolata
Version:        %{texlive_version}.%{texlive_noarch}.1.121svn54512
Release:        0
Summary:        A monospaced font, with support files for use with TeX
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-inconsolata-fonts >= %{texlive_version}
Recommends:     texlive-inconsolata-doc >= %{texlive_version}
Provides:       tex(i4-ly1-0.enc)
Provides:       tex(i4-ly1-1.enc)
Provides:       tex(i4-ly1-2.enc)
Provides:       tex(i4-ly1-3.enc)
Provides:       tex(i4-ly1-4.enc)
Provides:       tex(i4-ly1-5.enc)
Provides:       tex(i4-ly1-6.enc)
Provides:       tex(i4-ly1-7.enc)
Provides:       tex(i4-ot1-0.enc)
Provides:       tex(i4-ot1-1.enc)
Provides:       tex(i4-ot1-2.enc)
Provides:       tex(i4-ot1-3.enc)
Provides:       tex(i4-ot1-4.enc)
Provides:       tex(i4-ot1-5.enc)
Provides:       tex(i4-ot1-6.enc)
Provides:       tex(i4-ot1-7.enc)
Provides:       tex(i4-qx-0.enc)
Provides:       tex(i4-qx-1.enc)
Provides:       tex(i4-qx-2.enc)
Provides:       tex(i4-qx-3.enc)
Provides:       tex(i4-qx-4.enc)
Provides:       tex(i4-qx-5.enc)
Provides:       tex(i4-qx-6.enc)
Provides:       tex(i4-qx-7.enc)
Provides:       tex(i4-t1-0.enc)
Provides:       tex(i4-t1-1.enc)
Provides:       tex(i4-t1-2.enc)
Provides:       tex(i4-t1-3.enc)
Provides:       tex(i4-t1-4.enc)
Provides:       tex(i4-t1-5.enc)
Provides:       tex(i4-t1-6.enc)
Provides:       tex(i4-t1-7.enc)
Provides:       tex(i4-ts1.enc)
Provides:       tex(inconsolata.sty)
Provides:       tex(ly1-zi4b-0.tfm)
Provides:       tex(ly1-zi4b-1.tfm)
Provides:       tex(ly1-zi4b-2.tfm)
Provides:       tex(ly1-zi4b-3.tfm)
Provides:       tex(ly1-zi4b-4.tfm)
Provides:       tex(ly1-zi4b-5.tfm)
Provides:       tex(ly1-zi4b-6.tfm)
Provides:       tex(ly1-zi4b-7.tfm)
Provides:       tex(ly1-zi4nb-0.tfm)
Provides:       tex(ly1-zi4nb-1.tfm)
Provides:       tex(ly1-zi4nb-2.tfm)
Provides:       tex(ly1-zi4nb-3.tfm)
Provides:       tex(ly1-zi4nb-4.tfm)
Provides:       tex(ly1-zi4nb-5.tfm)
Provides:       tex(ly1-zi4nb-6.tfm)
Provides:       tex(ly1-zi4nb-7.tfm)
Provides:       tex(ly1-zi4nr-0.tfm)
Provides:       tex(ly1-zi4nr-1.tfm)
Provides:       tex(ly1-zi4nr-2.tfm)
Provides:       tex(ly1-zi4nr-3.tfm)
Provides:       tex(ly1-zi4nr-4.tfm)
Provides:       tex(ly1-zi4nr-5.tfm)
Provides:       tex(ly1-zi4nr-6.tfm)
Provides:       tex(ly1-zi4nr-7.tfm)
Provides:       tex(ly1-zi4r-0.tfm)
Provides:       tex(ly1-zi4r-1.tfm)
Provides:       tex(ly1-zi4r-2.tfm)
Provides:       tex(ly1-zi4r-3.tfm)
Provides:       tex(ly1-zi4r-4.tfm)
Provides:       tex(ly1-zi4r-5.tfm)
Provides:       tex(ly1-zi4r-6.tfm)
Provides:       tex(ly1-zi4r-7.tfm)
Provides:       tex(ly1zi4.fd)
Provides:       tex(ot1-zi4b-0.tfm)
Provides:       tex(ot1-zi4b-1.tfm)
Provides:       tex(ot1-zi4b-2.tfm)
Provides:       tex(ot1-zi4b-3.tfm)
Provides:       tex(ot1-zi4b-4.tfm)
Provides:       tex(ot1-zi4b-5.tfm)
Provides:       tex(ot1-zi4b-6.tfm)
Provides:       tex(ot1-zi4b-7.tfm)
Provides:       tex(ot1-zi4nb-0.tfm)
Provides:       tex(ot1-zi4nb-1.tfm)
Provides:       tex(ot1-zi4nb-2.tfm)
Provides:       tex(ot1-zi4nb-3.tfm)
Provides:       tex(ot1-zi4nb-4.tfm)
Provides:       tex(ot1-zi4nb-5.tfm)
Provides:       tex(ot1-zi4nb-6.tfm)
Provides:       tex(ot1-zi4nb-7.tfm)
Provides:       tex(ot1-zi4nr-0.tfm)
Provides:       tex(ot1-zi4nr-1.tfm)
Provides:       tex(ot1-zi4nr-2.tfm)
Provides:       tex(ot1-zi4nr-3.tfm)
Provides:       tex(ot1-zi4nr-4.tfm)
Provides:       tex(ot1-zi4nr-5.tfm)
Provides:       tex(ot1-zi4nr-6.tfm)
Provides:       tex(ot1-zi4nr-7.tfm)
Provides:       tex(ot1-zi4r-0.tfm)
Provides:       tex(ot1-zi4r-1.tfm)
Provides:       tex(ot1-zi4r-2.tfm)
Provides:       tex(ot1-zi4r-3.tfm)
Provides:       tex(ot1-zi4r-4.tfm)
Provides:       tex(ot1-zi4r-5.tfm)
Provides:       tex(ot1-zi4r-6.tfm)
Provides:       tex(ot1-zi4r-7.tfm)
Provides:       tex(ot1zi4.fd)
Provides:       tex(qx-zi4b-0.tfm)
Provides:       tex(qx-zi4b-1.tfm)
Provides:       tex(qx-zi4b-2.tfm)
Provides:       tex(qx-zi4b-3.tfm)
Provides:       tex(qx-zi4b-4.tfm)
Provides:       tex(qx-zi4b-5.tfm)
Provides:       tex(qx-zi4b-6.tfm)
Provides:       tex(qx-zi4b-7.tfm)
Provides:       tex(qx-zi4nb-0.tfm)
Provides:       tex(qx-zi4nb-1.tfm)
Provides:       tex(qx-zi4nb-2.tfm)
Provides:       tex(qx-zi4nb-3.tfm)
Provides:       tex(qx-zi4nb-4.tfm)
Provides:       tex(qx-zi4nb-5.tfm)
Provides:       tex(qx-zi4nb-6.tfm)
Provides:       tex(qx-zi4nb-7.tfm)
Provides:       tex(qx-zi4nr-0.tfm)
Provides:       tex(qx-zi4nr-1.tfm)
Provides:       tex(qx-zi4nr-2.tfm)
Provides:       tex(qx-zi4nr-3.tfm)
Provides:       tex(qx-zi4nr-4.tfm)
Provides:       tex(qx-zi4nr-5.tfm)
Provides:       tex(qx-zi4nr-6.tfm)
Provides:       tex(qx-zi4nr-7.tfm)
Provides:       tex(qx-zi4r-0.tfm)
Provides:       tex(qx-zi4r-1.tfm)
Provides:       tex(qx-zi4r-2.tfm)
Provides:       tex(qx-zi4r-3.tfm)
Provides:       tex(qx-zi4r-4.tfm)
Provides:       tex(qx-zi4r-5.tfm)
Provides:       tex(qx-zi4r-6.tfm)
Provides:       tex(qx-zi4r-7.tfm)
Provides:       tex(qxzi4.fd)
Provides:       tex(t1-zi4b-0.tfm)
Provides:       tex(t1-zi4b-1.tfm)
Provides:       tex(t1-zi4b-2.tfm)
Provides:       tex(t1-zi4b-3.tfm)
Provides:       tex(t1-zi4b-4.tfm)
Provides:       tex(t1-zi4b-5.tfm)
Provides:       tex(t1-zi4b-6.tfm)
Provides:       tex(t1-zi4b-7.tfm)
Provides:       tex(t1-zi4nb-0.tfm)
Provides:       tex(t1-zi4nb-1.tfm)
Provides:       tex(t1-zi4nb-2.tfm)
Provides:       tex(t1-zi4nb-3.tfm)
Provides:       tex(t1-zi4nb-4.tfm)
Provides:       tex(t1-zi4nb-5.tfm)
Provides:       tex(t1-zi4nb-6.tfm)
Provides:       tex(t1-zi4nb-7.tfm)
Provides:       tex(t1-zi4nr-0.tfm)
Provides:       tex(t1-zi4nr-1.tfm)
Provides:       tex(t1-zi4nr-2.tfm)
Provides:       tex(t1-zi4nr-3.tfm)
Provides:       tex(t1-zi4nr-4.tfm)
Provides:       tex(t1-zi4nr-5.tfm)
Provides:       tex(t1-zi4nr-6.tfm)
Provides:       tex(t1-zi4nr-7.tfm)
Provides:       tex(t1-zi4r-0.tfm)
Provides:       tex(t1-zi4r-1.tfm)
Provides:       tex(t1-zi4r-2.tfm)
Provides:       tex(t1-zi4r-3.tfm)
Provides:       tex(t1-zi4r-4.tfm)
Provides:       tex(t1-zi4r-5.tfm)
Provides:       tex(t1-zi4r-6.tfm)
Provides:       tex(t1-zi4r-7.tfm)
Provides:       tex(t1zi4.fd)
Provides:       tex(ts1-zi4b.tfm)
Provides:       tex(ts1-zi4nb.tfm)
Provides:       tex(ts1-zi4nr.tfm)
Provides:       tex(ts1-zi4r.tfm)
Provides:       tex(ts1zi4.fd)
Provides:       tex(zi4.map)
Provides:       tex(zi4.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(upquote.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source171:      inconsolata.tar.xz
Source172:      inconsolata.doc.tar.xz

%description -n texlive-inconsolata
Inconsolata is a monospaced font designed by Raph Levien. This
package contains the font (in both Adobe Type 1 and OpenType
formats) in regular and bold weights, with additional glyphs
and options to control slashed zero, upright quotes and a
shapelier lower-case L, plus metric files for use with TeX, and
LaTeX font definition and other relevant files.

%package -n texlive-inconsolata-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.121svn54512
Release:        0
Summary:        Documentation for texlive-inconsolata
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-inconsolata-doc
This package includes the documentation for texlive-inconsolata


%package -n texlive-inconsolata-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.121svn54512
Release:        0
Summary:        Severed fonts for texlive-inconsolata
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-inconsolata-fonts
The  separated fonts package for texlive-inconsolata
%post -n texlive-inconsolata
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap zi4.map' >> /var/run/texlive/run-updmap

%postun -n texlive-inconsolata 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap zi4.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-inconsolata
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-inconsolata-fonts
%files -n texlive-inconsolata-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/inconsolata/OFL.txt
%{_texmfdistdir}/doc/fonts/inconsolata/README
%{_texmfdistdir}/doc/fonts/inconsolata/afmcmds.txt
%{_texmfdistdir}/doc/fonts/inconsolata/inconsolata-doc.pdf
%{_texmfdistdir}/doc/fonts/inconsolata/inconsolata-doc.tex
%{_texmfdistdir}/doc/fonts/inconsolata/novarqu-crop.pdf
%{_texmfdistdir}/doc/fonts/inconsolata/novarqu-noupq-crop.pdf
%{_texmfdistdir}/doc/fonts/inconsolata/varqu-noupq-crop.pdf

%files -n texlive-inconsolata
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-0.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-1.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-2.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-3.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-4.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-5.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-6.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-7.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-0.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-1.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-2.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-3.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-4.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-5.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-6.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-7.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-0.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-1.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-2.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-3.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-4.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-5.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-6.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-7.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-0.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-1.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-2.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-3.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-4.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-5.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-6.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-7.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ts1.enc
%{_texmfdistdir}/fonts/map/dvips/inconsolata/zi4.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inconsolata/InconsolataN-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inconsolata/InconsolataN-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inconsolata/Inconsolatazi4-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inconsolata/Inconsolatazi4-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nb-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nb-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nb-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nb-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nb-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nb-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nb-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nb-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nr-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nr-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nr-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nr-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nr-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nr-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nr-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4nr-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nb-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nb-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nb-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nb-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nb-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nb-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nb-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nb-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nr-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nr-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nr-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nr-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nr-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nr-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nr-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4nr-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nb-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nb-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nb-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nb-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nb-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nb-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nb-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nb-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nr-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nr-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nr-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nr-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nr-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nr-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nr-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4nr-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nb-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nb-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nb-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nb-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nb-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nb-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nb-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nb-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nr-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nr-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nr-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nr-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nr-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nr-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nr-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4nr-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ts1-zi4b.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ts1-zi4nb.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ts1-zi4nr.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ts1-zi4r.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/inconsolata/Inconsolata-zi4b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inconsolata/Inconsolata-zi4r.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inconsolata/InconsolataN-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inconsolata/InconsolataN-Regular.pfb
%{_texmfdistdir}/tex/latex/inconsolata/inconsolata.fontspec
%{_texmfdistdir}/tex/latex/inconsolata/inconsolata.sty
%{_texmfdistdir}/tex/latex/inconsolata/inconsolatan.fontspec
%{_texmfdistdir}/tex/latex/inconsolata/ly1zi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/ot1zi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/qxzi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/t1zi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/ts1zi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/zi4.sty

%files -n texlive-inconsolata-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-inconsolata
%{_datadir}/fontconfig/conf.avail/58-texlive-inconsolata.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-inconsolata.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-inconsolata.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-inconsolata/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-inconsolata/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-inconsolata/fonts.scale
%{_datadir}/fonts/texlive-inconsolata/InconsolataN-Bold.otf
%{_datadir}/fonts/texlive-inconsolata/InconsolataN-Regular.otf
%{_datadir}/fonts/texlive-inconsolata/Inconsolatazi4-Bold.otf
%{_datadir}/fonts/texlive-inconsolata/Inconsolatazi4-Regular.otf
%{_datadir}/fonts/texlive-inconsolata/Inconsolata-zi4b.pfb
%{_datadir}/fonts/texlive-inconsolata/Inconsolata-zi4r.pfb
%{_datadir}/fonts/texlive-inconsolata/InconsolataN-Bold.pfb
%{_datadir}/fonts/texlive-inconsolata/InconsolataN-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-inconsolata-fonts-%{texlive_version}.%{texlive_noarch}.1.121svn54512-%{release}-zypper
%endif

%package -n texlive-index
Version:        %{texlive_version}.%{texlive_noarch}.4.1betasvn24099
Release:        0
Summary:        Extended index for LaTeX including multiple indexes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-index-doc >= %{texlive_version}
Provides:       tex(autind.sty)
Provides:       tex(bibref.sty)
Provides:       tex(index.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source173:      index.tar.xz
Source174:      index.doc.tar.xz

%description -n texlive-index
This is a reimplementation of LaTeX's indexing macros to
provide better support for indexing. For example, it supports
multiple indexes in a single document and provides a more
robust \index command. It supplies short hand notations for the
\index command (^{word}) and a * variation of \index
(abbreviated _{word}) that prints the word being indexed, as
well as creating an index entry for it.

%package -n texlive-index-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.1betasvn24099
Release:        0
Summary:        Documentation for texlive-index
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-index-doc
This package includes the documentation for texlive-index

%post -n texlive-index
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-index 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-index
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-index-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/index/README
%{_texmfdistdir}/doc/latex/index/TODO
%{_texmfdistdir}/doc/latex/index/agsmtst.tex
%{_texmfdistdir}/doc/latex/index/autind.tex
%{_texmfdistdir}/doc/latex/index/index.pdf
%{_texmfdistdir}/doc/latex/index/plaintst.tex
%{_texmfdistdir}/doc/latex/index/sample.tex
%{_texmfdistdir}/doc/latex/index/test.bib

%files -n texlive-index
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/index/xagsm.bst
%{_texmfdistdir}/bibtex/bst/index/xplain.bst
%{_texmfdistdir}/makeindex/index/bibref.ist
%{_texmfdistdir}/tex/latex/index/autind.sty
%{_texmfdistdir}/tex/latex/index/bibref.sty
%{_texmfdistdir}/tex/latex/index/index.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-index-%{texlive_version}.%{texlive_noarch}.4.1betasvn24099-%{release}-zypper
%endif

%package -n texlive-indextools
Version:        %{texlive_version}.%{texlive_noarch}.1.5.1svn38931
Release:        0
Summary:        Producing multiple indices
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-indextools-doc >= %{texlive_version}
Provides:       tex(indextools.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source175:      indextools.tar.xz
Source176:      indextools.doc.tar.xz

%description -n texlive-indextools
This package enables the user to produce and typeset one or
more indices simultaneously. The package is known to work in
LaTeX documents processed with pdfLaTeX, XeLaTeX and LuaLaTeX.
If makeindex is used for processing the index entries, no
particular setup is needed when TeX Live is used. Using xindy
or other programs, it is necessary to enable shell escape.
Shell escape is also needed if splitindex is used. This is a
fork of imakeidx, with new features and fixed bugs.

%package -n texlive-indextools-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5.1svn38931
Release:        0
Summary:        Documentation for texlive-indextools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-indextools-doc
This package includes the documentation for texlive-indextools

%post -n texlive-indextools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-indextools 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-indextools
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-indextools-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/indextools/README
%{_texmfdistdir}/doc/latex/indextools/indextools.pdf
%{_texmfdistdir}/doc/latex/indextools/issue5.pdf
%{_texmfdistdir}/doc/latex/indextools/latexmkrc
%{_texmfdistdir}/doc/latex/indextools/makefile

%files -n texlive-indextools
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/indextools/indextools.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-indextools-%{texlive_version}.%{texlive_noarch}.1.5.1svn38931-%{release}-zypper
%endif

%package -n texlive-infwarerr
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn53023
Release:        0
Summary:        Complete set of information/warning/error message macros
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-infwarerr-doc >= %{texlive_version}
Provides:       tex(infwarerr.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source177:      infwarerr.tar.xz
Source178:      infwarerr.doc.tar.xz

%description -n texlive-infwarerr
This package provides a complete set of macros for information,
warning and error messages. Under LaTeX, the commands are
wrappers for the corresponding LaTeX commands; under Plain TeX
they are available as complete implementations.

%package -n texlive-infwarerr-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn53023
Release:        0
Summary:        Documentation for texlive-infwarerr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-infwarerr-doc
This package includes the documentation for texlive-infwarerr

%post -n texlive-infwarerr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-infwarerr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-infwarerr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-infwarerr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/infwarerr/README.md
%{_texmfdistdir}/doc/latex/infwarerr/infwarerr.pdf

%files -n texlive-infwarerr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/infwarerr/infwarerr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-infwarerr-%{texlive_version}.%{texlive_noarch}.1.5svn53023-%{release}-zypper
%endif

%package -n texlive-initials
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        Adobe Type 1 decorative initial fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-initials-fonts >= %{texlive_version}
Recommends:     texlive-initials-doc >= %{texlive_version}
Provides:       tex(Acorn.fd)
Provides:       tex(Acorn.map)
Provides:       tex(Acorn.tfm)
Provides:       tex(AnnSton.fd)
Provides:       tex(AnnSton.map)
Provides:       tex(AnnSton.tfm)
Provides:       tex(ArtNouv.fd)
Provides:       tex(ArtNouv.map)
Provides:       tex(ArtNouv.tfm)
Provides:       tex(ArtNouvc.fd)
Provides:       tex(ArtNouvc.map)
Provides:       tex(ArtNouvc.tfm)
Provides:       tex(Carrickc.fd)
Provides:       tex(Carrickc.map)
Provides:       tex(Carrickc.tfm)
Provides:       tex(Eichenla.fd)
Provides:       tex(Eichenla.map)
Provides:       tex(Eichenla.tfm)
Provides:       tex(Eileen.fd)
Provides:       tex(Eileen.map)
Provides:       tex(Eileen.tfm)
Provides:       tex(EileenBl.fd)
Provides:       tex(EileenBl.map)
Provides:       tex(EileenBl.tfm)
Provides:       tex(Elzevier.fd)
Provides:       tex(Elzevier.map)
Provides:       tex(Elzevier.tfm)
Provides:       tex(GotIn.fd)
Provides:       tex(GotIn.map)
Provides:       tex(GotIn.tfm)
Provides:       tex(GoudyIn.fd)
Provides:       tex(GoudyIn.map)
Provides:       tex(GoudyIn.tfm)
Provides:       tex(Kinigcap.fd)
Provides:       tex(Kinigcap.map)
Provides:       tex(Kinigcap.tfm)
Provides:       tex(Konanur.fd)
Provides:       tex(Konanur.map)
Provides:       tex(Konanur.tfm)
Provides:       tex(Kramer.fd)
Provides:       tex(Kramer.map)
Provides:       tex(Kramer.tfm)
Provides:       tex(MorrisIn.fd)
Provides:       tex(MorrisIn.map)
Provides:       tex(MorrisIn.tfm)
Provides:       tex(Nouveaud.fd)
Provides:       tex(Nouveaud.map)
Provides:       tex(Nouveaud.tfm)
Provides:       tex(Romantik.fd)
Provides:       tex(Romantik.map)
Provides:       tex(Romantik.tfm)
Provides:       tex(Rothdn.fd)
Provides:       tex(Rothdn.map)
Provides:       tex(Rothdn.tfm)
Provides:       tex(RoyalIn.fd)
Provides:       tex(RoyalIn.map)
Provides:       tex(RoyalIn.tfm)
Provides:       tex(Sanremo.fd)
Provides:       tex(Sanremo.map)
Provides:       tex(Sanremo.tfm)
Provides:       tex(Starburst.fd)
Provides:       tex(Starburst.map)
Provides:       tex(Starburst.tfm)
Provides:       tex(Typocaps.fd)
Provides:       tex(Typocaps.map)
Provides:       tex(Typocaps.tfm)
Provides:       tex(Zallman.fd)
Provides:       tex(Zallman.map)
Provides:       tex(Zallman.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source179:      initials.tar.xz
Source180:      initials.doc.tar.xz

%description -n texlive-initials
For each font, at least a .pfb and a .tfm file is provided,
with an .fd file for use with LaTeX.

%package -n texlive-initials-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        Documentation for texlive-initials
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-initials-doc
This package includes the documentation for texlive-initials


%package -n texlive-initials-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        Severed fonts for texlive-initials
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-initials-fonts
The  separated fonts package for texlive-initials
%post -n texlive-initials
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap Acorn.map' >> /var/run/texlive/run-updmap
echo 'addMap AnnSton.map' >> /var/run/texlive/run-updmap
echo 'addMap ArtNouv.map' >> /var/run/texlive/run-updmap
echo 'addMap ArtNouvc.map' >> /var/run/texlive/run-updmap
echo 'addMap Carrickc.map' >> /var/run/texlive/run-updmap
echo 'addMap Eichenla.map' >> /var/run/texlive/run-updmap
echo 'addMap Eileen.map' >> /var/run/texlive/run-updmap
echo 'addMap EileenBl.map' >> /var/run/texlive/run-updmap
echo 'addMap Elzevier.map' >> /var/run/texlive/run-updmap
echo 'addMap GotIn.map' >> /var/run/texlive/run-updmap
echo 'addMap GoudyIn.map' >> /var/run/texlive/run-updmap
echo 'addMap Kinigcap.map' >> /var/run/texlive/run-updmap
echo 'addMap Konanur.map' >> /var/run/texlive/run-updmap
echo 'addMap Kramer.map' >> /var/run/texlive/run-updmap
echo 'addMap MorrisIn.map' >> /var/run/texlive/run-updmap
echo 'addMap Nouveaud.map' >> /var/run/texlive/run-updmap
echo 'addMap Romantik.map' >> /var/run/texlive/run-updmap
echo 'addMap Rothdn.map' >> /var/run/texlive/run-updmap
echo 'addMap RoyalIn.map' >> /var/run/texlive/run-updmap
echo 'addMap Sanremo.map' >> /var/run/texlive/run-updmap
echo 'addMap Starburst.map' >> /var/run/texlive/run-updmap
echo 'addMap Typocaps.map' >> /var/run/texlive/run-updmap
echo 'addMap Zallman.map' >> /var/run/texlive/run-updmap

%postun -n texlive-initials 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap Acorn.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap AnnSton.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap ArtNouv.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap ArtNouvc.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Carrickc.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Eichenla.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Eileen.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap EileenBl.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Elzevier.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap GotIn.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap GoudyIn.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Kinigcap.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Konanur.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Kramer.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap MorrisIn.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Nouveaud.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Romantik.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Rothdn.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap RoyalIn.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Sanremo.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Starburst.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Typocaps.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap Zallman.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-initials
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-initials-fonts
%files -n texlive-initials-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/initials/Acorn.tex
%{_texmfdistdir}/doc/fonts/initials/AnnSton.tex
%{_texmfdistdir}/doc/fonts/initials/ArtNouv.tex
%{_texmfdistdir}/doc/fonts/initials/ArtNouvc.tex
%{_texmfdistdir}/doc/fonts/initials/Carrickc.tex
%{_texmfdistdir}/doc/fonts/initials/Eichenla.tex
%{_texmfdistdir}/doc/fonts/initials/Eileen.tex
%{_texmfdistdir}/doc/fonts/initials/EileenBl.tex
%{_texmfdistdir}/doc/fonts/initials/Elzevier.tex
%{_texmfdistdir}/doc/fonts/initials/GotIn.tex
%{_texmfdistdir}/doc/fonts/initials/GoudyIn.tex
%{_texmfdistdir}/doc/fonts/initials/Kinigcap.tex
%{_texmfdistdir}/doc/fonts/initials/Konanur.tex
%{_texmfdistdir}/doc/fonts/initials/Kramer.tex
%{_texmfdistdir}/doc/fonts/initials/MorrisIn.tex
%{_texmfdistdir}/doc/fonts/initials/Nouveaud.tex
%{_texmfdistdir}/doc/fonts/initials/README
%{_texmfdistdir}/doc/fonts/initials/Romantik.tex
%{_texmfdistdir}/doc/fonts/initials/Rothdn.tex
%{_texmfdistdir}/doc/fonts/initials/RoyalIn.tex
%{_texmfdistdir}/doc/fonts/initials/Sanremo.tex
%{_texmfdistdir}/doc/fonts/initials/Starburst.tex
%{_texmfdistdir}/doc/fonts/initials/Typocaps.tex
%{_texmfdistdir}/doc/fonts/initials/Zallman.tex

%files -n texlive-initials
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/initials/config.Acorn
%{_texmfdistdir}/dvips/initials/config.AnnSton
%{_texmfdistdir}/dvips/initials/config.ArtNouv
%{_texmfdistdir}/dvips/initials/config.ArtNouvc
%{_texmfdistdir}/dvips/initials/config.Carrickc
%{_texmfdistdir}/dvips/initials/config.Eichenla
%{_texmfdistdir}/dvips/initials/config.Eileen
%{_texmfdistdir}/dvips/initials/config.EileenBl
%{_texmfdistdir}/dvips/initials/config.Elzevier
%{_texmfdistdir}/dvips/initials/config.GotIn
%{_texmfdistdir}/dvips/initials/config.GoudyIn
%{_texmfdistdir}/dvips/initials/config.Kinigcap
%{_texmfdistdir}/dvips/initials/config.Konanur
%{_texmfdistdir}/dvips/initials/config.Kramer
%{_texmfdistdir}/dvips/initials/config.MorrisIn
%{_texmfdistdir}/dvips/initials/config.Nouveaud
%{_texmfdistdir}/dvips/initials/config.Romantik
%{_texmfdistdir}/dvips/initials/config.Rothdn
%{_texmfdistdir}/dvips/initials/config.RoyalIn
%{_texmfdistdir}/dvips/initials/config.Sanremo
%{_texmfdistdir}/dvips/initials/config.Starburst
%{_texmfdistdir}/dvips/initials/config.Typocaps
%{_texmfdistdir}/dvips/initials/config.Zallman
%{_texmfdistdir}/fonts/afm/public/initials/Acorn.afm
%{_texmfdistdir}/fonts/afm/public/initials/AnnSton.afm
%{_texmfdistdir}/fonts/afm/public/initials/ArtNouv.afm
%{_texmfdistdir}/fonts/afm/public/initials/ArtNouvc.afm
%{_texmfdistdir}/fonts/afm/public/initials/Carrickc.afm
%{_texmfdistdir}/fonts/afm/public/initials/Eichenla.afm
%{_texmfdistdir}/fonts/afm/public/initials/Eileen.afm
%{_texmfdistdir}/fonts/afm/public/initials/EileenBl.afm
%{_texmfdistdir}/fonts/afm/public/initials/Elzevier.afm
%{_texmfdistdir}/fonts/afm/public/initials/GotIn.afm
%{_texmfdistdir}/fonts/afm/public/initials/GoudyIn.afm
%{_texmfdistdir}/fonts/afm/public/initials/Kinigcap.afm
%{_texmfdistdir}/fonts/afm/public/initials/Konanur.afm
%{_texmfdistdir}/fonts/afm/public/initials/Kramer.afm
%{_texmfdistdir}/fonts/afm/public/initials/MorrisIn.afm
%{_texmfdistdir}/fonts/afm/public/initials/Nouveaud.afm
%{_texmfdistdir}/fonts/afm/public/initials/Romantik.afm
%{_texmfdistdir}/fonts/afm/public/initials/Rothdn.afm
%{_texmfdistdir}/fonts/afm/public/initials/RoyalIn.afm
%{_texmfdistdir}/fonts/afm/public/initials/Sanremo.afm
%{_texmfdistdir}/fonts/afm/public/initials/Starburst.afm
%{_texmfdistdir}/fonts/afm/public/initials/Typocaps.afm
%{_texmfdistdir}/fonts/afm/public/initials/Zallman.afm
%{_texmfdistdir}/fonts/map/dvips/initials/Acorn.map
%{_texmfdistdir}/fonts/map/dvips/initials/AnnSton.map
%{_texmfdistdir}/fonts/map/dvips/initials/ArtNouv.map
%{_texmfdistdir}/fonts/map/dvips/initials/ArtNouvc.map
%{_texmfdistdir}/fonts/map/dvips/initials/Carrickc.map
%{_texmfdistdir}/fonts/map/dvips/initials/Eichenla.map
%{_texmfdistdir}/fonts/map/dvips/initials/Eileen.map
%{_texmfdistdir}/fonts/map/dvips/initials/EileenBl.map
%{_texmfdistdir}/fonts/map/dvips/initials/Elzevier.map
%{_texmfdistdir}/fonts/map/dvips/initials/GotIn.map
%{_texmfdistdir}/fonts/map/dvips/initials/GoudyIn.map
%{_texmfdistdir}/fonts/map/dvips/initials/Kinigcap.map
%{_texmfdistdir}/fonts/map/dvips/initials/Konanur.map
%{_texmfdistdir}/fonts/map/dvips/initials/Kramer.map
%{_texmfdistdir}/fonts/map/dvips/initials/MorrisIn.map
%{_texmfdistdir}/fonts/map/dvips/initials/Nouveaud.map
%{_texmfdistdir}/fonts/map/dvips/initials/Romantik.map
%{_texmfdistdir}/fonts/map/dvips/initials/Rothdn.map
%{_texmfdistdir}/fonts/map/dvips/initials/RoyalIn.map
%{_texmfdistdir}/fonts/map/dvips/initials/Sanremo.map
%{_texmfdistdir}/fonts/map/dvips/initials/Starburst.map
%{_texmfdistdir}/fonts/map/dvips/initials/Typocaps.map
%{_texmfdistdir}/fonts/map/dvips/initials/Zallman.map
%{_texmfdistdir}/fonts/tfm/public/initials/Acorn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/AnnSton.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/ArtNouv.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/ArtNouvc.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Carrickc.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Eichenla.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Eileen.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/EileenBl.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Elzevier.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/GotIn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/GoudyIn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Kinigcap.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Konanur.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Kramer.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/MorrisIn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Nouveaud.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Romantik.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Rothdn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/RoyalIn.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Sanremo.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Starburst.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Typocaps.tfm
%{_texmfdistdir}/fonts/tfm/public/initials/Zallman.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Acorn.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/AnnSton.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/ArtNouv.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/ArtNouvc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Carrickc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Eichenla.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Eileen.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/EileenBl.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Elzevier.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/GotIn.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/GoudyIn.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Kinigcap.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Konanur.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Kramer.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/MorrisIn.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Nouveaud.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Romantik.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Rothdn.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/RoyalIn.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Sanremo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Starburst.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Typocaps.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/initials/Zallman.pfb
%{_texmfdistdir}/tex/latex/initials/Acorn.fd
%{_texmfdistdir}/tex/latex/initials/AnnSton.fd
%{_texmfdistdir}/tex/latex/initials/ArtNouv.fd
%{_texmfdistdir}/tex/latex/initials/ArtNouvc.fd
%{_texmfdistdir}/tex/latex/initials/Carrickc.fd
%{_texmfdistdir}/tex/latex/initials/Eichenla.fd
%{_texmfdistdir}/tex/latex/initials/Eileen.fd
%{_texmfdistdir}/tex/latex/initials/EileenBl.fd
%{_texmfdistdir}/tex/latex/initials/Elzevier.fd
%{_texmfdistdir}/tex/latex/initials/GotIn.fd
%{_texmfdistdir}/tex/latex/initials/GoudyIn.fd
%{_texmfdistdir}/tex/latex/initials/Kinigcap.fd
%{_texmfdistdir}/tex/latex/initials/Konanur.fd
%{_texmfdistdir}/tex/latex/initials/Kramer.fd
%{_texmfdistdir}/tex/latex/initials/MorrisIn.fd
%{_texmfdistdir}/tex/latex/initials/Nouveaud.fd
%{_texmfdistdir}/tex/latex/initials/Romantik.fd
%{_texmfdistdir}/tex/latex/initials/Rothdn.fd
%{_texmfdistdir}/tex/latex/initials/RoyalIn.fd
%{_texmfdistdir}/tex/latex/initials/Sanremo.fd
%{_texmfdistdir}/tex/latex/initials/Starburst.fd
%{_texmfdistdir}/tex/latex/initials/Typocaps.fd
%{_texmfdistdir}/tex/latex/initials/Zallman.fd

%files -n texlive-initials-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-initials
%{_datadir}/fontconfig/conf.avail/58-texlive-initials.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-initials/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-initials/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-initials/fonts.scale
%{_datadir}/fonts/texlive-initials/Acorn.pfb
%{_datadir}/fonts/texlive-initials/AnnSton.pfb
%{_datadir}/fonts/texlive-initials/ArtNouv.pfb
%{_datadir}/fonts/texlive-initials/ArtNouvc.pfb
%{_datadir}/fonts/texlive-initials/Carrickc.pfb
%{_datadir}/fonts/texlive-initials/Eichenla.pfb
%{_datadir}/fonts/texlive-initials/Eileen.pfb
%{_datadir}/fonts/texlive-initials/EileenBl.pfb
%{_datadir}/fonts/texlive-initials/Elzevier.pfb
%{_datadir}/fonts/texlive-initials/GotIn.pfb
%{_datadir}/fonts/texlive-initials/GoudyIn.pfb
%{_datadir}/fonts/texlive-initials/Kinigcap.pfb
%{_datadir}/fonts/texlive-initials/Konanur.pfb
%{_datadir}/fonts/texlive-initials/Kramer.pfb
%{_datadir}/fonts/texlive-initials/MorrisIn.pfb
%{_datadir}/fonts/texlive-initials/Nouveaud.pfb
%{_datadir}/fonts/texlive-initials/Romantik.pfb
%{_datadir}/fonts/texlive-initials/Rothdn.pfb
%{_datadir}/fonts/texlive-initials/RoyalIn.pfb
%{_datadir}/fonts/texlive-initials/Sanremo.pfb
%{_datadir}/fonts/texlive-initials/Starburst.pfb
%{_datadir}/fonts/texlive-initials/Typocaps.pfb
%{_datadir}/fonts/texlive-initials/Zallman.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-initials-fonts-%{texlive_version}.%{texlive_noarch}.svn54080-%{release}-zypper
%endif

%package -n texlive-inkpaper
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        A mathematical paper template
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-inkpaper-doc >= %{texlive_version}
Provides:       tex(inkpaper.cls)
Requires:       tex(abstract.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(asymptote.sty)
Requires:       tex(calc.sty)
Requires:       tex(cite.sty)
Requires:       tex(ctexart.cls)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(listings.sty)
Requires:       tex(mfirstuc.sty)
Requires:       tex(microtype.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(textcase.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source181:      inkpaper.tar.xz
Source182:      inkpaper.doc.tar.xz

%description -n texlive-inkpaper
InkPaper is designed to write mathematical papers,especially
designed for Mathematics Students. ZJGS students. magazine
editors. NOTICE.This is not a Thesis class.

%package -n texlive-inkpaper-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Documentation for texlive-inkpaper
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-inkpaper-doc:zh-cn;en)

%description -n texlive-inkpaper-doc
This package includes the documentation for texlive-inkpaper

%post -n texlive-inkpaper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-inkpaper 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-inkpaper
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-inkpaper-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/inkpaper/LICENSE
%{_texmfdistdir}/doc/latex/inkpaper/README.md
%{_texmfdistdir}/doc/latex/inkpaper/inkpaper-cn.pdf
%{_texmfdistdir}/doc/latex/inkpaper/inkpaper-cn.tex
%{_texmfdistdir}/doc/latex/inkpaper/inkpaper-en.pdf
%{_texmfdistdir}/doc/latex/inkpaper/inkpaper-en.tex

%files -n texlive-inkpaper
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/inkpaper/inkpaper.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-inkpaper-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif

%package -n texlive-inline-images
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Inline images in base64 encoding
License:        LGPL-2.1-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-inline-images-doc >= %{texlive_version}
Provides:       tex(inline-images.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source183:      inline-images.tar.xz
Source184:      inline-images.doc.tar.xz

%description -n texlive-inline-images
The package provides a command \inlineimg to dynamically create
a file containing the inline image in base64 format, which is
decoded and included in the source file. Requirements LaTeX
must be run with option --shell-escape. Program base64.

%package -n texlive-inline-images-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Documentation for texlive-inline-images
License:        LGPL-2.1-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-inline-images-doc
This package includes the documentation for texlive-inline-images

%post -n texlive-inline-images
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-inline-images 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-inline-images
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-inline-images-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/inline-images/README.md
%{_texmfdistdir}/doc/latex/inline-images/examples/example.pdf
%{_texmfdistdir}/doc/latex/inline-images/examples/example.tex
%{_texmfdistdir}/doc/latex/inline-images/screenshots/example.jpg

%files -n texlive-inline-images
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/inline-images/inline-images.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-inline-images-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif

%package -n texlive-inlinebib
Version:        %{texlive_version}.%{texlive_noarch}.svn22018
Release:        0
Summary:        Citations in footnotes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-inlinebib-doc >= %{texlive_version}
Provides:       tex(inlinebib.sty)
Provides:       tex(pageranges.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source185:      inlinebib.tar.xz
Source186:      inlinebib.doc.tar.xz

%description -n texlive-inlinebib
A BibTeX style and a LaTeX package that allow for a full
bibliography at the end of the document as well as citation
details in footnotes. The footnote details include "op. cit."
and "ibid." contractions.

%package -n texlive-inlinebib-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn22018
Release:        0
Summary:        Documentation for texlive-inlinebib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-inlinebib-doc
This package includes the documentation for texlive-inlinebib

%post -n texlive-inlinebib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-inlinebib 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-inlinebib
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-inlinebib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/inlinebib/MANIFEST
%{_texmfdistdir}/doc/bibtex/inlinebib/inlinebib.htm
%{_texmfdistdir}/doc/bibtex/inlinebib/inlinebib.txt
%{_texmfdistdir}/doc/bibtex/inlinebib/inlinebib1.gif
%{_texmfdistdir}/doc/bibtex/inlinebib/inlinebib2.gif

%files -n texlive-inlinebib
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/inlinebib/inlinebib.bst
%{_texmfdistdir}/tex/latex/inlinebib/inlinebib.sty
%{_texmfdistdir}/tex/latex/inlinebib/pageranges.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-inlinebib-%{texlive_version}.%{texlive_noarch}.svn22018-%{release}-zypper
%endif

%package -n texlive-inlinedef
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Inline expansions within definitions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-inlinedef-doc >= %{texlive_version}
Provides:       tex(inlinedef.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source187:      inlinedef.tar.xz
Source188:      inlinedef.doc.tar.xz

%description -n texlive-inlinedef
The package provides a macro \Inline that precedes a \def or
\gdef. Within the definition text of an inlined definition,
keywords such as \Expand may be used to selectively inline
certain expansions at definition-time. This eases the process
of redefining macros in terms of the original definition, as
well as definitions in which the token that must be expanded is
deep within, where \expandafter would be difficult and \edef is
not suitable. Another application is as an easier version of
\aftergroup, by defining a macro in terms of expanded local
variables, then ending the group with
\expandafter\endgroup\macro.

%package -n texlive-inlinedef-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-inlinedef
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-inlinedef-doc
This package includes the documentation for texlive-inlinedef

%post -n texlive-inlinedef
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-inlinedef 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-inlinedef
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-inlinedef-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/inlinedef/README
%{_texmfdistdir}/doc/latex/inlinedef/inlinedef.pdf
%{_texmfdistdir}/doc/latex/inlinedef/inlinetest.tex

%files -n texlive-inlinedef
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/inlinedef/inlinedef.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-inlinedef-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-inputenx
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn52986
Release:        0
Summary:        Enhanced input encoding handling
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-inputenx-doc >= %{texlive_version}
Provides:       tex(inputenx.sty)
Provides:       tex(ix-alias.def)
Provides:       tex(ix-math.def)
Provides:       tex(ix-name.def)
Provides:       tex(ix-slot.def)
Provides:       tex(ix-uc.def)
Provides:       tex(x-ascii.def)
Provides:       tex(x-atarist.def)
Provides:       tex(x-cp1250.def)
Provides:       tex(x-cp1251.def)
Provides:       tex(x-cp1252.def)
Provides:       tex(x-cp1255.def)
Provides:       tex(x-cp1257.def)
Provides:       tex(x-cp437.def)
Provides:       tex(x-cp850.def)
Provides:       tex(x-cp852.def)
Provides:       tex(x-cp855.def)
Provides:       tex(x-cp858.def)
Provides:       tex(x-cp865.def)
Provides:       tex(x-cp866.def)
Provides:       tex(x-dec-mcs.def)
Provides:       tex(x-iso-8859-1.def)
Provides:       tex(x-iso-8859-10.def)
Provides:       tex(x-iso-8859-13.def)
Provides:       tex(x-iso-8859-14.def)
Provides:       tex(x-iso-8859-15.def)
Provides:       tex(x-iso-8859-16.def)
Provides:       tex(x-iso-8859-2.def)
Provides:       tex(x-iso-8859-3.def)
Provides:       tex(x-iso-8859-4.def)
Provides:       tex(x-iso-8859-5.def)
Provides:       tex(x-iso-8859-8.def)
Provides:       tex(x-iso-8859-9.def)
Provides:       tex(x-koi8-r.def)
Provides:       tex(x-mac-centeuro.def)
Provides:       tex(x-mac-cyrillic.def)
Provides:       tex(x-mac-roman.def)
Provides:       tex(x-nextstep.def)
Provides:       tex(x-verbatim.def)
Requires:       tex(inputenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source189:      inputenx.tar.xz
Source190:      inputenx.doc.tar.xz

%description -n texlive-inputenx
This package deals with input encodings. It provides a wider
range of input encodings using standard mappings, than does
inputenc; it also covers nearly all slots. In this way, it
serves as more uptodate replacement for package inputenc.

%package -n texlive-inputenx-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn52986
Release:        0
Summary:        Documentation for texlive-inputenx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-inputenx-doc
This package includes the documentation for texlive-inputenx

%post -n texlive-inputenx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-inputenx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-inputenx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-inputenx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/inputenx/README.md
%{_texmfdistdir}/doc/latex/inputenx/inputenx.pdf

%files -n texlive-inputenx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/inputenx/inputenx.sty
%{_texmfdistdir}/tex/latex/inputenx/ix-alias.def
%{_texmfdistdir}/tex/latex/inputenx/ix-math.def
%{_texmfdistdir}/tex/latex/inputenx/ix-name.def
%{_texmfdistdir}/tex/latex/inputenx/ix-slot.def
%{_texmfdistdir}/tex/latex/inputenx/ix-uc.def
%{_texmfdistdir}/tex/latex/inputenx/ix-utf8enc.dfu
%{_texmfdistdir}/tex/latex/inputenx/x-ascii.def
%{_texmfdistdir}/tex/latex/inputenx/x-atarist.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp1250.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp1251.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp1252.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp1255.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp1257.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp437.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp850.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp852.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp855.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp858.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp865.def
%{_texmfdistdir}/tex/latex/inputenx/x-cp866.def
%{_texmfdistdir}/tex/latex/inputenx/x-dec-mcs.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-1.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-10.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-13.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-14.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-15.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-16.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-2.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-3.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-4.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-5.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-8.def
%{_texmfdistdir}/tex/latex/inputenx/x-iso-8859-9.def
%{_texmfdistdir}/tex/latex/inputenx/x-koi8-r.def
%{_texmfdistdir}/tex/latex/inputenx/x-mac-centeuro.def
%{_texmfdistdir}/tex/latex/inputenx/x-mac-cyrillic.def
%{_texmfdistdir}/tex/latex/inputenx/x-mac-roman.def
%{_texmfdistdir}/tex/latex/inputenx/x-nextstep.def
%{_texmfdistdir}/tex/latex/inputenx/x-verbatim.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-inputenx-%{texlive_version}.%{texlive_noarch}.1.12svn52986-%{release}-zypper
%endif

%package -n texlive-inputtrc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn28019
Release:        0
Summary:        Trace which file loads which
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-inputtrc-doc >= %{texlive_version}
Provides:       tex(inputtrc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source191:      inputtrc.tar.xz
Source192:      inputtrc.doc.tar.xz

%description -n texlive-inputtrc
The package produces screen/log messages of the form '<current>
INPUTTING <next>' reporting LaTeX input commands (<current> and
<next> being file names). The message is indented to reflect
the level of input nesting. Tracing may be turned on and off,
and the unit of indentation may be adjusted. The implementation
somewhat resembles those of packages FiNK and inputfile.

%package -n texlive-inputtrc-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn28019
Release:        0
Summary:        Documentation for texlive-inputtrc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-inputtrc-doc
This package includes the documentation for texlive-inputtrc

%post -n texlive-inputtrc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-inputtrc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-inputtrc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-inputtrc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/inputtrc/README
%{_texmfdistdir}/doc/latex/inputtrc/README.pdf
%{_texmfdistdir}/doc/latex/inputtrc/RELEASE.txt
%{_texmfdistdir}/doc/latex/inputtrc/SrcFILEs.txt
%{_texmfdistdir}/doc/latex/inputtrc/inputtrc.pdf

%files -n texlive-inputtrc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/inputtrc/inputtrc.RLS
%{_texmfdistdir}/tex/latex/inputtrc/inputtrc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-inputtrc-%{texlive_version}.%{texlive_noarch}.0.0.3svn28019-%{release}-zypper
%endif

%package -n texlive-inriafonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54512
Release:        0
Summary:        Inria fonts with LaTeX support
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-inriafonts-fonts >= %{texlive_version}
Recommends:     texlive-inriafonts-doc >= %{texlive_version}
Provides:       tex(InriaSans-Bold-lf-ly1--base.tfm)
Provides:       tex(InriaSans-Bold-lf-ly1.tfm)
Provides:       tex(InriaSans-Bold-lf-ly1.vf)
Provides:       tex(InriaSans-Bold-lf-ot1.tfm)
Provides:       tex(InriaSans-Bold-lf-t1--base.tfm)
Provides:       tex(InriaSans-Bold-lf-t1.tfm)
Provides:       tex(InriaSans-Bold-lf-t1.vf)
Provides:       tex(InriaSans-Bold-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-Bold-lf-titling-ly1.tfm)
Provides:       tex(InriaSans-Bold-lf-titling-ly1.vf)
Provides:       tex(InriaSans-Bold-lf-titling-ot1.tfm)
Provides:       tex(InriaSans-Bold-lf-titling-t1--base.tfm)
Provides:       tex(InriaSans-Bold-lf-titling-t1.tfm)
Provides:       tex(InriaSans-Bold-lf-titling-t1.vf)
Provides:       tex(InriaSans-Bold-lf-ts1--base.tfm)
Provides:       tex(InriaSans-Bold-lf-ts1.tfm)
Provides:       tex(InriaSans-Bold-lf-ts1.vf)
Provides:       tex(InriaSans-Bold-osf-ly1--base.tfm)
Provides:       tex(InriaSans-Bold-osf-ly1.tfm)
Provides:       tex(InriaSans-Bold-osf-ly1.vf)
Provides:       tex(InriaSans-Bold-osf-ot1.tfm)
Provides:       tex(InriaSans-Bold-osf-t1--base.tfm)
Provides:       tex(InriaSans-Bold-osf-t1.tfm)
Provides:       tex(InriaSans-Bold-osf-t1.vf)
Provides:       tex(InriaSans-Bold-osf-ts1--base.tfm)
Provides:       tex(InriaSans-Bold-osf-ts1.tfm)
Provides:       tex(InriaSans-Bold-osf-ts1.vf)
Provides:       tex(InriaSans-Bold-sup-ly1--base.tfm)
Provides:       tex(InriaSans-Bold-sup-ly1.tfm)
Provides:       tex(InriaSans-Bold-sup-ly1.vf)
Provides:       tex(InriaSans-Bold-sup-ot1.tfm)
Provides:       tex(InriaSans-Bold-sup-t1--base.tfm)
Provides:       tex(InriaSans-Bold-sup-t1.tfm)
Provides:       tex(InriaSans-Bold-sup-t1.vf)
Provides:       tex(InriaSans-Bold-tlf-ly1--base.tfm)
Provides:       tex(InriaSans-Bold-tlf-ly1.tfm)
Provides:       tex(InriaSans-Bold-tlf-ly1.vf)
Provides:       tex(InriaSans-Bold-tlf-ot1.tfm)
Provides:       tex(InriaSans-Bold-tlf-t1--base.tfm)
Provides:       tex(InriaSans-Bold-tlf-t1.tfm)
Provides:       tex(InriaSans-Bold-tlf-t1.vf)
Provides:       tex(InriaSans-Bold-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-Bold-tlf-titling-ly1.tfm)
Provides:       tex(InriaSans-Bold-tlf-titling-ly1.vf)
Provides:       tex(InriaSans-Bold-tlf-titling-ot1.tfm)
Provides:       tex(InriaSans-Bold-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSans-Bold-tlf-titling-t1.tfm)
Provides:       tex(InriaSans-Bold-tlf-titling-t1.vf)
Provides:       tex(InriaSans-Bold-tlf-ts1--base.tfm)
Provides:       tex(InriaSans-Bold-tlf-ts1.tfm)
Provides:       tex(InriaSans-Bold-tlf-ts1.vf)
Provides:       tex(InriaSans-Bold-tosf-ly1--base.tfm)
Provides:       tex(InriaSans-Bold-tosf-ly1.tfm)
Provides:       tex(InriaSans-Bold-tosf-ly1.vf)
Provides:       tex(InriaSans-Bold-tosf-ot1.tfm)
Provides:       tex(InriaSans-Bold-tosf-t1--base.tfm)
Provides:       tex(InriaSans-Bold-tosf-t1.tfm)
Provides:       tex(InriaSans-Bold-tosf-t1.vf)
Provides:       tex(InriaSans-Bold-tosf-ts1--base.tfm)
Provides:       tex(InriaSans-Bold-tosf-ts1.tfm)
Provides:       tex(InriaSans-Bold-tosf-ts1.vf)
Provides:       tex(InriaSans-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-ly1.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-ly1.vf)
Provides:       tex(InriaSans-BoldItalic-lf-ot1.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-t1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-t1.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-t1.vf)
Provides:       tex(InriaSans-BoldItalic-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-titling-ly1.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-titling-ly1.vf)
Provides:       tex(InriaSans-BoldItalic-lf-titling-ot1.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-titling-t1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-titling-t1.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-titling-t1.vf)
Provides:       tex(InriaSans-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-ts1.tfm)
Provides:       tex(InriaSans-BoldItalic-lf-ts1.vf)
Provides:       tex(InriaSans-BoldItalic-osf-ly1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-osf-ly1.tfm)
Provides:       tex(InriaSans-BoldItalic-osf-ly1.vf)
Provides:       tex(InriaSans-BoldItalic-osf-ot1.tfm)
Provides:       tex(InriaSans-BoldItalic-osf-t1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-osf-t1.tfm)
Provides:       tex(InriaSans-BoldItalic-osf-t1.vf)
Provides:       tex(InriaSans-BoldItalic-osf-ts1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-osf-ts1.tfm)
Provides:       tex(InriaSans-BoldItalic-osf-ts1.vf)
Provides:       tex(InriaSans-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-sup-ly1.tfm)
Provides:       tex(InriaSans-BoldItalic-sup-ly1.vf)
Provides:       tex(InriaSans-BoldItalic-sup-ot1.tfm)
Provides:       tex(InriaSans-BoldItalic-sup-t1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-sup-t1.tfm)
Provides:       tex(InriaSans-BoldItalic-sup-t1.vf)
Provides:       tex(InriaSans-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-ly1.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-ly1.vf)
Provides:       tex(InriaSans-BoldItalic-tlf-ot1.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-t1.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-t1.vf)
Provides:       tex(InriaSans-BoldItalic-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-titling-ly1.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-titling-ly1.vf)
Provides:       tex(InriaSans-BoldItalic-tlf-titling-ot1.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-titling-t1.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-titling-t1.vf)
Provides:       tex(InriaSans-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-ts1.tfm)
Provides:       tex(InriaSans-BoldItalic-tlf-ts1.vf)
Provides:       tex(InriaSans-BoldItalic-tosf-ly1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-tosf-ly1.tfm)
Provides:       tex(InriaSans-BoldItalic-tosf-ly1.vf)
Provides:       tex(InriaSans-BoldItalic-tosf-ot1.tfm)
Provides:       tex(InriaSans-BoldItalic-tosf-t1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-tosf-t1.tfm)
Provides:       tex(InriaSans-BoldItalic-tosf-t1.vf)
Provides:       tex(InriaSans-BoldItalic-tosf-ts1--base.tfm)
Provides:       tex(InriaSans-BoldItalic-tosf-ts1.tfm)
Provides:       tex(InriaSans-BoldItalic-tosf-ts1.vf)
Provides:       tex(InriaSans-Italic-lf-ly1--base.tfm)
Provides:       tex(InriaSans-Italic-lf-ly1.tfm)
Provides:       tex(InriaSans-Italic-lf-ly1.vf)
Provides:       tex(InriaSans-Italic-lf-ot1.tfm)
Provides:       tex(InriaSans-Italic-lf-t1--base.tfm)
Provides:       tex(InriaSans-Italic-lf-t1.tfm)
Provides:       tex(InriaSans-Italic-lf-t1.vf)
Provides:       tex(InriaSans-Italic-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-Italic-lf-titling-ly1.tfm)
Provides:       tex(InriaSans-Italic-lf-titling-ly1.vf)
Provides:       tex(InriaSans-Italic-lf-titling-ot1.tfm)
Provides:       tex(InriaSans-Italic-lf-titling-t1--base.tfm)
Provides:       tex(InriaSans-Italic-lf-titling-t1.tfm)
Provides:       tex(InriaSans-Italic-lf-titling-t1.vf)
Provides:       tex(InriaSans-Italic-lf-ts1--base.tfm)
Provides:       tex(InriaSans-Italic-lf-ts1.tfm)
Provides:       tex(InriaSans-Italic-lf-ts1.vf)
Provides:       tex(InriaSans-Italic-osf-ly1--base.tfm)
Provides:       tex(InriaSans-Italic-osf-ly1.tfm)
Provides:       tex(InriaSans-Italic-osf-ly1.vf)
Provides:       tex(InriaSans-Italic-osf-ot1.tfm)
Provides:       tex(InriaSans-Italic-osf-t1--base.tfm)
Provides:       tex(InriaSans-Italic-osf-t1.tfm)
Provides:       tex(InriaSans-Italic-osf-t1.vf)
Provides:       tex(InriaSans-Italic-osf-ts1--base.tfm)
Provides:       tex(InriaSans-Italic-osf-ts1.tfm)
Provides:       tex(InriaSans-Italic-osf-ts1.vf)
Provides:       tex(InriaSans-Italic-sup-ly1--base.tfm)
Provides:       tex(InriaSans-Italic-sup-ly1.tfm)
Provides:       tex(InriaSans-Italic-sup-ly1.vf)
Provides:       tex(InriaSans-Italic-sup-ot1.tfm)
Provides:       tex(InriaSans-Italic-sup-t1--base.tfm)
Provides:       tex(InriaSans-Italic-sup-t1.tfm)
Provides:       tex(InriaSans-Italic-sup-t1.vf)
Provides:       tex(InriaSans-Italic-tlf-ly1--base.tfm)
Provides:       tex(InriaSans-Italic-tlf-ly1.tfm)
Provides:       tex(InriaSans-Italic-tlf-ly1.vf)
Provides:       tex(InriaSans-Italic-tlf-ot1.tfm)
Provides:       tex(InriaSans-Italic-tlf-t1--base.tfm)
Provides:       tex(InriaSans-Italic-tlf-t1.tfm)
Provides:       tex(InriaSans-Italic-tlf-t1.vf)
Provides:       tex(InriaSans-Italic-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-Italic-tlf-titling-ly1.tfm)
Provides:       tex(InriaSans-Italic-tlf-titling-ly1.vf)
Provides:       tex(InriaSans-Italic-tlf-titling-ot1.tfm)
Provides:       tex(InriaSans-Italic-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSans-Italic-tlf-titling-t1.tfm)
Provides:       tex(InriaSans-Italic-tlf-titling-t1.vf)
Provides:       tex(InriaSans-Italic-tlf-ts1--base.tfm)
Provides:       tex(InriaSans-Italic-tlf-ts1.tfm)
Provides:       tex(InriaSans-Italic-tlf-ts1.vf)
Provides:       tex(InriaSans-Italic-tosf-ly1--base.tfm)
Provides:       tex(InriaSans-Italic-tosf-ly1.tfm)
Provides:       tex(InriaSans-Italic-tosf-ly1.vf)
Provides:       tex(InriaSans-Italic-tosf-ot1.tfm)
Provides:       tex(InriaSans-Italic-tosf-t1--base.tfm)
Provides:       tex(InriaSans-Italic-tosf-t1.tfm)
Provides:       tex(InriaSans-Italic-tosf-t1.vf)
Provides:       tex(InriaSans-Italic-tosf-ts1--base.tfm)
Provides:       tex(InriaSans-Italic-tosf-ts1.tfm)
Provides:       tex(InriaSans-Italic-tosf-ts1.vf)
Provides:       tex(InriaSans-Light-lf-ly1--base.tfm)
Provides:       tex(InriaSans-Light-lf-ly1.tfm)
Provides:       tex(InriaSans-Light-lf-ly1.vf)
Provides:       tex(InriaSans-Light-lf-ot1.tfm)
Provides:       tex(InriaSans-Light-lf-t1--base.tfm)
Provides:       tex(InriaSans-Light-lf-t1.tfm)
Provides:       tex(InriaSans-Light-lf-t1.vf)
Provides:       tex(InriaSans-Light-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-Light-lf-titling-ly1.tfm)
Provides:       tex(InriaSans-Light-lf-titling-ly1.vf)
Provides:       tex(InriaSans-Light-lf-titling-ot1.tfm)
Provides:       tex(InriaSans-Light-lf-titling-t1--base.tfm)
Provides:       tex(InriaSans-Light-lf-titling-t1.tfm)
Provides:       tex(InriaSans-Light-lf-titling-t1.vf)
Provides:       tex(InriaSans-Light-lf-ts1--base.tfm)
Provides:       tex(InriaSans-Light-lf-ts1.tfm)
Provides:       tex(InriaSans-Light-lf-ts1.vf)
Provides:       tex(InriaSans-Light-osf-ly1--base.tfm)
Provides:       tex(InriaSans-Light-osf-ly1.tfm)
Provides:       tex(InriaSans-Light-osf-ly1.vf)
Provides:       tex(InriaSans-Light-osf-ot1.tfm)
Provides:       tex(InriaSans-Light-osf-t1--base.tfm)
Provides:       tex(InriaSans-Light-osf-t1.tfm)
Provides:       tex(InriaSans-Light-osf-t1.vf)
Provides:       tex(InriaSans-Light-osf-ts1--base.tfm)
Provides:       tex(InriaSans-Light-osf-ts1.tfm)
Provides:       tex(InriaSans-Light-osf-ts1.vf)
Provides:       tex(InriaSans-Light-sup-ly1--base.tfm)
Provides:       tex(InriaSans-Light-sup-ly1.tfm)
Provides:       tex(InriaSans-Light-sup-ly1.vf)
Provides:       tex(InriaSans-Light-sup-ot1.tfm)
Provides:       tex(InriaSans-Light-sup-t1--base.tfm)
Provides:       tex(InriaSans-Light-sup-t1.tfm)
Provides:       tex(InriaSans-Light-sup-t1.vf)
Provides:       tex(InriaSans-Light-tlf-ly1--base.tfm)
Provides:       tex(InriaSans-Light-tlf-ly1.tfm)
Provides:       tex(InriaSans-Light-tlf-ly1.vf)
Provides:       tex(InriaSans-Light-tlf-ot1.tfm)
Provides:       tex(InriaSans-Light-tlf-t1--base.tfm)
Provides:       tex(InriaSans-Light-tlf-t1.tfm)
Provides:       tex(InriaSans-Light-tlf-t1.vf)
Provides:       tex(InriaSans-Light-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-Light-tlf-titling-ly1.tfm)
Provides:       tex(InriaSans-Light-tlf-titling-ly1.vf)
Provides:       tex(InriaSans-Light-tlf-titling-ot1.tfm)
Provides:       tex(InriaSans-Light-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSans-Light-tlf-titling-t1.tfm)
Provides:       tex(InriaSans-Light-tlf-titling-t1.vf)
Provides:       tex(InriaSans-Light-tlf-ts1--base.tfm)
Provides:       tex(InriaSans-Light-tlf-ts1.tfm)
Provides:       tex(InriaSans-Light-tlf-ts1.vf)
Provides:       tex(InriaSans-Light-tosf-ly1--base.tfm)
Provides:       tex(InriaSans-Light-tosf-ly1.tfm)
Provides:       tex(InriaSans-Light-tosf-ly1.vf)
Provides:       tex(InriaSans-Light-tosf-ot1.tfm)
Provides:       tex(InriaSans-Light-tosf-t1--base.tfm)
Provides:       tex(InriaSans-Light-tosf-t1.tfm)
Provides:       tex(InriaSans-Light-tosf-t1.vf)
Provides:       tex(InriaSans-Light-tosf-ts1--base.tfm)
Provides:       tex(InriaSans-Light-tosf-ts1.tfm)
Provides:       tex(InriaSans-Light-tosf-ts1.vf)
Provides:       tex(InriaSans-LightItalic-lf-ly1--base.tfm)
Provides:       tex(InriaSans-LightItalic-lf-ly1.tfm)
Provides:       tex(InriaSans-LightItalic-lf-ly1.vf)
Provides:       tex(InriaSans-LightItalic-lf-ot1.tfm)
Provides:       tex(InriaSans-LightItalic-lf-t1--base.tfm)
Provides:       tex(InriaSans-LightItalic-lf-t1.tfm)
Provides:       tex(InriaSans-LightItalic-lf-t1.vf)
Provides:       tex(InriaSans-LightItalic-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-LightItalic-lf-titling-ly1.tfm)
Provides:       tex(InriaSans-LightItalic-lf-titling-ly1.vf)
Provides:       tex(InriaSans-LightItalic-lf-titling-ot1.tfm)
Provides:       tex(InriaSans-LightItalic-lf-titling-t1--base.tfm)
Provides:       tex(InriaSans-LightItalic-lf-titling-t1.tfm)
Provides:       tex(InriaSans-LightItalic-lf-titling-t1.vf)
Provides:       tex(InriaSans-LightItalic-lf-ts1--base.tfm)
Provides:       tex(InriaSans-LightItalic-lf-ts1.tfm)
Provides:       tex(InriaSans-LightItalic-lf-ts1.vf)
Provides:       tex(InriaSans-LightItalic-osf-ly1--base.tfm)
Provides:       tex(InriaSans-LightItalic-osf-ly1.tfm)
Provides:       tex(InriaSans-LightItalic-osf-ly1.vf)
Provides:       tex(InriaSans-LightItalic-osf-ot1.tfm)
Provides:       tex(InriaSans-LightItalic-osf-t1--base.tfm)
Provides:       tex(InriaSans-LightItalic-osf-t1.tfm)
Provides:       tex(InriaSans-LightItalic-osf-t1.vf)
Provides:       tex(InriaSans-LightItalic-osf-ts1--base.tfm)
Provides:       tex(InriaSans-LightItalic-osf-ts1.tfm)
Provides:       tex(InriaSans-LightItalic-osf-ts1.vf)
Provides:       tex(InriaSans-LightItalic-sup-ly1--base.tfm)
Provides:       tex(InriaSans-LightItalic-sup-ly1.tfm)
Provides:       tex(InriaSans-LightItalic-sup-ly1.vf)
Provides:       tex(InriaSans-LightItalic-sup-ot1.tfm)
Provides:       tex(InriaSans-LightItalic-sup-t1--base.tfm)
Provides:       tex(InriaSans-LightItalic-sup-t1.tfm)
Provides:       tex(InriaSans-LightItalic-sup-t1.vf)
Provides:       tex(InriaSans-LightItalic-tlf-ly1--base.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-ly1.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-ly1.vf)
Provides:       tex(InriaSans-LightItalic-tlf-ot1.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-t1--base.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-t1.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-t1.vf)
Provides:       tex(InriaSans-LightItalic-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-titling-ly1.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-titling-ly1.vf)
Provides:       tex(InriaSans-LightItalic-tlf-titling-ot1.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-titling-t1.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-titling-t1.vf)
Provides:       tex(InriaSans-LightItalic-tlf-ts1--base.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-ts1.tfm)
Provides:       tex(InriaSans-LightItalic-tlf-ts1.vf)
Provides:       tex(InriaSans-LightItalic-tosf-ly1--base.tfm)
Provides:       tex(InriaSans-LightItalic-tosf-ly1.tfm)
Provides:       tex(InriaSans-LightItalic-tosf-ly1.vf)
Provides:       tex(InriaSans-LightItalic-tosf-ot1.tfm)
Provides:       tex(InriaSans-LightItalic-tosf-t1--base.tfm)
Provides:       tex(InriaSans-LightItalic-tosf-t1.tfm)
Provides:       tex(InriaSans-LightItalic-tosf-t1.vf)
Provides:       tex(InriaSans-LightItalic-tosf-ts1--base.tfm)
Provides:       tex(InriaSans-LightItalic-tosf-ts1.tfm)
Provides:       tex(InriaSans-LightItalic-tosf-ts1.vf)
Provides:       tex(InriaSans-Regular-lf-ly1--base.tfm)
Provides:       tex(InriaSans-Regular-lf-ly1.tfm)
Provides:       tex(InriaSans-Regular-lf-ly1.vf)
Provides:       tex(InriaSans-Regular-lf-ot1.tfm)
Provides:       tex(InriaSans-Regular-lf-t1--base.tfm)
Provides:       tex(InriaSans-Regular-lf-t1.tfm)
Provides:       tex(InriaSans-Regular-lf-t1.vf)
Provides:       tex(InriaSans-Regular-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-Regular-lf-titling-ly1.tfm)
Provides:       tex(InriaSans-Regular-lf-titling-ly1.vf)
Provides:       tex(InriaSans-Regular-lf-titling-ot1.tfm)
Provides:       tex(InriaSans-Regular-lf-titling-t1--base.tfm)
Provides:       tex(InriaSans-Regular-lf-titling-t1.tfm)
Provides:       tex(InriaSans-Regular-lf-titling-t1.vf)
Provides:       tex(InriaSans-Regular-lf-ts1--base.tfm)
Provides:       tex(InriaSans-Regular-lf-ts1.tfm)
Provides:       tex(InriaSans-Regular-lf-ts1.vf)
Provides:       tex(InriaSans-Regular-osf-ly1--base.tfm)
Provides:       tex(InriaSans-Regular-osf-ly1.tfm)
Provides:       tex(InriaSans-Regular-osf-ly1.vf)
Provides:       tex(InriaSans-Regular-osf-ot1.tfm)
Provides:       tex(InriaSans-Regular-osf-t1--base.tfm)
Provides:       tex(InriaSans-Regular-osf-t1.tfm)
Provides:       tex(InriaSans-Regular-osf-t1.vf)
Provides:       tex(InriaSans-Regular-osf-ts1--base.tfm)
Provides:       tex(InriaSans-Regular-osf-ts1.tfm)
Provides:       tex(InriaSans-Regular-osf-ts1.vf)
Provides:       tex(InriaSans-Regular-sup-ly1--base.tfm)
Provides:       tex(InriaSans-Regular-sup-ly1.tfm)
Provides:       tex(InriaSans-Regular-sup-ly1.vf)
Provides:       tex(InriaSans-Regular-sup-ot1.tfm)
Provides:       tex(InriaSans-Regular-sup-t1--base.tfm)
Provides:       tex(InriaSans-Regular-sup-t1.tfm)
Provides:       tex(InriaSans-Regular-sup-t1.vf)
Provides:       tex(InriaSans-Regular-tlf-ly1--base.tfm)
Provides:       tex(InriaSans-Regular-tlf-ly1.tfm)
Provides:       tex(InriaSans-Regular-tlf-ly1.vf)
Provides:       tex(InriaSans-Regular-tlf-ot1.tfm)
Provides:       tex(InriaSans-Regular-tlf-t1--base.tfm)
Provides:       tex(InriaSans-Regular-tlf-t1.tfm)
Provides:       tex(InriaSans-Regular-tlf-t1.vf)
Provides:       tex(InriaSans-Regular-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSans-Regular-tlf-titling-ly1.tfm)
Provides:       tex(InriaSans-Regular-tlf-titling-ly1.vf)
Provides:       tex(InriaSans-Regular-tlf-titling-ot1.tfm)
Provides:       tex(InriaSans-Regular-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSans-Regular-tlf-titling-t1.tfm)
Provides:       tex(InriaSans-Regular-tlf-titling-t1.vf)
Provides:       tex(InriaSans-Regular-tlf-ts1--base.tfm)
Provides:       tex(InriaSans-Regular-tlf-ts1.tfm)
Provides:       tex(InriaSans-Regular-tlf-ts1.vf)
Provides:       tex(InriaSans-Regular-tosf-ly1--base.tfm)
Provides:       tex(InriaSans-Regular-tosf-ly1.tfm)
Provides:       tex(InriaSans-Regular-tosf-ly1.vf)
Provides:       tex(InriaSans-Regular-tosf-ot1.tfm)
Provides:       tex(InriaSans-Regular-tosf-t1--base.tfm)
Provides:       tex(InriaSans-Regular-tosf-t1.tfm)
Provides:       tex(InriaSans-Regular-tosf-t1.vf)
Provides:       tex(InriaSans-Regular-tosf-ts1--base.tfm)
Provides:       tex(InriaSans-Regular-tosf-ts1.tfm)
Provides:       tex(InriaSans-Regular-tosf-ts1.vf)
Provides:       tex(InriaSans.map)
Provides:       tex(InriaSans.sty)
Provides:       tex(InriaSerif-Bold-lf-ly1--base.tfm)
Provides:       tex(InriaSerif-Bold-lf-ly1.tfm)
Provides:       tex(InriaSerif-Bold-lf-ly1.vf)
Provides:       tex(InriaSerif-Bold-lf-ot1.tfm)
Provides:       tex(InriaSerif-Bold-lf-t1--base.tfm)
Provides:       tex(InriaSerif-Bold-lf-t1.tfm)
Provides:       tex(InriaSerif-Bold-lf-t1.vf)
Provides:       tex(InriaSerif-Bold-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-Bold-lf-titling-ly1.tfm)
Provides:       tex(InriaSerif-Bold-lf-titling-ly1.vf)
Provides:       tex(InriaSerif-Bold-lf-titling-ot1.tfm)
Provides:       tex(InriaSerif-Bold-lf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-Bold-lf-titling-t1.tfm)
Provides:       tex(InriaSerif-Bold-lf-titling-t1.vf)
Provides:       tex(InriaSerif-Bold-lf-ts1--base.tfm)
Provides:       tex(InriaSerif-Bold-lf-ts1.tfm)
Provides:       tex(InriaSerif-Bold-lf-ts1.vf)
Provides:       tex(InriaSerif-Bold-osf-ly1--base.tfm)
Provides:       tex(InriaSerif-Bold-osf-ly1.tfm)
Provides:       tex(InriaSerif-Bold-osf-ly1.vf)
Provides:       tex(InriaSerif-Bold-osf-ot1.tfm)
Provides:       tex(InriaSerif-Bold-osf-t1--base.tfm)
Provides:       tex(InriaSerif-Bold-osf-t1.tfm)
Provides:       tex(InriaSerif-Bold-osf-t1.vf)
Provides:       tex(InriaSerif-Bold-osf-ts1--base.tfm)
Provides:       tex(InriaSerif-Bold-osf-ts1.tfm)
Provides:       tex(InriaSerif-Bold-osf-ts1.vf)
Provides:       tex(InriaSerif-Bold-sup-ly1--base.tfm)
Provides:       tex(InriaSerif-Bold-sup-ly1.tfm)
Provides:       tex(InriaSerif-Bold-sup-ly1.vf)
Provides:       tex(InriaSerif-Bold-sup-ot1.tfm)
Provides:       tex(InriaSerif-Bold-sup-t1--base.tfm)
Provides:       tex(InriaSerif-Bold-sup-t1.tfm)
Provides:       tex(InriaSerif-Bold-sup-t1.vf)
Provides:       tex(InriaSerif-Bold-tlf-ly1--base.tfm)
Provides:       tex(InriaSerif-Bold-tlf-ly1.tfm)
Provides:       tex(InriaSerif-Bold-tlf-ly1.vf)
Provides:       tex(InriaSerif-Bold-tlf-ot1.tfm)
Provides:       tex(InriaSerif-Bold-tlf-t1--base.tfm)
Provides:       tex(InriaSerif-Bold-tlf-t1.tfm)
Provides:       tex(InriaSerif-Bold-tlf-t1.vf)
Provides:       tex(InriaSerif-Bold-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-Bold-tlf-titling-ly1.tfm)
Provides:       tex(InriaSerif-Bold-tlf-titling-ly1.vf)
Provides:       tex(InriaSerif-Bold-tlf-titling-ot1.tfm)
Provides:       tex(InriaSerif-Bold-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-Bold-tlf-titling-t1.tfm)
Provides:       tex(InriaSerif-Bold-tlf-titling-t1.vf)
Provides:       tex(InriaSerif-Bold-tlf-ts1--base.tfm)
Provides:       tex(InriaSerif-Bold-tlf-ts1.tfm)
Provides:       tex(InriaSerif-Bold-tlf-ts1.vf)
Provides:       tex(InriaSerif-Bold-tosf-ly1--base.tfm)
Provides:       tex(InriaSerif-Bold-tosf-ly1.tfm)
Provides:       tex(InriaSerif-Bold-tosf-ly1.vf)
Provides:       tex(InriaSerif-Bold-tosf-ot1.tfm)
Provides:       tex(InriaSerif-Bold-tosf-t1--base.tfm)
Provides:       tex(InriaSerif-Bold-tosf-t1.tfm)
Provides:       tex(InriaSerif-Bold-tosf-t1.vf)
Provides:       tex(InriaSerif-Bold-tosf-ts1--base.tfm)
Provides:       tex(InriaSerif-Bold-tosf-ts1.tfm)
Provides:       tex(InriaSerif-Bold-tosf-ts1.vf)
Provides:       tex(InriaSerif-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-ly1.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-ly1.vf)
Provides:       tex(InriaSerif-BoldItalic-lf-ot1.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-t1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-t1.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-t1.vf)
Provides:       tex(InriaSerif-BoldItalic-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-titling-ly1.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-titling-ly1.vf)
Provides:       tex(InriaSerif-BoldItalic-lf-titling-ot1.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-titling-t1.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-titling-t1.vf)
Provides:       tex(InriaSerif-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-ts1.tfm)
Provides:       tex(InriaSerif-BoldItalic-lf-ts1.vf)
Provides:       tex(InriaSerif-BoldItalic-osf-ly1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-osf-ly1.tfm)
Provides:       tex(InriaSerif-BoldItalic-osf-ly1.vf)
Provides:       tex(InriaSerif-BoldItalic-osf-ot1.tfm)
Provides:       tex(InriaSerif-BoldItalic-osf-t1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-osf-t1.tfm)
Provides:       tex(InriaSerif-BoldItalic-osf-t1.vf)
Provides:       tex(InriaSerif-BoldItalic-osf-ts1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-osf-ts1.tfm)
Provides:       tex(InriaSerif-BoldItalic-osf-ts1.vf)
Provides:       tex(InriaSerif-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-sup-ly1.tfm)
Provides:       tex(InriaSerif-BoldItalic-sup-ly1.vf)
Provides:       tex(InriaSerif-BoldItalic-sup-ot1.tfm)
Provides:       tex(InriaSerif-BoldItalic-sup-t1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-sup-t1.tfm)
Provides:       tex(InriaSerif-BoldItalic-sup-t1.vf)
Provides:       tex(InriaSerif-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-ly1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-ly1.vf)
Provides:       tex(InriaSerif-BoldItalic-tlf-ot1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-t1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-t1.vf)
Provides:       tex(InriaSerif-BoldItalic-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-titling-ly1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-titling-ly1.vf)
Provides:       tex(InriaSerif-BoldItalic-tlf-titling-ot1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-titling-t1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-titling-t1.vf)
Provides:       tex(InriaSerif-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-ts1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tlf-ts1.vf)
Provides:       tex(InriaSerif-BoldItalic-tosf-ly1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-tosf-ly1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tosf-ly1.vf)
Provides:       tex(InriaSerif-BoldItalic-tosf-ot1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tosf-t1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-tosf-t1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tosf-t1.vf)
Provides:       tex(InriaSerif-BoldItalic-tosf-ts1--base.tfm)
Provides:       tex(InriaSerif-BoldItalic-tosf-ts1.tfm)
Provides:       tex(InriaSerif-BoldItalic-tosf-ts1.vf)
Provides:       tex(InriaSerif-Italic-lf-ly1--base.tfm)
Provides:       tex(InriaSerif-Italic-lf-ly1.tfm)
Provides:       tex(InriaSerif-Italic-lf-ly1.vf)
Provides:       tex(InriaSerif-Italic-lf-ot1.tfm)
Provides:       tex(InriaSerif-Italic-lf-t1--base.tfm)
Provides:       tex(InriaSerif-Italic-lf-t1.tfm)
Provides:       tex(InriaSerif-Italic-lf-t1.vf)
Provides:       tex(InriaSerif-Italic-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-Italic-lf-titling-ly1.tfm)
Provides:       tex(InriaSerif-Italic-lf-titling-ly1.vf)
Provides:       tex(InriaSerif-Italic-lf-titling-ot1.tfm)
Provides:       tex(InriaSerif-Italic-lf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-Italic-lf-titling-t1.tfm)
Provides:       tex(InriaSerif-Italic-lf-titling-t1.vf)
Provides:       tex(InriaSerif-Italic-lf-ts1--base.tfm)
Provides:       tex(InriaSerif-Italic-lf-ts1.tfm)
Provides:       tex(InriaSerif-Italic-lf-ts1.vf)
Provides:       tex(InriaSerif-Italic-osf-ly1--base.tfm)
Provides:       tex(InriaSerif-Italic-osf-ly1.tfm)
Provides:       tex(InriaSerif-Italic-osf-ly1.vf)
Provides:       tex(InriaSerif-Italic-osf-ot1.tfm)
Provides:       tex(InriaSerif-Italic-osf-t1--base.tfm)
Provides:       tex(InriaSerif-Italic-osf-t1.tfm)
Provides:       tex(InriaSerif-Italic-osf-t1.vf)
Provides:       tex(InriaSerif-Italic-osf-ts1--base.tfm)
Provides:       tex(InriaSerif-Italic-osf-ts1.tfm)
Provides:       tex(InriaSerif-Italic-osf-ts1.vf)
Provides:       tex(InriaSerif-Italic-sup-ly1--base.tfm)
Provides:       tex(InriaSerif-Italic-sup-ly1.tfm)
Provides:       tex(InriaSerif-Italic-sup-ly1.vf)
Provides:       tex(InriaSerif-Italic-sup-ot1.tfm)
Provides:       tex(InriaSerif-Italic-sup-t1--base.tfm)
Provides:       tex(InriaSerif-Italic-sup-t1.tfm)
Provides:       tex(InriaSerif-Italic-sup-t1.vf)
Provides:       tex(InriaSerif-Italic-tlf-ly1--base.tfm)
Provides:       tex(InriaSerif-Italic-tlf-ly1.tfm)
Provides:       tex(InriaSerif-Italic-tlf-ly1.vf)
Provides:       tex(InriaSerif-Italic-tlf-ot1.tfm)
Provides:       tex(InriaSerif-Italic-tlf-t1--base.tfm)
Provides:       tex(InriaSerif-Italic-tlf-t1.tfm)
Provides:       tex(InriaSerif-Italic-tlf-t1.vf)
Provides:       tex(InriaSerif-Italic-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-Italic-tlf-titling-ly1.tfm)
Provides:       tex(InriaSerif-Italic-tlf-titling-ly1.vf)
Provides:       tex(InriaSerif-Italic-tlf-titling-ot1.tfm)
Provides:       tex(InriaSerif-Italic-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-Italic-tlf-titling-t1.tfm)
Provides:       tex(InriaSerif-Italic-tlf-titling-t1.vf)
Provides:       tex(InriaSerif-Italic-tlf-ts1--base.tfm)
Provides:       tex(InriaSerif-Italic-tlf-ts1.tfm)
Provides:       tex(InriaSerif-Italic-tlf-ts1.vf)
Provides:       tex(InriaSerif-Italic-tosf-ly1--base.tfm)
Provides:       tex(InriaSerif-Italic-tosf-ly1.tfm)
Provides:       tex(InriaSerif-Italic-tosf-ly1.vf)
Provides:       tex(InriaSerif-Italic-tosf-ot1.tfm)
Provides:       tex(InriaSerif-Italic-tosf-t1--base.tfm)
Provides:       tex(InriaSerif-Italic-tosf-t1.tfm)
Provides:       tex(InriaSerif-Italic-tosf-t1.vf)
Provides:       tex(InriaSerif-Italic-tosf-ts1--base.tfm)
Provides:       tex(InriaSerif-Italic-tosf-ts1.tfm)
Provides:       tex(InriaSerif-Italic-tosf-ts1.vf)
Provides:       tex(InriaSerif-Light-lf-ly1--base.tfm)
Provides:       tex(InriaSerif-Light-lf-ly1.tfm)
Provides:       tex(InriaSerif-Light-lf-ly1.vf)
Provides:       tex(InriaSerif-Light-lf-ot1.tfm)
Provides:       tex(InriaSerif-Light-lf-t1--base.tfm)
Provides:       tex(InriaSerif-Light-lf-t1.tfm)
Provides:       tex(InriaSerif-Light-lf-t1.vf)
Provides:       tex(InriaSerif-Light-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-Light-lf-titling-ly1.tfm)
Provides:       tex(InriaSerif-Light-lf-titling-ly1.vf)
Provides:       tex(InriaSerif-Light-lf-titling-ot1.tfm)
Provides:       tex(InriaSerif-Light-lf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-Light-lf-titling-t1.tfm)
Provides:       tex(InriaSerif-Light-lf-titling-t1.vf)
Provides:       tex(InriaSerif-Light-lf-ts1--base.tfm)
Provides:       tex(InriaSerif-Light-lf-ts1.tfm)
Provides:       tex(InriaSerif-Light-lf-ts1.vf)
Provides:       tex(InriaSerif-Light-osf-ly1--base.tfm)
Provides:       tex(InriaSerif-Light-osf-ly1.tfm)
Provides:       tex(InriaSerif-Light-osf-ly1.vf)
Provides:       tex(InriaSerif-Light-osf-ot1.tfm)
Provides:       tex(InriaSerif-Light-osf-t1--base.tfm)
Provides:       tex(InriaSerif-Light-osf-t1.tfm)
Provides:       tex(InriaSerif-Light-osf-t1.vf)
Provides:       tex(InriaSerif-Light-osf-ts1--base.tfm)
Provides:       tex(InriaSerif-Light-osf-ts1.tfm)
Provides:       tex(InriaSerif-Light-osf-ts1.vf)
Provides:       tex(InriaSerif-Light-sup-ly1--base.tfm)
Provides:       tex(InriaSerif-Light-sup-ly1.tfm)
Provides:       tex(InriaSerif-Light-sup-ly1.vf)
Provides:       tex(InriaSerif-Light-sup-ot1.tfm)
Provides:       tex(InriaSerif-Light-sup-t1--base.tfm)
Provides:       tex(InriaSerif-Light-sup-t1.tfm)
Provides:       tex(InriaSerif-Light-sup-t1.vf)
Provides:       tex(InriaSerif-Light-tlf-ly1--base.tfm)
Provides:       tex(InriaSerif-Light-tlf-ly1.tfm)
Provides:       tex(InriaSerif-Light-tlf-ly1.vf)
Provides:       tex(InriaSerif-Light-tlf-ot1.tfm)
Provides:       tex(InriaSerif-Light-tlf-t1--base.tfm)
Provides:       tex(InriaSerif-Light-tlf-t1.tfm)
Provides:       tex(InriaSerif-Light-tlf-t1.vf)
Provides:       tex(InriaSerif-Light-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-Light-tlf-titling-ly1.tfm)
Provides:       tex(InriaSerif-Light-tlf-titling-ly1.vf)
Provides:       tex(InriaSerif-Light-tlf-titling-ot1.tfm)
Provides:       tex(InriaSerif-Light-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-Light-tlf-titling-t1.tfm)
Provides:       tex(InriaSerif-Light-tlf-titling-t1.vf)
Provides:       tex(InriaSerif-Light-tlf-ts1--base.tfm)
Provides:       tex(InriaSerif-Light-tlf-ts1.tfm)
Provides:       tex(InriaSerif-Light-tlf-ts1.vf)
Provides:       tex(InriaSerif-Light-tosf-ly1--base.tfm)
Provides:       tex(InriaSerif-Light-tosf-ly1.tfm)
Provides:       tex(InriaSerif-Light-tosf-ly1.vf)
Provides:       tex(InriaSerif-Light-tosf-ot1.tfm)
Provides:       tex(InriaSerif-Light-tosf-t1--base.tfm)
Provides:       tex(InriaSerif-Light-tosf-t1.tfm)
Provides:       tex(InriaSerif-Light-tosf-t1.vf)
Provides:       tex(InriaSerif-Light-tosf-ts1--base.tfm)
Provides:       tex(InriaSerif-Light-tosf-ts1.tfm)
Provides:       tex(InriaSerif-Light-tosf-ts1.vf)
Provides:       tex(InriaSerif-LightItalic-lf-ly1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-ly1.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-ly1.vf)
Provides:       tex(InriaSerif-LightItalic-lf-ot1.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-t1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-t1.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-t1.vf)
Provides:       tex(InriaSerif-LightItalic-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-titling-ly1.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-titling-ly1.vf)
Provides:       tex(InriaSerif-LightItalic-lf-titling-ot1.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-titling-t1.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-titling-t1.vf)
Provides:       tex(InriaSerif-LightItalic-lf-ts1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-ts1.tfm)
Provides:       tex(InriaSerif-LightItalic-lf-ts1.vf)
Provides:       tex(InriaSerif-LightItalic-osf-ly1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-osf-ly1.tfm)
Provides:       tex(InriaSerif-LightItalic-osf-ly1.vf)
Provides:       tex(InriaSerif-LightItalic-osf-ot1.tfm)
Provides:       tex(InriaSerif-LightItalic-osf-t1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-osf-t1.tfm)
Provides:       tex(InriaSerif-LightItalic-osf-t1.vf)
Provides:       tex(InriaSerif-LightItalic-osf-ts1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-osf-ts1.tfm)
Provides:       tex(InriaSerif-LightItalic-osf-ts1.vf)
Provides:       tex(InriaSerif-LightItalic-sup-ly1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-sup-ly1.tfm)
Provides:       tex(InriaSerif-LightItalic-sup-ly1.vf)
Provides:       tex(InriaSerif-LightItalic-sup-ot1.tfm)
Provides:       tex(InriaSerif-LightItalic-sup-t1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-sup-t1.tfm)
Provides:       tex(InriaSerif-LightItalic-sup-t1.vf)
Provides:       tex(InriaSerif-LightItalic-tlf-ly1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-ly1.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-ly1.vf)
Provides:       tex(InriaSerif-LightItalic-tlf-ot1.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-t1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-t1.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-t1.vf)
Provides:       tex(InriaSerif-LightItalic-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-titling-ly1.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-titling-ly1.vf)
Provides:       tex(InriaSerif-LightItalic-tlf-titling-ot1.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-titling-t1.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-titling-t1.vf)
Provides:       tex(InriaSerif-LightItalic-tlf-ts1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-ts1.tfm)
Provides:       tex(InriaSerif-LightItalic-tlf-ts1.vf)
Provides:       tex(InriaSerif-LightItalic-tosf-ly1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-tosf-ly1.tfm)
Provides:       tex(InriaSerif-LightItalic-tosf-ly1.vf)
Provides:       tex(InriaSerif-LightItalic-tosf-ot1.tfm)
Provides:       tex(InriaSerif-LightItalic-tosf-t1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-tosf-t1.tfm)
Provides:       tex(InriaSerif-LightItalic-tosf-t1.vf)
Provides:       tex(InriaSerif-LightItalic-tosf-ts1--base.tfm)
Provides:       tex(InriaSerif-LightItalic-tosf-ts1.tfm)
Provides:       tex(InriaSerif-LightItalic-tosf-ts1.vf)
Provides:       tex(InriaSerif-Regular-lf-ly1--base.tfm)
Provides:       tex(InriaSerif-Regular-lf-ly1.tfm)
Provides:       tex(InriaSerif-Regular-lf-ly1.vf)
Provides:       tex(InriaSerif-Regular-lf-ot1.tfm)
Provides:       tex(InriaSerif-Regular-lf-t1--base.tfm)
Provides:       tex(InriaSerif-Regular-lf-t1.tfm)
Provides:       tex(InriaSerif-Regular-lf-t1.vf)
Provides:       tex(InriaSerif-Regular-lf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-Regular-lf-titling-ly1.tfm)
Provides:       tex(InriaSerif-Regular-lf-titling-ly1.vf)
Provides:       tex(InriaSerif-Regular-lf-titling-ot1.tfm)
Provides:       tex(InriaSerif-Regular-lf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-Regular-lf-titling-t1.tfm)
Provides:       tex(InriaSerif-Regular-lf-titling-t1.vf)
Provides:       tex(InriaSerif-Regular-lf-ts1--base.tfm)
Provides:       tex(InriaSerif-Regular-lf-ts1.tfm)
Provides:       tex(InriaSerif-Regular-lf-ts1.vf)
Provides:       tex(InriaSerif-Regular-osf-ly1--base.tfm)
Provides:       tex(InriaSerif-Regular-osf-ly1.tfm)
Provides:       tex(InriaSerif-Regular-osf-ly1.vf)
Provides:       tex(InriaSerif-Regular-osf-ot1.tfm)
Provides:       tex(InriaSerif-Regular-osf-t1--base.tfm)
Provides:       tex(InriaSerif-Regular-osf-t1.tfm)
Provides:       tex(InriaSerif-Regular-osf-t1.vf)
Provides:       tex(InriaSerif-Regular-osf-ts1--base.tfm)
Provides:       tex(InriaSerif-Regular-osf-ts1.tfm)
Provides:       tex(InriaSerif-Regular-osf-ts1.vf)
Provides:       tex(InriaSerif-Regular-sup-ly1--base.tfm)
Provides:       tex(InriaSerif-Regular-sup-ly1.tfm)
Provides:       tex(InriaSerif-Regular-sup-ly1.vf)
Provides:       tex(InriaSerif-Regular-sup-ot1.tfm)
Provides:       tex(InriaSerif-Regular-sup-t1--base.tfm)
Provides:       tex(InriaSerif-Regular-sup-t1.tfm)
Provides:       tex(InriaSerif-Regular-sup-t1.vf)
Provides:       tex(InriaSerif-Regular-tlf-ly1--base.tfm)
Provides:       tex(InriaSerif-Regular-tlf-ly1.tfm)
Provides:       tex(InriaSerif-Regular-tlf-ly1.vf)
Provides:       tex(InriaSerif-Regular-tlf-ot1.tfm)
Provides:       tex(InriaSerif-Regular-tlf-t1--base.tfm)
Provides:       tex(InriaSerif-Regular-tlf-t1.tfm)
Provides:       tex(InriaSerif-Regular-tlf-t1.vf)
Provides:       tex(InriaSerif-Regular-tlf-titling-ly1--base.tfm)
Provides:       tex(InriaSerif-Regular-tlf-titling-ly1.tfm)
Provides:       tex(InriaSerif-Regular-tlf-titling-ly1.vf)
Provides:       tex(InriaSerif-Regular-tlf-titling-ot1.tfm)
Provides:       tex(InriaSerif-Regular-tlf-titling-t1--base.tfm)
Provides:       tex(InriaSerif-Regular-tlf-titling-t1.tfm)
Provides:       tex(InriaSerif-Regular-tlf-titling-t1.vf)
Provides:       tex(InriaSerif-Regular-tlf-ts1--base.tfm)
Provides:       tex(InriaSerif-Regular-tlf-ts1.tfm)
Provides:       tex(InriaSerif-Regular-tlf-ts1.vf)
Provides:       tex(InriaSerif-Regular-tosf-ly1--base.tfm)
Provides:       tex(InriaSerif-Regular-tosf-ly1.tfm)
Provides:       tex(InriaSerif-Regular-tosf-ly1.vf)
Provides:       tex(InriaSerif-Regular-tosf-ot1.tfm)
Provides:       tex(InriaSerif-Regular-tosf-t1--base.tfm)
Provides:       tex(InriaSerif-Regular-tosf-t1.tfm)
Provides:       tex(InriaSerif-Regular-tosf-t1.vf)
Provides:       tex(InriaSerif-Regular-tosf-ts1--base.tfm)
Provides:       tex(InriaSerif-Regular-tosf-ts1.tfm)
Provides:       tex(InriaSerif-Regular-tosf-ts1.vf)
Provides:       tex(InriaSerif.map)
Provides:       tex(InriaSerif.sty)
Provides:       tex(LY1InriaSans-LF.fd)
Provides:       tex(LY1InriaSans-OsF.fd)
Provides:       tex(LY1InriaSans-Sup.fd)
Provides:       tex(LY1InriaSans-TLF.fd)
Provides:       tex(LY1InriaSans-TOsF.fd)
Provides:       tex(LY1InriaSerif-LF.fd)
Provides:       tex(LY1InriaSerif-OsF.fd)
Provides:       tex(LY1InriaSerif-Sup.fd)
Provides:       tex(LY1InriaSerif-TLF.fd)
Provides:       tex(LY1InriaSerif-TOsF.fd)
Provides:       tex(OT1InriaSans-LF.fd)
Provides:       tex(OT1InriaSans-OsF.fd)
Provides:       tex(OT1InriaSans-Sup.fd)
Provides:       tex(OT1InriaSans-TLF.fd)
Provides:       tex(OT1InriaSans-TOsF.fd)
Provides:       tex(OT1InriaSerif-LF.fd)
Provides:       tex(OT1InriaSerif-OsF.fd)
Provides:       tex(OT1InriaSerif-Sup.fd)
Provides:       tex(OT1InriaSerif-TLF.fd)
Provides:       tex(OT1InriaSerif-TOsF.fd)
Provides:       tex(T1InriaSans-LF.fd)
Provides:       tex(T1InriaSans-OsF.fd)
Provides:       tex(T1InriaSans-Sup.fd)
Provides:       tex(T1InriaSans-TLF.fd)
Provides:       tex(T1InriaSans-TOsF.fd)
Provides:       tex(T1InriaSerif-LF.fd)
Provides:       tex(T1InriaSerif-OsF.fd)
Provides:       tex(T1InriaSerif-Sup.fd)
Provides:       tex(T1InriaSerif-TLF.fd)
Provides:       tex(T1InriaSerif-TOsF.fd)
Provides:       tex(TS1InriaSans-LF.fd)
Provides:       tex(TS1InriaSans-OsF.fd)
Provides:       tex(TS1InriaSans-TLF.fd)
Provides:       tex(TS1InriaSans-TOsF.fd)
Provides:       tex(TS1InriaSerif-LF.fd)
Provides:       tex(TS1InriaSerif-OsF.fd)
Provides:       tex(TS1InriaSerif-TLF.fd)
Provides:       tex(TS1InriaSerif-TOsF.fd)
Provides:       tex(inriasans_2ikqt3.enc)
Provides:       tex(inriasans_aeswfl.enc)
Provides:       tex(inriasans_azhk4k.enc)
Provides:       tex(inriasans_clzm26.enc)
Provides:       tex(inriasans_dl3y4j.enc)
Provides:       tex(inriasans_efwr3l.enc)
Provides:       tex(inriasans_fhoe3z.enc)
Provides:       tex(inriasans_g56wvz.enc)
Provides:       tex(inriasans_gn4bcn.enc)
Provides:       tex(inriasans_kgbpoz.enc)
Provides:       tex(inriasans_necsus.enc)
Provides:       tex(inriasans_psyc4t.enc)
Provides:       tex(inriasans_pv4xsz.enc)
Provides:       tex(inriasans_rhfpoz.enc)
Provides:       tex(inriasans_rriqaz.enc)
Provides:       tex(inriasans_svhg3d.enc)
Provides:       tex(inriasans_x5ybkq.enc)
Provides:       tex(inriasans_yeotsr.enc)
Provides:       tex(inriasans_yl5fy2.enc)
Provides:       tex(inriaserif_2ikqt3.enc)
Provides:       tex(inriaserif_aeswfl.enc)
Provides:       tex(inriaserif_azhk4k.enc)
Provides:       tex(inriaserif_clzm26.enc)
Provides:       tex(inriaserif_dl3y4j.enc)
Provides:       tex(inriaserif_efwr3l.enc)
Provides:       tex(inriaserif_fhoe3z.enc)
Provides:       tex(inriaserif_g56wvz.enc)
Provides:       tex(inriaserif_gn4bcn.enc)
Provides:       tex(inriaserif_kgbpoz.enc)
Provides:       tex(inriaserif_necsus.enc)
Provides:       tex(inriaserif_psyc4t.enc)
Provides:       tex(inriaserif_pv4xsz.enc)
Provides:       tex(inriaserif_rhfpoz.enc)
Provides:       tex(inriaserif_rriqaz.enc)
Provides:       tex(inriaserif_svhg3d.enc)
Provides:       tex(inriaserif_x5ybkq.enc)
Provides:       tex(inriaserif_yeotsr.enc)
Provides:       tex(inriaserif_yl5fy2.enc)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source193:      inriafonts.tar.xz
Source194:      inriafonts.doc.tar.xz

%description -n texlive-inriafonts
Inria is a free font designed by Black[Foundry] for Inria
research institute. The font is available for free. It comes as
Serif and Sans Serif, each with three weights and matching
italics. Using these fonts with XeLaTeX and LuaLaTeX is easy
using the fontspec package; we refer to the documentation of
fontspec for more information. The present package provides a
way of using them with LaTeX and pdfLaTeX: it provides two
style files, InriaSerif.sty and InriaSans.sty, together with
the PostScript version of the fonts and their associated files.
These were created using autoinst.

%package -n texlive-inriafonts-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54512
Release:        0
Summary:        Documentation for texlive-inriafonts
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-inriafonts-doc
This package includes the documentation for texlive-inriafonts


%package -n texlive-inriafonts-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54512
Release:        0
Summary:        Severed fonts for texlive-inriafonts
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-inriafonts-fonts
The  separated fonts package for texlive-inriafonts
%post -n texlive-inriafonts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap InriaSans.map' >> /var/run/texlive/run-updmap
echo 'addMap InriaSerif.map' >> /var/run/texlive/run-updmap

%postun -n texlive-inriafonts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap InriaSans.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap InriaSerif.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-inriafonts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-inriafonts-fonts
%files -n texlive-inriafonts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/inriafonts/README
%{_texmfdistdir}/doc/fonts/inriafonts/inriafonts.pdf
%{_texmfdistdir}/doc/fonts/inriafonts/inriafonts.tex
%{_texmfdistdir}/doc/fonts/inriafonts/license-SIL-OFL.txt

%files -n texlive-inriafonts
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_2ikqt3.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_aeswfl.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_azhk4k.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_clzm26.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_dl3y4j.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_efwr3l.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_fhoe3z.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_g56wvz.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_gn4bcn.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_kgbpoz.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_necsus.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_psyc4t.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_pv4xsz.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_rhfpoz.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_rriqaz.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_svhg3d.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_x5ybkq.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_yeotsr.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriasans_yl5fy2.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_2ikqt3.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_aeswfl.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_azhk4k.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_clzm26.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_dl3y4j.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_efwr3l.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_fhoe3z.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_g56wvz.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_gn4bcn.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_kgbpoz.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_necsus.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_psyc4t.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_pv4xsz.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_rhfpoz.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_rriqaz.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_svhg3d.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_x5ybkq.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_yeotsr.enc
%{_texmfdistdir}/fonts/enc/dvips/inriafonts/inriaserif_yl5fy2.enc
%{_texmfdistdir}/fonts/map/dvips/inriafonts/InriaSans.map
%{_texmfdistdir}/fonts/map/dvips/inriafonts/InriaSerif.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSans-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSans-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSans-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSans-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSans-LightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSans-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSerif-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSerif-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSerif-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSerif-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSerif-LightItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/inriafonts/InriaSerif-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-BoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Light-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-LightItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSans-Regular-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-BoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Light-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-LightItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-titling-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-titling-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-titling-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-titling-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-titling-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/inriafonts/InriaSerif-Regular-tosf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSans-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSans-BoldItalic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSans-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSans-Light.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSans-LightItalic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSans-Regular.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSerif-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSerif-BoldItalic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSerif-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSerif-Light.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSerif-LightItalic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/inriafonts/InriaSerif-Regular.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSans-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSans-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSans-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSans-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSans-LightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSans-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSerif-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSerif-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSerif-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSerif-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSerif-LightItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/inriafonts/InriaSerif-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Light-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-LightItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSans-Regular-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Light-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-LightItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-lf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-lf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-tlf-titling-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-tlf-titling-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/inriafonts/InriaSerif-Regular-tosf-ts1.vf
%{_texmfdistdir}/tex/latex/inriafonts/InriaSans.sty
%{_texmfdistdir}/tex/latex/inriafonts/InriaSerif.sty
%{_texmfdistdir}/tex/latex/inriafonts/LY1InriaSans-LF.fd
%{_texmfdistdir}/tex/latex/inriafonts/LY1InriaSans-OsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/LY1InriaSans-Sup.fd
%{_texmfdistdir}/tex/latex/inriafonts/LY1InriaSans-TLF.fd
%{_texmfdistdir}/tex/latex/inriafonts/LY1InriaSans-TOsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/LY1InriaSerif-LF.fd
%{_texmfdistdir}/tex/latex/inriafonts/LY1InriaSerif-OsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/LY1InriaSerif-Sup.fd
%{_texmfdistdir}/tex/latex/inriafonts/LY1InriaSerif-TLF.fd
%{_texmfdistdir}/tex/latex/inriafonts/LY1InriaSerif-TOsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/OT1InriaSans-LF.fd
%{_texmfdistdir}/tex/latex/inriafonts/OT1InriaSans-OsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/OT1InriaSans-Sup.fd
%{_texmfdistdir}/tex/latex/inriafonts/OT1InriaSans-TLF.fd
%{_texmfdistdir}/tex/latex/inriafonts/OT1InriaSans-TOsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/OT1InriaSerif-LF.fd
%{_texmfdistdir}/tex/latex/inriafonts/OT1InriaSerif-OsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/OT1InriaSerif-Sup.fd
%{_texmfdistdir}/tex/latex/inriafonts/OT1InriaSerif-TLF.fd
%{_texmfdistdir}/tex/latex/inriafonts/OT1InriaSerif-TOsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/T1InriaSans-LF.fd
%{_texmfdistdir}/tex/latex/inriafonts/T1InriaSans-OsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/T1InriaSans-Sup.fd
%{_texmfdistdir}/tex/latex/inriafonts/T1InriaSans-TLF.fd
%{_texmfdistdir}/tex/latex/inriafonts/T1InriaSans-TOsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/T1InriaSerif-LF.fd
%{_texmfdistdir}/tex/latex/inriafonts/T1InriaSerif-OsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/T1InriaSerif-Sup.fd
%{_texmfdistdir}/tex/latex/inriafonts/T1InriaSerif-TLF.fd
%{_texmfdistdir}/tex/latex/inriafonts/T1InriaSerif-TOsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/TS1InriaSans-LF.fd
%{_texmfdistdir}/tex/latex/inriafonts/TS1InriaSans-OsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/TS1InriaSans-TLF.fd
%{_texmfdistdir}/tex/latex/inriafonts/TS1InriaSans-TOsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/TS1InriaSerif-LF.fd
%{_texmfdistdir}/tex/latex/inriafonts/TS1InriaSerif-OsF.fd
%{_texmfdistdir}/tex/latex/inriafonts/TS1InriaSerif-TLF.fd
%{_texmfdistdir}/tex/latex/inriafonts/TS1InriaSerif-TOsF.fd

%files -n texlive-inriafonts-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-inriafonts
%{_datadir}/fontconfig/conf.avail/58-texlive-inriafonts.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-inriafonts.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-inriafonts.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-inriafonts/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-inriafonts/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-inriafonts/fonts.scale
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Bold.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-BoldItalic.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Italic.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Light.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-LightItalic.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Regular.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Bold.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-BoldItalic.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Italic.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Light.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-LightItalic.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Regular.otf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Bold.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-BoldItalic.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Italic.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Light.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-LightItalic.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Regular.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Bold.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-BoldItalic.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Italic.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Light.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-LightItalic.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Regular.ttf
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Bold.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSans-BoldItalic.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Italic.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Light.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSans-LightItalic.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSans-Regular.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Bold.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-BoldItalic.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Italic.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Light.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-LightItalic.pfb
%{_datadir}/fonts/texlive-inriafonts/InriaSerif-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-inriafonts-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn54512-%{release}-zypper
%endif

%package -n texlive-insbox
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn34299
Release:        0
Summary:        Insert pictures/boxes into paragraphs
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-insbox-doc >= %{texlive_version}
Provides:       tex(insbox.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source195:      insbox.tar.xz
Source196:      insbox.doc.tar.xz

%description -n texlive-insbox
The package provides convenient bundling of the \parshape
primitive. LaTeX users should note that this is a generic
package, and should be loaded using \input .

%package -n texlive-insbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn34299
Release:        0
Summary:        Documentation for texlive-insbox
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-insbox-doc
This package includes the documentation for texlive-insbox

%post -n texlive-insbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-insbox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-insbox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-insbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/insbox/demo.pdf
%{_texmfdistdir}/doc/generic/insbox/demo.tex
%{_texmfdistdir}/doc/generic/insbox/pic1.eps
%{_texmfdistdir}/doc/generic/insbox/pic2.eps

%files -n texlive-insbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/insbox/insbox.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-insbox-%{texlive_version}.%{texlive_noarch}.2.2svn34299-%{release}-zypper
%endif

%package -n texlive-intcalc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn53168
Release:        0
Summary:        Expandable arithmetic operations with integers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-intcalc-doc >= %{texlive_version}
Provides:       tex(intcalc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source197:      intcalc.tar.xz
Source198:      intcalc.doc.tar.xz

%description -n texlive-intcalc
This package provides expandable arithmetic operations with
integers, using the e-TeX extension \numexpr if it is
available.

%package -n texlive-intcalc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn53168
Release:        0
Summary:        Documentation for texlive-intcalc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-intcalc-doc
This package includes the documentation for texlive-intcalc

%post -n texlive-intcalc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-intcalc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-intcalc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-intcalc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/intcalc/README.md
%{_texmfdistdir}/doc/latex/intcalc/intcalc.pdf

%files -n texlive-intcalc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/intcalc/intcalc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-intcalc-%{texlive_version}.%{texlive_noarch}.1.3svn53168-%{release}-zypper
%endif

%package -n texlive-interactiveworkbook
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        LaTeX-based interactive PDF on the Web
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-interactiveworkbook-doc >= %{texlive_version}
Provides:       tex(interactiveworkbook-web.sty)
Provides:       tex(interactiveworkbook.sty)
Requires:       tex(color.sty)
Requires:       tex(epsfig.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source199:      interactiveworkbook.tar.xz
Source200:      interactiveworkbook.doc.tar.xz

%description -n texlive-interactiveworkbook
The package interactiveworkbook gives the user the ability to
write LaTeX documents which, ultimately, create interactive
question-and-answer Portable Document Format (PDF) tutorials
meant to be used by Internet students and that, in particular,
freely use mathematical notation.

%package -n texlive-interactiveworkbook-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-interactiveworkbook
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-interactiveworkbook-doc
This package includes the documentation for texlive-interactiveworkbook

%post -n texlive-interactiveworkbook
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-interactiveworkbook 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-interactiveworkbook
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-interactiveworkbook-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/interactiveworkbook/documentation/interactiveworkbookmanual.pdf
%{_texmfdistdir}/doc/latex/interactiveworkbook/documentation/interactiveworkbookmanual.tex
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/WS_FTP.LOG
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/buttonappearance.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/checkclear.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/checksubmit.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques1.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques10.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques11.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques12.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques13.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques14.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques15.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques16.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques17.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques18.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques19.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques2.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques20.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques3.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques4.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques5.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques6.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques7.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques8.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques9.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/fieldclear.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/fieldsubmit.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/ndex.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/next.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonecheckfive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonecheckfour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonecheckone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonecheckthree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonechecktwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonefieldfive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonefieldfour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonefieldone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonefieldthree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonefieldtwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonepopupfive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonepopupfour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonepopupone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonepopupthree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonepopuptwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageoneradiofive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageoneradiofour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageoneradioone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageoneradiothree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageoneradiotwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreecheckfive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreecheckfour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreecheckone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreecheckthree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreechecktwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreefieldfive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreefieldfour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreefieldone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreefieldthree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreefieldtwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreepopupfive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreepopupfour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreepopupone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreepopupthree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreepopuptwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreeradiofive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreeradiofour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreeradioone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreeradiothree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreeradiotwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwocheckfive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwocheckfour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwocheckone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwocheckthree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwochecktwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwofieldfive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwofieldfour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwofieldone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwofieldthree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwofieldtwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwopopupfive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwopopupfour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwopopupone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwopopupthree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwopopuptwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetworadiofive.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetworadiofour.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetworadioone.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetworadiothree.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetworadiotwo.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/popupclear.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/popupsubmit.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/prev.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/radioclear.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/radiosubmit.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/return.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/rightcheckcorrect.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/rightfieldcorrect.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/rightpopupcorrect.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/rightradiocorrect.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/wrongcheckcorrect.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/wrongfieldcorrect.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/wrongpopupcorrect.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/wrongradiocorrect.eps
%{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/check.pdf
%{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/check.tex
%{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/field.pdf
%{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/field.tex
%{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/ndex.pdf
%{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/ndex.tex
%{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/popup.pdf
%{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/popup.tex
%{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/radio.pdf
%{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/radio.tex

%files -n texlive-interactiveworkbook
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/interactiveworkbook/interactiveworkbook-web.sty
%{_texmfdistdir}/tex/latex/interactiveworkbook/interactiveworkbook.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-interactiveworkbook-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-interchar
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn36312
Release:        0
Summary:        Managing character class schemes in XeTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-interchar-doc >= %{texlive_version}
Provides:       tex(interchar.sty)
Requires:       tex(expl3.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source201:      interchar.tar.xz
Source202:      interchar.doc.tar.xz

%description -n texlive-interchar
The package manages character class schemes of XeTeX. Using
this package, you may switch among different character class
schemes. Migration commands are provided for make packages
using this mechanism compatible with each others.

%package -n texlive-interchar-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn36312
Release:        0
Summary:        Documentation for texlive-interchar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-interchar-doc
This package includes the documentation for texlive-interchar

%post -n texlive-interchar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-interchar 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-interchar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-interchar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/interchar/README
%{_texmfdistdir}/doc/xelatex/interchar/interchar.pdf
%{_texmfdistdir}/doc/xelatex/interchar/interchar.tex
%{_texmfdistdir}/doc/xelatex/interchar/interchardemo1.pdf
%{_texmfdistdir}/doc/xelatex/interchar/interchardemo1.tex
%{_texmfdistdir}/doc/xelatex/interchar/interchartest.pdf
%{_texmfdistdir}/doc/xelatex/interchar/interchartest.tex

%files -n texlive-interchar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/interchar/interchar.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-interchar-%{texlive_version}.%{texlive_noarch}.0.0.2svn36312-%{release}-zypper
%endif

%package -n texlive-interfaces
Version:        %{texlive_version}.%{texlive_noarch}.3.1svn21474
Release:        0
Summary:        Set parameters for other packages, conveniently
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-interfaces-doc >= %{texlive_version}
Provides:       tex(interfaces-LaTeX.sty)
Provides:       tex(interfaces-appendix.sty)
Provides:       tex(interfaces-base.sty)
Provides:       tex(interfaces-bookmark.sty)
Provides:       tex(interfaces-embedfile.sty)
Provides:       tex(interfaces-enumitem.sty)
Provides:       tex(interfaces-environ.sty)
Provides:       tex(interfaces-etoolbox.sty)
Provides:       tex(interfaces-fancyhdr.sty)
Provides:       tex(interfaces-hypbmsec.sty)
Provides:       tex(interfaces-hyperref.sty)
Provides:       tex(interfaces-makecell.sty)
Provides:       tex(interfaces-marks.sty)
Provides:       tex(interfaces-pgfkeys.sty)
Provides:       tex(interfaces-scrlfile.sty)
Provides:       tex(interfaces-tikz.sty)
Provides:       tex(interfaces-titlesec.sty)
Provides:       tex(interfaces-tocloft.sty)
Provides:       tex(interfaces-truncate.sty)
Provides:       tex(interfaces-umrand.sty)
Provides:       tex(interfaces.sty)
Requires:       tex(auxhook.sty)
Requires:       tex(etex.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fp.sty)
Requires:       tex(gettitlestring.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(refcount.sty)
Requires:       tex(scrlfile.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source203:      interfaces.tar.xz
Source204:      interfaces.doc.tar.xz

%description -n texlive-interfaces
The package provides a small number of convenient macros that
access features in other frequently-used packages, or provide
interfaces to other useful facilities such as the pdfTeX
\pdfelapsedtime primitive. Most of these macros use pgfkeys to
provide a key-value syntax. The package also uses the package
scrlfile from the Koma-Script bundle (for controlled loading of
other files) and etoolbox. The package is bundled with
sub-packages containing actual interfaces: by default, the
package loads all available sub-packages, but techniques are
provided for the user to select no more than the interfaces
needed for a job.

%package -n texlive-interfaces-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.1svn21474
Release:        0
Summary:        Documentation for texlive-interfaces
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-interfaces-doc
This package includes the documentation for texlive-interfaces

%post -n texlive-interfaces
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-interfaces 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-interfaces
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-interfaces-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/interfaces/README
%{_texmfdistdir}/doc/latex/interfaces/interfaces.pdf

%files -n texlive-interfaces
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/interfaces/interfaces-LaTeX.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-appendix.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-base.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-bookmark.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-embedfile.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-enumitem.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-environ.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-etoolbox.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-fancyhdr.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-hypbmsec.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-hyperref.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-makecell.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-marks.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-pgfkeys.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-scrlfile.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-tikz.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-titlesec.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-tocloft.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-truncate.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces-umrand.sty
%{_texmfdistdir}/tex/latex/interfaces/interfaces.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-interfaces-%{texlive_version}.%{texlive_noarch}.3.1svn21474-%{release}-zypper
%endif

%package -n texlive-interpreter
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn27232
Release:        0
Summary:        Translate input files on the fly
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-interpreter-doc >= %{texlive_version}
Provides:       tex(interpreter.sty)
Provides:       tex(interpreter.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source205:      interpreter.tar.xz
Source206:      interpreter.doc.tar.xz

%description -n texlive-interpreter
The package preprocesses input files to a Lua(La)TeX run, on
the fly. The user defines Lua regular expressions to search for
patterns and modify input lines (or entire paragraphs)
accordingly, before TeX reads the material. In this way,
documents may be prepared in a non-TeX language (e.g., some
lightweight markup language) and turned into 'proper' TeX for
processing. The source of the documentation is typed in such a
lightweight language and is thus easily readable in a text
editor (the PDF file is also available, of course); the
transformation to TeX syntax via Interpreter's functions is
explained in the documentation itself. Interpreter is
implemented using the author's gates (lua version), and works
for plain TeX and LaTeX, but not ConTeXt.

%package -n texlive-interpreter-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn27232
Release:        0
Summary:        Documentation for texlive-interpreter
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-interpreter-doc
This package includes the documentation for texlive-interpreter

%post -n texlive-interpreter
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-interpreter 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-interpreter
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-interpreter-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/interpreter/README
%{_texmfdistdir}/doc/luatex/interpreter/i-doc.lua
%{_texmfdistdir}/doc/luatex/interpreter/interpreter-doc.pdf
%{_texmfdistdir}/doc/luatex/interpreter/interpreter-doc.tex
%{_texmfdistdir}/doc/luatex/interpreter/interpreter-doc.txt

%files -n texlive-interpreter
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/luatex/interpreter/interpreter.lua
%{_texmfdistdir}/tex/luatex/interpreter/interpreter.sty
%{_texmfdistdir}/tex/luatex/interpreter/interpreter.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-interpreter-%{texlive_version}.%{texlive_noarch}.1.2svn27232-%{release}-zypper
%endif

%package -n texlive-interval
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn50265
Release:        0
Summary:        Format mathematical intervals, ensuring proper spacing
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-interval-doc >= %{texlive_version}
Provides:       tex(interval.sty)
Requires:       tex(pgfkeys.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source207:      interval.tar.xz
Source208:      interval.doc.tar.xz

%description -n texlive-interval
When typing an open interval as $]a,b[$, a closing bracket is
being used in place of an opening fence and vice versa. This
leads to the wrong spacing in, say, $]-a,b[$ or $A\in]a,b[=B$.
The package attempts to solve this using: \interval{a}{b} ->
[a,b] \interval[open]{a}{b} -> ]a,b[ \interval[open left]{a}{b}
-> ]a,b] The package also supports fence scaling and ensures
that the enclosing fences will end up having the proper closing
and opening types. TeX maths does not do this job properly. The
package depends on pgfkeys.

%package -n texlive-interval-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn50265
Release:        0
Summary:        Documentation for texlive-interval
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-interval-doc
This package includes the documentation for texlive-interval

%post -n texlive-interval
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-interval 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-interval
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-interval-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/interval/README
%{_texmfdistdir}/doc/latex/interval/interval.pdf
%{_texmfdistdir}/doc/latex/interval/interval.tex

%files -n texlive-interval
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/interval/interval.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-interval-%{texlive_version}.%{texlive_noarch}.0.0.4svn50265-%{release}-zypper
%endif

%package -n texlive-intopdf
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.1svn51247
Release:        0
Summary:        Embed non-PDF files into PDF with hyperlink
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-intopdf-doc >= %{texlive_version}
Provides:       tex(intopdf.sty)
Requires:       tex(expl3.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source209:      intopdf.tar.xz
Source210:      intopdf.doc.tar.xz

%description -n texlive-intopdf
The package allows to embed non-PDF files (e.g., BibTeX) into
PDF with a hyperlink.

%package -n texlive-intopdf-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.1svn51247
Release:        0
Summary:        Documentation for texlive-intopdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-intopdf-doc
This package includes the documentation for texlive-intopdf

%post -n texlive-intopdf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-intopdf 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-intopdf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-intopdf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/intopdf/README.md
%{_texmfdistdir}/doc/latex/intopdf/intopdf.pdf

%files -n texlive-intopdf
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/intopdf/intopdf.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-intopdf-%{texlive_version}.%{texlive_noarch}.0.0.2.1svn51247-%{release}-zypper
%endif

%package -n texlive-intro-scientific
Version:        %{texlive_version}.%{texlive_noarch}.5th_editionsvn15878
Release:        0
Summary:        Introducing scientific/mathematical documents using LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source211:      intro-scientific.doc.tar.xz

%description -n texlive-intro-scientific
"Writing Scientific Documents Using LaTeX" is an article
introducing the use of LaTeX in typesetting scientific
documents. It covers the basics of creating a new LaTeX
document, special typesetting considerations, mathematical
typesetting and graphics. It also touches on bibliographic data
and BibTeX.
%post -n texlive-intro-scientific
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-intro-scientific 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-intro-scientific
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-intro-scientific
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/intro-scientific/Makefile
%{_texmfdistdir}/doc/latex/intro-scientific/README
%{_texmfdistdir}/doc/latex/intro-scientific/earth-moon.pdf
%{_texmfdistdir}/doc/latex/intro-scientific/scidoc.pdf
%{_texmfdistdir}/doc/latex/intro-scientific/scidoc.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-intro-scientific-%{texlive_version}.%{texlive_noarch}.5th_editionsvn15878-%{release}-zypper
%endif

%package -n texlive-inversepath
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Calculate inverse file paths
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-inversepath-doc >= %{texlive_version}
Provides:       tex(inversepath.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source212:      inversepath.tar.xz
Source213:      inversepath.doc.tar.xz

%description -n texlive-inversepath
The package calculates inverse relative paths. Such things may
be useful, for example, when writing an auxiliary file to a
different directory.

%package -n texlive-inversepath-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Documentation for texlive-inversepath
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-inversepath-doc
This package includes the documentation for texlive-inversepath

%post -n texlive-inversepath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-inversepath 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-inversepath
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-inversepath-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/inversepath/README
%{_texmfdistdir}/doc/latex/inversepath/inversepath.pdf

%files -n texlive-inversepath
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/inversepath/inversepath.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-inversepath-%{texlive_version}.%{texlive_noarch}.0.0.2svn15878-%{release}-zypper
%endif

%package -n texlive-invoice
Version:        %{texlive_version}.%{texlive_noarch}.svn48359
Release:        0
Summary:        Generate invoices
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-invoice-doc >= %{texlive_version}
Provides:       tex(invoice.sty)
Provides:       tex(invoicelabels.sty)
Requires:       tex(calc.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(siunitx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source214:      invoice.tar.xz
Source215:      invoice.doc.tar.xz

%description -n texlive-invoice
The package may be used for generating invoices. The package
can deal with invisible expense items and deductions; output
may be presented in any of 10 different languages. A
long-standing bug has been removed. Numbers now can show the
comma as decimal separator. The package depends on the fp, calc
and siunitx for its calculations.

%package -n texlive-invoice-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn48359
Release:        0
Summary:        Documentation for texlive-invoice
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-invoice-doc
This package includes the documentation for texlive-invoice

%post -n texlive-invoice
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-invoice 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-invoice
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-invoice-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/invoice/README
%{_texmfdistdir}/doc/latex/invoice/invoice.pdf
%{_texmfdistdir}/doc/latex/invoice/invoice.tex

%files -n texlive-invoice
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/invoice/invoice.sty
%{_texmfdistdir}/tex/latex/invoice/invoicelabels.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-invoice-%{texlive_version}.%{texlive_noarch}.svn48359-%{release}-zypper
%endif

%package -n texlive-invoice-class
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn49749
Release:        0
Summary:        Produces a standard US invoice from a CSV file
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-invoice-class-doc >= %{texlive_version}
Provides:       tex(invoice-class.cls)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(datatool.sty)
Requires:       tex(dcolumn.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(longtable.sty)
Requires:       tex(multicol.sty)
Requires:       tex(tabularx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source216:      invoice-class.tar.xz
Source217:      invoice-class.doc.tar.xz

%description -n texlive-invoice-class
This class produces a standard US commercial invoice using data
from a CSV file. Invoices can span multiple pages. The class is
configurable for different shipping addresses.

%package -n texlive-invoice-class-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn49749
Release:        0
Summary:        Documentation for texlive-invoice-class
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-invoice-class-doc
This package includes the documentation for texlive-invoice-class

%post -n texlive-invoice-class
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-invoice-class 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-invoice-class
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-invoice-class-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/invoice-class/README.md
%{_texmfdistdir}/doc/latex/invoice-class/doc/duck-invoice.cfg
%{_texmfdistdir}/doc/latex/invoice-class/doc/duck-invoice.csv
%{_texmfdistdir}/doc/latex/invoice-class/doc/duck-invoice.pdf
%{_texmfdistdir}/doc/latex/invoice-class/doc/duck-invoice.tex
%{_texmfdistdir}/doc/latex/invoice-class/doc/ducks.csv
%{_texmfdistdir}/doc/latex/invoice-class/doc/ducks.pdf
%{_texmfdistdir}/doc/latex/invoice-class/doc/ducks.tex
%{_texmfdistdir}/doc/latex/invoice-class/doc/invoice-class.pdf
%{_texmfdistdir}/doc/latex/invoice-class/doc/invoice-class.tex

%files -n texlive-invoice-class
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/invoice-class/invoice-class.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-invoice-class-%{texlive_version}.%{texlive_noarch}.1.0svn49749-%{release}-zypper
%endif

%package -n texlive-invoice2
Version:        %{texlive_version}.%{texlive_noarch}.svn46364
Release:        0
Summary:        Intelligent invoices with LaTeX3
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-invoice2-doc >= %{texlive_version}
Provides:       tex(invoice2.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(longtable.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(translations.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source218:      invoice2.tar.xz
Source219:      invoice2.doc.tar.xz

%description -n texlive-invoice2
Typeset invoices with automatic VAT and calculation of totals.
Supports internationalization, invoices are typeset with
booktabs for readability. Does not support separate projects
per invoice. Can be used as a replacement for invoice in most
cases.

%package -n texlive-invoice2-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn46364
Release:        0
Summary:        Documentation for texlive-invoice2
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-invoice2-doc
This package includes the documentation for texlive-invoice2

%post -n texlive-invoice2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-invoice2 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-invoice2
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-invoice2-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/invoice2/LICENSE-gpl-3.0.md
%{_texmfdistdir}/doc/latex/invoice2/README.md
%{_texmfdistdir}/doc/latex/invoice2/invoice2.pdf

%files -n texlive-invoice2
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/invoice2/invoice2-english.trsl
%{_texmfdistdir}/tex/latex/invoice2/invoice2-german.trsl
%{_texmfdistdir}/tex/latex/invoice2/invoice2-swissgerman.trsl
%{_texmfdistdir}/tex/latex/invoice2/invoice2.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-invoice2-%{texlive_version}.%{texlive_noarch}.svn46364-%{release}-zypper
%endif

%package -n texlive-iodhbwm
Version:        %{texlive_version}.%{texlive_noarch}.1.2.1svn54734
Release:        0
Summary:        Unofficial template of the DHBW Mannheim
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-iodhbwm-doc >= %{texlive_version}
Provides:       tex(iodhbwm-i18n.def)
Provides:       tex(iodhbwm-templates.sty)
Provides:       tex(iodhbwm.cls)
Requires:       tex(auxhook.sty)
Requires:       tex(babel.sty)
Requires:       tex(blindtext.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(listings.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(microtype.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(scrhack.sty)
Requires:       tex(scrlfile.sty)
Requires:       tex(setspace.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(totalcount.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source220:      iodhbwm.tar.xz
Source221:      iodhbwm.doc.tar.xz

%description -n texlive-iodhbwm
This package provides an unofficial template of the DHBW
Mannheim for the creation of bachelor thesis, studies or
project work with LaTeX. The aim of the package is the quick
creation of a basic framework without much effort.

%package -n texlive-iodhbwm-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2.1svn54734
Release:        0
Summary:        Documentation for texlive-iodhbwm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-iodhbwm-doc:de)

%description -n texlive-iodhbwm-doc
This package includes the documentation for texlive-iodhbwm

%post -n texlive-iodhbwm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-iodhbwm 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-iodhbwm
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-iodhbwm-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/iodhbwm/README.md
%{_texmfdistdir}/doc/latex/iodhbwm/examples/abstract/iodhbwm-auto-sections-with-abstract.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/abstract/iodhbwm-auto-sections-with-abstract.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/abstract/my-abstract.inc.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/acronyms/iodhbwm-acro.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/acronyms/iodhbwm-acro.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/appendix/iodhbwm-appendix-auto.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/appendix/iodhbwm-appendix-auto.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/appendix/iodhbwm-appendix.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/appendix/iodhbwm-appendix.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/bibliography/iodhbwm-biblatex-custom-option.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/bibliography/iodhbwm-biblatex-custom-option.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/bibliography/iodhbwm-biblatex-footcite.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/bibliography/iodhbwm-biblatex-footcite.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/bibliography/iodhbwm-biblatex-rename-heading.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/bibliography/iodhbwm-biblatex-rename-heading.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/bibliography/iodhbwm-biblatex-style-option.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/bibliography/iodhbwm-biblatex-style-option.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/customizing/iodhbwm-print.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/customizing/iodhbwm-print.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/customizing/iodhbwm-replace-part-naming.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/customizing/iodhbwm-replace-part-naming.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/customizing/iodhbwm-roman-numbers.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/customizing/iodhbwm-roman-numbers.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/how-to-use-iodhbwm/iodhbwm-advanced-starter.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/how-to-use-iodhbwm/iodhbwm-advanced-starter.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/how-to-use-iodhbwm/iodhbwm-recommended-starter.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/how-to-use-iodhbwm/iodhbwm-recommended-starter.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/how-to-use-iodhbwm/iodhbwm-simple-starter.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/how-to-use-iodhbwm/iodhbwm-simple-starter.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/listings/iodhbwm-listings-color.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/listings/iodhbwm-listings-color.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/listings/iodhbwm-listings.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/listings/iodhbwm-listings.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/references/iodhbwm-hyperref.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/references/iodhbwm-hyperref.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/references/iodhbwm-references.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/references/iodhbwm-references.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/titlepages/img/penguin-158298-pixabay.png
%{_texmfdistdir}/doc/latex/iodhbwm/examples/titlepages/iodhbwm-custom-titlepage.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/titlepages/iodhbwm-custom-titlepage.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/titlepages/iodhbwm-titlepage-logo.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/examples/titlepages/iodhbwm-titlepage-logo.tex
%{_texmfdistdir}/doc/latex/iodhbwm/examples/titlepages/my-titlepage.tex
%{_texmfdistdir}/doc/latex/iodhbwm/i18n/english/dhbw-declaration.def
%{_texmfdistdir}/doc/latex/iodhbwm/i18n/english/dhbw-titlepage-ba.def
%{_texmfdistdir}/doc/latex/iodhbwm/i18n/english/dhbw-titlepage-pa.def
%{_texmfdistdir}/doc/latex/iodhbwm/i18n/english/dhbw-titlepage-sa.def
%{_texmfdistdir}/doc/latex/iodhbwm/i18n/english/dhbw-titlepage.def
%{_texmfdistdir}/doc/latex/iodhbwm/i18n/ngerman/dhbw-declaration.def
%{_texmfdistdir}/doc/latex/iodhbwm/i18n/ngerman/dhbw-titlepage-ba.def
%{_texmfdistdir}/doc/latex/iodhbwm/i18n/ngerman/dhbw-titlepage-pa.def
%{_texmfdistdir}/doc/latex/iodhbwm/i18n/ngerman/dhbw-titlepage-sa.def
%{_texmfdistdir}/doc/latex/iodhbwm/i18n/ngerman/dhbw-titlepage.def
%{_texmfdistdir}/doc/latex/iodhbwm/iodhbwm.pdf
%{_texmfdistdir}/doc/latex/iodhbwm/iodhbwm.tex

%files -n texlive-iodhbwm
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/iodhbwm/dhbw-logo.png
%{_texmfdistdir}/tex/latex/iodhbwm/iodhbwm-i18n.def
%{_texmfdistdir}/tex/latex/iodhbwm/iodhbwm-templates.sty
%{_texmfdistdir}/tex/latex/iodhbwm/iodhbwm.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-iodhbwm-%{texlive_version}.%{texlive_noarch}.1.2.1svn54734-%{release}-zypper
%endif

%prep
%setup -q -c -T

%build

%install
    rm -rf %{buildroot}
    mkdir -p %{buildroot}%{_texmfdistdir}
    mkdir -p %{buildroot}%{_texmfmaindir}/tlpkg/tlpostcode
    mkdir -p %{buildroot}%{_datadir}/texlive/tlpkg
    mkdir -p %{buildroot}/var/adm/update-scripts
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf-dist
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf
    ln -sf ../../../share/texmf/tlpkg/tlpostcode \
                                    %{buildroot}%{_datadir}/texlive/tlpkg/tlpostcode
    ln -sf tlpkg/tlpostcode         %{buildroot}%{_texmfmaindir}/tlpostcode
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hrlatex-%{texlive_version}.%{texlive_noarch}.0.0.23svn18020-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hu-berlin-bundle-%{texlive_version}.%{texlive_noarch}.1.0.4svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hulipsum-%{texlive_version}.%{texlive_noarch}.1.0svn46803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hustthesis-%{texlive_version}.%{texlive_noarch}.1.4svn42547-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hvfloat-%{texlive_version}.%{texlive_noarch}.2.16svn52010-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hvindex-%{texlive_version}.%{texlive_noarch}.0.0.04svn46051-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hvqrurl-%{texlive_version}.%{texlive_noarch}.0.0.01asvn52993-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hycolor-%{texlive_version}.%{texlive_noarch}.1.10svn53584-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hypdvips-%{texlive_version}.%{texlive_noarch}.3.03svn53197-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyper-%{texlive_version}.%{texlive_noarch}.4.2dsvn17357-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyperbar-%{texlive_version}.%{texlive_noarch}.0.0.1svn48147-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hypernat-%{texlive_version}.%{texlive_noarch}.1.0bsvn17358-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyperref-%{texlive_version}.%{texlive_noarch}.7.00dsvn53837-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyperxmp-%{texlive_version}.%{texlive_noarch}.5.1svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyph-utf8-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-afrikaans-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-afrikaans.dat)<<'EOF'
%% from hyphen-afrikaans:
afrikaans loadhyph-af.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-afrikaans.def)<<'EOF'
%% from hyphen-afrikaans:
\addlanguage{afrikaans}{loadhyph-af.tex}{}{1}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-afrikaans.dat.lua)<<'EOF'
-- from hyphen-afrikaans:
	['afrikaans'] = {
		loader = 'loadhyph-af.tex',
		lefthyphenmin = 1,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-af.pat.txt',
		hyphenation = 'hyph-af.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-ancientgreek-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ancientgreek.dat)<<'EOF'
%% from hyphen-ancientgreek:
ancientgreek loadhyph-grc.tex
ibycus ibyhyph.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ancientgreek.def)<<'EOF'
%% from hyphen-ancientgreek:
\addlanguage{ancientgreek}{loadhyph-grc.tex}{}{1}{1}
\addlanguage{ibycus}{ibyhyph.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ancientgreek.dat.lua)<<'EOF'
-- from hyphen-ancientgreek:
	['ancientgreek'] = {
		loader = 'loadhyph-grc.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-grc.pat.txt',
		hyphenation = '',
	},
	['ibycus'] = {
		loader = 'ibyhyph.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		special = 'disabled:8-bit only',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-arabic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-arabic.dat)<<'EOF'
%% from hyphen-arabic:
arabic zerohyph.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-arabic.def)<<'EOF'
%% from hyphen-arabic:
\addlanguage{arabic}{zerohyph.tex}{}{2}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-arabic.dat.lua)<<'EOF'
-- from hyphen-arabic:
	['arabic'] = {
		loader = 'zerohyph.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-armenian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-armenian.dat)<<'EOF'
%% from hyphen-armenian:
armenian loadhyph-hy.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-armenian.def)<<'EOF'
%% from hyphen-armenian:
\addlanguage{armenian}{loadhyph-hy.tex}{}{1}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-armenian.dat.lua)<<'EOF'
-- from hyphen-armenian:
	['armenian'] = {
		loader = 'loadhyph-hy.tex',
		lefthyphenmin = 1,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-hy.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-base-%{texlive_version}.%{texlive_noarch}.svn54763-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move configuration files
    mkdir -p %{buildroot}%{_texmfconfdir}/tex/generic/config
    mv -f  %{buildroot}%{_texmfdistdir}/tex/generic/config/language.dat %{buildroot}%{_texmfconfdir}/tex/generic/config/
    rm -f  %{buildroot}%{_texmfdistdir}/tex/generic/config/language.dat
    ln -sf %{_texmfconfdir}/tex/generic/config/language.dat %{buildroot}%{_texmfdistdir}/tex/generic/config/language.dat
    mv -f  %{buildroot}%{_texmfdistdir}/tex/generic/config/language.dat.lua %{buildroot}%{_texmfconfdir}/tex/generic/config/
    rm -f  %{buildroot}%{_texmfdistdir}/tex/generic/config/language.dat.lua
    ln -sf %{_texmfconfdir}/tex/generic/config/language.dat.lua %{buildroot}%{_texmfdistdir}/tex/generic/config/language.dat.lua
    mv -f  %{buildroot}%{_texmfdistdir}/tex/generic/config/language.def %{buildroot}%{_texmfconfdir}/tex/generic/config/
    rm -f  %{buildroot}%{_texmfdistdir}/tex/generic/config/language.def
    ln -sf %{_texmfconfdir}/tex/generic/config/language.def %{buildroot}%{_texmfdistdir}/tex/generic/config/language.def
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-basque-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-basque.dat)<<'EOF'
%% from hyphen-basque:
basque loadhyph-eu.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-basque.def)<<'EOF'
%% from hyphen-basque:
\addlanguage{basque}{loadhyph-eu.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-basque.dat.lua)<<'EOF'
-- from hyphen-basque:
	['basque'] = {
		loader = 'loadhyph-eu.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-eu.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-belarusian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-belarusian.dat)<<'EOF'
%% from hyphen-belarusian:
belarusian loadhyph-be.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-belarusian.def)<<'EOF'
%% from hyphen-belarusian:
\addlanguage{belarusian}{loadhyph-be.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-belarusian.dat.lua)<<'EOF'
-- from hyphen-belarusian:
	['belarusian'] = {
		loader = 'loadhyph-be.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-be.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-bulgarian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-bulgarian.dat)<<'EOF'
%% from hyphen-bulgarian:
bulgarian loadhyph-bg.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-bulgarian.def)<<'EOF'
%% from hyphen-bulgarian:
\addlanguage{bulgarian}{loadhyph-bg.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-bulgarian.dat.lua)<<'EOF'
-- from hyphen-bulgarian:
	['bulgarian'] = {
		loader = 'loadhyph-bg.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-bg.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-catalan-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-catalan.dat)<<'EOF'
%% from hyphen-catalan:
catalan loadhyph-ca.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-catalan.def)<<'EOF'
%% from hyphen-catalan:
\addlanguage{catalan}{loadhyph-ca.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-catalan.dat.lua)<<'EOF'
-- from hyphen-catalan:
	['catalan'] = {
		loader = 'loadhyph-ca.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-ca.pat.txt',
		hyphenation = 'hyph-ca.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-chinese-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-chinese.dat)<<'EOF'
%% from hyphen-chinese:
pinyin loadhyph-zh-latn-pinyin.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-chinese.def)<<'EOF'
%% from hyphen-chinese:
\addlanguage{pinyin}{loadhyph-zh-latn-pinyin.tex}{}{1}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-chinese.dat.lua)<<'EOF'
-- from hyphen-chinese:
	['pinyin'] = {
		loader = 'loadhyph-zh-latn-pinyin.tex',
		lefthyphenmin = 1,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-zh-latn-pinyin.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-churchslavonic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-churchslavonic.dat)<<'EOF'
%% from hyphen-churchslavonic:
churchslavonic loadhyph-cu.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-churchslavonic.def)<<'EOF'
%% from hyphen-churchslavonic:
\addlanguage{churchslavonic}{loadhyph-cu.tex}{}{1}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-churchslavonic.dat.lua)<<'EOF'
-- from hyphen-churchslavonic:
	['churchslavonic'] = {
		loader = 'loadhyph-cu.tex',
		lefthyphenmin = 1,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-cu.pat.txt',
		hyphenation = 'hyph-cu.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-coptic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-coptic.dat)<<'EOF'
%% from hyphen-coptic:
coptic loadhyph-cop.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-coptic.def)<<'EOF'
%% from hyphen-coptic:
\addlanguage{coptic}{loadhyph-cop.tex}{}{1}{1}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-coptic.dat.lua)<<'EOF'
-- from hyphen-coptic:
	['coptic'] = {
		loader = 'loadhyph-cop.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-cop.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-croatian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-croatian.dat)<<'EOF'
%% from hyphen-croatian:
croatian loadhyph-hr.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-croatian.def)<<'EOF'
%% from hyphen-croatian:
\addlanguage{croatian}{loadhyph-hr.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-croatian.dat.lua)<<'EOF'
-- from hyphen-croatian:
	['croatian'] = {
		loader = 'loadhyph-hr.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-hr.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-czech-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-czech.dat)<<'EOF'
%% from hyphen-czech:
czech loadhyph-cs.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-czech.def)<<'EOF'
%% from hyphen-czech:
\addlanguage{czech}{loadhyph-cs.tex}{}{2}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-czech.dat.lua)<<'EOF'
-- from hyphen-czech:
	['czech'] = {
		loader = 'loadhyph-cs.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-cs.pat.txt',
		hyphenation = 'hyph-cs.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-danish-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-danish.dat)<<'EOF'
%% from hyphen-danish:
danish loadhyph-da.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-danish.def)<<'EOF'
%% from hyphen-danish:
\addlanguage{danish}{loadhyph-da.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-danish.dat.lua)<<'EOF'
-- from hyphen-danish:
	['danish'] = {
		loader = 'loadhyph-da.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-da.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-dutch-%{texlive_version}.%{texlive_noarch}.1.1svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-dutch.dat)<<'EOF'
%% from hyphen-dutch:
dutch loadhyph-nl.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-dutch.def)<<'EOF'
%% from hyphen-dutch:
\addlanguage{dutch}{loadhyph-nl.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-dutch.dat.lua)<<'EOF'
-- from hyphen-dutch:
	['dutch'] = {
		loader = 'loadhyph-nl.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-nl.pat.txt',
		hyphenation = 'hyph-nl.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-english-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-english.dat)<<'EOF'
%% from hyphen-english:
ukenglish loadhyph-en-gb.tex
=british
=UKenglish
usenglishmax loadhyph-en-us.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-english.def)<<'EOF'
%% from hyphen-english:
\addlanguage{ukenglish}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{british}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{UKenglish}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{usenglishmax}{loadhyph-en-us.tex}{}{2}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-english.dat.lua)<<'EOF'
-- from hyphen-english:
	['ukenglish'] = {
		loader = 'loadhyph-en-gb.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = { 'british', 'UKenglish' },
		patterns = 'hyph-en-gb.pat.txt',
		hyphenation = 'hyph-en-gb.hyp.txt',
	},
	['usenglishmax'] = {
		loader = 'loadhyph-en-us.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-en-us.pat.txt',
		hyphenation = 'hyph-en-us.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-esperanto-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-esperanto.dat)<<'EOF'
%% from hyphen-esperanto:
esperanto loadhyph-eo.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-esperanto.def)<<'EOF'
%% from hyphen-esperanto:
\addlanguage{esperanto}{loadhyph-eo.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-esperanto.dat.lua)<<'EOF'
-- from hyphen-esperanto:
	['esperanto'] = {
		loader = 'loadhyph-eo.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-eo.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-estonian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-estonian.dat)<<'EOF'
%% from hyphen-estonian:
estonian loadhyph-et.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-estonian.def)<<'EOF'
%% from hyphen-estonian:
\addlanguage{estonian}{loadhyph-et.tex}{}{2}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-estonian.dat.lua)<<'EOF'
-- from hyphen-estonian:
	['estonian'] = {
		loader = 'loadhyph-et.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-et.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-ethiopic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ethiopic.dat)<<'EOF'
%% from hyphen-ethiopic:
ethiopic loadhyph-mul-ethi.tex
=amharic
=geez
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ethiopic.def)<<'EOF'
%% from hyphen-ethiopic:
\addlanguage{ethiopic}{loadhyph-mul-ethi.tex}{}{1}{1}
\addlanguage{amharic}{loadhyph-mul-ethi.tex}{}{1}{1}
\addlanguage{geez}{loadhyph-mul-ethi.tex}{}{1}{1}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ethiopic.dat.lua)<<'EOF'
-- from hyphen-ethiopic:
	['ethiopic'] = {
		loader = 'loadhyph-mul-ethi.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = { 'amharic', 'geez' },
		patterns = 'hyph-mul-ethi.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-farsi-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-farsi.dat)<<'EOF'
%% from hyphen-farsi:
farsi zerohyph.tex
=persian
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-farsi.def)<<'EOF'
%% from hyphen-farsi:
\addlanguage{farsi}{zerohyph.tex}{}{2}{3}
\addlanguage{persian}{zerohyph.tex}{}{2}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-farsi.dat.lua)<<'EOF'
-- from hyphen-farsi:
	['farsi'] = {
		loader = 'zerohyph.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = { 'persian' },
		patterns = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-finnish-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-finnish.dat)<<'EOF'
%% from hyphen-finnish:
finnish loadhyph-fi.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-finnish.def)<<'EOF'
%% from hyphen-finnish:
\addlanguage{finnish}{loadhyph-fi.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-finnish.dat.lua)<<'EOF'
-- from hyphen-finnish:
	['finnish'] = {
		loader = 'loadhyph-fi.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-fi.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-french-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-french.dat)<<'EOF'
%% from hyphen-french:
french loadhyph-fr.tex
=patois
=francais
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-french.def)<<'EOF'
%% from hyphen-french:
\addlanguage{french}{loadhyph-fr.tex}{}{2}{2}
\addlanguage{patois}{loadhyph-fr.tex}{}{2}{2}
\addlanguage{francais}{loadhyph-fr.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-french.dat.lua)<<'EOF'
-- from hyphen-french:
	['french'] = {
		loader = 'loadhyph-fr.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'patois', 'francais' },
		patterns = 'hyph-fr.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-friulan-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-friulan.dat)<<'EOF'
%% from hyphen-friulan:
friulan loadhyph-fur.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-friulan.def)<<'EOF'
%% from hyphen-friulan:
\addlanguage{friulan}{loadhyph-fur.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-friulan.dat.lua)<<'EOF'
-- from hyphen-friulan:
	['friulan'] = {
		loader = 'loadhyph-fur.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-fur.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-galician-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-galician.dat)<<'EOF'
%% from hyphen-galician:
galician loadhyph-gl.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-galician.def)<<'EOF'
%% from hyphen-galician:
\addlanguage{galician}{loadhyph-gl.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-galician.dat.lua)<<'EOF'
-- from hyphen-galician:
	['galician'] = {
		loader = 'loadhyph-gl.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-gl.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-georgian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-georgian.dat)<<'EOF'
%% from hyphen-georgian:
georgian loadhyph-ka.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-georgian.def)<<'EOF'
%% from hyphen-georgian:
\addlanguage{georgian}{loadhyph-ka.tex}{}{1}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-georgian.dat.lua)<<'EOF'
-- from hyphen-georgian:
	['georgian'] = {
		loader = 'loadhyph-ka.tex',
		lefthyphenmin = 1,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-ka.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-german-%{texlive_version}.%{texlive_noarch}.svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-german.dat)<<'EOF'
%% from hyphen-german:
german loadhyph-de-1901.tex
ngerman loadhyph-de-1996.tex
swissgerman loadhyph-de-ch-1901.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-german.def)<<'EOF'
%% from hyphen-german:
\addlanguage{german}{loadhyph-de-1901.tex}{}{2}{2}
\addlanguage{ngerman}{loadhyph-de-1996.tex}{}{2}{2}
\addlanguage{swissgerman}{loadhyph-de-ch-1901.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-german.dat.lua)<<'EOF'
-- from hyphen-german:
	['german'] = {
		loader = 'loadhyph-de-1901.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-de-1901.pat.txt',
		hyphenation = '',
	},
	['ngerman'] = {
		loader = 'loadhyph-de-1996.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-de-1996.pat.txt',
		hyphenation = '',
	},
	['swissgerman'] = {
		loader = 'loadhyph-de-ch-1901.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-de-ch-1901.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-greek-%{texlive_version}.%{texlive_noarch}.5svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-greek.dat)<<'EOF'
%% from hyphen-greek:
greek loadhyph-el-polyton.tex
=polygreek
monogreek loadhyph-el-monoton.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-greek.def)<<'EOF'
%% from hyphen-greek:
\addlanguage{greek}{loadhyph-el-polyton.tex}{}{1}{1}
\addlanguage{polygreek}{loadhyph-el-polyton.tex}{}{1}{1}
\addlanguage{monogreek}{loadhyph-el-monoton.tex}{}{1}{1}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-greek.dat.lua)<<'EOF'
-- from hyphen-greek:
	['greek'] = {
		loader = 'loadhyph-el-polyton.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = { 'polygreek' },
		patterns = 'hyph-el-polyton.pat.txt',
		hyphenation = '',
	},
	['monogreek'] = {
		loader = 'loadhyph-el-monoton.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-el-monoton.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-hungarian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-hungarian.dat)<<'EOF'
%% from hyphen-hungarian:
hungarian loadhyph-hu.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-hungarian.def)<<'EOF'
%% from hyphen-hungarian:
\addlanguage{hungarian}{loadhyph-hu.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-hungarian.dat.lua)<<'EOF'
-- from hyphen-hungarian:
	['hungarian'] = {
		loader = 'loadhyph-hu.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-hu.pat.txt',
		hyphenation = '',
	},
EOF
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/generic/huhyphen/searchforerrors.rb \
	       %{_texmfdistdir}/doc/generic/huhyphen/testhyphenation.rb
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/doc/generic/huhyphen/searchforerrors.rb \
	       %{_texmfdistdir}/doc/generic/huhyphen/testhyphenation.rb
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-icelandic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-icelandic.dat)<<'EOF'
%% from hyphen-icelandic:
icelandic loadhyph-is.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-icelandic.def)<<'EOF'
%% from hyphen-icelandic:
\addlanguage{icelandic}{loadhyph-is.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-icelandic.dat.lua)<<'EOF'
-- from hyphen-icelandic:
	['icelandic'] = {
		loader = 'loadhyph-is.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-is.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-indic-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indic.dat)<<'EOF'
%% from hyphen-indic:
assamese loadhyph-as.tex
bengali loadhyph-bn.tex
gujarati loadhyph-gu.tex
hindi loadhyph-hi.tex
kannada loadhyph-kn.tex
malayalam loadhyph-ml.tex
marathi loadhyph-mr.tex
oriya loadhyph-or.tex
pali loadhyph-pi.tex
panjabi loadhyph-pa.tex
tamil loadhyph-ta.tex
telugu loadhyph-te.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indic.def)<<'EOF'
%% from hyphen-indic:
\addlanguage{assamese}{loadhyph-as.tex}{}{1}{1}
\addlanguage{bengali}{loadhyph-bn.tex}{}{1}{1}
\addlanguage{gujarati}{loadhyph-gu.tex}{}{1}{1}
\addlanguage{hindi}{loadhyph-hi.tex}{}{1}{1}
\addlanguage{kannada}{loadhyph-kn.tex}{}{1}{1}
\addlanguage{malayalam}{loadhyph-ml.tex}{}{1}{1}
\addlanguage{marathi}{loadhyph-mr.tex}{}{1}{1}
\addlanguage{oriya}{loadhyph-or.tex}{}{1}{1}
\addlanguage{pali}{loadhyph-pi.tex}{}{1}{2}
\addlanguage{panjabi}{loadhyph-pa.tex}{}{1}{1}
\addlanguage{tamil}{loadhyph-ta.tex}{}{1}{1}
\addlanguage{telugu}{loadhyph-te.tex}{}{1}{1}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indic.dat.lua)<<'EOF'
-- from hyphen-indic:
	['assamese'] = {
		loader = 'loadhyph-as.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-as.pat.txt',
		hyphenation = '',
	},
	['bengali'] = {
		loader = 'loadhyph-bn.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-bn.pat.txt',
		hyphenation = '',
	},
	['gujarati'] = {
		loader = 'loadhyph-gu.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-gu.pat.txt',
		hyphenation = '',
	},
	['hindi'] = {
		loader = 'loadhyph-hi.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-hi.pat.txt',
		hyphenation = '',
	},
	['kannada'] = {
		loader = 'loadhyph-kn.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-kn.pat.txt',
		hyphenation = '',
	},
	['malayalam'] = {
		loader = 'loadhyph-ml.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-ml.pat.txt',
		hyphenation = '',
	},
	['marathi'] = {
		loader = 'loadhyph-mr.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-mr.pat.txt',
		hyphenation = '',
	},
	['oriya'] = {
		loader = 'loadhyph-or.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-or.pat.txt',
		hyphenation = '',
	},
	['pali'] = {
		loader = 'loadhyph-pi.tex',
		lefthyphenmin = 1,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-pi.pat.txt',
		hyphenation = '',
	},
	['panjabi'] = {
		loader = 'loadhyph-pa.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-pa.pat.txt',
		hyphenation = '',
	},
	['tamil'] = {
		loader = 'loadhyph-ta.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-ta.pat.txt',
		hyphenation = '',
	},
	['telugu'] = {
		loader = 'loadhyph-te.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-te.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-indonesian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indonesian.dat)<<'EOF'
%% from hyphen-indonesian:
indonesian loadhyph-id.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indonesian.def)<<'EOF'
%% from hyphen-indonesian:
\addlanguage{indonesian}{loadhyph-id.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-indonesian.dat.lua)<<'EOF'
-- from hyphen-indonesian:
	['indonesian'] = {
		loader = 'loadhyph-id.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-id.pat.txt',
		hyphenation = 'hyph-id.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-interlingua-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-interlingua.dat)<<'EOF'
%% from hyphen-interlingua:
interlingua loadhyph-ia.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-interlingua.def)<<'EOF'
%% from hyphen-interlingua:
\addlanguage{interlingua}{loadhyph-ia.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-interlingua.dat.lua)<<'EOF'
-- from hyphen-interlingua:
	['interlingua'] = {
		loader = 'loadhyph-ia.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-ia.pat.txt',
		hyphenation = 'hyph-ia.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-irish-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-irish.dat)<<'EOF'
%% from hyphen-irish:
irish loadhyph-ga.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-irish.def)<<'EOF'
%% from hyphen-irish:
\addlanguage{irish}{loadhyph-ga.tex}{}{2}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-irish.dat.lua)<<'EOF'
-- from hyphen-irish:
	['irish'] = {
		loader = 'loadhyph-ga.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-ga.pat.txt',
		hyphenation = 'hyph-ga.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-italian-%{texlive_version}.%{texlive_noarch}.4.8gsvn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-italian.dat)<<'EOF'
%% from hyphen-italian:
italian loadhyph-it.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-italian.def)<<'EOF'
%% from hyphen-italian:
\addlanguage{italian}{loadhyph-it.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-italian.dat.lua)<<'EOF'
-- from hyphen-italian:
	['italian'] = {
		loader = 'loadhyph-it.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-it.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-kurmanji-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-kurmanji.dat)<<'EOF'
%% from hyphen-kurmanji:
kurmanji loadhyph-kmr.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-kurmanji.def)<<'EOF'
%% from hyphen-kurmanji:
\addlanguage{kurmanji}{loadhyph-kmr.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-kurmanji.dat.lua)<<'EOF'
-- from hyphen-kurmanji:
	['kurmanji'] = {
		loader = 'loadhyph-kmr.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-kmr.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-latin-%{texlive_version}.%{texlive_noarch}.3.1svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latin.dat)<<'EOF'
%% from hyphen-latin:
classiclatin loadhyph-la-x-classic.tex
latin loadhyph-la.tex
liturgicallatin loadhyph-la-x-liturgic.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latin.def)<<'EOF'
%% from hyphen-latin:
\addlanguage{classiclatin}{loadhyph-la-x-classic.tex}{}{2}{2}
\addlanguage{latin}{loadhyph-la.tex}{}{2}{2}
\addlanguage{liturgicallatin}{loadhyph-la-x-liturgic.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latin.dat.lua)<<'EOF'
-- from hyphen-latin:
	['classiclatin'] = {
		loader = 'loadhyph-la-x-classic.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-la-x-classic.pat.txt',
		hyphenation = '',
	},
	['latin'] = {
		loader = 'loadhyph-la.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-la.pat.txt',
		hyphenation = '',
	},
	['liturgicallatin'] = {
		loader = 'loadhyph-la-x-liturgic.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-la-x-liturgic.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-latvian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latvian.dat)<<'EOF'
%% from hyphen-latvian:
latvian loadhyph-lv.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latvian.def)<<'EOF'
%% from hyphen-latvian:
\addlanguage{latvian}{loadhyph-lv.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-latvian.dat.lua)<<'EOF'
-- from hyphen-latvian:
	['latvian'] = {
		loader = 'loadhyph-lv.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-lv.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-lithuanian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-lithuanian.dat)<<'EOF'
%% from hyphen-lithuanian:
lithuanian loadhyph-lt.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-lithuanian.def)<<'EOF'
%% from hyphen-lithuanian:
\addlanguage{lithuanian}{loadhyph-lt.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-lithuanian.dat.lua)<<'EOF'
-- from hyphen-lithuanian:
	['lithuanian'] = {
		loader = 'loadhyph-lt.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-lt.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-macedonian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-macedonian.dat)<<'EOF'
%% from hyphen-macedonian:
macedonian loadhyph-mk.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-macedonian.def)<<'EOF'
%% from hyphen-macedonian:
\addlanguage{macedonian}{loadhyph-mk.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-macedonian.dat.lua)<<'EOF'
-- from hyphen-macedonian:
	['macedonian'] = {
		loader = 'loadhyph-mk.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-mk.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-mongolian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-mongolian.dat)<<'EOF'
%% from hyphen-mongolian:
mongolian loadhyph-mn-cyrl.tex
mongolianlmc loadhyph-mn-cyrl-x-lmc.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-mongolian.def)<<'EOF'
%% from hyphen-mongolian:
\addlanguage{mongolian}{loadhyph-mn-cyrl.tex}{}{2}{2}
\addlanguage{mongolianlmc}{loadhyph-mn-cyrl-x-lmc.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-mongolian.dat.lua)<<'EOF'
-- from hyphen-mongolian:
	['mongolian'] = {
		loader = 'loadhyph-mn-cyrl.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-mn-cyrl.pat.txt',
		hyphenation = '',
	},
	['mongolianlmc'] = {
		loader = 'loadhyph-mn-cyrl-x-lmc.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		special = 'disabled:only for 8bit montex with lmc encoding',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-norwegian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-norwegian.dat)<<'EOF'
%% from hyphen-norwegian:
bokmal loadhyph-nb.tex
=norwegian
=norsk
nynorsk loadhyph-nn.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-norwegian.def)<<'EOF'
%% from hyphen-norwegian:
\addlanguage{bokmal}{loadhyph-nb.tex}{}{2}{2}
\addlanguage{norwegian}{loadhyph-nb.tex}{}{2}{2}
\addlanguage{norsk}{loadhyph-nb.tex}{}{2}{2}
\addlanguage{nynorsk}{loadhyph-nn.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-norwegian.dat.lua)<<'EOF'
-- from hyphen-norwegian:
	['bokmal'] = {
		loader = 'loadhyph-nb.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'norwegian', 'norsk' },
		patterns = 'hyph-nb.pat.txt',
		hyphenation = 'hyph-nb.hyp.txt',
	},
	['nynorsk'] = {
		loader = 'loadhyph-nn.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-nn.pat.txt',
		hyphenation = 'hyph-nn.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-occitan-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-occitan.dat)<<'EOF'
%% from hyphen-occitan:
occitan loadhyph-oc.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-occitan.def)<<'EOF'
%% from hyphen-occitan:
\addlanguage{occitan}{loadhyph-oc.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-occitan.dat.lua)<<'EOF'
-- from hyphen-occitan:
	['occitan'] = {
		loader = 'loadhyph-oc.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-oc.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-piedmontese-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-piedmontese.dat)<<'EOF'
%% from hyphen-piedmontese:
piedmontese loadhyph-pms.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-piedmontese.def)<<'EOF'
%% from hyphen-piedmontese:
\addlanguage{piedmontese}{loadhyph-pms.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-piedmontese.dat.lua)<<'EOF'
-- from hyphen-piedmontese:
	['piedmontese'] = {
		loader = 'loadhyph-pms.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-pms.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-polish-%{texlive_version}.%{texlive_noarch}.3.0asvn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-polish.dat)<<'EOF'
%% from hyphen-polish:
polish loadhyph-pl.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-polish.def)<<'EOF'
%% from hyphen-polish:
\addlanguage{polish}{loadhyph-pl.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-polish.dat.lua)<<'EOF'
-- from hyphen-polish:
	['polish'] = {
		loader = 'loadhyph-pl.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-pl.pat.txt',
		hyphenation = 'hyph-pl.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-portuguese-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-portuguese.dat)<<'EOF'
%% from hyphen-portuguese:
portuguese loadhyph-pt.tex
=portuges
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-portuguese.def)<<'EOF'
%% from hyphen-portuguese:
\addlanguage{portuguese}{loadhyph-pt.tex}{}{2}{3}
\addlanguage{portuges}{loadhyph-pt.tex}{}{2}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-portuguese.dat.lua)<<'EOF'
-- from hyphen-portuguese:
	['portuguese'] = {
		loader = 'loadhyph-pt.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = { 'portuges' },
		patterns = 'hyph-pt.pat.txt',
		hyphenation = 'hyph-pt.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-romanian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romanian.dat)<<'EOF'
%% from hyphen-romanian:
romanian loadhyph-ro.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romanian.def)<<'EOF'
%% from hyphen-romanian:
\addlanguage{romanian}{loadhyph-ro.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romanian.dat.lua)<<'EOF'
-- from hyphen-romanian:
	['romanian'] = {
		loader = 'loadhyph-ro.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-ro.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-romansh-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romansh.dat)<<'EOF'
%% from hyphen-romansh:
romansh loadhyph-rm.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romansh.def)<<'EOF'
%% from hyphen-romansh:
\addlanguage{romansh}{loadhyph-rm.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-romansh.dat.lua)<<'EOF'
-- from hyphen-romansh:
	['romansh'] = {
		loader = 'loadhyph-rm.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-rm.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-russian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-russian.dat)<<'EOF'
%% from hyphen-russian:
russian loadhyph-ru.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-russian.def)<<'EOF'
%% from hyphen-russian:
\addlanguage{russian}{loadhyph-ru.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-russian.dat.lua)<<'EOF'
-- from hyphen-russian:
	['russian'] = {
		loader = 'loadhyph-ru.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-ru.pat.txt',
		hyphenation = 'hyph-ru.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-sanskrit-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-sanskrit.dat)<<'EOF'
%% from hyphen-sanskrit:
sanskrit loadhyph-sa.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-sanskrit.def)<<'EOF'
%% from hyphen-sanskrit:
\addlanguage{sanskrit}{loadhyph-sa.tex}{}{1}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-sanskrit.dat.lua)<<'EOF'
-- from hyphen-sanskrit:
	['sanskrit'] = {
		loader = 'loadhyph-sa.tex',
		lefthyphenmin = 1,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-sa.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-serbian-%{texlive_version}.%{texlive_noarch}.1.0asvn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-serbian.dat)<<'EOF'
%% from hyphen-serbian:
serbian loadhyph-sr-latn.tex
serbianc loadhyph-sr-cyrl.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-serbian.def)<<'EOF'
%% from hyphen-serbian:
\addlanguage{serbian}{loadhyph-sr-latn.tex}{}{2}{2}
\addlanguage{serbianc}{loadhyph-sr-cyrl.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-serbian.dat.lua)<<'EOF'
-- from hyphen-serbian:
	['serbian'] = {
		loader = 'loadhyph-sr-latn.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-sh-latn.pat.txt,hyph-sh-cyrl.pat.txt',
		hyphenation = 'hyph-sh-latn.hyp.txt,hyph-sh-cyrl.hyp.txt',
	},
	['serbianc'] = {
		loader = 'loadhyph-sr-cyrl.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-sh-latn.pat.txt,hyph-sh-cyrl.pat.txt',
		hyphenation = 'hyph-sh-latn.hyp.txt,hyph-sh-cyrl.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-slovak-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovak.dat)<<'EOF'
%% from hyphen-slovak:
slovak loadhyph-sk.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovak.def)<<'EOF'
%% from hyphen-slovak:
\addlanguage{slovak}{loadhyph-sk.tex}{}{2}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovak.dat.lua)<<'EOF'
-- from hyphen-slovak:
	['slovak'] = {
		loader = 'loadhyph-sk.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-sk.pat.txt',
		hyphenation = 'hyph-sk.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-slovenian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovenian.dat)<<'EOF'
%% from hyphen-slovenian:
slovenian loadhyph-sl.tex
=slovene
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovenian.def)<<'EOF'
%% from hyphen-slovenian:
\addlanguage{slovenian}{loadhyph-sl.tex}{}{2}{2}
\addlanguage{slovene}{loadhyph-sl.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-slovenian.dat.lua)<<'EOF'
-- from hyphen-slovenian:
	['slovenian'] = {
		loader = 'loadhyph-sl.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'slovene' },
		patterns = 'hyph-sl.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-spanish-%{texlive_version}.%{texlive_noarch}.4.5svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-spanish.dat)<<'EOF'
%% from hyphen-spanish:
spanish loadhyph-es.tex
=espanol
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-spanish.def)<<'EOF'
%% from hyphen-spanish:
\addlanguage{spanish}{loadhyph-es.tex}{}{2}{2}
\addlanguage{espanol}{loadhyph-es.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-spanish.dat.lua)<<'EOF'
-- from hyphen-spanish:
	['spanish'] = {
		loader = 'loadhyph-es.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'espanol' },
		patterns = 'hyph-es.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-swedish-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-swedish.dat)<<'EOF'
%% from hyphen-swedish:
swedish loadhyph-sv.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-swedish.def)<<'EOF'
%% from hyphen-swedish:
\addlanguage{swedish}{loadhyph-sv.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-swedish.dat.lua)<<'EOF'
-- from hyphen-swedish:
	['swedish'] = {
		loader = 'loadhyph-sv.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-sv.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-thai-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-thai.dat)<<'EOF'
%% from hyphen-thai:
thai loadhyph-th.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-thai.def)<<'EOF'
%% from hyphen-thai:
\addlanguage{thai}{loadhyph-th.tex}{}{2}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-thai.dat.lua)<<'EOF'
-- from hyphen-thai:
	['thai'] = {
		loader = 'loadhyph-th.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-th.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-turkish-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkish.dat)<<'EOF'
%% from hyphen-turkish:
turkish loadhyph-tr.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkish.def)<<'EOF'
%% from hyphen-turkish:
\addlanguage{turkish}{loadhyph-tr.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkish.dat.lua)<<'EOF'
-- from hyphen-turkish:
	['turkish'] = {
		loader = 'loadhyph-tr.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-tr.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-turkmen-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkmen.dat)<<'EOF'
%% from hyphen-turkmen:
turkmen loadhyph-tk.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkmen.def)<<'EOF'
%% from hyphen-turkmen:
\addlanguage{turkmen}{loadhyph-tk.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-turkmen.dat.lua)<<'EOF'
-- from hyphen-turkmen:
	['turkmen'] = {
		loader = 'loadhyph-tk.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-tk.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-ukrainian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ukrainian.dat)<<'EOF'
%% from hyphen-ukrainian:
ukrainian loadhyph-uk.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ukrainian.def)<<'EOF'
%% from hyphen-ukrainian:
\addlanguage{ukrainian}{loadhyph-uk.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-ukrainian.dat.lua)<<'EOF'
-- from hyphen-ukrainian:
	['ukrainian'] = {
		loader = 'loadhyph-uk.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-uk.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-uppersorbian-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-uppersorbian.dat)<<'EOF'
%% from hyphen-uppersorbian:
uppersorbian loadhyph-hsb.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-uppersorbian.def)<<'EOF'
%% from hyphen-uppersorbian:
\addlanguage{uppersorbian}{loadhyph-hsb.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-uppersorbian.dat.lua)<<'EOF'
-- from hyphen-uppersorbian:
	['uppersorbian'] = {
		loader = 'loadhyph-hsb.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-hsb.pat.txt',
		hyphenation = 'hyph-hsb.hyp.txt',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphen-welsh-%{texlive_version}.%{texlive_noarch}.svn54568-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-welsh.dat)<<'EOF'
%% from hyphen-welsh:
welsh loadhyph-cy.tex
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-welsh.def)<<'EOF'
%% from hyphen-welsh:
\addlanguage{welsh}{loadhyph-cy.tex}{}{2}{3}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/hyphen-welsh.dat.lua)<<'EOF'
-- from hyphen-welsh:
	['welsh'] = {
		loader = 'loadhyph-cy.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-cy.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphenat-%{texlive_version}.%{texlive_noarch}.2.3csvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyphenex-%{texlive_version}.%{texlive_noarch}.svn37354-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hyplain-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ibycus-babel-%{texlive_version}.%{texlive_noarch}.3.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/latex/ibycus-babel/ibyhyph.pl
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ibygrk-fonts-%{texlive_version}.%{texlive_noarch}.4.5svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-ibygrk
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/ibygrk/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-ibygrk
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-ibygrk/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-ibygrk/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-ibygrk/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-ibygrk/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-ibygrk.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-ibygrk    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-ibygrk/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-icite-%{texlive_version}.%{texlive_noarch}.1.3asvn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-icsv-%{texlive_version}.%{texlive_noarch}.0.0.2svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-identkey-%{texlive_version}.%{texlive_noarch}.0.0.1.0svn49018-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-idxcmds-%{texlive_version}.%{texlive_noarch}.0.0.2csvn54554-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-idxlayout-%{texlive_version}.%{texlive_noarch}.0.0.4dsvn25821-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ieeepes-%{texlive_version}.%{texlive_noarch}.4.0svn17359-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ietfbibs-%{texlive_version}.%{texlive_noarch}.1.0.0svn41332-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-iffont-%{texlive_version}.%{texlive_noarch}.1.0.0svn38823-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ifmslide-%{texlive_version}.%{texlive_noarch}.0.0.47svn20727-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ifmtarg-%{texlive_version}.%{texlive_noarch}.1.2bsvn47544-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ifnextok-%{texlive_version}.%{texlive_noarch}.0.0.3svn23379-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ifoddpage-%{texlive_version}.%{texlive_noarch}.1.1svn40726-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ifplatform-%{texlive_version}.%{texlive_noarch}.0.0.4asvn45533-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ifptex-%{texlive_version}.%{texlive_noarch}.2.0svn52626-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ifsym-%{texlive_version}.%{texlive_noarch}.svn24868-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-iftex-%{texlive_version}.%{texlive_noarch}.1.0dsvn54159-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ifthenx-%{texlive_version}.%{texlive_noarch}.0.0.1asvn25819-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ifxptex-%{texlive_version}.%{texlive_noarch}.0.0.2svn46153-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-iitem-%{texlive_version}.%{texlive_noarch}.1.0svn29613-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ijmart-%{texlive_version}.%{texlive_noarch}.1.7svn30958-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ijqc-%{texlive_version}.%{texlive_noarch}.1.2svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ijsra-%{texlive_version}.%{texlive_noarch}.1.1svn44886-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-imac-%{texlive_version}.%{texlive_noarch}.svn17347-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-image-gallery-%{texlive_version}.%{texlive_noarch}.1.0jsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-imakeidx-%{texlive_version}.%{texlive_noarch}.1.3esvn42287-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-imfellenglish-fonts-%{texlive_version}.%{texlive_noarch}.svn38547-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-imfellenglish
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/iginomarini/imfellenglish/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/iginomarini/imfellenglish/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-imfellenglish
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-imfellenglish/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-imfellenglish/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-imfellenglish/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-imfellenglish/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-imfellenglish.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-imfellenglish    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-imfellenglish/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-imfellenglish.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-imfellenglish/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-imfellenglish.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-imfellenglish.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-impatient-%{texlive_version}.%{texlive_noarch}.2020svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-impatient-cn-%{texlive_version}.%{texlive_noarch}.2020svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-impatient-fr-%{texlive_version}.%{texlive_noarch}.2020svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-impnattypo-%{texlive_version}.%{texlive_noarch}.1.5svn50227-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-import-%{texlive_version}.%{texlive_noarch}.6.2svn54683-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-imsproc-%{texlive_version}.%{texlive_noarch}.0.0.1svn29803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-imtekda-%{texlive_version}.%{texlive_noarch}.1.7svn17667-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-incgraph-%{texlive_version}.%{texlive_noarch}.1.12svn36500-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-includernw-%{texlive_version}.%{texlive_noarch}.0.0.1.0svn47557-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-inconsolata-fonts-%{texlive_version}.%{texlive_noarch}.1.121svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-inconsolata
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/inconsolata/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/inconsolata/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-inconsolata
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-inconsolata/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-inconsolata/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-inconsolata/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-inconsolata/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-inconsolata.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-inconsolata    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-inconsolata/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-inconsolata.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-inconsolata/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-inconsolata.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-inconsolata.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-index-%{texlive_version}.%{texlive_noarch}.4.1betasvn24099-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-indextools-%{texlive_version}.%{texlive_noarch}.1.5.1svn38931-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-infwarerr-%{texlive_version}.%{texlive_noarch}.1.5svn53023-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-initials-fonts-%{texlive_version}.%{texlive_noarch}.svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-initials
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/initials/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-initials
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-initials/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-initials/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-initials/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-initials/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-initials.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-initials    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-initials/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-inkpaper-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-inline-images-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-inlinebib-%{texlive_version}.%{texlive_noarch}.svn22018-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-inlinedef-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-inputenx-%{texlive_version}.%{texlive_noarch}.1.12svn52986-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-inputtrc-%{texlive_version}.%{texlive_noarch}.0.0.3svn28019-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-inriafonts-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-inriafonts
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/inriafonts/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/truetype/public/inriafonts/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/inriafonts/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-inriafonts
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-inriafonts/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-inriafonts/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-inriafonts/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-inriafonts/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-inriafonts.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-inriafonts    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-inriafonts/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-inriafonts.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-inriafonts/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-inriafonts.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-inriafonts.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-insbox-%{texlive_version}.%{texlive_noarch}.2.2svn34299-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-intcalc-%{texlive_version}.%{texlive_noarch}.1.3svn53168-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-interactiveworkbook-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-interchar-%{texlive_version}.%{texlive_noarch}.0.0.2svn36312-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-interfaces-%{texlive_version}.%{texlive_noarch}.3.1svn21474-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-interpreter-%{texlive_version}.%{texlive_noarch}.1.2svn27232-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-interval-%{texlive_version}.%{texlive_noarch}.0.0.4svn50265-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-intopdf-%{texlive_version}.%{texlive_noarch}.0.0.2.1svn51247-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-intro-scientific-%{texlive_version}.%{texlive_noarch}.5th_editionsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-inversepath-%{texlive_version}.%{texlive_noarch}.0.0.2svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-invoice-%{texlive_version}.%{texlive_noarch}.svn48359-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-invoice-class-%{texlive_version}.%{texlive_noarch}.1.0svn49749-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-invoice2-%{texlive_version}.%{texlive_noarch}.svn46364-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-iodhbwm-%{texlive_version}.%{texlive_noarch}.1.2.1svn54734-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove this
    rm -vrf %{buildroot}%{_texmfdistdir}/tlpkg/tlpobj
    rm -vrf %{buildroot}%{_texmfmaindir}/tlpkg/tlpobj
    rm -v  %{buildroot}%{_datadir}/texlive/texmf
    rm -v  %{buildroot}%{_datadir}/texlive/texmf-dist
    rm -v  %{buildroot}%{_texmfmaindir}/tlpostcode
    rm -vr %{buildroot}%{_datadir}/texlive
    find %{buildroot}%{_texmfmaindir}/ %{buildroot}%{_texmfdistdir}/ \
        -type f -a -perm /g+w,o+w | xargs --no-run-if-empty chmod g-w,o-w

%changelog
