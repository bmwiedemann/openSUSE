#
# spec file for package perl-Devel-Cover-Report-Codecov
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


Name:           perl-Devel-Cover-Report-Codecov
Version:        0.25
Release:        0
%define cpan_name Devel-Cover-Report-Codecov
Summary:        Backend for Codecov reporting of coverage statistics
License:        MIT
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PI/PINE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Tar) >= 2.04
BuildRequires:  perl(Capture::Tiny) >= 0.30
BuildRequires:  perl(Cwd) >= 3.47
BuildRequires:  perl(Cwd::Guard) >= 0.04
BuildRequires:  perl(Devel::Cover) >= 1.20
BuildRequires:  perl(File::Temp) >= 0.2304
BuildRequires:  perl(File::Which) >= 1.19
BuildRequires:  perl(Furl) >= 3.07
BuildRequires:  perl(IO::Socket::SSL) >= 2.016
BuildRequires:  perl(JSON::XS) >= 3.01
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Module::Find) >= 0.13
BuildRequires:  perl(Perl::Critic) >= 1.125
BuildRequires:  perl(Sub::Retry) >= 0.06
BuildRequires:  perl(Test::Deep) >= 0.117
BuildRequires:  perl(Test::Exception) >= 0.400000
BuildRequires:  perl(Test::Mock::Guard) >= 0.10
BuildRequires:  perl(Test::Mock::Time) >= v0.1.6
BuildRequires:  perl(Test::MockObject) >= 1.20150527
BuildRequires:  perl(Test::More) >= 1.001014
BuildRequires:  perl(Test::Perl::Critic) >= 1.03
BuildRequires:  perl(Test::Requires::Git) >= 1.003
BuildRequires:  perl(URI) >= 1.60
Requires:       perl(Capture::Tiny) >= 0.30
Requires:       perl(Devel::Cover)
Requires:       perl(Furl) >= 3.07
Requires:       perl(IO::Socket::SSL) >= 2.016
Requires:       perl(JSON::XS) >= 3.01
Requires:       perl(Module::Find) >= 0.13
Requires:       perl(Sub::Retry) >= 0.06
Requires:       perl(URI) >= 1.60
%{perl_requires}

%description
Devel::Cover::Report::Codecov is coverage reporter for at
https://codecov.io.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
rm t/codecov/service/mercurial/configuration.t
# MANUAL END

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# MANUAL BEGIN
rm %{buildroot}/usr/bin/dev/create-perlcriticrc.pl
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc appveyor.yml Changes minil.toml README.md
%license LICENSE

%changelog
