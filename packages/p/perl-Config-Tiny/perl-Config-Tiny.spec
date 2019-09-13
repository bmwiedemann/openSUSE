#
# spec file for package perl-Config-Tiny
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Config-Tiny
Version:        2.24
Release:        0
%define cpan_name Config-Tiny
Summary:        Read/Write .ini style files with as little code as possible
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Config-Tiny/
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Spec) >= 3.3
BuildRequires:  perl(File::Temp) >= 0.22
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
%doc Changes README test.conf
%license LICENSE

%changelog
