#
# spec file for package perl-AnyEvent
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name AnyEvent
Name:           perl-AnyEvent
Version:        7.170.0
Release:        0
# 7.17 -> normalize -> 7.170.0
%define cpan_version 7.17
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        The DBI of event loop programming
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
# MANUAL
#BuildArch:     noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
Provides:       perl(AE)
Provides:       perl(AE::Log::COLLECT)
Provides:       perl(AE::Log::FILTER)
Provides:       perl(AE::Log::LOG)
Provides:       perl(AnyEvent) = %{version}
Provides:       perl(AnyEvent::Base)
Provides:       perl(AnyEvent::CondVar)
Provides:       perl(AnyEvent::CondVar::Base)
Provides:       perl(AnyEvent::DNS)
Provides:       perl(AnyEvent::Debug)
Provides:       perl(AnyEvent::Debug::Backtrace)
Provides:       perl(AnyEvent::Debug::Wrap)
Provides:       perl(AnyEvent::Debug::Wrapped)
Provides:       perl(AnyEvent::Debug::shell)
Provides:       perl(AnyEvent::Handle)
Provides:       perl(AnyEvent::IO)
Provides:       perl(AnyEvent::IO::IOAIO)
Provides:       perl(AnyEvent::IO::Perl)
Provides:       perl(AnyEvent::Impl::Cocoa)
Provides:       perl(AnyEvent::Impl::EV)
Provides:       perl(AnyEvent::Impl::Event)
Provides:       perl(AnyEvent::Impl::EventLib)
Provides:       perl(AnyEvent::Impl::FLTK)
Provides:       perl(AnyEvent::Impl::Glib)
Provides:       perl(AnyEvent::Impl::IOAsync)
Provides:       perl(AnyEvent::Impl::Irssi)
Provides:       perl(AnyEvent::Impl::POE)
Provides:       perl(AnyEvent::Impl::Perl)
Provides:       perl(AnyEvent::Impl::Qt)
Provides:       perl(AnyEvent::Impl::Qt::Io)
Provides:       perl(AnyEvent::Impl::Qt::Timer)
Provides:       perl(AnyEvent::Impl::Tk)
Provides:       perl(AnyEvent::Impl::UV)
Provides:       perl(AnyEvent::Log)
Provides:       perl(AnyEvent::Log::COLLECT)
Provides:       perl(AnyEvent::Log::Ctx)
Provides:       perl(AnyEvent::Log::FILTER)
Provides:       perl(AnyEvent::Log::LOG)
Provides:       perl(AnyEvent::Loop)
Provides:       perl(AnyEvent::Socket)
Provides:       perl(AnyEvent::Strict)
Provides:       perl(AnyEvent::TLS)
Provides:       perl(AnyEvent::Util)
Provides:       perl(DB)
%undefine       __perllib_provides
Recommends:     perl(Async::Interrupt) >= 1
Recommends:     perl(EV) >= 4
Recommends:     perl(Guard) >= 1.20
Recommends:     perl(JSON) >= 2.90
Recommends:     perl(JSON::XS) >= 2.200
Recommends:     perl(Net::SSLeay) >= 1.330
Recommends:     perl(Task::Weaken)
%{perl_requires}

%description
AnyEvent provides a uniform interface to various event loops. This allows
module authors to use event loop functionality without forcing module users
to use a specific event loop implementation (since more than one event loop
cannot coexist peacefully).

The interface itself is vaguely similar, but not identical to the Event
module.

During the first call of any watcher-creation method, the module tries to
detect the currently loaded event loop by probing whether one of the
following modules is already loaded: EV, AnyEvent::Loop, Event, Glib, Tk,
Event::Lib, Qt, POE. The first one found is used. If none are detected, the
module tries to load the first four modules in the order given; but note
that if EV is not available, the pure-perl AnyEvent::Loop should always
work, so the other two are not normally tried.

Because AnyEvent first checks for modules that are already loaded, loading
an event model explicitly before first using AnyEvent will likely make that
model the default. For example:

   use Tk;
   use AnyEvent;

   # .. AnyEvent will likely default to Tk

The _likely_ means that, if any module loads another event model and starts
using it, all bets are off - this case should be very rare though, as very
few modules hardcode event loops without announcing this very loudly.

The pure-perl implementation of AnyEvent is called 'AnyEvent::Loop'. Like
other event modules you can load it explicitly and enjoy the high
availability of that event loop :)

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes mktest README util
%license COPYING

%changelog
