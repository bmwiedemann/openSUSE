#
# spec file for package perl-WWW-Form-UrlEncoded
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-WWW-Form-UrlEncoded
Version:        0.25
Release:        0
%define cpan_name WWW-Form-UrlEncoded
Summary:        Parser and Builder for Application/X-Www-Form-Urlencoded
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(JSON) >= 2
BuildRequires:  perl(Module::Build) >= 0.380000
BuildRequires:  perl(Test::More) >= 0.98
%{perl_requires}

%description
WWW::Form::UrlEncoded provides application/x-www-form-urlencoded parser and
builder. This module aims to have compatibility with other CPAN modules
like HTTP::Body's urlencoded parser.

This module try to use WWW::Form::UrlEncoded::XS by default and fail to it,
use WWW::Form::UrlEncoded::PP instead

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -name ".keep" -printf "/bin/rm -v '%p'\n" |/bin/sh
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes minil.toml README.md
%license LICENSE

%changelog
