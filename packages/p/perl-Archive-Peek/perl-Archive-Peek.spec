#
# spec file for package perl-Archive-Peek
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


%define cpan_name Archive-Peek
Name:           perl-Archive-Peek
Version:        0.37
Release:        0
Summary:        Peek into archives without extracting them
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Z/ZM/ZMUGHAL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Types::Path::Tiny)
Requires:       perl(Archive::Tar)
Requires:       perl(Archive::Zip)
Requires:       perl(Moo)
Requires:       perl(Types::Path::Tiny)
%{perl_requires}

%description
This module lets you peek into archives without extracting them. It
currently supports tar files and zip files. To support Bzip2- compressed
files, you should install IO::Uncompress::Bunzip2.

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
%doc CHANGES README

%changelog
