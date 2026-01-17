#
# spec file for package perl-Protocol-Redis-Faster
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Protocol-Redis-Faster
Name:           perl-Protocol-Redis-Faster
Version:        0.4.0
Release:        0
# 0.004 -> normalize -> 0.4.0
%define cpan_version 0.004
License:        Artistic-2.0
Summary:        Optimized pure-perl Redis protocol parser/encoder (DEPRECATED)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Protocol::Redis) >= 1.0
BuildRequires:  perl(Protocol::Redis::Test)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(parent)
Requires:       perl(Protocol::Redis) >= 1.0
Requires:       perl(parent)
Provides:       perl(Protocol::Redis::Faster) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This is an empty subclass of Protocol::Redis. The optimizations it used to
contain have been implemented in the base class. Consider
Protocol::Redis::XS for faster parsing.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md README
%license LICENSE

%changelog
