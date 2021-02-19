#
# spec file for package perl-MooseX-App
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


%define cpan_name MooseX-App
Name:           perl-MooseX-App
Version:        1.41
Release:        0
Summary:        Write user-friendly command line apps with even less suffering
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAROS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-UPSTREAM fixes https://bugzilla.opensuse.org/show_bug.cgi?id=1181616 and might get superseded by https://github.com/maros/MooseX-App/pull/64
Patch0:         0000_reproducible_bash_completion.patch
# PATCH-FIX-UPSTREAM fixes https://github.com/maros/MooseX-App/issues/62 and might get superseded by https://github.com/maros/MooseX-App/pull/66
Patch1:         0001_fix_testing_for_Moose_2.2014.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(List::Util) >= 1.44
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Moose) >= 2.00
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(Pod::Elemental)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Config::Any)
Requires:       perl(List::Util) >= 1.44
Requires:       perl(Module::Pluggable)
Requires:       perl(Moose) >= 2.00
Requires:       perl(MooseX::Types::Path::Class)
Requires:       perl(Pod::Elemental)
Requires:       perl(namespace::autoclean)
Recommends:     perl(File::HomeDir)
Recommends:     perl(IO::Interactive)
Recommends:     perl(Term::ReadKey)
Recommends:     perl(Text::WagnerFischer)
Recommends:     perl(Win32::Console::ANSI)
%{perl_requires}

%description
MooseX-App is a highly customisable helper to write user-friendly command
line applications without having to worry about most of the annoying things
usually involved. Just take any existing Moose class, add a single line
('use MooseX-App qw(PluginA PluginB ...);') and create one class for each
command in an underlying namespace. Options and positional parameters can
be defined as simple Moose accessors using the 'option' and 'parameter'
keywords respectively.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1
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
%doc Changes README.md TODO
%license LICENCE LICENSE

%changelog
