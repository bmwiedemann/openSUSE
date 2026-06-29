#
# spec file for package perl-Git-Wrapper
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


%define cpan_name Git-Wrapper
Name:           perl-Git-Wrapper
Version:        0.48.0
Release:        0
# 0.048 -> normalize -> 0.48.0
%define cpan_version 0.048
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Wrap git(7) command-line interface
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GENEHACK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::CheckBin)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
Requires:       perl(File::chdir)
Requires:       perl(IPC::Cmd)
Requires:       perl(Sort::Versions)
Provides:       perl(Git::Wrapper) = %{version}
Provides:       perl(Git::Wrapper::Exception) = %{version}
Provides:       perl(Git::Wrapper::File::RawModification) = %{version}
Provides:       perl(Git::Wrapper::Log) = %{version}
Provides:       perl(Git::Wrapper::Status) = %{version}
Provides:       perl(Git::Wrapper::Statuses) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  git-core
Requires:       git-core
# MANUAL END

%description
Git::Wrapper provides an API for git(7) that uses Perl data structures for
argument passing, instead of CLI-style '--options' as Git does.

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
%doc Changes README.md
%license LICENSE

%changelog
