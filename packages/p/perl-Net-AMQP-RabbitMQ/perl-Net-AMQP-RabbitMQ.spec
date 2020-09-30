#
# spec file for package perl-Net-AMQP-RabbitMQ
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


Name:           perl-Net-AMQP-RabbitMQ
Version:        2.40007
Release:        0
%define cpan_name Net-AMQP-RabbitMQ
Summary:        Interact with RabbitMQ over AMQP using librabbitmq
License:        MIT
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTEMLE/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  openssl-devel
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Math::Int64) >= 0.34
Requires:       perl(Math::Int64) >= 0.34
%{perl_requires}

%description
'Net::AMQP::RabbitMQ' provides a simple wrapper around the librabbitmq
library that allows connecting, declaring exchanges and queues, binding and
unbinding queues, publishing, consuming and receiving events.

Error handling in this module is primarily achieve by 'Perl_croak' (die).
You should be making good use of 'eval' around these methods to ensure that
you appropriately catch the errors.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
# disabled because checks need network connection
# while testing which breaks in OBS
# make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes net-amqp-rabbitmq.sublime-project
%license LICENSE LICENSE-MIT

%changelog
