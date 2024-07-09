#
# spec file for package perl-Net-AMQP-RabbitMQ
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Net-AMQP-RabbitMQ
Name:           perl-Net-AMQP-RabbitMQ
Version:        2.40012
Release:        0
#Upstream: MPL
License:        MPL-1.1
Summary:        Interact with RabbitMQ over AMQP using librabbitmq
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTEMLE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Math::Int64) >= 0.34
Requires:       perl(Math::Int64) >= 0.34
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  openssl-devel
# MANUAL END

%description
'Net::AMQP::RabbitMQ' provides a simple wrapper around the librabbitmq
library that allows connecting, declaring exchanges and queues, binding and
unbinding queues, publishing, consuming and receiving events.

Error handling in this module is primarily achieve by 'Perl_croak' (die).
You should be making good use of 'eval' around these methods to ensure that
you appropriately catch the errors.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
# MANUAL no testing (needs network)
#make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md run-one-test
%license LICENSE LICENSE-MIT

%changelog
