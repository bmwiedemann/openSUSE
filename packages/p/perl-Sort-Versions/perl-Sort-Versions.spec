#
# spec file for package perl-Sort-Versions
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Sort-Versions
Version:        1.62
Release:        0
%define cpan_name Sort-Versions
Summary:        Perl 5 Module for Sorting of Revision-Like Numbers
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sort-Versions/
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Sort::Versions allows easy sorting of mixed non-numeric and numeric
strings, like the 'version numbers' that many shared library systems and
revision control packages use. This is quite useful if you are trying to
deal with shared libraries. It can also be applied to applications that
intersperse variable-width numeric fields within text. Other applications
can undoubtedly be found.

For an explanation of the algorithm, it's simplest to look at these
examples:

  1.1   <  1.2
  1.1a  <  1.2
  1.1   <  1.1.1
  1.1   <  1.1a
  1.1.a <  1.1a
  1     <  a
  a     <  b
  1     <  2
  1.1-3 <  1.1-4
  1.1-5 <  1.1.6

More precisely (but less comprehensibly), the two strings are treated as
subunits delimited by periods or hyphens. Each subunit can contain any
number of groups of digits or non-digits. If digit groups are being
compared on both sides, a numeric comparison is used, otherwise a ASCII
ordering is used. A group or subgroup with more units will win if all
comparisons are equal. A period binds digit groups together more tightly
than a hyphen.

Some packages use a different style of version numbering: a simple real
number written as a decimal. Sort::Versions has limited support for this
style: when comparing two subunits which are both digit groups, if either
subunit has a leading zero, then both are treated like digits after a
decimal point. So for example:

  0002  <  1
  1.06  <  1.5

This won39t always work, because there won39t always be a leading zero in
real-number style version numbers. There is no way for Sort::Versions to
know which style was intended. But a lot of the time it will do the right
thing. If you are making up version numbers, the style with (possibly) more
than one dot is the style to use.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes LICENSE README

%changelog
