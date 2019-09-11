#
# spec file for package perl-MooseX-AttributeHelpers
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


Name:           perl-MooseX-AttributeHelpers
Version:        0.25
Release:        0
%define cpan_name MooseX-AttributeHelpers
Summary:        (DEPRECATED) Extend your attribute interfaces
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-AttributeHelpers/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(JSON::PP) >= 2.27300
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Moose) >= 0.56
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Meta::Method)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Test::Exception) >= 0.210000
BuildRequires:  perl(Test::Moose)
Requires:       perl(JSON::PP) >= 2.27300
Requires:       perl(Moose) >= 0.56
Requires:       perl(Moose::Meta::Attribute)
Requires:       perl(Moose::Meta::Method)
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util::TypeConstraints)
%{perl_requires}

%description
*This distribution is deprecated. The features it provides have been added
to the Moose core code as Moose::Meta::Attribute::Native. This distribution
should not be used by any new code.*

While Moose attributes provide you with a way to name your accessors,
readers, writers, clearers and predicates, this library provides commonly
used attribute helper methods for more specific types of data.

As seen in the SYNOPSIS, you specify the extension via the 'metaclass'
parameter. Available meta classes are:

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
