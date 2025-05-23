#
# spec file for package perl-IPC-System-Simple
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


%define cpan_name IPC-System-Simple
Name:           perl-IPC-System-Simple
Version:        1.300.0
Release:        0
# 1.30 -> normalize -> 1.300.0
%define cpan_version 1.30
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Run commands simply, with detailed diagnostics
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(IPC::System::Simple) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Calling Perl's in-built 'system()' function is easy, determining if it was
successful is _hard_. Let's face it, '$?' isn't the nicest variable in the
world to play with, and even if you _do_ check it, producing a
well-formatted error string takes a lot of work.

'IPC::System::Simple' takes the hard work out of calling external commands.
In fact, if you want to be really lazy, you can just write:

    use IPC::System::Simple qw(system);

and all of your 'system' commands will either succeed (run to completion
and return a zero exit value), or die with rich diagnostic messages.

The 'IPC::System::Simple' module also provides a simple replacement to
Perl's backticks operator. Simply write:

    use IPC::System::Simple qw(capture);

and then use the capture() command just like you'd use backticks. If
there's an error, it will die with a detailed description of what went
wrong. Better still, you can even use 'capturex()' to run the equivalent of
backticks, but without the shell:

    use IPC::System::Simple qw(capturex);

    my $result = capturex($command, @args);

If you want more power than the basic interface, including the ability to
specify which exit values are acceptable, trap errors, or process
diagnostics, then read on!

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes examples README
%license LICENSE

%changelog
