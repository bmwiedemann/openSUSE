#
# spec file for package perl-Meta-Builder
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Meta-Builder
Version:        0.004
Release:        0
%define cpan_name Meta-Builder
Summary:        Tools for creating Meta objects to track custom metrics
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Fennec::Lite)
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Test::Exception)
%{perl_requires}

%description
Meta programming is becoming more and more popular. The popularity of Meta
programming comes from the fact that many problems are made significantly
easier. There are a few specialized Meta tools out there, for instance
Class:MOP which is used by Moose to track class metadata.

Meta::Builder is designed to be a generic tool for writing Meta objects.
Unlike specialized tools, Meta::Builder makes no assumptions about what
metrics you will care about. Meta::Builder also makes it simple for others
to extend your meta-object based tools by providing hooks for other
packages to add metrics to your meta object.

If a specialized Meta object tool is available to meet your needs please
use it. However if you need a simple Meta object to track a couple metrics,
use Meta::Builder.

Meta::Builder is also low-sugar and low-dep. In most cases you will not
want a class that needs a meta object to use your meta-object class
directly. Rather you will usually want to create a sugar class that exports
enhanced API functions that manipulate the meta object.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
