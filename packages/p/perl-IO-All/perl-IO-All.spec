#
# spec file for package perl-IO-All
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name IO-All
Name:           perl-IO-All
Version:        0.870.0
Release:        0
# 0.87 -> normalize -> 0.870.0
%define cpan_version 0.87
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        IO::All to Larry Wall!
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(IO::All) = %{version}
Provides:       perl(IO::All::Base)
Provides:       perl(IO::All::DBM)
Provides:       perl(IO::All::Dir)
Provides:       perl(IO::All::File)
Provides:       perl(IO::All::Filesys)
Provides:       perl(IO::All::Link)
Provides:       perl(IO::All::MLDBM)
Provides:       perl(IO::All::Pipe)
Provides:       perl(IO::All::STDIO)
Provides:       perl(IO::All::Socket)
Provides:       perl(IO::All::String)
Provides:       perl(IO::All::Temp)
%undefine       __perllib_provides
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
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING example README
%license LICENSE

%changelog
