#
# spec file for package perl-Archive-Zip
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Archive-Zip
Version:        1.68
Release:        0
%define cpan_name Archive-Zip
Summary:        Provide an interface to ZIP archive files
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.017
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Compress::Raw::Zlib) >= 2.017
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README.md

%changelog
