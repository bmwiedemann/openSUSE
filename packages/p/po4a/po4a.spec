#
# spec file for package po4a
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           po4a
Version:        0.56
Release:        0
Summary:        Framework to translate documentation and other materials
License:        GPL-2.0
Group:          Development/Tools/Other
Url:            https://po4a.org/
Source:         https://github.com/mquinson/po4a/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt-tools
BuildRequires:  perl-Module-Build >= 0.40
BuildRequires:  perl-SGMLS >= 1.03ii
BuildRequires:  perl-Term-ReadKey
BuildRequires:  perl-Text-WrapI18N
BuildRequires:  perl-Unicode-LineBreak
BuildRequires:  perl-base
BuildRequires:  perl-gettext >= 1.01
BuildRequires:  perl-YAML-Tiny

# for test suite
BuildRequires:  docbook_4
BuildRequires:  iso_ent
BuildRequires:  opensp
BuildRequires:  perl-HTML-Parser

Requires:       %{name}-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}
%lang_package

%description
Po4a extracts the translatable material from its input in a PO file.
When the PO file is translated, it re-injects the translation in the structure of the document, and generates the translated document.
If a string is not translated (i.e. it was not translated or it is "fuzzy"
because the original document was updated), the original string is used.
This permits to provide always up-to-date documentation.

po4a supports currently the following formats:
  * manpages
  * POD
  * XML (generic, DocBook, XHTML, Dia, Guide, or WML)
  * SGML
  * TeX (generic, LaTeX, or Texinfo)
  * text (simple text files with some formatting, markdown, or AsciiDoc)
  * INI

%prep
%setup -q

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}
%find_lang %{name} --with-man --all-name
rm -f %{buildroot}%{perl_vendorarch}/auto/po4a/.packlist

%check
# requires texlive, which is too heavy for the package
rm t/19-tex.t

#run the tests
./Build test

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README* TODO
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/Locale/
%{perl_vendorlib}/Locale/Po4a
%{_mandir}/man[1357]/*

%files lang -f %{name}.lang
%defattr(-,root,root)
%dir %{_mandir}/ca
%dir %{_mandir}/pl
%dir %{_mandir}/pt
%dir %{_mandir}/uk
%dir %{_mandir}/zh_CHS

%changelog
