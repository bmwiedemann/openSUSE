#
# spec file for package perl-Devel-PartialDump
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


Name:           perl-Devel-PartialDump
Version:        0.20
Release:        0
%define cpan_name Devel-PartialDump
Summary:        Partial dumping of data structures, optimized for argument printing
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Devel-PartialDump/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.009
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(ok)
Requires:       perl(Class::Tiny)
Requires:       perl(Sub::Exporter)
Requires:       perl(namespace::clean) >= 0.19
%{perl_requires}

%description
This module is a data dumper optimized for logging of arbitrary parameters.

It attempts to truncate overly verbose data, in a way that is hopefully
more useful for diagnostics warnings than

    warn Dumper(@stuff);

Unlike other data dumping modules there are no attempts at correctness or
cross referencing, this is only meant to provide a slightly deeper look
into the data in question.

There is a default recursion limit, and a default truncation of long lists,
and the dump is formatted on one line (new lines in strings are escaped),
to aid in readability.

You can enable it temporarily by importing functions like 'warn', 'croak'
etc to get more informative errors during development, or even use it as:

    BEGIN { local $@; eval "use Devel::PartialDump qw(...)" }

to get DWIM formatting only if it's installed, without introducing a
dependency.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes CONTRIBUTING LICENCE README

%changelog
