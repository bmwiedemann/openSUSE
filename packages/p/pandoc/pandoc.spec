#
# spec file for package pandoc
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


%global pkg_name pandoc
%bcond_with tests
Name:           %{pkg_name}
Version:        2.19.2
Release:        0
Summary:        Conversion between markup formats
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-JuicyPixels-devel
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base64-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-citeproc-devel
BuildRequires:  ghc-commonmark-devel
BuildRequires:  ghc-commonmark-extensions-devel
BuildRequires:  ghc-commonmark-pandoc-devel
BuildRequires:  ghc-connection-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-doclayout-devel
BuildRequires:  ghc-doctemplates-devel
BuildRequires:  ghc-emojis-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-gridtables-devel
BuildRequires:  ghc-haddock-library-devel
BuildRequires:  ghc-hslua-aeson-devel
BuildRequires:  ghc-hslua-devel
BuildRequires:  ghc-hslua-module-doclayout-devel
BuildRequires:  ghc-hslua-module-path-devel
BuildRequires:  ghc-hslua-module-system-devel
BuildRequires:  ghc-hslua-module-text-devel
BuildRequires:  ghc-hslua-module-version-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-ipynb-devel
BuildRequires:  ghc-jira-wiki-markup-devel
BuildRequires:  ghc-lpeg-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-pandoc-lua-marshal-devel
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-servant-server-devel
BuildRequires:  ghc-skylighting-core-devel
BuildRequires:  ghc-skylighting-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-tagsoup-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-texmath-devel
BuildRequires:  ghc-text-conversions-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unicode-collation-devel
BuildRequires:  ghc-unicode-transforms-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-devel
BuildRequires:  ghc-xml-types-devel
BuildRequires:  ghc-yaml-devel
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  ghc-zlib-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-lua-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
Pandoc is a Haskell library for converting from one markup format to another,
and a command-line tool that uses this library. The formats it can handle
include

- light markup formats (many variants of Markdown, reStructuredText, AsciiDoc,
Org-mode, Muse, Textile, txt2tags) - HTML formats (HTML 4 and 5) - Ebook
formats (EPUB v2 and v3, FB2) - Documentation formats (GNU TexInfo, Haddock) -
Roff formats (man, ms) - TeX formats (LaTeX, ConTeXt) - XML formats (DocBook 4
and 5, JATS, TEI Simple, OpenDocument) - Outline formats (OPML) - Bibliography
formats (BibTeX, BibLaTeX, CSL JSON, CSL YAML, RIS) - Word processor formats
(Docx, RTF, ODT) - Interactive notebook formats (Jupyter notebook ipynb) - Page
layout formats (InDesign ICML) - Wiki markup formats (MediaWiki, DokuWiki,
TikiWiki, TWiki, Vimwiki, XWiki, ZimWiki, Jira wiki, Creole) - Slide show
formats (LaTeX Beamer, PowerPoint, Slidy, reveal.js, Slideous, S5, DZSlides) -
Data formats (CSV and TSV tables) - PDF (via external programs such as pdflatex
or wkhtmltopdf)

Pandoc can convert mathematical content in documents between TeX, MathML, Word
equations, roff eqn, and plain text. It includes a powerful system for
automatic citations and bibliographies, and it can be customized extensively
using templates, filters, and custom readers and writers written in Lua.

%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%prep
%autosetup

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}
# Link duplicate template files
%fdupes %{buildroot}%{_datadir}/%{pkg_name}-%{version}/data/templates/

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license COPYING.md
%doc AUTHORS.md README.md changelog.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/citeproc
%dir %{_datadir}/%{name}-%{version}/citeproc/biblatex-localization
%dir %{_datadir}/%{name}-%{version}/data
%dir %{_datadir}/%{name}-%{version}/data/docx
%dir %{_datadir}/%{name}-%{version}/data/docx/_rels
%dir %{_datadir}/%{name}-%{version}/data/docx/docProps
%dir %{_datadir}/%{name}-%{version}/data/docx/word
%dir %{_datadir}/%{name}-%{version}/data/docx/word/_rels
%dir %{_datadir}/%{name}-%{version}/data/docx/word/theme
%dir %{_datadir}/%{name}-%{version}/data/dzslides
%dir %{_datadir}/%{name}-%{version}/data/odt
%dir %{_datadir}/%{name}-%{version}/data/odt/Configurations2
%dir %{_datadir}/%{name}-%{version}/data/odt/Configurations2/accelerator
%dir %{_datadir}/%{name}-%{version}/data/odt/META-INF
%dir %{_datadir}/%{name}-%{version}/data/odt/Thumbnails
%dir %{_datadir}/%{name}-%{version}/data/pptx
%dir %{_datadir}/%{name}-%{version}/data/pptx/_rels
%dir %{_datadir}/%{name}-%{version}/data/pptx/docProps
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/_rels
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/notesMasters
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/notesMasters/_rels
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/notesSlides
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/notesSlides/_rels
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/slideMasters
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/slideMasters/_rels
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/slides
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/slides/_rels
%dir %{_datadir}/%{name}-%{version}/data/pptx/ppt/theme
%dir %{_datadir}/%{name}-%{version}/data/templates
%dir %{_datadir}/%{name}-%{version}/data/translations
%{_datadir}/%{name}-%{version}/COPYRIGHT
%{_datadir}/%{name}-%{version}/MANUAL.txt
%{_datadir}/%{name}-%{version}/citeproc/biblatex-localization/*.lbx.strings
%{_datadir}/%{name}-%{version}/data/abbreviations
%{_datadir}/%{name}-%{version}/data/bash_completion.tpl
%{_datadir}/%{name}-%{version}/data/creole.lua
%{_datadir}/%{name}-%{version}/data/default.csl
%{_datadir}/%{name}-%{version}/data/docbook-entities.txt
%{_datadir}/%{name}-%{version}/data/docx/?Content_Types?.xml
%{_datadir}/%{name}-%{version}/data/docx/_rels/.rels
%{_datadir}/%{name}-%{version}/data/docx/docProps/app.xml
%{_datadir}/%{name}-%{version}/data/docx/docProps/core.xml
%{_datadir}/%{name}-%{version}/data/docx/docProps/custom.xml
%{_datadir}/%{name}-%{version}/data/docx/word/_rels/document.xml.rels
%{_datadir}/%{name}-%{version}/data/docx/word/_rels/footnotes.xml.rels
%{_datadir}/%{name}-%{version}/data/docx/word/comments.xml
%{_datadir}/%{name}-%{version}/data/docx/word/document.xml
%{_datadir}/%{name}-%{version}/data/docx/word/fontTable.xml
%{_datadir}/%{name}-%{version}/data/docx/word/footnotes.xml
%{_datadir}/%{name}-%{version}/data/docx/word/numbering.xml
%{_datadir}/%{name}-%{version}/data/docx/word/settings.xml
%{_datadir}/%{name}-%{version}/data/docx/word/styles.xml
%{_datadir}/%{name}-%{version}/data/docx/word/theme/theme1.xml
%{_datadir}/%{name}-%{version}/data/docx/word/webSettings.xml
%{_datadir}/%{name}-%{version}/data/dzslides/template.html
%{_datadir}/%{name}-%{version}/data/epub.css
%{_datadir}/%{name}-%{version}/data/init.lua
%{_datadir}/%{name}-%{version}/data/odt/Configurations2/accelerator/current.xml
%{_datadir}/%{name}-%{version}/data/odt/META-INF/manifest.xml
%{_datadir}/%{name}-%{version}/data/odt/Thumbnails/thumbnail.png
%{_datadir}/%{name}-%{version}/data/odt/content.xml
%{_datadir}/%{name}-%{version}/data/odt/manifest.rdf
%{_datadir}/%{name}-%{version}/data/odt/meta.xml
%{_datadir}/%{name}-%{version}/data/odt/mimetype
%{_datadir}/%{name}-%{version}/data/odt/settings.xml
%{_datadir}/%{name}-%{version}/data/odt/styles.xml
%{_datadir}/%{name}-%{version}/data/pptx/?Content_Types?.xml
%{_datadir}/%{name}-%{version}/data/pptx/_rels/.rels
%{_datadir}/%{name}-%{version}/data/pptx/docProps/app.xml
%{_datadir}/%{name}-%{version}/data/pptx/docProps/core.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/_rels/presentation.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/notesMasters/_rels/notesMaster1.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/notesMasters/notesMaster1.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/notesSlides/_rels/notesSlide1.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/notesSlides/_rels/notesSlide2.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/notesSlides/notesSlide1.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/notesSlides/notesSlide2.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/presProps.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/presentation.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout1.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout10.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout11.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout2.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout3.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout4.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout5.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout6.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout7.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout8.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/_rels/slideLayout9.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout1.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout10.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout11.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout2.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout3.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout4.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout5.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout6.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout7.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout8.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideLayouts/slideLayout9.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideMasters/_rels/slideMaster1.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slideMasters/slideMaster1.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slides/_rels/slide1.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slides/_rels/slide2.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slides/_rels/slide3.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slides/_rels/slide4.xml.rels
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slides/slide1.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slides/slide2.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slides/slide3.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/slides/slide4.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/tableStyles.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/theme/theme1.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/theme/theme2.xml
%{_datadir}/%{name}-%{version}/data/pptx/ppt/viewProps.xml
%{_datadir}/%{name}-%{version}/data/sample.lua
%{_datadir}/%{name}-%{version}/data/templates/affiliations.jats
%{_datadir}/%{name}-%{version}/data/templates/article.jats_publishing
%{_datadir}/%{name}-%{version}/data/templates/default.asciidoc
%{_datadir}/%{name}-%{version}/data/templates/default.asciidoctor
%{_datadir}/%{name}-%{version}/data/templates/default.biblatex
%{_datadir}/%{name}-%{version}/data/templates/default.bibtex
%{_datadir}/%{name}-%{version}/data/templates/default.commonmark
%{_datadir}/%{name}-%{version}/data/templates/default.context
%{_datadir}/%{name}-%{version}/data/templates/default.docbook4
%{_datadir}/%{name}-%{version}/data/templates/default.docbook5
%{_datadir}/%{name}-%{version}/data/templates/default.dokuwiki
%{_datadir}/%{name}-%{version}/data/templates/default.dzslides
%{_datadir}/%{name}-%{version}/data/templates/default.epub2
%{_datadir}/%{name}-%{version}/data/templates/default.epub3
%{_datadir}/%{name}-%{version}/data/templates/default.haddock
%{_datadir}/%{name}-%{version}/data/templates/default.html4
%{_datadir}/%{name}-%{version}/data/templates/default.html5
%{_datadir}/%{name}-%{version}/data/templates/default.icml
%{_datadir}/%{name}-%{version}/data/templates/default.jats_archiving
%{_datadir}/%{name}-%{version}/data/templates/default.jats_articleauthoring
%{_datadir}/%{name}-%{version}/data/templates/default.jats_publishing
%{_datadir}/%{name}-%{version}/data/templates/default.jira
%{_datadir}/%{name}-%{version}/data/templates/default.latex
%{_datadir}/%{name}-%{version}/data/templates/default.man
%{_datadir}/%{name}-%{version}/data/templates/default.markdown
%{_datadir}/%{name}-%{version}/data/templates/default.markua
%{_datadir}/%{name}-%{version}/data/templates/default.mediawiki
%{_datadir}/%{name}-%{version}/data/templates/default.ms
%{_datadir}/%{name}-%{version}/data/templates/default.muse
%{_datadir}/%{name}-%{version}/data/templates/default.opendocument
%{_datadir}/%{name}-%{version}/data/templates/default.opml
%{_datadir}/%{name}-%{version}/data/templates/default.org
%{_datadir}/%{name}-%{version}/data/templates/default.plain
%{_datadir}/%{name}-%{version}/data/templates/default.revealjs
%{_datadir}/%{name}-%{version}/data/templates/default.rst
%{_datadir}/%{name}-%{version}/data/templates/default.rtf
%{_datadir}/%{name}-%{version}/data/templates/default.s5
%{_datadir}/%{name}-%{version}/data/templates/default.slideous
%{_datadir}/%{name}-%{version}/data/templates/default.slidy
%{_datadir}/%{name}-%{version}/data/templates/default.tei
%{_datadir}/%{name}-%{version}/data/templates/default.texinfo
%{_datadir}/%{name}-%{version}/data/templates/default.textile
%{_datadir}/%{name}-%{version}/data/templates/default.xwiki
%{_datadir}/%{name}-%{version}/data/templates/default.zimwiki
%{_datadir}/%{name}-%{version}/data/templates/styles.html
%{_datadir}/%{name}-%{version}/data/translations/*.yaml

%files -n ghc-%{name} -f ghc-%{name}.files
%license COPYING.md

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc AUTHORS.md README.md changelog.md

%changelog
