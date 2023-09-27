#
# spec file for package perl-MCE
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


%define cpan_name MCE
Name:           perl-MCE
Version:        1.889.0
Release:        0
%define cpan_version 1.889
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Many-Core Engine for Perl providing parallel processing capabilities
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
Provides:       perl(MCE) = 1.889.0
Provides:       perl(MCE::Candy) = 1.889.0
Provides:       perl(MCE::Channel) = 1.889.0
Provides:       perl(MCE::Channel::Mutex) = 1.889.0
Provides:       perl(MCE::Channel::MutexFast) = 1.889.0
Provides:       perl(MCE::Channel::Simple) = 1.889.0
Provides:       perl(MCE::Channel::SimpleFast) = 1.889.0
Provides:       perl(MCE::Channel::Threads) = 1.889.0
Provides:       perl(MCE::Channel::ThreadsFast) = 1.889.0
Provides:       perl(MCE::Child) = 1.889.0
Provides:       perl(MCE::Core::Input::Generator) = 1.889.0
Provides:       perl(MCE::Core::Input::Handle) = 1.889.0
Provides:       perl(MCE::Core::Input::Iterator) = 1.889.0
Provides:       perl(MCE::Core::Input::Request) = 1.889.0
Provides:       perl(MCE::Core::Input::Sequence) = 1.889.0
Provides:       perl(MCE::Core::Manager) = 1.889.0
Provides:       perl(MCE::Core::Validation) = 1.889.0
Provides:       perl(MCE::Core::Worker) = 1.889.0
Provides:       perl(MCE::Flow) = 1.889.0
Provides:       perl(MCE::Grep) = 1.889.0
Provides:       perl(MCE::Loop) = 1.889.0
Provides:       perl(MCE::Map) = 1.889.0
Provides:       perl(MCE::Mutex) = 1.889.0
Provides:       perl(MCE::Mutex::Channel) = 1.889.0
Provides:       perl(MCE::Mutex::Channel2) = 1.889.0
Provides:       perl(MCE::Mutex::Flock) = 1.889.0
Provides:       perl(MCE::Queue) = 1.889.0
Provides:       perl(MCE::Relay) = 1.889.0
Provides:       perl(MCE::Signal) = 1.889.0
Provides:       perl(MCE::Step) = 1.889.0
Provides:       perl(MCE::Stream) = 1.889.0
Provides:       perl(MCE::Subs) = 1.889.0
Provides:       perl(MCE::Util) = 1.889.0
%define         __perllib_provides /bin/true
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
