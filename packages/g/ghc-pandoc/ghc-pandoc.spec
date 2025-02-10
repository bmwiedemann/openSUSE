#
# spec file for package ghc-pandoc
#
# Copyright (c) 2025 SUSE LLC
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
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        3.6.2
Release:        0
Summary:        Conversion between markup formats
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-Glob-prof
BuildRequires:  ghc-JuicyPixels-devel
BuildRequires:  ghc-JuicyPixels-prof
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-aeson-pretty-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-citeproc-devel
BuildRequires:  ghc-citeproc-prof
BuildRequires:  ghc-commonmark-devel
BuildRequires:  ghc-commonmark-extensions-devel
BuildRequires:  ghc-commonmark-extensions-prof
BuildRequires:  ghc-commonmark-pandoc-devel
BuildRequires:  ghc-commonmark-pandoc-prof
BuildRequires:  ghc-commonmark-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-connection-devel
BuildRequires:  ghc-crypton-connection-prof
BuildRequires:  ghc-crypton-devel
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-crypton-x509-system-devel
BuildRequires:  ghc-crypton-x509-system-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-djot-devel
BuildRequires:  ghc-djot-prof
BuildRequires:  ghc-doclayout-devel
BuildRequires:  ghc-doclayout-prof
BuildRequires:  ghc-doctemplates-devel
BuildRequires:  ghc-doctemplates-prof
BuildRequires:  ghc-emojis-devel
BuildRequires:  ghc-emojis-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-gridtables-devel
BuildRequires:  ghc-gridtables-prof
BuildRequires:  ghc-haddock-library-devel
BuildRequires:  ghc-haddock-library-prof
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-ipynb-devel
BuildRequires:  ghc-ipynb-prof
BuildRequires:  ghc-jira-wiki-markup-devel
BuildRequires:  ghc-jira-wiki-markup-prof
BuildRequires:  ghc-libyaml-devel
BuildRequires:  ghc-libyaml-prof
BuildRequires:  ghc-mime-types-devel
BuildRequires:  ghc-mime-types-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-pretty-show-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-skylighting-core-devel
BuildRequires:  ghc-skylighting-core-prof
BuildRequires:  ghc-skylighting-devel
BuildRequires:  ghc-skylighting-prof
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-tagsoup-devel
BuildRequires:  ghc-tagsoup-prof
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-texmath-devel
BuildRequires:  ghc-texmath-prof
BuildRequires:  ghc-text-conversions-devel
BuildRequires:  ghc-text-conversions-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-tls-prof
BuildRequires:  ghc-typst-devel
BuildRequires:  ghc-typst-prof
BuildRequires:  ghc-unicode-collation-devel
BuildRequires:  ghc-unicode-collation-prof
BuildRequires:  ghc-unicode-transforms-devel
BuildRequires:  ghc-unicode-transforms-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-conduit-prof
BuildRequires:  ghc-xml-devel
BuildRequires:  ghc-xml-prof
BuildRequires:  ghc-xml-types-devel
BuildRequires:  ghc-xml-types-prof
BuildRequires:  ghc-yaml-devel
BuildRequires:  ghc-yaml-prof
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  ghc-zip-archive-prof
BuildRequires:  ghc-zlib-devel
BuildRequires:  ghc-zlib-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-golden-prof
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tasty-quickcheck-prof
%endif

%description
Pandoc is a Haskell library for converting from one markup format to another.
The formats it can handle include

- light markup formats (many variants of Markdown, reStructuredText, AsciiDoc,
Org-mode, Muse, Textile, txt2tags, djot) - HTML formats (HTML 4 and 5) - Ebook
formats (EPUB v2 and v3, FB2) - Documentation formats (GNU TexInfo, Haddock) -
Roff formats (man, ms) - TeX formats (LaTeX, ConTeXt) - Typst - XML formats
(DocBook 4 and 5, JATS, TEI Simple, OpenDocument) - Outline formats (OPML) -
Bibliography formats (BibTeX, BibLaTeX, CSL JSON, CSL YAML, RIS) - Word
processor formats (Docx, RTF, ODT) - Interactive notebook formats (Jupyter
notebook ipynb) - Page layout formats (InDesign ICML) - Wiki markup formats
(MediaWiki, DokuWiki, TikiWiki, TWiki, Vimwiki, XWiki, ZimWiki, Jira wiki,
Creole) - Slide show formats (LaTeX Beamer, PowerPoint, Slidy, reveal.js,
Slideous, S5, DZSlides) - Data formats (CSV and TSV tables) - PDF (via external
programs such as pdflatex or wkhtmltopdf)

Pandoc can convert mathematical content in documents between TeX, MathML, Word
equations, roff eqn, typst, and plain text. It includes a powerful system for
automatic citations and bibliographies, and it can be customized extensively
using templates, filters, and custom readers and writers written in Lua.

For the pandoc command-line program, see the 'pandoc-cli' package.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%{pkg_name}-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%{pkg_name}-doc
This package provides the Haskell %{pkg_name} library documentation.

%package -n ghc-%{pkg_name}-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%{pkg_name}-devel = %{version}-%{release}
Supplements:    (ghc-%{pkg_name}-devel and ghc-prof)

%description -n ghc-%{pkg_name}-prof
This package provides the Haskell %{pkg_name} profiling library.

%prep
%autosetup -n %{pkg_name}-%{version}
cp -p %{SOURCE1} %{pkg_name}.cabal

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
%dir %{_datadir}/%{pkg_name}-%{version}
%dir %{_datadir}/%{pkg_name}-%{version}/citeproc
%dir %{_datadir}/%{pkg_name}-%{version}/citeproc/biblatex-localization
%dir %{_datadir}/%{pkg_name}-%{version}/data
%dir %{_datadir}/%{pkg_name}-%{version}/data/docx
%dir %{_datadir}/%{pkg_name}-%{version}/data/docx/_rels
%dir %{_datadir}/%{pkg_name}-%{version}/data/docx/docProps
%dir %{_datadir}/%{pkg_name}-%{version}/data/docx/word
%dir %{_datadir}/%{pkg_name}-%{version}/data/docx/word/_rels
%dir %{_datadir}/%{pkg_name}-%{version}/data/docx/word/theme
%dir %{_datadir}/%{pkg_name}-%{version}/data/dzslides
%dir %{_datadir}/%{pkg_name}-%{version}/data/odt
%dir %{_datadir}/%{pkg_name}-%{version}/data/odt/META-INF
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/_rels
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/docProps
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/_rels
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/notesMasters
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/notesMasters/_rels
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/notesSlides
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/notesSlides/_rels
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideMasters
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideMasters/_rels
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slides
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slides/_rels
%dir %{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/theme
%dir %{_datadir}/%{pkg_name}-%{version}/data/templates
%dir %{_datadir}/%{pkg_name}-%{version}/data/translations
%{_datadir}/%{pkg_name}-%{version}/COPYRIGHT
%{_datadir}/%{pkg_name}-%{version}/MANUAL.txt
%{_datadir}/%{pkg_name}-%{version}/citeproc/biblatex-localization/*.lbx.strings
%{_datadir}/%{pkg_name}-%{version}/data/abbreviations
%{_datadir}/%{pkg_name}-%{version}/data/bash_completion.tpl
%{_datadir}/%{pkg_name}-%{version}/data/creole.lua
%{_datadir}/%{pkg_name}-%{version}/data/default.csl
%{_datadir}/%{pkg_name}-%{version}/data/docbook-entities.txt
%{_datadir}/%{pkg_name}-%{version}/data/docx/?Content_Types?.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/_rels/.rels
%{_datadir}/%{pkg_name}-%{version}/data/docx/docProps/app.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/docProps/core.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/docProps/custom.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/_rels/document.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/_rels/footnotes.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/comments.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/document.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/fontTable.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/footnotes.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/numbering.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/settings.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/styles.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/theme/theme1.xml
%{_datadir}/%{pkg_name}-%{version}/data/docx/word/webSettings.xml
%{_datadir}/%{pkg_name}-%{version}/data/dzslides/template.html
%{_datadir}/%{pkg_name}-%{version}/data/epub.css
%{_datadir}/%{pkg_name}-%{version}/data/init.lua
%{_datadir}/%{pkg_name}-%{version}/data/odt/META-INF/manifest.xml
%{_datadir}/%{pkg_name}-%{version}/data/odt/content.xml
%{_datadir}/%{pkg_name}-%{version}/data/odt/manifest.rdf
%{_datadir}/%{pkg_name}-%{version}/data/odt/meta.xml
%{_datadir}/%{pkg_name}-%{version}/data/odt/mimetype
%{_datadir}/%{pkg_name}-%{version}/data/odt/styles.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/?Content_Types?.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/_rels/.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/docProps/app.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/docProps/core.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/_rels/presentation.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/notesMasters/_rels/notesMaster1.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/notesMasters/notesMaster1.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/notesSlides/_rels/notesSlide1.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/notesSlides/_rels/notesSlide2.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/notesSlides/notesSlide1.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/notesSlides/notesSlide2.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/presProps.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/presentation.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout1.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout10.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout11.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout2.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout3.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout4.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout5.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout6.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout7.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout8.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout9.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout1.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout10.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout11.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout2.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout3.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout4.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout5.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout6.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout7.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout8.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout9.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideMasters/_rels/slideMaster1.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slideMasters/slideMaster1.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slides/_rels/slide1.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slides/_rels/slide2.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slides/_rels/slide3.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slides/_rels/slide4.xml.rels
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slides/slide1.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slides/slide2.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slides/slide3.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/slides/slide4.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/tableStyles.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/theme/theme1.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/theme/theme2.xml
%{_datadir}/%{pkg_name}-%{version}/data/pptx/ppt/viewProps.xml
%{_datadir}/%{pkg_name}-%{version}/data/templates/affiliations.jats
%{_datadir}/%{pkg_name}-%{version}/data/templates/after-header-includes.latex
%{_datadir}/%{pkg_name}-%{version}/data/templates/article.jats_publishing
%{_datadir}/%{pkg_name}-%{version}/data/templates/common.latex
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.ansi
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.asciidoc
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.beamer
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.biblatex
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.bibtex
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.chunkedhtml
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.commonmark
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.context
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.djot
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.docbook4
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.docbook5
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.dokuwiki
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.dzslides
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.epub2
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.epub3
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.haddock
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.html4
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.html5
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.icml
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.jats_archiving
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.jats_articleauthoring
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.jats_publishing
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.jira
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.latex
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.man
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.markdown
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.markua
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.mediawiki
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.ms
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.muse
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.opendocument
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.openxml
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.opml
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.org
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.plain
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.revealjs
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.rst
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.rtf
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.s5
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.slideous
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.slidy
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.tei
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.texinfo
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.textile
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.typst
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.xwiki
%{_datadir}/%{pkg_name}-%{version}/data/templates/default.zimwiki
%{_datadir}/%{pkg_name}-%{version}/data/templates/font-settings.latex
%{_datadir}/%{pkg_name}-%{version}/data/templates/fonts.latex
%{_datadir}/%{pkg_name}-%{version}/data/templates/hypersetup.latex
%{_datadir}/%{pkg_name}-%{version}/data/templates/passoptions.latex
%{_datadir}/%{pkg_name}-%{version}/data/templates/styles.citations.html
%{_datadir}/%{pkg_name}-%{version}/data/templates/styles.html
%{_datadir}/%{pkg_name}-%{version}/data/templates/template.typst
%{_datadir}/%{pkg_name}-%{version}/data/translations/*.yaml

%files devel -f %{name}-devel.files
%doc AUTHORS.md README.md changelog.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license COPYING.md

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
