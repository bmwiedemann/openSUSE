#
# spec file for package perl-Search-Xapian
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Search-Xapian
Name:           perl-Search-Xapian
Version:        1.2.25.5
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl XS frontend to the Xapian C++ search library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLLY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::Leak)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libxapian-devel
# MANUAL END

%description
This module wraps most methods of most Xapian classes. The missing classes
and methods should be added in the future. It also provides a simplified,
more 'perlish' interface to some common operations, as demonstrated above.

There are some gaps in the POD documentation for wrapped classes, but you
can read the Xapian C++ API documentation at
https://xapian.org/docs/apidoc/html/annotated.html for details of these.
Alternatively, take a look at the code in the examples and tests.

If you want to use Search::Xapian and the threads module together, make
sure you're using Search::Xapian >= 1.0.4.0 and Perl >= 5.8.7. As of
1.0.4.0, Search::Xapian uses CLONE_SKIP to make sure that the perl wrapper
objects aren't copied to new threads - without this the underlying C++
objects can get destroyed more than once.

If you encounter problems, or have any comments, suggestions, patches, etc
please email the Xapian-discuss mailing list (details of which can be found
at https://xapian.org/lists).

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README

%changelog
