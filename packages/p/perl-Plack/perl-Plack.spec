#
# spec file for package perl-Plack
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


Name:           perl-Plack
Version:        1.0039
Release:        0
%define cpan_name Plack
Summary:        Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Plack/
Source0:        http://www.cpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Apache::LogFormat::Compiler) >= 0.12
BuildRequires:  perl(Cookie::Baker) >= 0.05
BuildRequires:  perl(Devel::StackTrace) >= 1.23
BuildRequires:  perl(Devel::StackTrace::AsHTML) >= 0.11
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(Filesys::Notify::Simple)
BuildRequires:  perl(HTTP::Body) >= 1.06
BuildRequires:  perl(HTTP::Headers::Fast) >= 0.18
BuildRequires:  perl(HTTP::Message) >= 5.814
BuildRequires:  perl(HTTP::Tiny) >= 0.034
BuildRequires:  perl(Hash::MultiValue) >= 0.05
BuildRequires:  perl(Pod::Usage) >= 1.36
BuildRequires:  perl(Stream::Buffered) >= 0.02
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP) >= 2.00
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.59
BuildRequires:  perl(parent)
Requires:       perl(Apache::LogFormat::Compiler) >= 0.12
Requires:       perl(Cookie::Baker) >= 0.05
Requires:       perl(Devel::StackTrace) >= 1.23
Requires:       perl(Devel::StackTrace::AsHTML) >= 0.11
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(Filesys::Notify::Simple)
Requires:       perl(HTTP::Body) >= 1.06
Requires:       perl(HTTP::Headers::Fast) >= 0.18
Requires:       perl(HTTP::Message) >= 5.814
Requires:       perl(HTTP::Tiny) >= 0.034
Requires:       perl(Hash::MultiValue) >= 0.05
Requires:       perl(Pod::Usage) >= 1.36
Requires:       perl(Stream::Buffered) >= 0.02
Requires:       perl(Test::TCP) >= 2.00
Requires:       perl(Try::Tiny)
Requires:       perl(URI) >= 1.59
Requires:       perl(parent)
%{perl_requires}

%description
Plack is a set of tools for using the PSGI stack. It contains middleware
components, a reference server and utilities for Web application
frameworks. Plack is like Ruby's Rack or Python's Paste for WSGI.

See PSGI for the PSGI specification and PSGI::FAQ to know what PSGI and
Plack are and why we need them.

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
