#
# spec file for package perl-Image-ExifTool
#
# Copyright (c) 2020 SUSE LLC
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
Version:        12.06
Release:        0
Summary:        Perl module to read and write meta information
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Languages/Perl
URL:            https://exiftool.sourceforge.io/
Source:         https://downloads.sf.net/exiftool/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
Requires:       perl(File::RandomAccess)
Conflicts:      exiftool < %{version}
BuildArch:      noarch
%{?perl_requires}

%description
ExifTool is a customisable set of Perl modules plus a full-featured
application for reading and writing meta information in a wide variety of
files, including the maker note information of many digital cameras by
various manufacturers such as Canon, Casio, FujiFilm, GE, HP, JVC/Victor,
Kodak, Leaf, Minolta/Konica-Minolta, Nikon, Olympus/Epson, Panasonic/Leica,
Pentax/Asahi, Reconyx, Ricoh, Samsung, Sanyo, Sigma/Foveon and Sony.

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

%package -n perl-File-RandomAccess
Summary:        Random access reads of sequential file or scalar
Group:          Development/Languages/Perl

%description -n perl-File-RandomAccess
Allows random access to sequential file by buffering the file if
necessary. Also allows access to data in memory to be accessed as
if it were a file.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} V=1

%check
make %{?_smp_mflags} V=1 test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files
%doc Changes README html
%doc config_files/
%exclude %{_bindir}/exiftool
%exclude %{_mandir}/man?/exiftool.?%{?ext_man}
%{perl_vendorlib}/Image/
%{_mandir}/man?/Image::ExifTool*

%files -n exiftool
%doc fmt_files/
%doc arg_files/
%{_bindir}/exiftool
%{_mandir}/man?/exiftool.?%{?ext_man}

%files -n perl-File-RandomAccess
%{perl_vendorlib}/File/
%{_mandir}/man?/File::RandomAccess*

%changelog
