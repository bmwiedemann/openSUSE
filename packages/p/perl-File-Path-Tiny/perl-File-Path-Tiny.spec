#
# spec file for package perl-File-Path-Tiny
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


%define cpan_name File-Path-Tiny
Name:           perl-File-Path-Tiny
Version:        1.0.0
Release:        0
# 1.0 -> normalize -> 1.0.0
%define cpan_version 1.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Recursive versions of mkdir() and rmdir() without as much overhead as Fi[cut]
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMUEY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Exception)
Requires:       perl(Test::Exception)
Provides:       perl(File::Path::Tiny) = %{version}
%undefine       __perllib_provides
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
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README

%changelog
