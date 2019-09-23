#
# spec file for package perl-MooseX-Daemonize
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-Daemonize
Version:        0.21
Release:        0
%define cpan_name MooseX-Daemonize
Summary:        Role for daemonizing your Moose based application
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Daemonize/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::AssertOS)
BuildRequires:  perl(Devel::CheckOS) >= 1.63
BuildRequires:  perl(File::Path) >= 2.080000
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::Getopt::OptionTypeMap)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(File::Path) >= 2.080000
Requires:       perl(Moose)
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(MooseX::Getopt)
Requires:       perl(MooseX::Getopt::OptionTypeMap)
Requires:       perl(MooseX::Types::Path::Class)
Requires:       perl(Sub::Exporter)
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
Often you want to write a persistent daemon that has a pid file, and
responds appropriately to Signals. This module provides a set of basic
roles as an infrastructure to do that.

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
%doc Changes CONTRIBUTING examples IDEAS LICENCE README

%changelog
