#
# spec file for package grepmail
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           grepmail
Version:        5.3104
Release:        0
Summary:        Search Mailboxes for a Particular E-Mail
License:        GPL-2.0+
Group:          Productivity/Networking/Email/Utilities
URL:            https://metacpan.org/release/grepmail
Source:         http://search.cpan.org/CPAN/authors/id/D/DC/DCOPPIT/grepmail-%{version}.tar.gz
Patch2:         grepmail-buildfix.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Mail::Mbox::MessageParser) >= 1.4001
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI::Escape)
## not in factory ## BuildRequires:  perl(Benchmark::Timer) => 0.7100
Requires:       perl(Date::Parse)
Requires:       perl(Mail::Mbox::MessageParser) >= 1.4001
Requires:       perl(Time::Local)
# Date::Manip is only used as fallback
Recommends:     perl(Date::Manip)
BuildArch:      noarch
%{perl_requires}

%description
Grepmail searches a normal, gzipped, bzipped, or tzipped mailbox for a
given regular expression, and returns any e-mails that match that
expression. Piped input is allowed and date restrictions are supported.

%prep
%setup -q
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
%if 0%{?suse_version} <= 1320
# needed for <= 13.2, but breaks 'make test' in > 13.2
%patch2
%endif
rm inc/Scalar/Util.pm
%if 0%{?suse_version} >= 1320
rm -rf inc/File/Spec*
%endif

%build
PERL_EXTUTILS_AUTOINSTALL=--skip perl Makefile.PL INSTALLDIRS=site
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
# do not perl_process_packlist (noarch)
# remove .packlist file
rm -rf %{buildroot}%{perl_vendorarch}
# remove perllocal.pod file
rm -rf %{buildroot}%{perl_archlib}
%perl_gen_filelist
install -m 755 anonymize_mailbox %{buildroot}%{_bindir}

%files
%defattr (-, root, root)
%doc README CHANGES LICENSE
%{_mandir}/man?/*
%{_bindir}/anonymize_mailbox
%{_bindir}/grepmail

%changelog
