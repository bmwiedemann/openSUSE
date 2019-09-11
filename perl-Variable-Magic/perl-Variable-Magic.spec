#
# spec file for package perl-Variable-Magic
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


Name:           perl-Variable-Magic
Version:        0.62
Release:        0
%define cpan_name Variable-Magic
Summary:        Associate user-defined magic to variables from Perl
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Variable-Magic/
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPIT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Magic is Perl's way of enhancing variables. This mechanism lets the user
add extra data to any variable and hook syntactical operations (such as
access, assignment or destruction) that can be applied to it. With this
module, you can add your own magic to any variable without having to write
a single line of XS.

You'll realize that these magic variables look a lot like tied variables.
It is not surprising, as tied variables are implemented as a special kind
of magic, just like any 'irregular' Perl variable : scalars like '$!', '$('
or '$^W', the '%ENV' and '%SIG' hashes, the '@ISA' array, 'vec()' and
'substr()' lvalues, threads::shared variables... They all share the same
underlying C API, and this module gives you direct access to it.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README samples

%changelog
