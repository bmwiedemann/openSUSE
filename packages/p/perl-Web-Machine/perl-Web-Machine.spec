#
# spec file for package perl-Web-Machine
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


Name:           perl-Web-Machine
Version:        0.17
Release:        0
%define cpan_name Web-Machine
Summary:        Perl port of Webmachine
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Web-Machine/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Headers::ActionPack) >= 0.07
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(IO::Handle::Util)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Net::HTTP)
BuildRequires:  perl(Plack::Component)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(parent)
Requires:       perl(HTTP::Headers::ActionPack) >= 0.07
Requires:       perl(HTTP::Status)
Requires:       perl(Hash::MultiValue)
Requires:       perl(IO::Handle::Util)
Requires:       perl(Module::Runtime)
Requires:       perl(Plack::Component)
Requires:       perl(Plack::Request)
Requires:       perl(Plack::Response)
Requires:       perl(Plack::Util)
Requires:       perl(Sub::Exporter)
Requires:       perl(Try::Tiny)
Requires:       perl(parent)
%{perl_requires}

%description
'Web::Machine' provides a RESTful web framework modeled as a state machine.
You define one or more resource classes. Each resource represents a single
RESTful URI end point, such as a user, an email, etc. The resource class
can also be the target for 'POST' requests to create a new user, email,
etc.

Each resource is a state machine, and each request for a resource is
handled by running the request through that state machine.

'Web::Machine' is built on top of Plack, but it handles the full request
and response cycle.

See Web::Machine::Manual for more details on using 'Web::Machine' in
general, and how 'Web::Machine' and Plack interact.

This is a port of at https://github.com/basho/webmachine, actually it is
much closer to the Ruby
version|https://github.com/seancribbs/webmachine-ruby, with a little bit of
at https://github.com/tautologistics/nodemachine and even some of at
https://github.com/benoitc/pywebmachine thrown in for good measure.

You can learn a bit about Web::Machine's history from the slides for my
2012 YAPC::NA
talk|https://speakerdeck.com/stevan_little/rest-from-the-trenches.

To learn more about Webmachine, take a look at the links in the SEE ALSO
section.

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
%doc Changes CONTRIBUTING.md examples LICENSE README.md

%changelog
