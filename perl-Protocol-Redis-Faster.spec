#
# spec file for package perl-Protocol-Redis-Faster
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Protocol-Redis-Faster
Version:        0.003
Release:        0
%define cpan_name Protocol-Redis-Faster
Summary:        Optimized pure-perl Redis protocol parser/encoder
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Protocol::Redis) >= 1.0000
BuildRequires:  perl(Protocol::Redis::Test)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(parent)
Requires:       perl(Protocol::Redis) >= 1.0000
Requires:       perl(parent)
%{perl_requires}

%description
This module implements the Protocol::Redis API with more optimized
pure-perl internals. See Protocol::Redis for usage documentation.

This is a low level parsing module, if you are looking to use Redis in
Perl, try Redis, Redis::hiredis, or Mojo::Redis.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING.md README
%license LICENSE

%changelog
