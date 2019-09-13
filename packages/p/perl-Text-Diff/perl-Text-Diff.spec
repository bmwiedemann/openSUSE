#
# spec file for package perl-Text-Diff
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


Name:           perl-Text-Diff
Version:        1.45
Release:        0
%define cpan_name Text-Diff
Summary:        Perform diffs on files and record sets
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Diff/
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Algorithm::Diff) >= 1.19
Requires:       perl(Algorithm::Diff) >= 1.19
%{perl_requires}

%description
'diff()' provides a basic set of services akin to the GNU 'diff' utility.
It is not anywhere near as feature complete as GNU 'diff', but it is better
integrated with Perl and available on all platforms. It is often faster
than shelling out to a system's 'diff' executable for small files, and
generally slower on larger files.

Relies on Algorithm::Diff for, well, the algorithm. This may not produce
the same exact diff as a system's local 'diff' executable, but it will be a
valid diff and comprehensible by 'patch'. We haven't seen any differences
between Algorithm::Diff's logic and GNU 'diff''s, but we have not examined
them to make sure they are indeed identical.

*Note*: If you don't want to import the 'diff' function, do one of the
following:

   use Text::Diff ();

   require Text::Diff;

That's a pretty rare occurrence, so 'diff()' is exported by default.

If you pass a filename, but the file can't be read, then 'diff()' will
'croak'.

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
%license LICENSE

%changelog
