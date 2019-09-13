#
# spec file for package perl-Net-IDN-Nameprep
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


Name:           perl-Net-IDN-Nameprep
Version:        1.102
Release:        0
%define cpan_name Net-IDN-Nameprep
Summary:        Stringprep Profile for Internationalized Domain Names (S<RFC 3491>)
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-IDN-Nameprep/
Source0:        http://www.cpan.org/authors/id/C/CF/CFAERBER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Unicode::Stringprep) >= 1.1
Requires:       perl(Unicode::Stringprep) >= 1.1
%{perl_requires}

%description
This module implements the _nameprep_ specification, which describes how to
prepare internationalized domain name (IDN) labels in order to increase the
likelihood that name input and name comparison work in ways that make sense
for typical users throughout the world. Nameprep is a profile of the
stringprep protocol and is used as part of a suite of on-the-wire protocols
for internationalizing the Domain Name System (DNS).

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes LICENSE README

%changelog
