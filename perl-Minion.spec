#
# spec file for package perl-Minion
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Minion
Name:           perl-Minion
Version:        10.300.0
Release:        0
# 10.30 -> normalize -> 10.300.0
%define cpan_version 10.30
License:        Artistic-2.0
Summary:        Job queue
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Mojolicious) >= 9.0
BuildRequires:  perl(YAML::XS) >= 0.67
Requires:       perl(Mojolicious) >= 9.0
Requires:       perl(YAML::XS) >= 0.67
Provides:       perl(Minion) = %{version}
Provides:       perl(Minion::Backend)
Provides:       perl(Minion::Backend::Pg)
Provides:       perl(Minion::Command::minion)
Provides:       perl(Minion::Command::minion::job)
Provides:       perl(Minion::Command::minion::worker)
Provides:       perl(Minion::Iterator)
Provides:       perl(Minion::Job)
Provides:       perl(Minion::Worker)
Provides:       perl(Mojolicious::Plugin::Minion)
Provides:       perl(Mojolicious::Plugin::Minion::Admin)
%undefine       __perllib_provides
%{perl_requires}

%description
Minion is a high performance job queue for the Perl programming language,
with support for multiple named queues, priorities, high priority fast
lane, delayed jobs, job dependencies, job progress, job results, retries
with backoff, rate limiting, unique jobs, expiring jobs, statistics,
distributed workers, parallel processing, autoscaling, remote control, at
https://mojolicious.org admin ui, resource leak protection and multiple
backends (such as at https://www.postgresql.org).

Job queues allow you to process time and/or computationally intensive tasks
in background processes, outside of the request/response lifecycle of web
applications. Among those tasks you'll commonly find image resizing, spam
filtering, HTTP downloads, building tarballs, warming caches and basically
everything else you can imagine that's not super fast.

Take a look at our excellent documentation in Minion::Guide!

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples README.md
%license LICENSE

%changelog
