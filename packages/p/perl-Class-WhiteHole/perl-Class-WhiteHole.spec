#
# spec file for package perl-Class-WhiteHole
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Class-WhiteHole
Version:        0.04
Release:        0
Url:            http://cpan.org/modules/by-module/Class/
Summary:        Base class to treat unhandled method calls as errors
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Source:         http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/Class-WhiteHole-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
It's possible to accidentally inherit an AUTOLOAD method. Often this
will happen if a class somewhere in the chain uses AutoLoader or
defines one of their own. This can lead to confusing error messages
when method lookups fail.

Sometimes you want to avoid this accidental inheritance.  In that case,
inherit from Class::WhiteHole. All unhandled methods will produce
normal Perl error messages.



Authors:
--------
    Michael G Schwern <schwern@pobox.com>

%prep
%setup -n Class-WhiteHole-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}
make test

%install
%perl_make_install
%perl_process_packlist

%files
%defattr(-,root,root)
%doc Changes
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Class
%{perl_vendorarch}/auto/Class

%changelog
