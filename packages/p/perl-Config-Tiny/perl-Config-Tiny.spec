#
# spec file for package perl-Config-Tiny
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Config-Tiny
Name:           perl-Config-Tiny
Version:        2.26
Release:        0
Summary:        Read/Write .ini style files with as little code as possible
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Spec) >= 3.3
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(Test::More) >= 1.001002
Requires:       perl(File::Spec) >= 3.3
Requires:       perl(File::Temp) >= 0.22
%{perl_requires}

%description
'Config::Tiny' is a Perl class to read and write .ini style configuration
files with as little code as possible, reducing load time and memory
overhead.

Most of the time it is accepted that Perl applications use a lot of memory
and modules.

The '*::Tiny' family of modules is specifically intended to provide an
ultralight alternative to the standard modules.

This module is primarily for reading human written files, and anything we
write shouldn't need to have documentation/comments. If you need something
with more power move up to Config::Simple, Config::General or one of the
many other 'Config::*' modules.

Lastly, Config::Tiny does *not* preserve your comments, whitespace, or the
order of your config file.

See Config::Tiny::Ordered (and possibly others) for the preservation of the
order of the entries in the file.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README test.conf
%license LICENSE

%changelog
