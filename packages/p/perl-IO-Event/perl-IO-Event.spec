#
# spec file for package perl-IO-Event
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name IO-Event
Name:           perl-IO-Event
Version:        0.814.0
Release:        0
# 0.814 -> normalize -> 0.814.0
%define cpan_version 0.814
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tied Filehandles for Nonblocking IO with Object Callbacks
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Event)
BuildRequires:  perl(List::SomeUtils)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(parent)
Requires:       perl(List::SomeUtils)
Requires:       perl(parent)
Provides:       perl(IO::Event) = %{version}
Provides:       perl(IO::Event::AnyEvent) = %{version}
Provides:       perl(IO::Event::Callback) = %{version}
Provides:       perl(IO::Event::Emulate) = %{version}
Provides:       perl(IO::Event::Event) = %{version}
Provides:       perl(IO::Event::INET::Callback)
Provides:       perl(IO::Event::Socket::UNIX)
Provides:       perl(IO::Event::UNIX::Callback)
%undefine       __perllib_provides
Recommends:     perl(AnyEvent)
Recommends:     perl(EV)
Recommends:     perl(Event)
%{perl_requires}

%description
IO::Event provides a object-based callback system for handling nonblocking
IO. The design goal is to provide a system that just does the right thing
w/o the user needing to think about it much.

All APIs are kept as simple as possible yet at the same time, all
functionality is accessible if needed. Simple things are easy. Hard things
are possible.

Most of the time file handling syntax will work fine: '<$filehandle>' and
'print $filehandle 'stuff''.

IO::Event provides automatic buffering of output (with a callback to
throttle). It provides automatic line-at-a-time input.

After initial setup, call 'IO::Event::loop()'.

IO::Event was originally written to use Event. IO::Event still defaults to
using Event but it can now use AnyEvent or its own event loop.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README
%license LICENSE

%changelog
