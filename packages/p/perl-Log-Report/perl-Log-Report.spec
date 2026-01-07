#
# spec file for package perl-Log-Report
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Log-Report
Name:           perl-Log-Report
Version:        1.440.0
Release:        0
# 1.44 -> normalize -> 1.440.0
%define cpan_version 1.44
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Report a problem, pluggable handlers and language support
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.90
BuildRequires:  perl(Log::Report::Optional) >= 1.70
BuildRequires:  perl(String::Print) >= 1.0
BuildRequires:  perl(Sys::Syslog) >= 0.27
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Pod) >= 1
Requires:       perl(Devel::GlobalDestruction) >= 0.90
Requires:       perl(Log::Report::Optional) >= 1.70
Requires:       perl(String::Print) >= 1.0
Requires:       perl(Sys::Syslog) >= 0.27
Provides:       perl(Log::Report) = %{version}
Provides:       perl(Log::Report::DBIC::Profiler) = %{version}
Provides:       perl(Log::Report::Die) = %{version}
Provides:       perl(Log::Report::Dispatcher) = %{version}
Provides:       perl(Log::Report::Dispatcher::Callback) = %{version}
Provides:       perl(Log::Report::Dispatcher::File) = %{version}
Provides:       perl(Log::Report::Dispatcher::Log4perl) = %{version}
Provides:       perl(Log::Report::Dispatcher::LogDispatch) = %{version}
Provides:       perl(Log::Report::Dispatcher::Perl) = %{version}
Provides:       perl(Log::Report::Dispatcher::Syslog) = %{version}
Provides:       perl(Log::Report::Dispatcher::Try) = %{version}
Provides:       perl(Log::Report::Domain) = %{version}
Provides:       perl(Log::Report::Exception) = %{version}
Provides:       perl(Log::Report::Message) = %{version}
Provides:       perl(Log::Report::Translator) = %{version}
Provides:       perl(MojoX::Log::Report) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Get messages to users and logs. 'Log::Report' combines three tasks which
are closely related in one:

* 1. logging (like Log::Log4Perl and syslog), and

* 2. exceptions (like 'error' and 'info'), with

* 3. translations (like 'gettext' and Locale::TextDomain)

You *do not need* to use this module for all three reasons: pick what you
need now, maybe extend the usage later. Read more about how and why in the
DETAILS section, below. Especially, you should *read about the REASON
parameter*.

Also, you can study this module swiftly via the article published in the
German Perl '$foo-magazine'. English version:
https://perl.overmeer.net/log-report/papers/201306-PerlMagazine-article-en.
html

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog README.md

%changelog
