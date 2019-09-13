#
# spec file for package perl-File-Path-Tiny
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-File-Path-Tiny
Version:        0.9
Release:        0
%define cpan_name File-Path-Tiny
Summary:        Recursive Versions of Mkdir() and Rmdir() Without As Much Overhead As Fi[cut]
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Path-Tiny/
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMUEY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Exception)
Requires:       perl(Test::Exception)
%{perl_requires}

%description
The goal here is simply to provide recursive versions of mkdir() and
rmdir() with as little code and overhead as possible.

This module is in no way meant to derogate File::Path and is in no way an
endorsement to go out and replace all use of File::Path with
File::Path::Tiny.

File::Path is very good at what it does but there's simply a lot happening
that we can do without much of the time.

Here are some things File::Path has/does that this module attempts to do
without:

* * multiple interfaces

Backwards compatibility brings in a lot of code and logic that we don't
need from here on out.

* * chdir()s

It forces a ton of chdir()s which could leave you somewhere you're not
planning on being and requires much more overhead to do.

This module provides a way to disable that if you know it is safe to do so
in your circumstance.

* * can croak not allowing you to detect and handle failure

Just let me handle errors how I want. Don't make my entire app die or have
to wrap it in an eval

The exception here is the security checks can croak, which is what you
want. See DIAGNOSTICS for more info.

* * A well intentioned output system

Just let me do the output how I want. (Nothing, As HTML, print to a
filehandle, etc...)

* * A well intentioned and experimental (IE subject to change) error
  handling system.

Just keep it simple and detect failure via a boolean check and do what I
want with the error. See "How can I make/remove multiple paths?"

* * According to its POD, removing a tree is apparently not safe unless you
  tell it to be with the ‘safe’ or 'keep_root' attributes.

Seems like that should just happen, I don't want to worry about
accidentally removing / when I pass it /tmp

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

%changelog
