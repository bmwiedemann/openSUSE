#
# spec file for package perl-Mason
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


Name:           perl-Mason
Version:        2.24
Release:        0
%define cpan_name Mason
Summary:        Powerful, high-performance templating for the web and beyond
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Mason/
Source0:        http://www.cpan.org/authors/id/J/JS/JSWARTZ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Class::Unload)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Guard)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Log::Any) >= 0.08
BuildRequires:  perl(Method::Signatures::Simple)
BuildRequires:  perl(Moose) >= 1.15
BuildRequires:  perl(MooseX::HasDefaults) >= 0.03
BuildRequires:  perl(MooseX::StrictConstructor) >= 0.13
BuildRequires:  perl(Test::Class::Most)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Capture::Tiny)
Requires:       perl(Class::Load)
Requires:       perl(Class::Unload)
Requires:       perl(Devel::GlobalDestruction)
Requires:       perl(Exception::Class)
Requires:       perl(Guard)
Requires:       perl(IPC::System::Simple)
Requires:       perl(JSON)
Requires:       perl(Log::Any) >= 0.08
Requires:       perl(Method::Signatures::Simple)
Requires:       perl(Moose) >= 1.15
Requires:       perl(MooseX::HasDefaults) >= 0.03
Requires:       perl(MooseX::StrictConstructor) >= 0.13
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
Mason is a powerful Perl-based templating system, designed to generate
dynamic content of all kinds.

Unlike many templating systems, Mason does not attempt to invent an
alternate, "easier" syntax for templates. It provides a set of syntax and
features specific to template creation, but underneath it is still clearly
and proudly recognizable as Perl.

Mason is most often used for generating web pages. It has a companion web
framework, Poet, designed to take maximum advantage of its routing and
content generation features. It can also be used as the templating layer
for web frameworks such as Catalyst::View::Mason2 and
Dancer::Template::Mason2.

All documentation is indexed at the Mason::Manual manpage.

The previous major version of Mason (1.x) is available under the name the
HTML::Mason manpage.

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
