#
# spec file for package perl-PDF-API2
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


%define cpan_name PDF-API2
Name:           perl-PDF-API2
Version:        2.45.0
Release:        0
%define cpan_version 2.045
License:        LGPL-2.1-or-later
Summary:        Create, modify, and examine PDF files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SS/SSIMMS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Zlib) >= 1.0
BuildRequires:  perl(Font::TTF)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle)
Requires:       perl(Compress::Zlib) >= 1.0
Requires:       perl(Font::TTF)
Provides:       perl(PDF::API2)
Provides:       perl(PDF::API2::Annotation) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Array) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Bool) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Dict) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::File) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Filter) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Filter::ASCII85Decode) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Filter::ASCIIHexDecode) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Filter::FlateDecode) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Filter::LZWDecode) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Filter::RunLengthDecode) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Literal) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Name) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Null) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Number) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Objind) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Page) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Pages) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::String) = 2.45.0
Provides:       perl(PDF::API2::Basic::PDF::Utils) = 2.45.0
Provides:       perl(PDF::API2::Content) = 2.45.0
Provides:       perl(PDF::API2::Content::Text) = 2.45.0
Provides:       perl(PDF::API2::Lite) = 2.45.0
Provides:       perl(PDF::API2::Matrix) = 2.45.0
Provides:       perl(PDF::API2::NamedDestination) = 2.45.0
Provides:       perl(PDF::API2::Outline) = 2.45.0
Provides:       perl(PDF::API2::Outlines) = 2.45.0
Provides:       perl(PDF::API2::Page) = 2.45.0
Provides:       perl(PDF::API2::Resource) = 2.45.0
Provides:       perl(PDF::API2::Resource::BaseFont) = 2.45.0
Provides:       perl(PDF::API2::Resource::CIDFont) = 2.45.0
Provides:       perl(PDF::API2::Resource::CIDFont::CJKFont) = 2.45.0
Provides:       perl(PDF::API2::Resource::CIDFont::TrueType) = 2.45.0
Provides:       perl(PDF::API2::Resource::CIDFont::TrueType::FontFile) = 2.45.0
Provides:       perl(PDF::API2::Resource::ColorSpace) = 2.45.0
Provides:       perl(PDF::API2::Resource::ColorSpace::DeviceN) = 2.45.0
Provides:       perl(PDF::API2::Resource::ColorSpace::Indexed) = 2.45.0
Provides:       perl(PDF::API2::Resource::ColorSpace::Indexed::ACTFile) = 2.45.0
Provides:       perl(PDF::API2::Resource::ColorSpace::Indexed::Hue) = 2.45.0
Provides:       perl(PDF::API2::Resource::ColorSpace::Indexed::WebColor) = 2.45.0
Provides:       perl(PDF::API2::Resource::ColorSpace::Separation) = 2.45.0
Provides:       perl(PDF::API2::Resource::Colors) = 2.45.0
Provides:       perl(PDF::API2::Resource::ExtGState) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::BdFont) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::bankgothic) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::courier) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::courierbold) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::courierboldoblique) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::courieroblique) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::georgia) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::georgiabold) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::georgiabolditalic) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::georgiaitalic) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::helvetica) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::helveticabold) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::helveticaboldoblique) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::helveticaoblique) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::symbol) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::timesbold) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::timesbolditalic) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::timesitalic) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::timesroman) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::trebuchet) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::trebuchetbold) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::trebuchetbolditalic) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::trebuchetitalic) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::verdana) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::verdanabold) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::verdanabolditalic) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::verdanaitalic) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::webdings) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::wingdings) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::CoreFont::zapfdingbats) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::Postscript) = 2.45.0
Provides:       perl(PDF::API2::Resource::Font::SynFont) = 2.45.0
Provides:       perl(PDF::API2::Resource::Glyphs) = 2.45.0
Provides:       perl(PDF::API2::Resource::PaperSizes) = 2.45.0
Provides:       perl(PDF::API2::Resource::Pattern) = 2.45.0
Provides:       perl(PDF::API2::Resource::Shading) = 2.45.0
Provides:       perl(PDF::API2::Resource::UniFont) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Form) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::codabar) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::code128) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::code3of9) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::ean13) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::int2of5) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::qrcode) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Form::Hybrid) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Image) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Image::GD) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Image::GIF) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Image::JPEG) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Image::PNG) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Image::PNM) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Image::TIFF) = 2.45.0
Provides:       perl(PDF::API2::Resource::XObject::Image::TIFF::File) = 2.45.0
Provides:       perl(PDF::API2::UniWrap) = 2.45.0
Provides:       perl(PDF::API2::Util) = 2.45.0
Provides:       perl(PDF::API2::ViewerPreferences) = 2.45.0
Provides:       perl(PDF::API2::Win32) = 2.45.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
Create, modify, and examine PDF files

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes PATENTS README
%license LICENSE

%changelog
