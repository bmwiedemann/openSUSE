#
# spec file for package perl-CGI-Application
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


%define cpan_name CGI-Application
Name:           perl-CGI-Application
Version:        4.610.0
Release:        0
# 4.61 -> normalize -> 4.610.0
%define cpan_version 4.61
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Framework for building reusable web-applications
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARTO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI) >= 4.210
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Test::Requires)
Requires:       perl(CGI) >= 4.210
Requires:       perl(Class::ISA)
Requires:       perl(HTML::Template)
Requires:       perl(Module::Build)
Requires:       perl(Test::Requires)
Provides:       perl(CGI::Application) = %{version}
Provides:       perl(CGI::Application::Mailform)
%undefine       __perllib_provides
Recommends:     perl(CGI::PSGI) >= 0.90
%{perl_requires}

%description
It is intended that your Application Module will be implemented as a
sub-class of CGI::Application. This is done simply as follows:

    package My::App;
    use base 'CGI::Application';

*Notation and Conventions*

For the purpose of this document, we will refer to the following
conventions:

  WebApp.pm   The Perl module which implements your Application Module class.
  WebApp      Your Application Module class; a sub-class of CGI::Application.
  webapp.cgi  The Instance Script which implements your Application Module.
  $webapp     An instance (object) of your Application Module class.
  $c          Same as $webapp, used in instance methods to pass around the
              current object. (Sometimes referred as "$self" in other code)

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license ARTISTIC GPL

%changelog
