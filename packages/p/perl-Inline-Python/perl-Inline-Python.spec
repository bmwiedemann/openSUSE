#
# spec file for package perl-Inline-Python
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


Name:           perl-Inline-Python
Version:        0.56
Release:        0
%define cpan_name Inline-Python
Summary:        Write Perl subs and classes in Python
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Inline-Python/
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NINE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::MD5) >= 2.5
BuildRequires:  perl(Inline) >= 0.46
BuildRequires:  perl(Proc::ProcessTable) >= 0.53
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Number::Delta)
Requires:       perl(Digest::MD5) >= 2.5
Requires:       perl(Inline) >= 0.46
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  python-devel
# MANUAL END

%description
The 'Inline::Python' module allows you to put Python source code directly
"inline" in a Perl script or module. It sets up an in-process Python
interpreter, runs your code, and then examines Python's symbol table for
things to bind to Perl. The process of interrogating the Python interpreter
for globals only occurs the first time you run your Python code. The
namespace is cached, and subsequent calls use the cached version.

This document describes 'Inline::Python', the Perl package which gives you
access to a Python interpreter. For lack of a better place to keep it, it
also gives you instructions on how to use 'perlmodule', the Python package
which gives you access to the Perl interpreter.

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
%doc Changes README TESTED ToDo

%changelog
