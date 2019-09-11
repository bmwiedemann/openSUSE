#
# spec file for package perl-Pod-Eventual
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Pod-Eventual
Version:        0.094001
Release:        0
%define cpan_name Pod-Eventual
Summary:        read a POD document as a series of trivial events
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Pod-Eventual/
Source:         http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Mixin::Linewise::Readers) >= 0.102
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
#BuildRequires: perl(Pod::Eventual)
#BuildRequires: perl(Pod::Eventual::Simple)
#BuildRequires: perl(String::Truncate)
Requires:       perl(Mixin::Linewise::Readers) >= 0.102
%{perl_requires}

%description
POD is a pretty simple format to write, but it can be a big pain to deal
with reading it and doing anything useful with it. Most existing POD
parsers care about semantics, like whether a '=item' occurred after an
'=over' but before a 'back', figuring out how to link a 'L<>', and other
things like that.

Pod::Eventual is much less ambitious and much more stupid. Fortunately,
stupid is often better. (That's what I keep telling myself, anyway.)

Pod::Eventual reads line-based input and produces events describing each
POD paragraph or directive it finds. Once complete events are immediately
passed to the 'handle_event' method. This method should be implemented by
Pod::Eventual subclasses. If it isn't, Pod::Eventual's own 'handle_event'
will be called, and will raise an exception.

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
%doc Changes eg LICENSE README

%changelog
