#
# spec file for package perl-Router-Simple
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


Name:           perl-Router-Simple
Version:        0.17
Release:        0
%define cpan_name Router-Simple
Summary:        simple HTTP router
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Router-Simple/
Source:         http://www.cpan.org/authors/id/T/TO/TOKUHIROM/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Lite) >= 0.05
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(parent)
Requires:       perl(Class::Accessor::Lite) >= 0.05
Requires:       perl(parent)
%{perl_requires}

%description
Router::Simple is a simple router class.

Its main purpose is to serve as a dispatcher for web applications.

Router::Simple can match against PSGI '$env' directly, which means it's
easy to use with PSGI supporting web frameworks.

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
%doc Changes LICENSE minil.toml README.md

%changelog
