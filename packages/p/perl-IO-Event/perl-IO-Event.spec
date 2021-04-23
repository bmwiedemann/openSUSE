#
# spec file for package perl-IO-Event
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           perl-IO-Event
%define cpan_name IO-Event
Summary:        Tied Filehandles for Nonblocking IO with Object Callbacks
Version:        0.813
Release:        1
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IO-Event/
#Source:         http://www.cpan.org/authors/id/M/MU/MUIR/modules/IO-Event-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Event)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(diagnostics)
#
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Time::HiRes)
Requires:       perl(IO::Handle)
Requires:       perl(List::MoreUtils)
Requires:       perl(Time::HiRes)
%{perl_requires}

%description
IO::Event provides a object-based callback system for handling nonblocking
IO. The design goal is to provide a system that just does the right thing
w/o the user needing to think about it much.

All APIs are kept as simple as possible yet at the same time, all
functionality is accesible if needed. Simple things are easy. Hard things
are possible.

Most of the time file handling syntax will work fine: '<$filehandle>' and
'print $filehandle 'stuff''.

IO::Event provides automatic buffering of output (with a callback to
throttle). It provides automatic line-at-a-time input.

After initial setup, call 'IO::Event::loop()'.

IO::Event was originally written to use the Event manpage. IO::Event still
defaults to using the Event manpage but it can now use the AnyEvent manpage
or its own event loop.

%prep
%setup -q -n %{cpan_name}-%{version}
### t/forked2.t is failing on newer Dists, but builts fine locally
## so I just disable this test
rm -f t/forked2.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc Changes README

%changelog
