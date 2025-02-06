#
# spec file for package perl-libintl-perl
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


%define cpan_name libintl-perl
Name:           perl-libintl-perl
Version:        1.350.0
Release:        0
# 1.35 -> normalize -> 1.350.0
%define cpan_version 1.35
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        GPL-3.0-or-later
Summary:        High-Level Interface to Uniforum Message Translation
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUIDO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        libintl-perl-rpmlintrc
Source2:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(version) >= 0.77
Requires:       perl(version) >= 0.77
Provides:       perl(Locale::Messages) = %{version}
Provides:       perl(Locale::Recode)
Provides:       perl(Locale::Recode::_Aliases)
Provides:       perl(Locale::Recode::_Conversions)
Provides:       perl(Locale::RecodeData)
Provides:       perl(Locale::RecodeData::ASMO_449)
Provides:       perl(Locale::RecodeData::ATARI_ST)
Provides:       perl(Locale::RecodeData::ATARI_ST_EURO)
Provides:       perl(Locale::RecodeData::CP10007)
Provides:       perl(Locale::RecodeData::CP1250)
Provides:       perl(Locale::RecodeData::CP1251)
Provides:       perl(Locale::RecodeData::CP1252)
Provides:       perl(Locale::RecodeData::CP1253)
Provides:       perl(Locale::RecodeData::CP1254)
Provides:       perl(Locale::RecodeData::CP1256)
Provides:       perl(Locale::RecodeData::CP1257)
Provides:       perl(Locale::RecodeData::CSN_369103)
Provides:       perl(Locale::RecodeData::CWI)
Provides:       perl(Locale::RecodeData::DEC_MCS)
Provides:       perl(Locale::RecodeData::EBCDIC_AT_DE)
Provides:       perl(Locale::RecodeData::EBCDIC_AT_DE_A)
Provides:       perl(Locale::RecodeData::EBCDIC_CA_FR)
Provides:       perl(Locale::RecodeData::EBCDIC_DK_NO)
Provides:       perl(Locale::RecodeData::EBCDIC_DK_NO_A)
Provides:       perl(Locale::RecodeData::EBCDIC_ES)
Provides:       perl(Locale::RecodeData::EBCDIC_ES_A)
Provides:       perl(Locale::RecodeData::EBCDIC_ES_S)
Provides:       perl(Locale::RecodeData::EBCDIC_FI_SE)
Provides:       perl(Locale::RecodeData::EBCDIC_FI_SE_A)
Provides:       perl(Locale::RecodeData::EBCDIC_FR)
Provides:       perl(Locale::RecodeData::EBCDIC_IS_FRISS)
Provides:       perl(Locale::RecodeData::EBCDIC_IT)
Provides:       perl(Locale::RecodeData::EBCDIC_PT)
Provides:       perl(Locale::RecodeData::EBCDIC_UK)
Provides:       perl(Locale::RecodeData::EBCDIC_US)
Provides:       perl(Locale::RecodeData::ECMA_CYRILLIC)
Provides:       perl(Locale::RecodeData::GEORGIAN_ACADEMY)
Provides:       perl(Locale::RecodeData::GEORGIAN_PS)
Provides:       perl(Locale::RecodeData::GOST_19768_74)
Provides:       perl(Locale::RecodeData::GREEK7)
Provides:       perl(Locale::RecodeData::GREEK7_OLD)
Provides:       perl(Locale::RecodeData::GREEK_CCITT)
Provides:       perl(Locale::RecodeData::HP_ROMAN8)
Provides:       perl(Locale::RecodeData::IBM037)
Provides:       perl(Locale::RecodeData::IBM038)
Provides:       perl(Locale::RecodeData::IBM1004)
Provides:       perl(Locale::RecodeData::IBM1026)
Provides:       perl(Locale::RecodeData::IBM1047)
Provides:       perl(Locale::RecodeData::IBM256)
Provides:       perl(Locale::RecodeData::IBM273)
Provides:       perl(Locale::RecodeData::IBM274)
Provides:       perl(Locale::RecodeData::IBM275)
Provides:       perl(Locale::RecodeData::IBM277)
Provides:       perl(Locale::RecodeData::IBM278)
Provides:       perl(Locale::RecodeData::IBM280)
Provides:       perl(Locale::RecodeData::IBM281)
Provides:       perl(Locale::RecodeData::IBM284)
Provides:       perl(Locale::RecodeData::IBM285)
Provides:       perl(Locale::RecodeData::IBM290)
Provides:       perl(Locale::RecodeData::IBM297)
Provides:       perl(Locale::RecodeData::IBM420)
Provides:       perl(Locale::RecodeData::IBM423)
Provides:       perl(Locale::RecodeData::IBM424)
Provides:       perl(Locale::RecodeData::IBM437)
Provides:       perl(Locale::RecodeData::IBM500)
Provides:       perl(Locale::RecodeData::IBM850)
Provides:       perl(Locale::RecodeData::IBM851)
Provides:       perl(Locale::RecodeData::IBM852)
Provides:       perl(Locale::RecodeData::IBM855)
Provides:       perl(Locale::RecodeData::IBM857)
Provides:       perl(Locale::RecodeData::IBM860)
Provides:       perl(Locale::RecodeData::IBM861)
Provides:       perl(Locale::RecodeData::IBM862)
Provides:       perl(Locale::RecodeData::IBM863)
Provides:       perl(Locale::RecodeData::IBM864)
Provides:       perl(Locale::RecodeData::IBM865)
Provides:       perl(Locale::RecodeData::IBM866)
Provides:       perl(Locale::RecodeData::IBM868)
Provides:       perl(Locale::RecodeData::IBM869)
Provides:       perl(Locale::RecodeData::IBM870)
Provides:       perl(Locale::RecodeData::IBM871)
Provides:       perl(Locale::RecodeData::IBM874)
Provides:       perl(Locale::RecodeData::IBM875)
Provides:       perl(Locale::RecodeData::IBM880)
Provides:       perl(Locale::RecodeData::IBM891)
Provides:       perl(Locale::RecodeData::IBM903)
Provides:       perl(Locale::RecodeData::IBM904)
Provides:       perl(Locale::RecodeData::IBM905)
Provides:       perl(Locale::RecodeData::IBM918)
Provides:       perl(Locale::RecodeData::IEC_P27_1)
Provides:       perl(Locale::RecodeData::INIS)
Provides:       perl(Locale::RecodeData::INIS_8)
Provides:       perl(Locale::RecodeData::INIS_CYRILLIC)
Provides:       perl(Locale::RecodeData::ISO_10367_BOX)
Provides:       perl(Locale::RecodeData::ISO_2033_1983)
Provides:       perl(Locale::RecodeData::ISO_5427)
Provides:       perl(Locale::RecodeData::ISO_5427_EXT)
Provides:       perl(Locale::RecodeData::ISO_5428)
Provides:       perl(Locale::RecodeData::ISO_8859_1)
Provides:       perl(Locale::RecodeData::ISO_8859_10)
Provides:       perl(Locale::RecodeData::ISO_8859_11)
Provides:       perl(Locale::RecodeData::ISO_8859_13)
Provides:       perl(Locale::RecodeData::ISO_8859_14)
Provides:       perl(Locale::RecodeData::ISO_8859_15)
Provides:       perl(Locale::RecodeData::ISO_8859_16)
Provides:       perl(Locale::RecodeData::ISO_8859_2)
Provides:       perl(Locale::RecodeData::ISO_8859_3)
Provides:       perl(Locale::RecodeData::ISO_8859_4)
Provides:       perl(Locale::RecodeData::ISO_8859_5)
Provides:       perl(Locale::RecodeData::ISO_8859_6)
Provides:       perl(Locale::RecodeData::ISO_8859_7)
Provides:       perl(Locale::RecodeData::ISO_8859_8)
Provides:       perl(Locale::RecodeData::ISO_8859_9)
Provides:       perl(Locale::RecodeData::KOI8_R)
Provides:       perl(Locale::RecodeData::KOI8_RU)
Provides:       perl(Locale::RecodeData::KOI8_T)
Provides:       perl(Locale::RecodeData::KOI8_U)
Provides:       perl(Locale::RecodeData::KOI_8)
Provides:       perl(Locale::RecodeData::LATIN_GREEK)
Provides:       perl(Locale::RecodeData::LATIN_GREEK_1)
Provides:       perl(Locale::RecodeData::MACARABIC)
Provides:       perl(Locale::RecodeData::MACCROATIAN)
Provides:       perl(Locale::RecodeData::MACCYRILLIC)
Provides:       perl(Locale::RecodeData::MACGREEK)
Provides:       perl(Locale::RecodeData::MACHEBREW)
Provides:       perl(Locale::RecodeData::MACICELAND)
Provides:       perl(Locale::RecodeData::MACINTOSH)
Provides:       perl(Locale::RecodeData::MACROMANIA)
Provides:       perl(Locale::RecodeData::MACTHAI)
Provides:       perl(Locale::RecodeData::MACTURKISH)
Provides:       perl(Locale::RecodeData::MACUKRAINE)
Provides:       perl(Locale::RecodeData::MAC_IS)
Provides:       perl(Locale::RecodeData::MAC_SAMI)
Provides:       perl(Locale::RecodeData::MAC_UK)
Provides:       perl(Locale::RecodeData::NATS_DANO)
Provides:       perl(Locale::RecodeData::NATS_SEFI)
Provides:       perl(Locale::RecodeData::NEXTSTEP)
Provides:       perl(Locale::RecodeData::SAMI_WS2)
Provides:       perl(Locale::RecodeData::TIS_620)
Provides:       perl(Locale::RecodeData::US_ASCII)
Provides:       perl(Locale::RecodeData::UTF_8)
Provides:       perl(Locale::RecodeData::VISCII)
Provides:       perl(Locale::RecodeData::_Encode)
Provides:       perl(Locale::TextDomain) = %{version}
Provides:       perl(Locale::Util)
Provides:       perl(Locale::gettext_dumb)
Provides:       perl(Locale::gettext_pp)
Provides:       perl(MyInstall)
Provides:       perl(__TiedTextDomain)
%undefine       __perllib_provides
Recommends:     perl(File::ShareDir)
%{perl_requires}
# MANUAL BEGIN
Requires:       gettext-runtime >= 0.12.2
# MANUAL END

%description
This is an internationalization library for Perl that aims to be
compatible with the Uniforum message translations system as implemented
for example in GNU gettext.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Credits FAQ NEWS README README.md README-oldversions README.solaris README.win32 REFERENCES THANKS TODO
%license COPYING

%changelog
