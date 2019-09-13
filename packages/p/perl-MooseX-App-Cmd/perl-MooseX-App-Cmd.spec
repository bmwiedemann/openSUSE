#
# spec file for package perl-MooseX-App-Cmd
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-MooseX-App-Cmd
Version:        0.32
Release:        0
%define cpan_name MooseX-App-Cmd
Summary:        Mashes up MooseX::Getopt and App::Cmd
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-App-Cmd/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::Cmd) >= 0.321
BuildRequires:  perl(App::Cmd::Command)
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.091
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(YAML)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(App::Cmd) >= 0.321
Requires:       perl(App::Cmd::Command)
Requires:       perl(Getopt::Long::Descriptive) >= 0.091
Requires:       perl(Moose)
Requires:       perl(Moose::Object)
Requires:       perl(MooseX::Getopt)
Requires:       perl(MooseX::NonMoose)
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
This module marries App::Cmd with MooseX::Getopt.

Use it like App::Cmd advises (especially see App::Cmd::Tutorial), swapping
App::Cmd::Command for MooseX::App::Cmd::Command.

Then you can write your moose commands as Moose classes, with
MooseX::Getopt defining the options for you instead of 'opt_spec' returning
a Getopt::Long::Descriptive spec.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENSE README

%changelog
