#
# spec file for package perl-PDF-API2
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


%define cpan_name PDF-API2
Name:           perl-PDF-API2
Version:        2.47.0
Release:        0
# 2.047 -> normalize -> 2.47.0
%define cpan_version 2.047
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
Provides:       perl(PDF::API2::Annotation) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Array) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Bool) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Dict) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::File) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Filter) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Filter::ASCII85Decode) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Filter::ASCIIHexDecode) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Filter::FlateDecode) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Filter::LZWDecode) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Filter::RunLengthDecode) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Literal) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Name) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Null) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Number) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Objind) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Page) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Pages) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::String) = %{version}
Provides:       perl(PDF::API2::Basic::PDF::Utils) = %{version}
Provides:       perl(PDF::API2::Content) = %{version}
Provides:       perl(PDF::API2::Content::Text) = %{version}
Provides:       perl(PDF::API2::Lite) = %{version}
Provides:       perl(PDF::API2::Matrix) = %{version}
Provides:       perl(PDF::API2::NamedDestination) = %{version}
Provides:       perl(PDF::API2::Outline) = %{version}
Provides:       perl(PDF::API2::Outlines) = %{version}
Provides:       perl(PDF::API2::Page) = %{version}
Provides:       perl(PDF::API2::Resource) = %{version}
Provides:       perl(PDF::API2::Resource::BaseFont) = %{version}
Provides:       perl(PDF::API2::Resource::CIDFont) = %{version}
Provides:       perl(PDF::API2::Resource::CIDFont::CJKFont) = %{version}
Provides:       perl(PDF::API2::Resource::CIDFont::TrueType) = %{version}
Provides:       perl(PDF::API2::Resource::CIDFont::TrueType::FontFile) = %{version}
Provides:       perl(PDF::API2::Resource::ColorSpace) = %{version}
Provides:       perl(PDF::API2::Resource::ColorSpace::DeviceN) = %{version}
Provides:       perl(PDF::API2::Resource::ColorSpace::Indexed) = %{version}
Provides:       perl(PDF::API2::Resource::ColorSpace::Indexed::ACTFile) = %{version}
Provides:       perl(PDF::API2::Resource::ColorSpace::Indexed::Hue) = %{version}
Provides:       perl(PDF::API2::Resource::ColorSpace::Indexed::WebColor) = %{version}
Provides:       perl(PDF::API2::Resource::ColorSpace::Separation) = %{version}
Provides:       perl(PDF::API2::Resource::Colors) = %{version}
Provides:       perl(PDF::API2::Resource::ExtGState) = %{version}
Provides:       perl(PDF::API2::Resource::Font) = %{version}
Provides:       perl(PDF::API2::Resource::Font::BdFont) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::bankgothic) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::courier) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::courierbold) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::courierboldoblique) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::courieroblique) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::georgia) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::georgiabold) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::georgiabolditalic) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::georgiaitalic) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::helvetica) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::helveticabold) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::helveticaboldoblique) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::helveticaoblique) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::symbol) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::timesbold) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::timesbolditalic) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::timesitalic) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::timesroman) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::trebuchet) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::trebuchetbold) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::trebuchetbolditalic) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::trebuchetitalic) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::verdana) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::verdanabold) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::verdanabolditalic) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::verdanaitalic) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::webdings) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::wingdings) = %{version}
Provides:       perl(PDF::API2::Resource::Font::CoreFont::zapfdingbats) = %{version}
Provides:       perl(PDF::API2::Resource::Font::Postscript) = %{version}
Provides:       perl(PDF::API2::Resource::Font::SynFont) = %{version}
Provides:       perl(PDF::API2::Resource::Glyphs) = %{version}
Provides:       perl(PDF::API2::Resource::PaperSizes) = %{version}
Provides:       perl(PDF::API2::Resource::Pattern) = %{version}
Provides:       perl(PDF::API2::Resource::Shading) = %{version}
Provides:       perl(PDF::API2::Resource::UniFont) = %{version}
Provides:       perl(PDF::API2::Resource::XObject) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Form) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::codabar) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::code128) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::code3of9) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::ean13) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::int2of5) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Form::BarCode::qrcode) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Form::Hybrid) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Image) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Image::GD) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Image::GIF) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Image::JPEG) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Image::PNG) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Image::PNM) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Image::TIFF) = %{version}
Provides:       perl(PDF::API2::Resource::XObject::Image::TIFF::File) = %{version}
Provides:       perl(PDF::API2::UniWrap) = %{version}
Provides:       perl(PDF::API2::Util) = %{version}
Provides:       perl(PDF::API2::ViewerPreferences) = %{version}
Provides:       perl(PDF::API2::Win32) = %{version}
%undefine       __perllib_provides
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
