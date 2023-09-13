#
# spec file for package perl-CPAN-Mini
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


%define cpan_name CPAN-Mini
Name:           perl-CPAN-Mini
Version:        1.111017
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Create a minimal mirror of CPAN
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Zlib) >= 1.20
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(File::HomeDir) >= 0.57
BuildRequires:  perl(File::Path) >= 2.04
BuildRequires:  perl(LWP::UserAgent) >= 5
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(URI) >= 1
Requires:       perl(Compress::Zlib) >= 1.20
Requires:       perl(File::HomeDir) >= 0.57
Requires:       perl(File::Path) >= 2.04
Requires:       perl(LWP::UserAgent) >= 5
Requires:       perl(URI) >= 1
%{perl_requires}

%description
CPAN::Mini provides a simple mechanism to build and update a minimal mirror
of the CPAN on your local disk. It contains only those files needed to
install the newest version of every distribution. Those files are:

  * 01mailrc.txt.gz

  * 02packages.details.txt.gz

  * 03modlist.data.gz

  * the last non-developer release of every dist for every author

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
