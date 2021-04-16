#
# spec file for package perl-Test-HTTP-MockServer
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Test-HTTP-MockServer
Name:           perl-Test-HTTP-MockServer
Version:        0.0.1
Release:        0
License:        Apache-2.0
Summary:        Implement a mock HTTP server for use in tests
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DRUOSO/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Parser)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Module::Build) >= 0.390000
Requires:       perl(HTTP::Parser)
Requires:       perl(HTTP::Response)
Requires:       perl(JSON::XS)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  netcfg
Requires:       netcfg
# MANUAL END

%description
Sometimes, when writing a test, you don't have to oportunity to do
dependency injection of the type of transport used in a specific API.
Sometimes that code willl unequivocally always use actual HTTP and the only
control you have is over the host and port to which it will connect.

This class offer a simple way to mock the service being called. It does
that by binding to a random port on localhost and allowing you to inspect
which port that was. Using a random port means that this can be used by
tests running in parallel on the same host.

The socket will be bound and listened on the main test process, such that
the lifetime of the connection is defined by the lifetime of the test
itself.

Since the socket will be already bound and listened to, the two conntrol
methods (start_mock_server and stop_mock_server) fork only for the accept
call, which means that it is safe to call start and stop several times
during the test in order to change the expectations of the mocked code.

That allows you to easily configure the expectations of the mock server
across each step of your test case. On the other hand, it also means that
no state is shared between the code running in the mock server and the test
code.

%prep
%autosetup  -n %{cpan_name}-v%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc README

%changelog
