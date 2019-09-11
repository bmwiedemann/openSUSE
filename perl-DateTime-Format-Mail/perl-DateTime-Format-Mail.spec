#
# spec file for package perl-DateTime-Format-Mail
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-DateTime-Format-Mail
Version:        0.403
Release:        0
%define cpan_name DateTime-Format-Mail
Summary:        Convert between DateTime and RFC2822/822 formats
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DateTime-Format-Mail/
Source0:        http://www.cpan.org/authors/id/B/BO/BOOK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime) >= 1.04
BuildRequires:  perl(Params::Validate)
Requires:       perl(DateTime) >= 1.04
Requires:       perl(Params::Validate)
%{perl_requires}

%description
RFCs 2822 and 822 specify date formats to be used by email. This module
parses and emits such dates.

RFC2822 (April 2001) introduces a slightly different format of date than
that used by RFC822 (August 1982). The main correction is that the
preferred format is more limited, and thus easier to parse
programmatically.

Despite the ease of generating and parsing perfectly valid RFC822 and
RFC2822 people still get it wrong. So this module provides four things for
those handling mail dates:

* 1

A strict parser that will only accept RFC2822 dates, so you can see where
you're right.

* 2

A strict formatter, so you can generate the right stuff to begin with.

* 3

A _loose_ parser, so you can take the misbegotten output from other
programs and turn it into something useful. This includes various minor
errors as well as some somewhat more bizarre mistakes. The file
_t/sample_dates_ in this module's distribution should give you an idea of
what's valid, while _t/invalid.t_ should do the same for what's not. Those
regarded as invalid are just a bit *too* strange to allow.

* 4

Interoperation with the rest of the DateTime suite. These are a collection
of modules to handle dates in a modern and accurate fashion. In particular,
they make it trivial to parse, manipulate and then format dates. Shifting
timezones is a doddle, and converting between formats is a cinch.

As a future direction, I'm contemplating an even stricter parser that will
only accept dates with no obsolete elements.

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
%doc Changes CREDITS LICENSE README

%changelog
