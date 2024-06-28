#
# spec file for package perl-MCE
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


%define cpan_name MCE
Name:           perl-MCE
Version:        1.897.0
Release:        0
# 1.897 -> normalize -> 1.897.0
%define cpan_version 1.897
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Many-Core Engine for Perl providing parallel processing capabilities
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
Provides:       perl(MCE) = %{version}
Provides:       perl(MCE::Candy) = %{version}
Provides:       perl(MCE::Channel) = %{version}
Provides:       perl(MCE::Channel::Mutex) = %{version}
Provides:       perl(MCE::Channel::MutexFast) = %{version}
Provides:       perl(MCE::Channel::Simple) = %{version}
Provides:       perl(MCE::Channel::SimpleFast) = %{version}
Provides:       perl(MCE::Channel::Threads) = %{version}
Provides:       perl(MCE::Channel::ThreadsFast) = %{version}
Provides:       perl(MCE::Child) = %{version}
Provides:       perl(MCE::Core::Input::Generator) = %{version}
Provides:       perl(MCE::Core::Input::Handle) = %{version}
Provides:       perl(MCE::Core::Input::Iterator) = %{version}
Provides:       perl(MCE::Core::Input::Request) = %{version}
Provides:       perl(MCE::Core::Input::Sequence) = %{version}
Provides:       perl(MCE::Core::Manager) = %{version}
Provides:       perl(MCE::Core::Validation) = %{version}
Provides:       perl(MCE::Core::Worker) = %{version}
Provides:       perl(MCE::Flow) = %{version}
Provides:       perl(MCE::Grep) = %{version}
Provides:       perl(MCE::Loop) = %{version}
Provides:       perl(MCE::Map) = %{version}
Provides:       perl(MCE::Mutex) = %{version}
Provides:       perl(MCE::Mutex::Channel) = %{version}
Provides:       perl(MCE::Mutex::Channel2) = %{version}
Provides:       perl(MCE::Mutex::Flock) = %{version}
Provides:       perl(MCE::Queue) = %{version}
Provides:       perl(MCE::Relay) = %{version}
Provides:       perl(MCE::Signal) = %{version}
Provides:       perl(MCE::Step) = %{version}
Provides:       perl(MCE::Stream) = %{version}
Provides:       perl(MCE::Subs) = %{version}
Provides:       perl(MCE::Util) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Sereal::Decoder) >= 3.015
Recommends:     perl(Sereal::Encoder) >= 3.015
%{perl_requires}

%description
MCE spawns a pool of workers and therefore does not fork a new process per
each element of data. Instead, MCE follows a bank queuing model. Imagine
the line being the data and bank-tellers the parallel workers. MCE enhances
that model by adding the ability to chunk the next n elements from the
input stream to the next available worker.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes Credits README.md
%license Copying LICENSE

%changelog
