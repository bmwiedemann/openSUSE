#
# spec file for package perl-Archive-Tar-Wrapper
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Archive-Tar-Wrapper
Version:        0.38
Release:        0
#Upstream: GPL-1.0-or-later
%define cpan_name Archive-Tar-Wrapper
Summary:        API wrapper around the 'tar' utility
License:        GPL-3.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARFREITAS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Test::Simple) >= 1.302073
Requires:       perl(CPAN::Meta)
Requires:       perl(File::Which)
Requires:       perl(IPC::Run)
Requires:       perl(Log::Log4perl)
%{perl_requires}

%description
*Archive::Tar::Wrapper* is an API wrapper around the 'tar' command line
program. It never stores anything in memory, but works on temporary
directory structures on disk instead. It provides a mapping between the
logical paths in the tarball and the 'real' files in the temporary
directory on disk.

It differs from Archive::Tar in two ways:

  * *Archive::Tar::Wrapper* almost doesn't hold anything in memory (see 'write'
method), instead using disk as storage.

  * *Archive::Tar::Wrapper* is 100% compliant with the platform's 'tar' utility
because it uses it internally.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING.md README.md
%license LICENSE

%changelog
