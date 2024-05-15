#
# spec file for package perl-MIME-tools
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


%define cpan_name MIME-tools
Name:           perl-MIME-tools
Version:        5.515.0
Release:        0
# 5.515 -> normalize -> 5.515.0
%define cpan_version 5.515
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tools to manipulate MIME messages
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSKOLL/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(File::Temp) >= 0.18
BuildRequires:  perl(Mail::Field) >= 1.05
BuildRequires:  perl(Mail::Header) >= 1.01
BuildRequires:  perl(Mail::Internet) >= 1.0203
BuildRequires:  perl(Test::Deep)
Requires:       perl(File::Temp) >= 0.18
Requires:       perl(Mail::Field) >= 1.05
Requires:       perl(Mail::Header) >= 1.01
Requires:       perl(Mail::Internet) >= 1.0203
Provides:       perl(MIME::Body) = %{version}
Provides:       perl(MIME::Body::File)
Provides:       perl(MIME::Body::InCore)
Provides:       perl(MIME::Body::Scalar)
Provides:       perl(MIME::Decoder) = %{version}
Provides:       perl(MIME::Decoder::Base64) = %{version}
Provides:       perl(MIME::Decoder::BinHex) = %{version}
Provides:       perl(MIME::Decoder::Binary) = %{version}
Provides:       perl(MIME::Decoder::Gzip64) = %{version}
Provides:       perl(MIME::Decoder::NBit) = %{version}
Provides:       perl(MIME::Decoder::QuotedPrint) = %{version}
Provides:       perl(MIME::Decoder::UU) = %{version}
Provides:       perl(MIME::Entity) = %{version}
Provides:       perl(MIME::Field::ConTraEnc) = %{version}
Provides:       perl(MIME::Field::ContDisp) = %{version}
Provides:       perl(MIME::Field::ContType) = %{version}
Provides:       perl(MIME::Field::ParamVal) = %{version}
Provides:       perl(MIME::Head) = %{version}
Provides:       perl(MIME::Parser) = %{version}
Provides:       perl(MIME::Parser::FileInto)
Provides:       perl(MIME::Parser::FileUnder)
Provides:       perl(MIME::Parser::Filer)
Provides:       perl(MIME::Parser::Reader)
Provides:       perl(MIME::Parser::Results)
Provides:       perl(MIME::Tools) = %{version}
Provides:       perl(MIME::WordDecoder)
Provides:       perl(MIME::WordDecoder::ISO_8859)
Provides:       perl(MIME::WordDecoder::US_ASCII)
Provides:       perl(MIME::WordDecoder::UTF_8)
Provides:       perl(MIME::Words) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Convert::BinHex)
%{perl_requires}

%description
Tools to manipulate MIME messages

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog examples README
%license COPYING

%changelog
