#
# spec file for package ghc-pandoc
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


%global pkg_name pandoc
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        3.14
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Conversion between markup formats
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-JuicyPixels-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-asciidoc-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-citeproc-devel
BuildRequires:  ghc-commonmark-devel
BuildRequires:  ghc-commonmark-extensions-devel
BuildRequires:  ghc-commonmark-pandoc-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-crypton-connection-devel
BuildRequires:  ghc-crypton-devel
BuildRequires:  ghc-crypton-x509-system-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-djot-devel
BuildRequires:  ghc-doclayout-devel
BuildRequires:  ghc-doctemplates-devel
BuildRequires:  ghc-emojis-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-gridtables-devel
BuildRequires:  ghc-haddock-library-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-ipynb-devel
BuildRequires:  ghc-jira-wiki-markup-devel
BuildRequires:  ghc-mime-types-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-skylighting-core-devel
BuildRequires:  ghc-skylighting-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-tagsoup-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-texmath-devel
BuildRequires:  ghc-text-builder-devel
BuildRequires:  ghc-text-conversions-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-typst-devel
BuildRequires:  ghc-unicode-collation-devel
BuildRequires:  ghc-unicode-data-devel
BuildRequires:  ghc-unicode-transforms-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-devel
BuildRequires:  ghc-xml-types-devel
BuildRequires:  ghc-yamlet-aeson-devel
BuildRequires:  ghc-yamlet-devel
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  ghc-zlib-devel
Requires:       pandoc-data = %{version}-%{release}
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-Glob-prof
BuildRequires:  ghc-JuicyPixels-prof
BuildRequires:  ghc-aeson-pretty-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-asciidoc-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-citeproc-prof
BuildRequires:  ghc-commonmark-extensions-prof
BuildRequires:  ghc-commonmark-pandoc-prof
BuildRequires:  ghc-commonmark-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-connection-prof
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-crypton-x509-system-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-djot-prof
BuildRequires:  ghc-doclayout-prof
BuildRequires:  ghc-doctemplates-prof
BuildRequires:  ghc-emojis-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-gridtables-prof
BuildRequires:  ghc-haddock-library-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-ipynb-prof
BuildRequires:  ghc-jira-wiki-markup-prof
BuildRequires:  ghc-mime-types-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-skylighting-core-prof
BuildRequires:  ghc-skylighting-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-tagsoup-prof
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-texmath-prof
BuildRequires:  ghc-text-builder-prof
BuildRequires:  ghc-text-conversions-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-tls-prof
BuildRequires:  ghc-typst-prof
BuildRequires:  ghc-unicode-collation-prof
BuildRequires:  ghc-unicode-data-prof
BuildRequires:  ghc-unicode-transforms-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-xml-conduit-prof
BuildRequires:  ghc-xml-prof
BuildRequires:  ghc-xml-types-prof
BuildRequires:  ghc-yamlet-aeson-prof
BuildRequires:  ghc-yamlet-prof
BuildRequires:  ghc-zip-archive-prof
BuildRequires:  ghc-zlib-prof
%endif
%if %{with tests}
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-tasty-golden-prof
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-prof
%endif
%endif

%description
Pandoc is a Haskell library for converting from one markup format to another.
The formats it can handle include

- light markup formats (many variants of Markdown, reStructuredText, AsciiDoc,
Org-mode, Muse, Textile, txt2tags, djot, bbcode) - HTML formats (HTML 4 and 5,
chunked HTML) - Ebook formats (EPUB v2 and v3, FB2) - Documentation formats
(GNU TexInfo, Haddock, Vimdoc) - Roff formats (man, ms, mdoc) - TeX formats
(LaTeX, ConTeXt) - Typst - ANSI-formatted text - XML formats (DocBook 4 and 5,
JATS, TEI Simple, OpenDocument) - Outline formats (OPML) - Bibliography formats
(BibTeX, BibLaTeX, CSL JSON, CSL YAML, RIS) - Word processor formats (Docx,
RTF, ODT, FODT) - Interactive notebook formats (Jupyter notebook ipynb) - Page
layout formats (InDesign ICML) - Wiki markup formats (MediaWiki, DokuWiki,
TikiWiki, TWiki, Vimwiki, XWiki, ZimWiki, Jira wiki, Creole) - Slide show
formats (LaTeX Beamer, PowerPoint, Slidy, reveal.js, Slideous, S5, DZSlides) -
Data formats (CSV and TSV tables, Excel spreadsheets) - Serialization formats
(Haskell, JSON, or XML representation of the AST) - PDF (via external programs
such as pdflatex or wkhtmltopdf)

Pandoc can convert mathematical content in documents between TeX, MathML, Word
equations, roff eqn, typst, and plain text. It includes a powerful system for
automatic citations and bibliographies, and it can be customized extensively
using templates, filters, and custom readers and writers written in Lua.

For the pandoc command-line program, see the 'pandoc-cli' package.

%package -n pandoc-data
Summary:        Data files for pandoc
BuildArch:      noarch

%description -n pandoc-data
This package provides the runtime data files for the pandoc library and
command-line program.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%pkg_name-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%pkg_name-doc
This package provides the Haskell %{pkg_name} library documentation.

%if %{with ghc_prof}
%package -n ghc-%pkg_name-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%pkg_name-devel = %{version}-%{release}
Supplements:    (ghc-%pkg_name-devel and ghc-prof)

%description -n ghc-%pkg_name-prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
%autosetup -p1 -n %pkg_name-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license COPYING.md

%files -n pandoc-data
%license COPYING.md
%dir %{_datadir}/%pkg_name-%{version}
%dir %{_datadir}/%pkg_name-%{version}/citeproc
%dir %{_datadir}/%pkg_name-%{version}/citeproc/biblatex-localization
%dir %{_datadir}/%pkg_name-%{version}/data
%dir %{_datadir}/%pkg_name-%{version}/data/docx
%dir %{_datadir}/%pkg_name-%{version}/data/docx/_rels
%dir %{_datadir}/%pkg_name-%{version}/data/docx/docProps
%dir %{_datadir}/%pkg_name-%{version}/data/docx/word
%dir %{_datadir}/%pkg_name-%{version}/data/docx/word/_rels
%dir %{_datadir}/%pkg_name-%{version}/data/docx/word/theme
%dir %{_datadir}/%pkg_name-%{version}/data/dzslides
%dir %{_datadir}/%pkg_name-%{version}/data/odt
%dir %{_datadir}/%pkg_name-%{version}/data/odt/META-INF
%dir %{_datadir}/%pkg_name-%{version}/data/pptx
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/_rels
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/docProps
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/_rels
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/notesMasters
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/notesMasters/_rels
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/notesSlides
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/notesSlides/_rels
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideMasters
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideMasters/_rels
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slides
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slides/_rels
%dir %{_datadir}/%pkg_name-%{version}/data/pptx/ppt/theme
%dir %{_datadir}/%pkg_name-%{version}/data/templates
%dir %{_datadir}/%pkg_name-%{version}/data/translations
%{_datadir}/%pkg_name-%{version}/COPYRIGHT
%{_datadir}/%pkg_name-%{version}/MANUAL.txt
%{_datadir}/%pkg_name-%{version}/citeproc/biblatex-localization/*.lbx.strings
%{_datadir}/%pkg_name-%{version}/data/abbreviations
%{_datadir}/%pkg_name-%{version}/data/creole.lua
%{_datadir}/%pkg_name-%{version}/data/default.csl
%{_datadir}/%pkg_name-%{version}/data/docbook-entities.txt
%{_datadir}/%pkg_name-%{version}/data/docx/?Content_Types?.xml
%{_datadir}/%pkg_name-%{version}/data/docx/_rels/.rels
%{_datadir}/%pkg_name-%{version}/data/docx/docProps/app.xml
%{_datadir}/%pkg_name-%{version}/data/docx/docProps/core.xml
%{_datadir}/%pkg_name-%{version}/data/docx/docProps/custom.xml
%{_datadir}/%pkg_name-%{version}/data/docx/word/_rels/document.xml.rels
%{_datadir}/%pkg_name-%{version}/data/docx/word/_rels/footnotes.xml.rels
%{_datadir}/%pkg_name-%{version}/data/docx/word/comments.xml
%{_datadir}/%pkg_name-%{version}/data/docx/word/document.xml
%{_datadir}/%pkg_name-%{version}/data/docx/word/fontTable.xml
%{_datadir}/%pkg_name-%{version}/data/docx/word/footnotes.xml
%{_datadir}/%pkg_name-%{version}/data/docx/word/numbering.xml
%{_datadir}/%pkg_name-%{version}/data/docx/word/settings.xml
%{_datadir}/%pkg_name-%{version}/data/docx/word/styles.xml
%{_datadir}/%pkg_name-%{version}/data/docx/word/theme/theme1.xml
%{_datadir}/%pkg_name-%{version}/data/docx/word/webSettings.xml
%{_datadir}/%pkg_name-%{version}/data/dzslides/template.html
%{_datadir}/%pkg_name-%{version}/data/epub.css
%{_datadir}/%pkg_name-%{version}/data/init.lua
%{_datadir}/%pkg_name-%{version}/data/odt/META-INF/manifest.xml
%{_datadir}/%pkg_name-%{version}/data/odt/content.xml
%{_datadir}/%pkg_name-%{version}/data/odt/manifest.rdf
%{_datadir}/%pkg_name-%{version}/data/odt/meta.xml
%{_datadir}/%pkg_name-%{version}/data/odt/mimetype
%{_datadir}/%pkg_name-%{version}/data/odt/styles.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/?Content_Types?.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/_rels/.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/docProps/app.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/docProps/core.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/_rels/presentation.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/notesMasters/_rels/notesMaster1.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/notesMasters/notesMaster1.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/notesSlides/_rels/notesSlide1.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/notesSlides/_rels/notesSlide2.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/notesSlides/notesSlide1.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/notesSlides/notesSlide2.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/presProps.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/presentation.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout1.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout10.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout11.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout2.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout3.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout4.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout5.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout6.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout7.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout8.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout9.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout1.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout10.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout11.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout2.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout3.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout4.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout5.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout6.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout7.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout8.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideLayouts/slideLayout9.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideMasters/_rels/slideMaster1.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slideMasters/slideMaster1.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slides/_rels/slide1.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slides/_rels/slide2.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slides/_rels/slide3.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slides/_rels/slide4.xml.rels
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slides/slide1.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slides/slide2.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slides/slide3.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/slides/slide4.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/tableStyles.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/theme/theme1.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/theme/theme2.xml
%{_datadir}/%pkg_name-%{version}/data/pptx/ppt/viewProps.xml
%{_datadir}/%pkg_name-%{version}/data/templates/affiliations.jats
%{_datadir}/%pkg_name-%{version}/data/templates/after-header-includes.latex
%{_datadir}/%pkg_name-%{version}/data/templates/article.jats_publishing
%{_datadir}/%pkg_name-%{version}/data/templates/common.latex
%{_datadir}/%pkg_name-%{version}/data/templates/default.ansi
%{_datadir}/%pkg_name-%{version}/data/templates/default.asciidoc
%{_datadir}/%pkg_name-%{version}/data/templates/default.bbcode
%{_datadir}/%pkg_name-%{version}/data/templates/default.beamer
%{_datadir}/%pkg_name-%{version}/data/templates/default.biblatex
%{_datadir}/%pkg_name-%{version}/data/templates/default.bibtex
%{_datadir}/%pkg_name-%{version}/data/templates/default.chunkedhtml
%{_datadir}/%pkg_name-%{version}/data/templates/default.commonmark
%{_datadir}/%pkg_name-%{version}/data/templates/default.context
%{_datadir}/%pkg_name-%{version}/data/templates/default.djot
%{_datadir}/%pkg_name-%{version}/data/templates/default.docbook4
%{_datadir}/%pkg_name-%{version}/data/templates/default.docbook5
%{_datadir}/%pkg_name-%{version}/data/templates/default.dokuwiki
%{_datadir}/%pkg_name-%{version}/data/templates/default.dzslides
%{_datadir}/%pkg_name-%{version}/data/templates/default.epub2
%{_datadir}/%pkg_name-%{version}/data/templates/default.epub3
%{_datadir}/%pkg_name-%{version}/data/templates/default.haddock
%{_datadir}/%pkg_name-%{version}/data/templates/default.html4
%{_datadir}/%pkg_name-%{version}/data/templates/default.html5
%{_datadir}/%pkg_name-%{version}/data/templates/default.icml
%{_datadir}/%pkg_name-%{version}/data/templates/default.jats_archiving
%{_datadir}/%pkg_name-%{version}/data/templates/default.jats_articleauthoring
%{_datadir}/%pkg_name-%{version}/data/templates/default.jats_publishing
%{_datadir}/%pkg_name-%{version}/data/templates/default.jira
%{_datadir}/%pkg_name-%{version}/data/templates/default.latex
%{_datadir}/%pkg_name-%{version}/data/templates/default.man
%{_datadir}/%pkg_name-%{version}/data/templates/default.markdown
%{_datadir}/%pkg_name-%{version}/data/templates/default.markua
%{_datadir}/%pkg_name-%{version}/data/templates/default.mediawiki
%{_datadir}/%pkg_name-%{version}/data/templates/default.ms
%{_datadir}/%pkg_name-%{version}/data/templates/default.muse
%{_datadir}/%pkg_name-%{version}/data/templates/default.opendocument
%{_datadir}/%pkg_name-%{version}/data/templates/default.openxml
%{_datadir}/%pkg_name-%{version}/data/templates/default.opml
%{_datadir}/%pkg_name-%{version}/data/templates/default.org
%{_datadir}/%pkg_name-%{version}/data/templates/default.plain
%{_datadir}/%pkg_name-%{version}/data/templates/default.revealjs
%{_datadir}/%pkg_name-%{version}/data/templates/default.rst
%{_datadir}/%pkg_name-%{version}/data/templates/default.rtf
%{_datadir}/%pkg_name-%{version}/data/templates/default.s5
%{_datadir}/%pkg_name-%{version}/data/templates/default.slideous
%{_datadir}/%pkg_name-%{version}/data/templates/default.slidy
%{_datadir}/%pkg_name-%{version}/data/templates/default.t2t
%{_datadir}/%pkg_name-%{version}/data/templates/default.tei
%{_datadir}/%pkg_name-%{version}/data/templates/default.texinfo
%{_datadir}/%pkg_name-%{version}/data/templates/default.textile
%{_datadir}/%pkg_name-%{version}/data/templates/default.typst
%{_datadir}/%pkg_name-%{version}/data/templates/default.vimdoc
%{_datadir}/%pkg_name-%{version}/data/templates/default.xwiki
%{_datadir}/%pkg_name-%{version}/data/templates/default.zimwiki
%{_datadir}/%pkg_name-%{version}/data/templates/document-metadata.latex
%{_datadir}/%pkg_name-%{version}/data/templates/font-settings.latex
%{_datadir}/%pkg_name-%{version}/data/templates/fonts.latex
%{_datadir}/%pkg_name-%{version}/data/templates/hypersetup.latex
%{_datadir}/%pkg_name-%{version}/data/templates/passoptions.latex
%{_datadir}/%pkg_name-%{version}/data/templates/styles.citations.html
%{_datadir}/%pkg_name-%{version}/data/templates/styles.html
%{_datadir}/%pkg_name-%{version}/data/templates/template.typst
%{_datadir}/%pkg_name-%{version}/data/translations/*.yaml

%files devel -f %{name}-devel.files
%doc AUTHORS.md README.md changelog.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license COPYING.md

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
