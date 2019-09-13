#
# spec file for package perl-IO-All
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


Name:           perl-IO-All
Version:        0.87
Release:        0
%define cpan_name IO-All
Summary:        IO::All to Larry Wall!
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IO-All/
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
Recommends:     perl(File::MimeInfo)
Recommends:     perl(File::ReadBackwards)
%{perl_requires}

%description
IO::All combines all of the best Perl IO modules into a single nifty object
oriented interface to greatly simplify your everyday Perl IO idioms. It
exports a single function called 'io', which returns a new IO::All object.
And that object can do it all!

The IO::All object is a proxy for IO::File, IO::Dir, IO::Socket, Tie::File,
File::Spec, File::Path, File::MimeInfo and File::ReadBackwards; as well as
all the DBM and MLDBM modules. You can use most of the methods found in
these classes and in IO::Handle (which they inherit from). IO::All adds
dozens of other helpful idiomatic methods including file stat and
manipulation functions.

IO::All is pluggable, and modules like IO::All::LWP and IO::All::Mailto add
even more functionality. Optionally, every IO::All object can be tied to
itself. This means that you can use most perl IO builtins on it: readline,
'<>', getc, print, printf, syswrite, sysread, close.

The distinguishing magic of IO::All is that it will automatically open (and
close) files, directories, sockets and other IO things for you. You never
need to specify the mode ('<', '>>', etc), since it is determined by the
usage context. That means you can replace this:

    open STUFF, '<', './mystuff'
      or die "Can't open './mystuff' for input:\n$!";
    local $/;
    my $stuff = <STUFF>;
    close STUFF;

with this:

    my $stuff < io './mystuff';

And that is a *good thing*!

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
%doc Changes CONTRIBUTING example README
%license LICENSE

%changelog
