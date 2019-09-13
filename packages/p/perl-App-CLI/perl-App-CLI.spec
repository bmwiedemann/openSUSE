#
# spec file for package perl-App-CLI
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


Name:           perl-App-CLI
Version:        0.50
Release:        0
%define cpan_name App-CLI
Summary:        Dispatcher module for command line interface programs
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PT/PTC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Pod::Simple::Text)
# Works also without this!
#BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::Pod)
Requires:       perl(Capture::Tiny)
Requires:       perl(Class::Load)
Requires:       perl(Locale::Maketext::Simple)
Requires:       perl(Pod::Simple::Text)
%{perl_requires}

%description
'App::CLI' dispatches CLI (command line interface) based commands into
command classes. It also supports subcommand and per-command options.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.md
%license LICENSE

%changelog
