#
# spec file for package perl-autovivification
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


Name:           perl-autovivification
Version:        0.18
Release:        0
%define cpan_name autovivification
Summary:        Lexically disable autovivification
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/autovivification/
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPIT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
When an undefined variable is dereferenced, it gets silently upgraded to an
array or hash reference (depending of the type of the dereferencing). This
behaviour is called _autovivification_ and usually does what you mean (e.g.
when you store a value) but it may be unnatural or surprising because your
variables gets populated behind your back. This is especially true when
several levels of dereferencing are involved, in which case all levels are
vivified up to the last, or when it happens in intuitively read-only
constructs like 'exists'.

This pragma lets you disable autovivification for some constructs and
optionally throws a warning or an error when it would have happened.

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
