#
# spec file for package perl-IO-stringy
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


Name:           perl-IO-stringy
Version:        2.113
Release:        0
%define cpan_name IO-Stringy
Summary:        I/O on in-core objects like strings and arrays
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
This toolkit primarily provides modules for performing both traditional and
object-oriented i/o) on things _other_ than normal filehandles; in
particular, IO::Scalar, IO::ScalarArray, and IO::Lines.

In the more-traditional IO::Handle front, we have IO::AtomicFile which may
be used to painlessly create files which are updated atomically.

And in the "this-may-prove-useful" corner, we have IO::Wrap, whose exported
wraphandle() function will clothe anything that's not a blessed object in
an IO::Handle-like wrapper... so you can just use OO syntax and stop
worrying about whether your function's caller handed you a string, a
globref, or a FileHandle.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes contrib examples README
%license COPYING LICENSE

%changelog
