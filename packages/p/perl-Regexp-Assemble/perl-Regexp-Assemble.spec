#
# spec file for package perl-Regexp-Assemble
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


Name:           perl-Regexp-Assemble
Version:        0.38
Release:        0
%define cpan_name Regexp-Assemble
Summary:        Assemble multiple Regular Expressions into a single RE
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Regexp-Assemble/
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 1.001014
%{perl_requires}

%description
Regexp::Assemble takes an arbitrary number of regular expressions and
assembles them into a single regular expression (or RE) that matches all
that the individual REs match.

As a result, instead of having a large list of expressions to loop over, a
target string only needs to be tested against one expression. This is
interesting when you have several thousand patterns to deal with. Serious
effort is made to produce the smallest pattern possible.

It is also possible to track the original patterns, so that you can
determine which, among the source patterns that form the assembled pattern,
was the one that caused the match to occur.

You should realise that large numbers of alternations are processed in
perl's regular expression engine in O(n) time, not O(1). If you are still
having performance problems, you should look at using a trie. Note that
Perl's own regular expression engine will implement trie optimisations in
perl 5.10 (they are already available in perl 5.9.3 if you want to try them
out). 'Regexp::Assemble' will do the right thing when it knows it's running
on a trie'd perl. (At least in some version after this one).

Some more examples of usage appear in the accompanying README. If that file
is not easy to access locally, you can find it on a web repository such as
http://search.cpan.org/dist/Regexp-Assemble/README or
http://cpan.uwinnipeg.ca/htdocs/Regexp-Assemble/README.html.

See also LIMITATIONS.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's,/usr/local/bin/perl.*,/usr/bin/perl,' `find examples -type f`
# MANUAL END

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
%doc Changes examples README TODO
%license LICENSE

%changelog
