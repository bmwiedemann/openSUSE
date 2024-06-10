#
# spec file for package perl-Test-Cmd
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Cmd
Version:        1.09
Release:        0
%define cpan_name Test-Cmd
Summary:        Perl module for portable testing of commands and scripts
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Cmd/
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The 'Test::Cmd' module provides a low-level framework for portable
automated testing of executable commands and scripts (in any language, not
just Perl), especially commands and scripts that interact with the file
system.

The 'Test::Cmd' module makes no assumptions about what constitutes a
successful or failed test. Attempting to read a file that doesn't exist,
for example, may or may not be an error, depending on the software being
tested.

Consequently, no 'Test::Cmd' methods (including the 'new()' method) exit,
die or throw any other sorts of exceptions (but they all do return useful
error indications). Exceptions or other error status should be handled by a
higher layer: a subclass of the Test::Cmd manpage, or another testing
framework such as the the Test manpage or the Test::Simple manpage Perl
modules, or by the test itself.

(That said, see the the Test::Cmd::Common manpage module if you want a
similar module that provides exception handling, either to use directly in
your own tests, or as an example of how to use 'Test::Cmd'.)

In addition to running tests and evaluating conditions, the 'Test::Cmd'
module manages and cleans up one or more temporary workspace directories,
and provides methods for creating files and directories in those workspace
directories from in-line data (that is, here-documents), allowing tests to
be completely self-contained. When used in conjunction with another testing
framework, the 'Test::Cmd' module can function as a _fixture_ (common
startup code for multiple tests) for simple management of command execution
and temporary workspaces.

The 'Test::Cmd' module inherits the File::Spec manpage methods
('file_name_is_absolute()', 'catfile()', etc.) to support writing tests
portably across a variety of operating and file systems.

A 'Test::Cmd' environment object is created via the usual invocation:

    $test = Test::Cmd->new();

Arguments to the 'Test::Cmd::new' method are keyword-value pairs that may
be used to initialize the object, typically by invoking the same-named
method as the keyword.

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
%doc Changes LICENSE README

%changelog
