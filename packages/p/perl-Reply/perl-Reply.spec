#
# spec file for package perl-Reply
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


Name:           perl-Reply
Version:        0.42
Release:        0
%define cpan_name Reply
Summary:        Read, eval, print, loop, yay!
License:        MIT
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Config::INI::Reader::Ordered)
BuildRequires:  perl(Devel::LexAlias)
BuildRequires:  perl(Eval::Closure) >= 0.11
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Config::INI::Reader::Ordered)
Requires:       perl(Devel::LexAlias)
Requires:       perl(Eval::Closure) >= 0.11
Requires:       perl(File::HomeDir)
Requires:       perl(Getopt::Long) >= 2.36
Requires:       perl(Module::Runtime)
Requires:       perl(Package::Stash)
Requires:       perl(PadWalker)
Requires:       perl(Try::Tiny)
Recommends:     perl(App::Nopaste)
Recommends:     perl(B::Keywords)
Recommends:     perl(Carp::Always)
Recommends:     perl(Class::Refresh) >= 0.05
Recommends:     perl(Data::Dump)
Recommends:     perl(Data::Printer)
Recommends:     perl(IO::Pager)
Recommends:     perl(Proc::InvokeEditor)
Recommends:     perl(Term::ReadKey)
Recommends:     perl(Term::ReadLine::Gnu)
%{perl_requires}

%description
NOTE: This is an early release, and implementation details of this module
are still very much in flux. Feedback is welcome!

Reply is a lightweight, extensible REPL for Perl. It is plugin-based (see
Reply::Plugin), and through plugins supports many advanced features such as
coloring and pretty printing, readline support, and pluggable commands.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
