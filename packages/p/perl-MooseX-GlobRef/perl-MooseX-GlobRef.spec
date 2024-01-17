#
# spec file for package perl-MooseX-GlobRef
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           perl-MooseX-GlobRef
Version:        0.0701
Release:        0
%define cpan_name MooseX-GlobRef
Summary:        Store a Moose object in glob reference
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-GlobRef/
#Source:         http://www.cpan.org/authors/id/D/DE/DEXTER/MooseX-GlobRef-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(Test::Assert)
BuildRequires:  perl(Test::Unit::Lite) >= 0.12
Requires:       perl(Moose) >= 0.94
%{perl_requires}

%description
This module allows to store Moose object in glob reference of file handle.
The class attributes will be stored in hash slot associated with glob
reference. It allows to create a Moose version of the IO::Handle manpage.

The attributes can be accessed directly with following expression:

  my $hashref = \%{*$self};
  print $hashref->{key};

or shorter:

  print *$self->{key};

but the standard accessors should be used instead:

  print $self->key;

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc Changes eg Incompatibilities LICENSE README xt

%changelog
