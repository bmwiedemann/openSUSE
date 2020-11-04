#
# spec file for package perl-App-Rad-Plugin-MoreHelp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-App-Rad-Plugin-MoreHelp
Version:        0.0001
Release:        0
%define cpan_name App-Rad-Plugin-MoreHelp
Summary:        App::Rad plugin for providing extra help info
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/App-Rad-Plugin-MoreHelp/
Source:         http://www.cpan.org/authors/id/I/IR/IRONCAMEL/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::Rad)
Requires:       perl(App::Rad)
%{perl_requires}

%description
This is an App::Rad manpage plugin for providing extra help info. It
provides a 'more_help' method which can be used to provide extra info that
will be appended to to bottom of the help message.

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
%doc Changes LICENSE README README.md

%changelog
