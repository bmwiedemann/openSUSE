#
# spec file for package perl-Plack-Middleware-LogErrors
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Plack-Middleware-LogErrors
Version:        0.003
Release:        0
%define cpan_name Plack-Middleware-LogErrors
Summary:        Map psgi.errors to psgix.logger or other logger
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Plack-Middleware-LogErrors/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(parent)
Requires:       perl(Plack::Middleware)
Requires:       perl(Plack::Util::Accessor)
Requires:       perl(parent)
%{perl_requires}

%description
'psgi.errors' defaults to 'STDERR' in most backends, which results in
content going somewhere unhelpful like the server console.

This middleware simply remaps the 'psgi.errors' stream to the
'psgix.logger' stream, or an explicit logger that you provide.

This is especially handy when used in combination with other middlewares
such as Plack::Middleware::LogWarn (which diverts Perl warnings to
'psgi.errors'); Plack::Middleware::HTTPExceptions (which diverts uncaught
exceptions to 'psgi.errors'); and Plack::Middleware::AccessLog, which
defaults to 'psgi.errors' when not passed a logger -- which is also
automatically applied via plackup (so if you provided no '--access-log'
option indicating a filename, 'psgi.errors' is used).

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING examples LICENCE README

%changelog
