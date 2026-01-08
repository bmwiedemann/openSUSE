#
# spec file for package perl-PDF-Builder
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name PDF-Builder
Name:           perl-PDF-Builder
Version:        3.28.0
Release:        0
# 3.028 -> normalize -> 3.28.0
%define cpan_version 3.028
License:        LGPL-2.1-or-later
Summary:        Facilitates the creation and modification of PDF files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMPERRY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Zlib) >= 1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.66
BuildRequires:  perl(Font::TTF) >= 1.40
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle) >= 1
Requires:       perl(Compress::Zlib) >= 1
Requires:       perl(Font::TTF) >= 1.40
Provides:       perl(PDF::Builder) = %{version}
Provides:       perl(PDF::Builder::Annotation) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Array) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Bool) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Dict) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::File) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Filter) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Filter::ASCII85Decode) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Filter::ASCIIHexDecode) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Filter::FlateDecode) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Filter::LZWDecode) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Filter::RunLengthDecode) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Literal) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Name) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Null) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Number) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Objind) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Page) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Pages) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::String) = %{version}
Provides:       perl(PDF::Builder::Basic::PDF::Utils) = %{version}
Provides:       perl(PDF::Builder::Content) = %{version}
Provides:       perl(PDF::Builder::Content::Column_docs) = %{version}
Provides:       perl(PDF::Builder::Content::Hyphenate_basic) = %{version}
Provides:       perl(PDF::Builder::Content::Text) = %{version}
Provides:       perl(PDF::Builder::Docs) = %{version}
Provides:       perl(PDF::Builder::FontManager) = %{version}
Provides:       perl(PDF::Builder::Lite) = %{version}
Provides:       perl(PDF::Builder::Matrix) = %{version}
Provides:       perl(PDF::Builder::NamedDestination) = %{version}
Provides:       perl(PDF::Builder::Outline) = %{version}
Provides:       perl(PDF::Builder::Outlines) = %{version}
Provides:       perl(PDF::Builder::Page) = %{version}
Provides:       perl(PDF::Builder::Resource) = %{version}
Provides:       perl(PDF::Builder::Resource::BaseFont) = %{version}
Provides:       perl(PDF::Builder::Resource::CIDFont) = %{version}
Provides:       perl(PDF::Builder::Resource::CIDFont::CJKFont) = %{version}
Provides:       perl(PDF::Builder::Resource::CIDFont::TrueType) = %{version}
Provides:       perl(PDF::Builder::Resource::CIDFont::TrueType::FontFile) = %{version}
Provides:       perl(PDF::Builder::Resource::ColorSpace) = %{version}
Provides:       perl(PDF::Builder::Resource::ColorSpace::DeviceN) = %{version}
Provides:       perl(PDF::Builder::Resource::ColorSpace::Indexed) = %{version}
Provides:       perl(PDF::Builder::Resource::ColorSpace::Indexed::ACTFile) = %{version}
Provides:       perl(PDF::Builder::Resource::ColorSpace::Indexed::Hue) = %{version}
Provides:       perl(PDF::Builder::Resource::ColorSpace::Indexed::WebColor) = %{version}
Provides:       perl(PDF::Builder::Resource::ColorSpace::Separation) = %{version}
Provides:       perl(PDF::Builder::Resource::Colors) = %{version}
Provides:       perl(PDF::Builder::Resource::ExtGState) = %{version}
Provides:       perl(PDF::Builder::Resource::Font) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::BdFont) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::bankgothic) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::courier) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::courierbold) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::courierboldoblique) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::courieroblique) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::georgia) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::georgiabold) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::georgiabolditalic) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::georgiaitalic) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::helvetica) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::helveticabold) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::helveticaboldoblique) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::helveticaoblique) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::symbol) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::timesbold) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::timesbolditalic) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::timesitalic) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::timesroman) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::trebuchet) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::trebuchetbold) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::trebuchetbolditalic) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::trebuchetitalic) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::verdana) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::verdanabold) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::verdanabolditalic) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::verdanaitalic) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::webdings) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::wingdings) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::CoreFont::zapfdingbats) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::Postscript) = %{version}
Provides:       perl(PDF::Builder::Resource::Font::SynFont) = %{version}
Provides:       perl(PDF::Builder::Resource::Glyphs) = %{version}
Provides:       perl(PDF::Builder::Resource::PaperSizes) = %{version}
Provides:       perl(PDF::Builder::Resource::Pattern) = %{version}
Provides:       perl(PDF::Builder::Resource::Shading) = %{version}
Provides:       perl(PDF::Builder::Resource::UniFont) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Form) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Form::BarCode) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Form::BarCode::codabar) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Form::BarCode::code128) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Form::BarCode::code3of9) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Form::BarCode::ean13) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Form::BarCode::int2of5) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Form::Hybrid) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::GD) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::GIF) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::JPEG) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::PNG) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::PNG_IPL) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::PNM) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::SVG) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::TIFF) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::TIFF::File) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::TIFF::File_GT) = %{version}
Provides:       perl(PDF::Builder::Resource::XObject::Image::TIFF_GT) = %{version}
Provides:       perl(PDF::Builder::UniWrap) = %{version}
Provides:       perl(PDF::Builder::Util) = %{version}
Provides:       perl(PDF::Builder::ViewerPreferences) = %{version}
Provides:       perl(PDF::Builder::Win32) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Facilitates the creation and modification of PDF files

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CONTRIBUTING.md docs examples README.md SECURITY.md
%license LICENSE

%changelog
