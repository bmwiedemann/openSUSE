#
# spec file for package perl-Getopt-Long-Descriptive
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Getopt-Long-Descriptive
Version:        0.104
Release:        0
%define cpan_name Getopt-Long-Descriptive
Summary:        Getopt::Long, but simpler and more powerful
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Params::Validate) >= 0.97
BuildRequires:  perl(Sub::Exporter) >= 0.972
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.005
Requires:       perl(Params::Validate) >= 0.97
Requires:       perl(Sub::Exporter) >= 0.972
Requires:       perl(Sub::Exporter::Util)
%{perl_requires}

%description
Getopt::Long::Descriptive is yet another Getopt library. It's built atop
Getopt::Long, and gets a lot of its features, but tries to avoid making you
think about its huge array of options.

It also provides usage (help) messages, data validation, and a few other
useful features.

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
%doc Changes README
%license LICENSE

%changelog
