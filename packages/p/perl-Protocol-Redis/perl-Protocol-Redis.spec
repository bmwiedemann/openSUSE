#
# spec file for package perl-Protocol-Redis
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


%define cpan_name Protocol-Redis
Name:           perl-Protocol-Redis
Version:        2.0.100
Release:        0
# 2.0001 -> normalize -> 2.0.100
%define cpan_version 2.0001
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Redis protocol parser/encoder with asynchronous capabilities
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/U/UN/UNDEF/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Test::More) >= 0.94
Provides:       perl(Protocol::Redis) = %{version}
Provides:       perl(Protocol::Redis::Test)
%undefine       __perllib_provides
%{perl_requires}

%description
Redis protocol parser/encoder with asynchronous capabilities and at
http://redis.io/topics/pipelining support.

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
%doc Changes examples
%license LICENSE

%changelog
