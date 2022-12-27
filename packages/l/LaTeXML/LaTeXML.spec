#
# spec file for package LaTeXML
#
# Copyright (c) 2022 SUSE LLC
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


Name:           LaTeXML
Version:        0.8.7
Release:        1%{?dist}
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Utilities
Summary:        TeX and LaTeX to XML translator
URL:            http://dlmf.nist.gov/LaTeXML/
Source:         https://math.nist.gov/~BMiller/LaTeXML/releases/%{name}-%{version}.tar.gz
BuildArch:      noarch
%define perl_modules perl(Archive::Zip) perl(DB_File) perl(File::Which) perl(Getopt::Long) perl(IO::String) perl(Image::Size) perl(JSON::XS) perl(LWP::Protocol::https) perl(Parse::RecDescent) perl(Text::Unidecode) perl(Test::Simple) perl(Time::HiRes) perl(URI) perl(XML::LibXML) perl(XML::LibXSLT) perl(Pod::Find) perl(UUID::Tiny)
BuildRequires:  %perl_modules
BuildRequires:  perl
BuildRequires:  perl-macros
Requires:       %perl_modules
Requires:       perl(%{name})
%{perl_requires}
Recommends:     ImageMagick
Recommends:     texlive

%description
LaTeXML is a TeX & LaTeX to XML, HTML, MathML, ePub, JATS, ... converter.

%package -n perl-%{name}
Summary:        Perl files for %{name}
Requires:       %perl_modules
%{perl_requires}

%description -n perl-%{name}
Perl files for %{name}

%prep
%setup -q

%build
sed -i 's@\#\!/usr/bin/env perl@\#\!/usr/bin/perl@' bin/*
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist

%check
make test %{?_smp_mflags}

%files
%defattr(-,root,root)
%{_bindir}/latexml
%{_bindir}/latexmlc
%{_bindir}/latexmlfind
%{_bindir}/latexmlmath
%{_bindir}/latexmlpost
%{_mandir}/man1/*

%files -n perl-%{name}
%{_mandir}/man3/%{name}*
%{perl_vendorlib}/*

%changelog
