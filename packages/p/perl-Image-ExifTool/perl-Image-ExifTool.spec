#
# spec file for package perl-Image-ExifTool
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


%define cpan_name Image-ExifTool

Name:           perl-Image-ExifTool
Version:        12.52
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Read and write meta information
URL:            https://metacpan.org/release/%{cpan_name}
# use non-release build because of CVE-2022-23935
#Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXIFTOOL/%%{cpan_name}-%%{version}.tar.gz
Source0:        https://exiftool.org/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Recommends:     perl(Archive::Zip)
Recommends:     perl(Compress::Zlib)
Recommends:     perl(Digest::SHA)
Recommends:     perl(IO::Compress::RawDeflate)
Recommends:     perl(IO::Uncompress::RawInflate)
Recommends:     perl(POSIX::strptime)
%{perl_requires}
# MANUAL BEGIN
Requires:       perl(File::RandomAccess) >= 1.11
# MANUAL END

%description
Reads and writes meta information in a wide variety of files, including the
maker notes of many digital cameras by various manufacturers such as Canon,
Casio, DJI, FLIR, FujiFilm, GE, GoPro, HP, JVC/Victor, Kodak, Leaf,
Minolta/Konica-Minolta, Nikon, Nintendo, Olympus/Epson, Panasonic/Leica,
Pentax/Asahi, Phase One, Reconyx, Ricoh, Samsung, Sanyo, Sigma/Foveon and
Sony.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes config_files html README
%exclude %{_bindir}/exiftool
%exclude %{_mandir}/man?/exiftool.?%{?ext_man}
%exclude %{perl_vendorlib}/File/
%exclude %{_mandir}/man?/File::RandomAccess*

%package -n exiftool
Summary:        Customisable application to read and write meta information in files
Group:          Productivity/Graphics/Other
Requires:       perl(Image::ExifTool) = %{version}
Recommends:     perl(Archive::Zip)
# Per https://perldoc.perl.org/index-modules-I.html, these are the part of perl-base.
#Recommends:     perl(Compress::Zlib)
#Recommends:     perl(Digest::MD5)
#Recommends:     perl(Digest::SHA)
#Recommends:     perl(IO::Compress::Bzip2)
#Recommends:     perl(Time::HiRes)

%description -n exiftool
ExifTool is a a full-featured application for reading and writing
meta information in a wide variety of files, including the maker
note information of many digital cameras by various manufacturers
such as Canon, Casio, FujiFilm, GE, HP, JVC/Victor, Kodak, Leaf,
Minolta/Konica-Minolta, Nikon, Olympus/Epson, Panasonic/Leica,
Pentax/Asahi, Reconyx, Ricoh, Samsung, Sanyo, Sigma/Foveon and Sony.

%files -n exiftool
%doc fmt_files/
%doc arg_files/
%{_bindir}/exiftool
%{_mandir}/man?/exiftool.?%{?ext_man}

%package -n perl-File-RandomAccess
Summary:        Random access reads of sequential file or scalar
Group:          Development/Languages/Perl

%description -n perl-File-RandomAccess
Allows random access to sequential file by buffering the file if
necessary. Also allows access to data in memory to be accessed as
if it were a file.

%files -n perl-File-RandomAccess
%{perl_vendorlib}/File/
%{_mandir}/man?/File::RandomAccess*

%changelog
