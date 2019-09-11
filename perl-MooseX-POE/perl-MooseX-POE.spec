#
# spec file for package perl-MooseX-POE
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-POE
Version:        0.215
Release:        0
%define cpan_name MooseX-POE
Summary:        The Illicit Love Child of Moose and POE
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-POE/
Source:         http://www.cpan.org/authors/id/G/GE/GETTY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose) >= 2.0002
BuildRequires:  perl(POE) >= 1.310
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.90
#BuildRequires: perl(Base)
#BuildRequires: perl(Coro)
#BuildRequires: perl(Coro::Semaphore)
#BuildRequires: perl(Coro::Util)
#BuildRequires: perl(Device::SerialPort)
#BuildRequires: perl(Getty)
#BuildRequires: perl(JSON::Any)
#BuildRequires: perl(Moose::Exporter)
#BuildRequires: perl(Moose::Meta::Method)
#BuildRequires: perl(Moose::Role)
#BuildRequires: perl(MooseX::Coro)
#BuildRequires: perl(MooseX::Daemonize)
#BuildRequires: perl(MooseX::POE)
#BuildRequires: perl(MooseX::POE::Aliased)
#BuildRequires: perl(MooseX::POE::Meta::Method::State)
#BuildRequires: perl(MooseX::POE::Meta::Role)
#BuildRequires: perl(MooseX::POE::Meta::Trait)
#BuildRequires: perl(MooseX::POE::Role)
#BuildRequires: perl(MooseX::POE::SweetArgs)
#BuildRequires: perl(MooseX::Workers)
#BuildRequires: perl(mxpoe)
#BuildRequires: perl(Pants)
#BuildRequires: perl(POE::Filter::Line)
#BuildRequires: perl(POE::Session)
#BuildRequires: perl(POE::Wheel::ReadLine)
#BuildRequires: perl(POE::Wheel::ReadWrite)
#BuildRequires: perl(Rollo)
#BuildRequires: perl(Sys::Mmap)
#BuildRequires: perl(Test::Memory::Cycle)
#BuildRequires: perl(Test::Moose)
Requires:       perl(Moose) >= 2.0002
Requires:       perl(POE) >= 1.310
%{perl_requires}

%description
MooseX::POE is a the Moose manpage wrapper around a the POE::Session
manpage.

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
%doc Changes LICENSE README README.md

%changelog
