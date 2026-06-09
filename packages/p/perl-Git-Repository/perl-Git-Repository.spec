#
# spec file for package perl-Git-Repository
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


%define cpan_name Git-Repository
Name:           perl-Git-Repository
Version:        1.326.0
Release:        0
# 1.326 -> normalize -> 1.326.0
%define cpan_version 1.326
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl interface to Git repositories
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Git::Version::Compare) >= 1.1
BuildRequires:  perl(System::Command) >= 1.118
BuildRequires:  perl(Test::Requires::Git) >= 1.5
BuildRequires:  perl(namespace::clean)
Requires:       perl(Git::Version::Compare) >= 1.1
Requires:       perl(System::Command) >= 1.118
Requires:       perl(namespace::clean)
Provides:       perl(Git::Repository) = %{version}
Provides:       perl(Git::Repository::Command) = %{version}
Provides:       perl(Git::Repository::Plugin) = %{version}
Provides:       perl(Test::Git) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  git-core
# MANUAL END

%description
Git::Repository is a Perl interface to Git, for scripted interactions with
repositories. It's a low-level interface that allows calling any Git
command, whether _porcelain_ or _plumbing_, including bidirectional
commands such as 'git commit-tree'.

A Git::Repository object simply provides context to the git commands being
run. It is possible to call the 'command()' and 'run()' methods against the
class itself, and the context (typically _current working directory_) will
be obtained from the options and environment.

As a low-level interface, it provides no sugar for particular Git commands.
Specifically, it will not prepare environment variables that individual Git
commands may need or use.

However, the 'GIT_DIR' and 'GIT_WORK_TREE' environment variables are
special: if the command is run in the context of a Git::Repository object,
they will be overridden by the object's 'git_dir' and 'work_tree'
attributes, respectively. It is still possible to override them if
necessary, using the 'env' option.

Git::Repository requires at least Git 1.5.0, and is expected to support any
later version.

See Git::Repository::Tutorial for more code examples.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README
%license LICENSE

%changelog
