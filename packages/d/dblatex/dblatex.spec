#
# spec file for package dblatex
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           dblatex
Version:        0.3.10
Release:        0
Summary:        DocBook to LaTeX Publishing
License:        GPL-2.0-only
Group:          Productivity/Publishing/DocBook
URL:            http://dblatex.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
#PATCH-FIX-OPENSUSE dblatex-0.3.4-disable-debian.patch toganm@opensuse.org -disables debian specific installation parts
Patch0:         dblatex-0.3.4-disable-debian.patch
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  grep
BuildRequires:  libxslt-tools
BuildRequires:  python2-base
BuildRequires:  python-rpm-macros
BuildRequires:  pyxml
BuildRequires:  texlive-epstopdf
BuildRequires:  texlive-latex
BuildRequires:  texlive-makeindex
BuildRequires:  transfig
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(amssymb.sty)
BuildRequires:  tex(anysize.sty)
BuildRequires:  tex(appendix.sty)
BuildRequires:  tex(bookmark.sty)
BuildRequires:  tex(changebar.sty)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(colortbl.sty)
BuildRequires:  tex(courier.sty)
BuildRequires:  tex(eucal.sty)
BuildRequires:  tex(fancybox.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(float.sty)
BuildRequires:  tex(footmisc.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(helvet.sty)
BuildRequires:  tex(hhline.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(ifpdf.sty)
BuildRequires:  tex(ifthen.sty)
BuildRequires:  tex(latexsym.sty)
BuildRequires:  tex(listings.sty)
BuildRequires:  tex(longtable.sty)
BuildRequires:  tex(lscape.sty)
BuildRequires:  tex(mathptmx.sty)
BuildRequires:  tex(mathrsfs.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(overpic.sty)
BuildRequires:  tex(palatino.sty)
BuildRequires:  tex(pdfpages.sty)
BuildRequires:  tex(pifont.sty)
BuildRequires:  tex(refcount.sty)
BuildRequires:  tex(rotating.sty)
BuildRequires:  tex(stmaryrd.sty)
BuildRequires:  tex(subfigure.sty)
BuildRequires:  tex(tabularx.sty)
BuildRequires:  tex(textcomp.sty)
BuildRequires:  tex(titlesec.sty)
BuildRequires:  tex(wasysym.sty)
Requires:       docbook_4
Requires:       pyxml
Requires:       texlive-epstopdf
Requires:       texlive-latex
# grep for \usepackage in dblatex but require only one
# style of a texlive package
# Required by all TeX engines and locales
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(appendix.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(calc.sty)
Requires:       tex(changebar.sty)
Requires:       tex(color.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hhline.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(lscape.sty)
Requires:       tex(multirow.sty)
Requires:       tex(overpic.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(pifont.sty)
Requires:       tex(refcount.sty)
Requires:       tex(subfigure.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(titlesec.sty)
# XeTeX
Recommends:     tex(amstext.sty)
# not XeTeX
Recommends:     tex(courier.sty)
Recommends:     tex(helvet.sty)
Recommends:     tex(mathptmx.sty)
Recommends:     tex(mathrsfs.sty)
# db2latex contrib style
Recommends:     tex(anysize.sty)
Recommends:     tex(fancybox.sty)
Recommends:     tex(rotating.sty)
Recommends:     tex(palatino.sty)
# some extra unicode symbols (runtime detection)
Recommends:     tex(stmaryrd.sty)
Recommends:     tex(wasysym.sty)
# not XeTex and languages [ja,ko,zh]
Recommends:     tex(CJKutf8.sty)
# End of optional dependencies
BuildArch:      noarch

%description
dblatex is a program that transforms your SGML/XMLDocBook documents to DVI,
PostScript or PDF by translating them into pure LaTeX as a first process.
MathML 2.0 markups are supported, too. It started as a clone of DB2LaTeX.

%package doc
Summary:        DocBook to LaTeX Publishing - Documentation
Group:          Documentation/HTML

%description doc
dblatex is a program that transforms your SGML/XMLDocBook documents to DVI,
PostScript or PDF by translating them into pure LaTeX as a first process.
MathML 2.0 markups are supported, too. It started as a clone of DB2LaTeX.

%prep
%setup -q
%patch0 -p1
# correct doc paths in setup
sed -i 's@share/doc/dblatex@%{_docdir}/dblatex@g' setup.py

# Remove any She-bang lines
sed -i '/#!\/usr\//d' lib/dbtexmf/dblatex/xetex/fsencoder.py \
  lib/dbtexmf/dblatex/xetex/fontspec.py \
  lib/dbtexmf/dblatex/xetex/fsconfig.py

%build
%python2_build

%install
%python2_install
sed -i "s|env python|python2|g" %{buildroot}%{_bindir}/dblatex
%fdupes %{buildroot}%{_docdir}
%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{python2_sitelib}

%files doc
%{_docdir}/dblatex

%files
%{_bindir}/dblatex
%{_datadir}/dblatex
%{python2_sitelib}/*
%{_mandir}/man1/dblatex.1%{?ext_man}

%changelog
