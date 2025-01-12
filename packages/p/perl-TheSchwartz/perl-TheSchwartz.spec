#
# spec file for package perl-TheSchwartz
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


%define cpan_name TheSchwartz
Name:           perl-TheSchwartz
Version:        1.180.0
Release:        0
# 1.18 -> normalize -> 1.180.0
%define cpan_version 1.18
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Reliable job queue
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKIYM/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Data::ObjectDriver) >= 0.04
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(Data::ObjectDriver) >= 0.04
Provides:       perl(TheSchwartz) = %{version}
Provides:       perl(TheSchwartz::Error)
Provides:       perl(TheSchwartz::ExitStatus)
Provides:       perl(TheSchwartz::FuncMap)
Provides:       perl(TheSchwartz::Job)
Provides:       perl(TheSchwartz::JobHandle)
Provides:       perl(TheSchwartz::Worker)
%undefine       __perllib_provides
%{perl_requires}

%description
TheSchwartz is a reliable job queue system. Your application can put jobs
into the system, and your worker processes can pull jobs from the queue
atomically to perform. Failed jobs can be left in the queue to retry later.

_Abilities_ specify what jobs a worker process can perform. Abilities are
the names of 'TheSchwartz::Worker' sub-classes, as in the synopsis: the
'MyWorker' class name is used to specify that the worker script can perform
the job. When using the 'TheSchwartz' client's 'work' functions, the
class-ability duality is used to automatically dispatch to the proper class
to do the actual work.

TheSchwartz clients will also prefer to do jobs for unused abilities before
reusing a particular ability, to avoid exhausting the supply of one kind of
job while jobs of other types stack up.

Some jobs with high setup times can be performed more efficiently if a
group of related jobs are performed together. TheSchwartz offers a facility
to _coalesce_ jobs into groups, which a properly constructed worker can
find and perform at once. For example, if your worker were delivering
email, you might store the domain name from the recipient's address as the
coalescing value. The worker that grabs that job could then batch deliver
all the mail for that domain once it connects to that domain's mail server.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes doc README.md
%license LICENSE

%changelog
