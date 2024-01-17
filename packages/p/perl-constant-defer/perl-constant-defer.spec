#
# spec file for package perl-constant-defer
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-constant-defer
Version:        6
Release:        0
#Upstream: GPL-1.0+
%define cpan_name constant-defer
Summary:        Constant Subs with Deferred Value Calculation
License:        GPL-3.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/constant-defer/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'constant::defer' creates a subroutine which on the first call runs given
code to calculate its value, and on any subsequent calls just returns that
value, like a constant. The value code is discarded once run, allowing it
to be garbage collected.

Deferring a calculation is good if it might take a lot of work or produce a
big result but is only needed sometimes or only well into a program run. If
it's never needed then the value code never runs.

A deferred constant is generally not inlined or folded (see the
perlop/Constant Folding manpage) since it's not a single scalar value. In
the current implementation a deferred constant becomes a plain constant
after the first use, so may inline etc in code compiled after that (see the
/IMPLEMENTATION manpage below).

See _examples/simple.pl_ in the constant-defer source code for a complete
sample program.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes COPYING examples README

%changelog
