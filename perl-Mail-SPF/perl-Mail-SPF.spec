#
# spec file for package perl-Mail-SPF
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define cpan_name Mail-SPF
Name:           perl-Mail-SPF
Version:        2.9.0
Release:        0
Summary:        An object-oriented implementation of Sender Policy Framework
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
URL:            http://search.cpan.org/dist/Mail-SPF/
Source0:        http://www.cpan.org/authors/id/J/JM/JMEHNLE/mail-spf/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         fix_pod.patch
Patch1:         skip_test.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Error)
BuildRequires:  perl(Module::Build) >= 0.2805
BuildRequires:  perl(Net::DNS) >= 0.62
BuildRequires:  perl(Net::DNS::Resolver::Programmable) >= 0.003
BuildRequires:  perl(NetAddr::IP) >= 4
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(URI) >= 1.13
BuildRequires:  perl(version)
Requires:       perl(Error)
Requires:       perl(Net::DNS) >= 0.62
Requires:       perl(NetAddr::IP) >= 4
Requires:       perl(URI) >= 1.13
Requires:       perl(version)
Recommends:     perl(NetAddr::IP) >= 4.007
BuildArch:      noarch
%{perl_requires}

%description
*Mail::SPF* is an object-oriented implementation of Sender Policy Framework
(SPF). See the http://www.openspf.org manpage for more information about
SPF.

This class collection aims to fully conform to the SPF specification (RFC
4408) so as to serve both as a production quality SPF implementation and as
a reference for other developers of SPF implementations.

%prep
%setup -q -n %{cpan_name}-v%{version}
%patch0 -p1
%patch1 -p1

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES README TODO
%license LICENSE
%{_sbindir}/spfd

%changelog
