#
# spec file for package perl-Task-Moose
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Task-Moose
Version:        0.03
Release:        0
%define cpan_name Task-Moose
Summary:        Moose in a box
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Task-Moose/
#Source:         http://www.cpan.org/authors/id/D/DO/DOY/Task-Moose-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
Patch0:         Task-Moose_fix_perl_5_26_INC_without_cwd.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 0.92
Requires:       perl(Moose) >= 0.92
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# Manual from the documentation
BuildRequires:  perl(Moose::Autobox)
BuildRequires:  perl(MooseX::App::Cmd)
BuildRequires:  perl(MooseX::ClassAttribute)
BuildRequires:  perl(MooseX::Clone)
BuildRequires:  perl(MooseX::ConfigFromFile)
BuildRequires:  perl(MooseX::Daemonize)
BuildRequires:  perl(MooseX::Declare)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::GlobRef)
BuildRequires:  perl(MooseX::InsideOut)
BuildRequires:  perl(MooseX::Iterator)
BuildRequires:  perl(MooseX::LazyLogDispatch)
BuildRequires:  perl(MooseX::Log::Log4perl)
BuildRequires:  perl(MooseX::LogDispatch)
BuildRequires:  perl(MooseX::Method::Signatures)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(MooseX::Object::Pluggable)
BuildRequires:  perl(MooseX::POE)
BuildRequires:  perl(MooseX::Param)
BuildRequires:  perl(MooseX::Params::Validate)
BuildRequires:  perl(MooseX::Role::Cmd)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(MooseX::Role::TraitConstructor)
BuildRequires:  perl(MooseX::SemiAffordanceAccessor)
BuildRequires:  perl(MooseX::SimpleConfig)
BuildRequires:  perl(MooseX::Singleton)
BuildRequires:  perl(MooseX::Storage)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(MooseX::Traits)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::DateTime)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(MooseX::Types::Set::Object)
BuildRequires:  perl(MooseX::Types::Structured)
BuildRequires:  perl(MooseX::Workers)
BuildRequires:  perl(Pod::Coverage::Moose)
BuildRequires:  perl(namespace::autoclean)
%{perl_requires}

%description
This Task installs Moose and then optionally installs a number of Moose
extensions listed below. This list is meant to be comprehensive, so if I
missed something please let me know.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p0

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
%defattr(644,root,root,755)
%doc Changes README

%changelog
