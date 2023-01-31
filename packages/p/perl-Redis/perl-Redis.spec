#
# spec file for package perl-Redis
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Redis
Name:           perl-Redis
Version:        2.000
Release:        0
License:        Artistic-2.0
Summary:        Perl binding for Redis database
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAMS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.63_03
BuildRequires:  perl(IO::Socket::Timeout) >= 0.29
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::TCP) >= 1.19
BuildRequires:  perl(Try::Tiny)
Requires:       perl(IO::Socket::Timeout) >= 0.29
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
Pure perl bindings for https://redis.io/

This version supports protocol 2.x (multi-bulk) or later of Redis available
at https://github.com/antirez/redis/.

This documentation lists commands which are exercised in test suite, but
additional commands will work correctly since protocol specifies enough
information to support almost all commands with same piece of code with a
little help of 'AUTOLOAD'.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
