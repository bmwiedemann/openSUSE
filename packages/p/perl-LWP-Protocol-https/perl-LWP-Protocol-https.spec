#
# spec file for package perl-LWP-Protocol-https
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-LWP-Protocol-https
Version:        6.09
Release:        0
%define cpan_name LWP-Protocol-https
Summary:        Provide https support for LWP::UserAgent
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         %{cpan_name}-6.09-systemca.diff
Patch1:         CVE-2014-3230.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Socket::SSL) >= 1.54
BuildRequires:  perl(IO::Socket::SSL::Utils)
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::UserAgent) >= 6.06
#BuildRequires:  perl(Mozilla::CA) >= 20180117
BuildRequires:  perl(Net::HTTPS) >= 6
BuildRequires:  perl(Test::RequiresInternet)
Requires:       perl(IO::Socket::SSL) >= 1.54
Requires:       perl(LWP::Protocol::http)
Requires:       perl(LWP::UserAgent) >= 6.06
#Requires:       perl(Mozilla::CA) >= 20180117
Requires:       perl(Net::HTTPS) >= 6
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
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1
%patch1 -p1

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
%doc Changes CONTRIBUTING.md
%license LICENSE

%changelog
