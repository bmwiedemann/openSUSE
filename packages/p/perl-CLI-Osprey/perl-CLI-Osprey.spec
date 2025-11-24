#
# spec file for package perl-CLI-Osprey
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name CLI-Osprey
Name:           perl-CLI-Osprey
Version:        0.90.0
Release:        0
# 0.09 -> normalize -> 0.90.0
%define cpan_version 0.09
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        MooX::Options + MooX::Cmd + Sanity
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.100
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.34
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Lib)
BuildRequires:  perl(Test::More) >= 1
Requires:       perl(Getopt::Long::Descriptive) >= 0.100
Requires:       perl(Module::Runtime)
Requires:       perl(Moo)
Requires:       perl(Moo::Role)
Requires:       perl(Path::Tiny)
Provides:       perl(CLI::Osprey) = %{version}
Provides:       perl(CLI::Osprey::Descriptive) = %{version}
Provides:       perl(CLI::Osprey::Descriptive::Usage) = %{version}
Provides:       perl(CLI::Osprey::InlineSubcommand) = %{version}
Provides:       perl(CLI::Osprey::Role) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
CLI::Osprey is a module to assist in writing commandline applications with
M* OO modules (Moose, Moo, Mo). With it, you structure your app as one or
more modules, which get instantiated with the commandline arguments as
attributes. Arguments are parsed using Getopt::Long::Descriptive, and both
long and short help messages as well as complete manual pages are
automatically generated. An app can be a single command with options, or
have sub-commands (like 'git'). Sub-commands can be defined as modules
(with options of their own) or as simple coderefs.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
