#
# spec file for package perl-App-Cmd
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


%define cpan_name App-Cmd
Name:           perl-App-Cmd
Version:        0.335
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Write command line apps with less suffering
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.13
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Getopt::Long) >= 2.39
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.084
BuildRequires:  perl(IO::TieCombine)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Pod::Usage) >= 1.61
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(experimental)
BuildRequires:  perl(parent)
Requires:       perl(Capture::Tiny) >= 0.13
Requires:       perl(Class::Load) >= 0.06
Requires:       perl(Data::OptList)
Requires:       perl(Getopt::Long) >= 2.39
Requires:       perl(Getopt::Long::Descriptive) >= 0.084
Requires:       perl(IO::TieCombine)
Requires:       perl(Module::Pluggable::Object)
Requires:       perl(Pod::Usage) >= 1.61
Requires:       perl(String::RewritePrefix)
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::Util)
Requires:       perl(Sub::Install)
Requires:       perl(experimental)
Requires:       perl(parent)
%{perl_requires}

%description
App::Cmd is intended to make it easy to write complex command-line
applications without having to think about most of the annoying things
usually involved.

For information on how to start using App::Cmd, see App::Cmd::Tutorial.

%prep
%autosetup  -n %{cpan_name}-%{version}
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
%doc Changes README
%license LICENSE

%changelog
