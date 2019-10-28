#
# spec file for package perl-JSON-RPC
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-JSON-RPC
Version:        1.06
Release:        0
%define         cpan_name JSON-RPC
Summary:        JSON RPC 2.0 Server Implementation
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/JSON-RPC/
Source:         http://www.cpan.org/authors/id/D/DM/DMAKI/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Router::Simple)
BuildRequires:  perl(parent)
Requires:       perl(CGI)
Requires:       perl(Class::Accessor::Lite)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Response)
Requires:       perl(JSON)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Plack)
Requires:       perl(Router::Simple)
Requires:       perl(parent)
Recommends:     perl(JSON::XS)
%{perl_requires}

%description
JSON::RPC is a set of modules that implement JSON RPC 2.0 protocol.

    If you are using old JSON::RPC code (up to 0.96), DO NOT EXPECT
    YOUR CODE TO WORK WITH THIS VERSION. THIS VERSION IS 
    ****BACKWARDS INCOMPATIBLE****

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
%doc Changes cpanfile LICENSE Makefile README.md

%changelog
