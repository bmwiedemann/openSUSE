#
# spec file for package perl-Inline-Python
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Inline-Python
Name:           perl-Inline-Python
Version:        0.57
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Write Perl subs and classes in Python
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NINE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         initperl_prototype.diff
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
BuildRequires:  python3-devel
BuildRequires:  perl(Parse::RecDescent)
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
%autosetup  -n %{cpan_name}-%{version} -p1

%build
export INLINE_PYTHON_EXECUTABLE=/usr/bin/python3
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README TESTED ToDo

%changelog
