#
# spec file for package perl-IO-Async
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


%define cpan_name IO-Async
Name:           perl-IO-Async
Version:        0.802
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Asynchronous event-driven programming
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Future) >= 0.33
BuildRequires:  perl(Future::Utils) >= 0.18
BuildRequires:  perl(Module::Build) >= 0.400400
BuildRequires:  perl(Socket) >= 2.007
BuildRequires:  perl(Struct::Dumb)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Future::IO::Impl)
BuildRequires:  perl(Test::Identity)
BuildRequires:  perl(Test::Metrics::Any)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Refcount)
Requires:       perl(Future) >= 0.33
Requires:       perl(Future::Utils) >= 0.18
Requires:       perl(Socket) >= 2.007
Requires:       perl(Struct::Dumb)
Recommends:     perl(IO::Socket::IP)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  netcfg
BuildRequires:  perl(Test2::V0)
# MANUAL END

%description
This collection of modules allows programs to be written that perform
asynchronous filehandle IO operations. A typical program using them would
consist of a single subclass of IO::Async::Loop to act as a container of
other objects, which perform the actual IO work required by the program. As
well as IO handles, the loop also supports timers and signal handlers, and
includes more higher-level functionality built on top of these basic parts.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README
%license LICENSE

%changelog
