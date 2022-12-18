#
# spec file for package gscan2pdf
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


Name:           gscan2pdf
Version:        2.13.1
Release:        0
Summary:        Easy scan to PDF
License:        GPL-3.0-only
URL:            https://sourceforge.net/projects/gscan2pdf/
Source0:        https://sourceforge.net/projects/gscan2pdf/files/gscan2pdf/%{version}/gscan2pdf-%{version}.tar.xz
Source1:        https://sourceforge.net/projects/gscan2pdf/files/gscan2pdf/%{version}/gscan2pdf-%{version}.tar.xz.asc
Source9:        gscan2pdf.keyring
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
Requires:       perl-base = %{perl_version}
Requires:       unpaper
Requires:       perl(Config::General)
Requires:       perl(Data::UUID)
Requires:       perl(Date::Calc)
Requires:       perl(Exception::Class)
Requires:       perl(Filesys::Df)
Requires:       perl(Glib)
Requires:       perl(GooCanvas2)
Requires:       perl(Gtk3)
Requires:       perl(Gtk3::ImageView)
Requires:       perl(Gtk3::SimpleList)
Requires:       perl(Image::Magick)
Requires:       perl(Image::Sane)
Requires:       perl(List::MoreUtils)
Requires:       perl(Locale::Language)
Requires:       perl(Locale::gettext)
Requires:       perl(Log::Log4perl)
Requires:       perl(PDF::Builder)
Requires:       perl(Proc::ProcessTable)
Requires:       perl(Readonly)
Requires:       perl(Set::IntSpan)
Requires:       perl(Try::Tiny)
Requires:       typelib(GooCanvas) = 2.0
%if 0%{?sle_version} >= 150200 && 0%{?is_opensuse} || 0%{?sle_version} >= 150200 || 0%{?suse_version} > 1500
Requires:       typelib(GdkPixdata) = 2.0
%endif
Requires:       djvulibre
Requires:       pdftk
Requires:       tiff
Recommends:     gocr
Recommends:     tesseract-ocr
BuildArch:      noarch
%{perl_requires}

%description
A GUI to ease the process of producing a multipage PDF from a scan.

Features:
 * Compatible with any SANE-capable scanner
 * Crop, threshold & clean up scan
 * Reorder pages via DND
 * Write multi-page scan to PDF, DjVu or TIFF
 * Write single scans to any format supported by ImageMagick
 * Ocropus & tesseract support
 * Place OCR output at boundary boxes supplied by Ocropus
 * Incorporate PDF metadata in filename

%lang_package

%prep
%autosetup

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install
%perl_process_packlist
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%files
%doc %{_datadir}/help/C/%{name}/
%license LICENCE
%{_bindir}/gscan2pdf
%{_datadir}/%{name}/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/net.sourceforge.gscan2pdf.appdata.xml
%{_datadir}/applications/net.sourceforge.gscan2pdf.desktop
%{_datadir}/pixmaps/gscan2pdf.svg
%{_mandir}/man1/gscan2pdf.1p%{?ext_man}
%{perl_vendorlib}/Gscan2pdf/

%files lang -f %{name}.lang

%changelog
