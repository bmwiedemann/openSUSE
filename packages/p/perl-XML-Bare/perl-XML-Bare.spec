#
# spec file for package perl-XML-Bare
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-XML-Bare
Version:        0.53
Release:        0
%define cpan_name XML-Bare
Summary:        Minimal XML parser implemented via a C state engine
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-Bare/
Source:         http://www.cpan.org/authors/id/C/CO/CODECHILD/%{cpan_name}-%{version}.tar.gz
Patch0:         fix-pointers.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.94
%{perl_requires}

%description
This module is a 'Bare' XML parser. It is implemented in C. The parser
itself is a simple state engine that is less than 500 lines of C. The
parser builds a C struct tree from input text. That C struct tree is
converted to a Perl hash by a Perl function that makes basic calls back to
the C to go through the nodes sequentially.

The parser itself will only cease parsing if it encounters tags that are
not closed properly. All other inputs will parse, even invalid inputs. To
allowing checking for validity, a schema checker is included in the module
as well.

The schema format is custom and is meant to be as simple as possible. It is
based loosely around the way multiplicity is handled in Perl regular
expressions.

%prep
%autosetup -p1 -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
