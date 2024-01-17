#
# spec file for package perl-MooseX-MultiInitArg
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-MultiInitArg
Version:        0.02
Release:        0
%define cpan_name MooseX-MultiInitArg
Summary:        Attributes with aliases for constructor arguments
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-MultiInitArg/
Source:         http://www.cpan.org/authors/id/F/FR/FRODWITH/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build::Tiny) >= 0.023
BuildRequires:  perl(Moose)
#BuildRequires: perl(Moose::Meta::Attribute)
#BuildRequires: perl(Moose::Role)
#BuildRequires: perl(MooseX::MultiInitArg)
#BuildRequires: perl(MooseX::MultiInitArg::Attribute)
#BuildRequires: perl(MooseX::MultiInitArg::Trait)
Requires:       perl(Moose)
%{perl_requires}

%description
If you've ever wanted to be able to call an attribute any number of things
while you're passing arguments to your object constructor, Now You Can.

The primary motivator is that I have some attributes that were named
inconsistently, and I wanted to rename them without breaking backwards
compatibility with my existing API.

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
%doc Changes cpanfile LICENSE README

%changelog
