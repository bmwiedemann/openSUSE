#
# spec file for package perl-AnyEvent
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


Name:           perl-AnyEvent
Version:        7.16
Release:        0
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
%define cpan_name AnyEvent
Summary:        The DBI of event loop programming
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# MANUAL
#BuildArch:     noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Canary::Stability)
Recommends:     perl(Async::Interrupt) >= 1
Recommends:     perl(EV) >= 4
Recommends:     perl(Guard) >= 1.02
Recommends:     perl(JSON) >= 2.09
Recommends:     perl(JSON::XS) >= 2.2
Recommends:     perl(Net::SSLeay) >= 1.33
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes mktest README util
%license COPYING

%changelog
