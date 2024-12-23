#
# spec file for package perl-UNIVERSAL-moniker
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name UNIVERSAL-moniker
Name:           perl-UNIVERSAL-moniker
Version:        0.08
Release:        0
Summary:        UNIVERAL::moniker
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/dist/UNIVERSAL-moniker
Source:         %{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildArch:      noarch
%{perl_requires}

%description
Class names in Perl often don't sound great when spoken, or look good when
written in prose. For this reason, we tend to say things like "customer" or
"basket" when we are referring to 'My::Site::User::Customer' or
'My::Site::Shop::Basket'. We thought it would be nice if our classes knew
what we would prefer to call them.

This module will add a 'moniker' (and 'plural_moniker') method to
'UNIVERSAL', and so to every class or module.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
