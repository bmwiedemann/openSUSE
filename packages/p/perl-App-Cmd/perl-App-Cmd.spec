#
# spec file for package perl-App-Cmd
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-App-Cmd
Version:        0.331
Release:        0
%define cpan_name App-Cmd
Summary:        Write Command Line Apps with Less Suffering
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/App-Cmd/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.13
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(Getopt::Long) >= 2.39
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.084
BuildRequires:  perl(IO::TieCombine)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Pod::Usage) >= 1.61
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(parent)
Requires:       perl(Capture::Tiny) >= 0.13
Requires:       perl(Class::Load) >= 0.06
Requires:       perl(Data::OptList)
Requires:       perl(Getopt::Long) >= 2.39
Requires:       perl(Getopt::Long::Descriptive) >= 0.084
Requires:       perl(IO::TieCombine)
Requires:       perl(Module::Pluggable::Object)
Requires:       perl(Pod::Usage) >= 1.61
Requires:       perl(String::RewritePrefix)
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::Util)
Requires:       perl(Sub::Install)
Requires:       perl(parent)
%{perl_requires}

%description
App::Cmd is intended to make it easy to write complex command-line
applications without having to think about most of the annoying things
usually involved.

For information on how to start using App::Cmd, see App::Cmd::Tutorial.

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
%doc Changes LICENSE README

%changelog
