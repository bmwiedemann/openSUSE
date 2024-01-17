#
# spec file for package perl-strictures
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


Name:           perl-strictures
Version:        2.000006
Release:        0
%define cpan_name strictures
Summary:        Turn on strict and make most warnings fatal
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
I've been writing the equivalent of this module at the top of my code for
about a year now. I figured it was time to make it shorter.

Things like the importer in 'use Moose' don't help me because they turn
warnings on but don't make them fatal -- which from my point of view is
useless because I want an exception to tell me my code isn't
warnings-clean.

Any time I see a warning from my code, that indicates a mistake.

Any time my code encounters a mistake, I want a crash -- not spew to STDERR
and then unknown (and probably undesired) subsequent behaviour.

I also want to ensure that obvious coding mistakes, like indirect object
syntax (and not so obvious mistakes that cause things to accidentally
compile as such) get caught, but not at the cost of an XS dependency and
not at the cost of blowing things up on another machine.

Therefore, strictures turns on additional checking, but only when it thinks
it's running in a test file in a VCS checkout -- although if this causes
undesired behaviour this can be overridden by setting the
'PERL_STRICTURES_EXTRA' environment variable.

If additional useful author side checks come to mind, I'll add them to the
'PERL_STRICTURES_EXTRA' code path only -- this will result in a minor
version increase (e.g. 1.000000 to 1.001000 (1.1.0) or similar). Any fixes
only to the mechanism of this code will result in a sub-version increase
(e.g. 1.000000 to 1.000001 (1.0.1)).

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
