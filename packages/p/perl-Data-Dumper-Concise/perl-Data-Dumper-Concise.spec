#
# spec file for package perl-Data-Dumper-Concise
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Data-Dumper-Concise
Version:        2.023
Release:        0
%define cpan_name Data-Dumper-Concise
Summary:        Less indentation and newlines plus sub deparsing
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Dumper-Concise/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module always exports a single function, Dumper, which can be called
with an array of values to dump those values.

It exists, fundamentally, as a convenient way to reproduce a set of Dumper
options that we've found ourselves using across large numbers of
applications, primarily for debugging output.

The principle guiding theme is "all the concision you can get while still
having a useful dump and not doing anything cleverer than setting
Data::Dumper options" - it's been pointed out to us that
Data::Dump::Streamer can produce shorter output with less lines of code. We
know. This is simpler and we've never seen it segfault. But for
complex/weird structures, it generally rocks. You should use it as well,
when Concise is underkill. We do.

Why is deparsing on when the aim is concision? Because you often want to
know what subroutine refs you have when debugging and because if you were
planning to eval this back in you probably wanted to remove subrefs first
and add them back in a custom way anyway. Note that this -does- force using
the pure perl Dumper rather than the XS one, but I've never in my life seen
Data::Dumper show up in a profile so "who cares?".

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
