#
# spec file for package perl-String-ShellQuote
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-String-ShellQuote
Version:        1.04
Release:        0
Summary:        Quote strings for passing through the shell
License:        Artistic-1.0 OR GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/String-ShellQuote/
Source:         http://www.cpan.org/authors/id/R/RO/ROSCH/String-ShellQuote-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildArch:      noarch
%{perl_requires}

%description
This module contains some functions which are useful for quoting strings
which are going to pass through the shell or a shell-like object.

%prep
%setup -q -n String-ShellQuote-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -print0 | xargs -0 --no-run-if-empty rm -f
find %{buildroot} -depth -type d -print0 | xargs -0 --no-run-if-empty rmdir 2>/dev/null || true
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
