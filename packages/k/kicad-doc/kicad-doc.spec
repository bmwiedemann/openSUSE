#
# spec file for package kicad-doc
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


%global flavor @BUILD_FLAVOR@%{nil}
%define sname kicad-doc

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%if "%flavor" == "pdf"
%define pkg_suffix -pdf
%bcond_without pdf
# Disabled, fails to build, asciidoc+dblatex no longer supported by upstream
# E.g. https://gitlab.com/kicad/services/kicad-doc/-/issues/808
ExclusiveArch:  do_not_build
%endif

%if "%flavor" == "html"
%bcond_with pdf
%endif

Name:           kicad-doc%{?pkg_suffix}
Version:        8.0.3
Release:        0
Summary:        Documentation and tutorials for KiCad
License:        CC-BY-SA-3.0 AND GPL-3.0-or-later
Group:          Documentation/HTML
URL:            https://www.kicad.org
Source:         https://gitlab.com/kicad/services/%{sname}/-/archive/%{version}/%{sname}-%{version}.tar.bz2#/%{sname}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE kicad-doc-notimestamp.patch davejplater@gmail.com -- Remove time stamped footer from html pages.
Patch0:         kicad-doc-notimestamp.patch
BuildRequires:  asciidoc >= 8.6.9
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gettext >= 0.18
BuildRequires:  libxslt-tools
BuildRequires:  po4a >= 0.45
BuildRequires:  source-highlight
BuildRequires:  perl(Unicode::LineBreak)
%if %{with pdf}
BuildRequires:  dblatex >= 0.3.4
BuildRequires:  texlive-babel-catalan
BuildRequires:  texlive-babel-dutch
BuildRequires:  texlive-babel-french
BuildRequires:  texlive-babel-german
BuildRequires:  texlive-babel-italian
BuildRequires:  texlive-babel-polish
BuildRequires:  texlive-babel-russian
BuildRequires:  texlive-babel-spanish
BuildRequires:  texlive-fandol
BuildRequires:  texlive-gnu-freefont
BuildRequires:  texlive-xetex
BuildRequires:  vlgothic-fonts
BuildRequires:  tex(8r.enc)
BuildRequires:  tex(bahasa.ldf)
BuildRequires:  tex(cmap.sty)
BuildRequires:  tex(eu1enc.def)
BuildRequires:  tex(fancybox.sty)
BuildRequires:  tex(japanese.ldf)
BuildRequires:  tex(mathptmx.sty)
BuildRequires:  tex(mathrsfs.sty)
BuildRequires:  tex(pcrr8t.tfm)
BuildRequires:  tex(phvb8t.tfm)
BuildRequires:  tex(psyr.tfm)
BuildRequires:  tex(ptmr8t.tfm)
BuildRequires:  tex(pzdr.tfm)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(xeCJK.sty)
BuildRequires:  tex(xltxtra.sty)
# kicad-doc owns the directories
BuildRequires:  kicad-doc
%endif
BuildArch:      noarch
Recommends:     kicad = %{version}

%description
Kicad is an open source software for the creation of electronic
schematic diagrams and printed circuit board artwork.
This is the documentation package for KiCad. It contains documentation
and tutorials.

%package        ca
Summary:        Catalan documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:ca)
Requires:       %{name}-en = %{version}

%description    ca
This package contains Catalan documentation and tutorials for KiCad

%package        de
Summary:        German documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:de)
Requires:       %{name}-en = %{version}

%description    de
This package contains German documentation and tutorials for KiCad

%package        en
Summary:        English documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:en)
Requires:       kicad = %{version}
Requires:       kicad-doc = %{version}

%description    en
This package contains English documentation and tutorials for KiCad

%package        es
Summary:        Spanish documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:es)
Requires:       %{name}-en = %{version}

%description    es
This package contains Spanish documentation and tutorials for KiCad

%package        fr
Summary:        French documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:fr)
Requires:       %{name}-en = %{version}

%description    fr
This package contains French documentation and tutorials for KiCad

%package        id
Summary:        Indonesian documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:id)
Requires:       %{name}-en = %{version}

%description    id
This package contains Indonesian documentation and tutorials for KiCad

%package        it
Summary:        Italian documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:it)
Requires:       %{name}-en = %{version}

%description    it
This package contains Italian documentation and tutorials for KiCad

%package        ja
Summary:        Japanese documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:ja)
Requires:       %{name}-en = %{version}

%description    ja
This package contains Japanese documentation and tutorials for KiCad

%package        pl
Summary:        Polish documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:pl)
Requires:       %{name}-en = %{version}

%description    pl
This package contains Polish documentation and tutorials for KiCad

%package        ru
Summary:        Russian documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:ru)
Requires:       %{name}-en = %{version}

%description    ru
This package contains Russian documentation and tutorials for KiCad

%package        zh
Summary:        Chinese documentation and tutorials for KiCad
Group:          Documentation/Other
Provides:       locale(%{name}:zh)
Requires:       %{name}-en = %{version}

%description    zh
This package contains Chinese documentation and tutorials for KiCad

%prep
%autosetup -p0 -n %{sname}-%{version}

# asciidoc errors out if the `[code]` style is used with an unknown language
# https://gitlab.com/kicad/services/kicad-doc/-/issues/851
find . -iname \*adoc -exec sed -i -e 's/\[code/\[source/' '{}' \;
# Fix incorrect column with specifiers
# https://gitlab.com/kicad/services/kicad-doc/-/issues/852
find . -iname \*adoc -exec sed -i -e '/\[.*cols=/ { :m s/\(cols=.*\)\([0-9]\)%/\1\2/g ; t m }' '{}' \;
# asciidoc interprets the '[--...]' on a new line as a style name
find . -iname cli.adoc -exec sed -i -e 's/^\[--/ \[--/' '{}' \;

# These files are actually GIFs, https://gitlab.com/kicad/services/kicad-doc/-/issues/822
mv src/gerbview/images/zh/gerbview_x2_attribute.{png,gif}
mv src/gerbview/images/zh/gerbview_x2_component.{png,gif}
mv src/gerbview/images/zh/gerbview_x2_net.{png,gif}

%if %{with pdf}
# Workaround for dblatex bug #117 - randomly selected warning symbol
cp /usr/share/dblatex/latex/graphics/warning.pdf CMakeSupport/
%endif

%build
# Supported output formats: html;pdf;epub;
%if %{with pdf}
# SOURCE_DATE_EPOCH affirmation variable used by TeX
export FORCE_SOURCE_DATE=1
# Do not build PL translations, bad interaction of po4a, asciidoc and xetex (gh#KiCad/kicad-doc#697)
# RU also fails, "Undefined control sequence \cyrchar."
%cmake -DKICAD_DOC_PATH=%{_docdir}/kicad/help -DADOC_TOOLCHAIN=asciidoc -DPDF_GENERATOR=dblatex -DBUILD_FORMATS='pdf;' -DLANGUAGES='ca;de;en;es;fr;id;it;ja;zh'
%else
%cmake -DKICAD_DOC_PATH=%{_docdir}/kicad/help -DADOC_TOOLCHAIN=asciidoc -DBUILD_FORMATS='html;'
%endif
%{make_jobs}

%install
%cmake_install

for lang in ca de en es fr id it ja pl ru zh ; do
    %fdupes %{buildroot}%{_docdir}/kicad/help/$lang
done

%if %{without pdf}
%files
%dir %{_docdir}/kicad/
%dir %{_docdir}/kicad/help/
%doc AUTHORS_README.adoc CHEATSHEET.adoc README.adoc
%license LICENSE.adoc
%endif

%files ca
%{_docdir}/kicad/help/ca/

%files de
%{_docdir}/kicad/help/de/

%files en
%{_docdir}/kicad/help/en/

%files es
%{_docdir}/kicad/help/es/

%files fr
%{_docdir}/kicad/help/fr/

%files id
%{_docdir}/kicad/help/id/

%files it
%{_docdir}/kicad/help/it/

%files ja
%{_docdir}/kicad/help/ja/

%if %{without pdf}
%files pl
%{_docdir}/kicad/help/pl/

%files ru
%{_docdir}/kicad/help/ru/
%endif

%files zh
%{_docdir}/kicad/help/zh/

%changelog
