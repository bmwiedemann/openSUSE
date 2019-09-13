#
# spec file for package perl-Event
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Event
Version:        1.27
Release:        0
%define cpan_name Event
Summary:        Event loop processing
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{version}.tar.gz
Source1:        perl-Event-rpmlintrc
Source2:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
ALERT: Marc Lehmann may have taken over the future of event loops in Perl.
Check out his libev library and EV Perl module. 25 Aug 2009

The Event module provide a central facility to watch for various types of
events and invoke a callback when these events occur. The idea is to delay
the handling of events so that they may be dispatched in priority order
when it is safe for callbacks to execute.

Events (in the ordinary sense of the word) are detected by *watchers*,
which reify them as *events* (in the special Event module sense). For
clarity, the former type of events may be called "source events", and the
latter "target events". Source events, such as signals arriving, happen
whether or not they are being watched. If a source event occurs which a
watcher is actively watching then the watcher generates a corresponding
target event. Target events are only created by watchers. If several
watchers are interested in the same source event then each will generate
their own target event. Hence, any particular source event may result in
zero, one, two, or any number of target events: the same as the number of
watchers which were actively watching for it.

Target events are queued to be processed in priority order (priority being
determined by the creating watcher) and in FIFO order among events of the
same priority. Queued ("pending") events can, in some cases, be cancelled
before being processed. A queued event is processed by being passed to the
callback function (or method on a particular object or class) which was
specified to the watcher.

A watcher, once created, operates autonomously without the Event user
having to retain any reference to it. However, keeping a reference makes it
possible to modify most of the watcher's characteristics. A watcher can be
switched between active and inactive states. When inactive, it does not
generate target events.

Some types of source event are not reified as target events immediately.
Signals received, for example, are counted initially. The counted signals
are reified at certain execution points. Hence, signal events may be
processed out of order, and if handled carelessly, on the wrong side of a
state change in event handling. A useful way to view this is that
occurrence of the source event is not actually the arrival of the signal
but is triggered by the counting of the signal.

Reification can be forced when necessary. The schedule on which some other
events are created is non-obvious. This is especially the case with
watchers that watch for a condition rather than an event. In some cases,
target events are generated on a schedule that depends on the operation of
the event loop.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc ANNOUNCE Changes README README.EV TODO Tutorial.pdf Tutorial.pdf-errata.txt util

%changelog
