#
# spec file for package po4a
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


Name:           po4a
Version:        0.73
Release:        0
Summary:        Framework to translate documentation and other materials
License:        GPL-2.0-only
%if "%{_vendor}" == "debbuild"
Group:          text
%else
Group:          Development/Tools/Other
%endif
URL:            https://po4a.org/
Source:         https://github.com/mquinson/po4a/releases/download/v%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Workaround for build error with perl 5.40, see https://github.com/mquinson/po4a/issues/508
Patch0:         po4a.diff

%if "%{_vendor}" == "debbuild"
BuildRequires:  deb-perl-macros
BuildRequires:  docbook
BuildRequires:  docbook-xml
BuildRequires:  docbook-xsl
BuildRequires:  gettext
BuildRequires:  libmodule-build-perl
BuildRequires:  libpod-parser-perl
BuildRequires:  libsgmls-perl
BuildRequires:  libterm-readkey-perl
BuildRequires:  libunicode-linebreak-perl
BuildRequires:  libyaml-tiny-perl
BuildRequires:  perl
BuildRequires:  texlive-binaries
BuildRequires:  texlive-latex-base
BuildRequires:  xsltproc

%else
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt-tools
BuildRequires:  perl-Module-Build >= 0.40
BuildRequires:  perl-SGMLS >= 1.03ii
BuildRequires:  perl-Term-ReadKey
BuildRequires:  perl-Test-Pod
BuildRequires:  perl-Text-WrapI18N
BuildRequires:  perl-Unicode-LineBreak
BuildRequires:  perl-YAML-Tiny
BuildRequires:  perl-base
BuildRequires:  perl-gettext >= 1.01
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Syntax::Keyword::Try)
# for test suite
BuildRequires:  docbook_4
BuildRequires:  iso_ent
%endif
BuildRequires:  opensp

%{perl_requires}
%if "%{_vendor}" == "debbuild"
#Requires:       ${misc:Depends}
Requires:       gettext
Requires:       libpod-parser-perl
Requires:       libsgmls-perl
Requires:       libyaml-tiny-perl
Requires:       opensp
Recommends:     liblocale-gettext-perl
Recommends:     libterm-readkey-perl
Recommends:     libtext-wrapi18n-perl
Recommends:     libunicode-linebreak-perl
%else
Requires:       gettext-tools
Requires:       perl-SGMLS
Requires:       perl-YAML-Tiny
Requires:       perl(Pod::Parser)
Requires:       perl(Syntax::Keyword::Try)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%lang_package
%endif

%description
Po4a extracts the translatable material from its input in a PO file.
When the PO file is translated, it re-injects the translation in the structure of the document,
and generates the translated document.
If a string is not translated (i.e. it was not translated or it is "fuzzy"
because the original document was updated), the original string is used.
This permits to provide always up-to-date documentation.

po4a supports currently the following formats:
  * manpages
  * POD
  * XML (generic, DocBook, XHTML, Dia, Guide, or WML)
  * SGML
  * TeX (generic, LaTeX, BibTex or Texinfo)
  * text (simple text files with some formatting, markdown, rubydoc or AsciiDoc)
  * INI
  * YAML
  * KernelHelp

%prep
%setup -q
%patch -P0

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%find_lang %{name} --with-man --all-name

%check
# requires texlive, which is too heavy for the package
rm -rf t/fmt-tex.t t/fmt/tex

#run the tests
./Build test

%files
%defattr(644,root,root,755)
%doc NEWS README* TODO
%license COPYING
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/Locale/
%{perl_vendorlib}/Locale/Po4a
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%files lang -f %{name}.lang
%defattr(-,root,root)
%dir %{_mandir}/ca
%dir %{_mandir}/de
%dir %{_mandir}/es
%dir %{_mandir}/fr
%dir %{_mandir}/it
%dir %{_mandir}/ja
%dir %{_mandir}/nb
%dir %{_mandir}/nl
%dir %{_mandir}/pl
%dir %{_mandir}/pt
%dir %{_mandir}/pt_BR
%dir %{_mandir}/ru
%dir %{_mandir}/sr_Cyrl
%dir %{_mandir}/uk
%dir %{_mandir}/zh_Hant

%changelog
