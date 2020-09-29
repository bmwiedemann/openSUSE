#
# spec file for package perl-PadWalker
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-PadWalker
Version:        2.5
Release:        0
%define cpan_name PadWalker
Summary:        Play with other peoples' lexical variables
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBIN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
PadWalker is a module which allows you to inspect (and even change!)
lexical variables in any subroutine which called you. It will only show
those variables which are in scope at the point of the call.

PadWalker is particularly useful for debugging. It's even used by Perl's
built-in debugger. (It can also be used for evil, of course.)

I wouldn't recommend using PadWalker directly in production code, but it's
your call. Some of the modules that use PadWalker internally are certainly
safe for and useful in production.

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
%doc Changes README

%changelog
