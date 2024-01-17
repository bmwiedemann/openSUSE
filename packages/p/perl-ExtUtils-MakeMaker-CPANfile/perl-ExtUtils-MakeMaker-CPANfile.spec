#
# spec file for package perl-ExtUtils-MakeMaker-CPANfile
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-ExtUtils-MakeMaker-CPANfile
Version:        0.09
Release:        0
%define cpan_name ExtUtils-MakeMaker-CPANfile
Summary:        Cpanfile Support for Eumm
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Converter) >= 2.141170
BuildRequires:  perl(Module::CPANfile)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.76
Requires:       perl(CPAN::Meta::Converter) >= 2.141170
Requires:       perl(Module::CPANfile)
Requires:       perl(Test::More) >= 0.88
Requires:       perl(version) >= 0.76
%{perl_requires}

%description
ExtUtils::MakeMaker::CPANfile loads 'cpanfile' in your distribution and
modifies parameters for 'WriteMakefile' in your Makefile.PL. Just use it
instead of ExtUtils::MakeMaker (which should be loaded internally), and
prepare 'cpanfile'.

As of version 0.03, ExtUtils::MakeMaker::CPANfile also removes
WriteMakefile parameters that the installed version of ExtUtils::MakeMaker
doesn't know, to avoid warnings.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README.md
%license LICENSE

%changelog
