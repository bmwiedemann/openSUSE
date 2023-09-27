#
# spec file for package perl-Mojo-IOLoop-ReadWriteProcess
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


%define cpan_name Mojo-IOLoop-ReadWriteProcess
Name:           perl-Mojo-IOLoop-ReadWriteProcess
Version:        0.340.0
Release:        0
%define cpan_version 0.34
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Execute external programs or internal code blocks as separate process
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZARATE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::SharedMem)
BuildRequires:  perl(Module::Build) >= 0.4005
BuildRequires:  perl(Mojolicious) >= 9.340.0
BuildRequires:  perl(Test::Exception)
Requires:       perl(IPC::SharedMem)
Requires:       perl(Mojolicious) >= 9.340.0
Provides:       perl(Mojo::IOLoop::ReadWriteProcess) = 0.340.0
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v1)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Cpuacct)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Cpuset)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Devices)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Freezer)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Memory)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Netcls)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Netprio)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v1::PID)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v1::RDMA)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v2)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v2::CPU)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v2::IO)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v2::Memory)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v2::PID)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::CGroup::v2::RDMA)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::Container)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::Exception)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::Namespace)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::Pool)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::Queue)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::Session)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::Shared::Lock)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::Shared::Memory)
Provides:       perl(Mojo::IOLoop::ReadWriteProcess::Shared::Semaphore)
%define         __perllib_provides /bin/true
%{perl_requires}

%description
Mojo::IOLoop::ReadWriteProcess is yet another process manager.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
