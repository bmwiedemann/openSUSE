#
# spec file for package perl-Font-TTF
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


%define cpan_name Font-TTF
Name:           perl-Font-TTF
Version:        1.60.0
Release:        0
# 1.06 -> normalize -> 1.60.0
%define cpan_version 1.06
#Upstream: Artistic-2.0
License:        Artistic-2.0 AND OFL-1.1
Summary:        TTF font support for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BH/BHALLISSY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::String)
Requires:       perl(IO::String)
Provides:       perl(Font::TTF) = %{version}
Provides:       perl(Font::TTF::AATKern)
Provides:       perl(Font::TTF::AATutils)
Provides:       perl(Font::TTF::Anchor)
Provides:       perl(Font::TTF::Bsln)
Provides:       perl(Font::TTF::Cmap)
Provides:       perl(Font::TTF::Coverage)
Provides:       perl(Font::TTF::Cvt_) = 0.0.100
Provides:       perl(Font::TTF::DSIG)
Provides:       perl(Font::TTF::Delta)
Provides:       perl(Font::TTF::Dumper)
Provides:       perl(Font::TTF::EBDT)
Provides:       perl(Font::TTF::EBLC)
Provides:       perl(Font::TTF::Fdsc)
Provides:       perl(Font::TTF::Feat)
Provides:       perl(Font::TTF::Features::Cvar)
Provides:       perl(Font::TTF::Features::Size)
Provides:       perl(Font::TTF::Features::Sset)
Provides:       perl(Font::TTF::Fmtx)
Provides:       perl(Font::TTF::Font) = 0.390.0
Provides:       perl(Font::TTF::Fpgm) = 0.0.100
Provides:       perl(Font::TTF::GDEF)
Provides:       perl(Font::TTF::GPOS)
Provides:       perl(Font::TTF::GSUB)
Provides:       perl(Font::TTF::Glat)
Provides:       perl(Font::TTF::Gloc)
Provides:       perl(Font::TTF::Glyf)
Provides:       perl(Font::TTF::Glyph)
Provides:       perl(Font::TTF::GrFeat)
Provides:       perl(Font::TTF::Hdmx)
Provides:       perl(Font::TTF::Head)
Provides:       perl(Font::TTF::Hhea)
Provides:       perl(Font::TTF::Hmtx)
Provides:       perl(Font::TTF::Kern)
Provides:       perl(Font::TTF::Kern::ClassArray)
Provides:       perl(Font::TTF::Kern::CompactClassArray)
Provides:       perl(Font::TTF::Kern::OrderedList)
Provides:       perl(Font::TTF::Kern::StateTable)
Provides:       perl(Font::TTF::Kern::Subtable)
Provides:       perl(Font::TTF::LTSH)
Provides:       perl(Font::TTF::Loca)
Provides:       perl(Font::TTF::Maxp)
Provides:       perl(Font::TTF::Mort)
Provides:       perl(Font::TTF::Mort::Chain)
Provides:       perl(Font::TTF::Mort::Contextual)
Provides:       perl(Font::TTF::Mort::Insertion)
Provides:       perl(Font::TTF::Mort::Ligature)
Provides:       perl(Font::TTF::Mort::Noncontextual)
Provides:       perl(Font::TTF::Mort::Rearrangement)
Provides:       perl(Font::TTF::Mort::Subtable)
Provides:       perl(Font::TTF::Name) = 1.100.0
Provides:       perl(Font::TTF::OS_2)
Provides:       perl(Font::TTF::OTTags)
Provides:       perl(Font::TTF::OldCmap)
Provides:       perl(Font::TTF::OldMort)
Provides:       perl(Font::TTF::PCLT)
Provides:       perl(Font::TTF::PSNames)
Provides:       perl(Font::TTF::Post) = 0.10.0
Provides:       perl(Font::TTF::Prep) = 0.0.100
Provides:       perl(Font::TTF::Prop)
Provides:       perl(Font::TTF::Segarr) = 0.0.100
Provides:       perl(Font::TTF::Silf)
Provides:       perl(Font::TTF::Sill)
Provides:       perl(Font::TTF::Table) = 0.0.100
Provides:       perl(Font::TTF::Ttc) = 0.0.100
Provides:       perl(Font::TTF::Ttopen)
Provides:       perl(Font::TTF::Utils) = 0.0.100
Provides:       perl(Font::TTF::Vhea)
Provides:       perl(Font::TTF::Vmtx)
Provides:       perl(Font::TTF::Win32)
Provides:       perl(Font::TTF::Woff)
Provides:       perl(Font::TTF::Woff::MetaData)
Provides:       perl(Font::TTF::Woff::PrivateData)
Provides:       perl(Font::TTF::XMLparse)
%undefine       __perllib_provides
%{perl_requires}

%description
This module allows you to do almost anything to a TrueType/OpenType Font
including modify and inspect nearly all tables.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTORS README.TXT TODO
%license LICENSE

%changelog
