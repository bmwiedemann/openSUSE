#
# spec file for package perl-Module-Build-WithXSpp
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Module-Build-WithXSpp
Version:        0.14
Release:        0
%define cpan_name Module-Build-WithXSpp
Summary:        XS++ enhanced flavour of Module::Build
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Module-Build-WithXSpp/
Source:         http://www.cpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.04
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.2205
BuildRequires:  perl(ExtUtils::Typemaps) >= 1.00
BuildRequires:  perl(ExtUtils::XSpp) >= 0.11
BuildRequires:  perl(Module::Build) >= 0.26
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(ExtUtils::CppGuess) >= 0.04
Requires:       perl(ExtUtils::ParseXS) >= 2.2205
Requires:       perl(ExtUtils::Typemaps) >= 1.00
Requires:       perl(ExtUtils::XSpp) >= 0.11
Requires:       perl(Module::Build) >= 0.26
%{perl_requires}

%description
This subclass of the Module::Build manpage adds some tools and processes to
make it easier to use for wrapping C++ using XS++ (the ExtUtils::XSpp
manpage).

There are a few minor differences from using 'Module::Build' for an
ordinary XS module and a few conventions that you should be aware of as an
XS++ module author. They are documented in the the /"FEATURES AND
CONVENTIONS" manpage section below. But if you can't be bothered to read
all that, you may choose skip it and blindly follow the advice in the
/"JUMP START FOR THE IMPATIENT" manpage.

An example of a full distribution based on this build tool can be found in
the the ExtUtils::XSpp manpage distribution under _examples/XSpp-Example_.
Using that example as the basis for your 'Module::Build::WithXSpp'-based
distribution is probably a good idea.

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

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
