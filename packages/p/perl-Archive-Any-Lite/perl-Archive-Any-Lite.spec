#
# spec file for package perl-Archive-Any-Lite
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Archive-Any-Lite
Name:           perl-Archive-Any-Lite
Version:        0.11
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple CPAN package extractor
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Tar) >= 1.76
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile) >= 0.07
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(Test::More) >= 0.82
BuildRequires:  perl(Test::UseAllModules) >= 0.10
Requires:       perl(Archive::Tar) >= 1.76
Requires:       perl(Archive::Zip)
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(IO::Uncompress::Bunzip2)
Requires:       perl(IO::Zlib)
%{perl_requires}

%description
This is a fork of Archive::Any by Michael Schwern and Clint Moore. The main
difference is this works properly even when you fork(), and may require
less memory to extract a tarball. On the other hand, this isn't pluggable
(this only supports file formats used in the CPAN toolchains), and this
doesn't check mime types (at least as of this writing).

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
