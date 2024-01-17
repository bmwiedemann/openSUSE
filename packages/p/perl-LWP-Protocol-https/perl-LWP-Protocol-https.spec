#
# spec file for package perl-LWP-Protocol-https
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


%define cpan_name LWP-Protocol-https
Name:           perl-LWP-Protocol-https
Version:        6.110.0
Release:        0
%define cpan_version 6.11
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Provide https support for LWP::UserAgent
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         %{cpan_name}-6.09-systemca.diff
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Socket::SSL) >= 1.970
BuildRequires:  perl(IO::Socket::SSL::Utils)
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::UserAgent) >= 6.06
BuildRequires:  perl(Net::HTTPS) >= 6
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs) >= 0.002010
BuildRequires:  perl(Test::RequiresInternet)
Requires:       perl(IO::Socket::SSL) >= 1.970
Requires:       perl(LWP::Protocol::http)
Requires:       perl(LWP::UserAgent) >= 6.06
Requires:       perl(Net::HTTPS) >= 6
Provides:       perl(LWP::Protocol::https) = 6.110.0
Provides:       perl(LWP::Protocol::https::Socket) = 6.110.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
The LWP::Protocol::https module provides support for using https schemed
URLs with LWP. This module is a plug-in to the LWP protocol handling, so
you don't use it directly. Once the module is installed LWP is able to
access sites using HTTP over SSL/TLS.

If hostname verification is requested by LWP::UserAgent's 'ssl_opts', and
neither 'SSL_ca_file' nor 'SSL_ca_path' is set, then 'SSL_ca_file' is
implied to be the one provided by Mozilla::CA. If the Mozilla::CA module
isn't available SSL requests will fail. Either install this module, set up
an alternative 'SSL_ca_file' or disable hostname verification.

This module used to be bundled with the libwww-perl, but it was unbundled
in v6.02 in order to be able to declare its dependencies properly for the
CPAN tool-chain. Applications that need https support can just declare
their dependency on LWP::Protocol::https and will no longer need to know
what underlying modules to install.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CONTRIBUTING.md
%license LICENSE

%changelog
