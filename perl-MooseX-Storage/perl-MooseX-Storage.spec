#
# spec file for package perl-MooseX-Storage
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


Name:           perl-MooseX-Storage
Version:        0.52
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0+
%define cpan_name MooseX-Storage
Summary:        Serialization Framework for Moose Classes
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Storage/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(IO::AtomicFile)
BuildRequires:  perl(JSON::MaybeXS) >= 1.001000
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.99
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Deep::Type)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(YAML::Any)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(IO::AtomicFile)
Requires:       perl(JSON::MaybeXS) >= 1.001000
Requires:       perl(Module::Runtime)
Requires:       perl(Moose) >= 0.99
Requires:       perl(Moose::Meta::Attribute)
Requires:       perl(Moose::Role)
Requires:       perl(String::RewritePrefix)
Requires:       perl(YAML::Any)
Requires:       perl(namespace::autoclean)
Recommends:     perl(IO::AtomicFile)
Recommends:     perl(JSON::MaybeXS) >= 1.001000
Recommends:     perl(MooseX::Storage::Format::JSONpm)
Recommends:     perl(YAML)
Recommends:     perl(YAML::Any)
Recommends:     perl(YAML::Syck)
Recommends:     perl(YAML::XS)
%{perl_requires}

%description
MooseX::Storage is a serialization framework for Moose, it provides a very
flexible and highly pluggable way to serialize Moose classes to a number of
different formats and styles.

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
%doc Changes CONTRIBUTING LICENSE README

%changelog
