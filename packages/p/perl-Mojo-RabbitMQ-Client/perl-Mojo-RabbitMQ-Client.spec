#
# spec file for package perl-Mojo-RabbitMQ-Client
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


Name:           perl-Mojo-RabbitMQ-Client
Version:        0.3.1
Release:        0
%define cpan_name Mojo-RabbitMQ-Client
Summary:        Mojo::IOLoop based RabbitMQ client
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SE/SEBAPOD/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Mojolicious) >= 7.53
BuildRequires:  perl(Net::AMQP) >= 0.06
BuildRequires:  perl(Test::Exception) >= 0.430000
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(File::ShareDir)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Mojolicious) >= 7.53
Requires:       perl(Net::AMQP) >= 0.06
%{perl_requires}
# MANUAL BEGIN
# Net::AMQP only supports 64 bit: https://rt.cpan.org/Public/Bug/Display.html?id=87816
ExcludeArch:    i586 armv7l ppc
# MANUAL END

%description
Mojo::RabbitMQ::Client is a rewrite of AnyEvent::RabbitMQ to work on top of
Mojo::IOLoop.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples minil.toml README.md
%license LICENSE

%changelog
