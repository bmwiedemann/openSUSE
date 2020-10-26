#
# spec file for package perl-File-ShareDir
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


Name:           perl-File-ShareDir
Version:        1.118
Release:        0
%define cpan_name File-ShareDir
Summary:        Locate per-dist and per-module shared files
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Inspector) >= 1.12
BuildRequires:  perl(File::Path) >= 2.080000
BuildRequires:  perl(Test::More) >= 0.90
Requires:       perl(Class::Inspector) >= 1.12
Recommends:     perl(List::MoreUtils) >= 0.428
Recommends:     perl(Params::Util) >= 1.07
%{perl_requires}
# MANUAL BEGIN
# because File::ShareDir::Install is in inc/ it won't be seen as a
# dependency by cpanspec
BuildRequires:  perl(File::ShareDir::Install)
# MANUAL END

%description
The intent of File::ShareDir is to provide a companion to Class::Inspector
and File::HomeDir, modules that take a process that is well-known by
advanced Perl developers but gets a little tricky, and make it more
available to the larger Perl community.

Quite often you want or need your Perl module (CPAN or otherwise) to have
access to a large amount of read-only data that is stored on the
file-system at run-time.

On a linux-like system, this would be in a place such as /usr/share,
however Perl runs on a wide variety of different systems, and so the use of
any one location is unreliable.

Perl provides a little-known method for doing this, but almost nobody is
aware that it exists. As a result, module authors often go through some
very strange ways to make the data available to their code.

The most common of these is to dump the data out to an enormous Perl data
structure and save it into the module itself. The result are enormous
multi-megabyte .pm files that chew up a lot of memory needlessly.

Another method is to put the data "file" after the __DATA__ compiler tag
and limit yourself to access as a filehandle.

The problem to solve is really quite simple.

  1. Write the data files to the system at install time.
  
  2. Know where you put them at run-time.

Perl's install system creates an "auto" directory for both every
distribution and for every module file.

These are used by a couple of different auto-loading systems to store code
fragments generated at install time, and various other modules written by
the Perl "ancient masters".

But the same mechanism is available to any dist or module to store any sort
of data.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README.md testrules.yml
%license LICENSE

%changelog
