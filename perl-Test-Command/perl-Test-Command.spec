#
# spec file for package perl-Test-Command
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


Name:           perl-Test-Command
Version:        0.11
Release:        0
%define cpan_name Test-Command
Summary:        Test routines for external commands
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Command/
Source:         http://www.cpan.org/authors/id/D/DA/DANBOO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
#BuildRequires: perl(Test::Command)
%{perl_requires}

%description
'Test::Command' intends to bridge the gap between the well tested functions
and objects you choose and their usage in your programs. By examining the
exit status, terminating signal, STDOUT and STDERR of your program you can
determine if it is behaving as expected.

This includes testing the various combinations and permutations of options
and arguments as well as the interactions between the various functions and
objects that make up your program.

The various test functions below can accept either a command string or an
array reference for the first argument. If the command is expressed as a
string it is passed to 'system' as is. If the command is expressed as an
array reference it is dereferenced and passed to 'system' as a list. See
''perldoc -f system'' for how these may differ.

The final argument for the test functions, '$name', is optional. By default
the '$name' is a concatenation of the test function name, the command
string and the expected value. This construction is generally sufficient
for identifying a failing test, but you may always specify your own '$name'
if desired.

Any of the test functions can be used as instance methods on a
'Test::Command' object. This is done by dropping the initial '$cmd'
argument and instead using arrow notation.

All of the following 'exit_is_num' calls are equivalent.

   exit_is_num('true', 0);
   exit_is_num('true', 0, 'exit_is_num: true, 0');
   exit_is_num(['true'], 0);
   exit_is_num(['true'], 0, 'exit_is_num: true, 0');

   my $cmd = Test::Command->new( cmd => 'true' );

   exit_is_num($cmd, 0);
   exit_is_num($cmd, 0, 'exit_is_num: true, 0');
   $cmd->exit_is_num(0);
   $cmd->exit_is_num(0, 'exit_is_num: true, 0');

   $cmd = Test::Command->new( cmd => ['true'] );

   exit_is_num($cmd, 0);
   exit_is_num($cmd, 0, 'exit_is_num: true, 0');
   $cmd->exit_is_num(0);
   $cmd->exit_is_num(0, 'exit_is_num: true, 0');

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
