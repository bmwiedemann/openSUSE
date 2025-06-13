#
# spec file for package perl-Archive-Zip
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


%define cpan_name Archive-Zip
Name:           perl-Archive-Zip
Version:        1.680.0
Release:        0
# 1.68 -> normalize -> 1.680.0
%define cpan_version 1.68
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Provide an interface to ZIP archive files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.017
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Compress::Raw::Zlib) >= 2.017
Provides:       perl(Archive::Zip) = %{version}
Provides:       perl(Archive::Zip::Archive) = %{version}
Provides:       perl(Archive::Zip::BufferedFileHandle) = %{version}
Provides:       perl(Archive::Zip::DirectoryMember) = %{version}
Provides:       perl(Archive::Zip::FileMember) = %{version}
Provides:       perl(Archive::Zip::Member) = %{version}
Provides:       perl(Archive::Zip::MemberRead) = %{version}
Provides:       perl(Archive::Zip::MockFileHandle) = %{version}
Provides:       perl(Archive::Zip::NewFileMember) = %{version}
Provides:       perl(Archive::Zip::StringMember) = %{version}
Provides:       perl(Archive::Zip::Tree) = %{version}
Provides:       perl(Archive::Zip::ZipFileMember) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The Archive::Zip module allows a Perl program to create, manipulate, read,
and write Zip archive files.

Zip archives can be created, or you can read from existing zip files.

Once created, they can be written to files, streams, or strings. Members
can be added, removed, extracted, replaced, rearranged, and enumerated.
They can also be renamed or have their dates, comments, or other attributes
queried or modified. Their data can be compressed or uncompressed as
needed.

Members can be created from members in existing Zip files, or from existing
directories, files, or strings.

This module uses the Compress::Raw::Zlib library to read and write the
compressed streams inside the files.

One can use Archive::Zip::MemberRead to read the zip file archive members
as if they were files.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes examples README.md

%changelog
