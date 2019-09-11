#
# spec file for package perl-File-Which
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


Name:           perl-File-Which
Version:        1.23
Release:        0
%define cpan_name File-Which
Summary:        Perl implementation of the which utility as an API
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
File::Which finds the full or relative paths to executable programs on the
system. This is normally the function of 'which' utility. 'which' is
typically implemented as either a program or a built in shell command. On
some platforms, such as Microsoft Windows it is not provided as part of the
core operating system. This module provides a consistent API to this
functionality regardless of the underlying platform.

The focus of this module is correctness and portability. As a consequence
platforms where the current directory is implicitly part of the search path
such as Microsoft Windows will find executables in the current directory,
whereas on platforms such as UNIX where this is not the case executables in
the current directory will only be found if the current directory is
explicitly added to the path.

If you need a portable 'which' on the command line in an environment that
does not provide it, install App::pwhich which provides a command line
interface to this API.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
chmod a+x corpus/test-bin-unix/0
# MANUAL END

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
%doc author.yml Changes README
%license LICENSE

%changelog
