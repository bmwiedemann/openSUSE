#
# spec file for package perl-Heap
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Heap
Name:           perl-Heap
Version:        0.800.0
Release:        0
# 0.80 -> normalize -> 0.800.0
%define cpan_version 0.80
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extensions for keeping data partially sorted
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMM/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Heap) = %{version}
Provides:       perl(Heap::Binary) = %{version}
Provides:       perl(Heap::Binomial) = %{version}
Provides:       perl(Heap::Elem) = %{version}
Provides:       perl(Heap::Elem::Num) = %{version}
Provides:       perl(Heap::Elem::NumRev) = %{version}
Provides:       perl(Heap::Elem::Ref) = %{version}
Provides:       perl(Heap::Elem::RefRev) = %{version}
Provides:       perl(Heap::Elem::Str) = %{version}
Provides:       perl(Heap::Elem::StrRev) = %{version}
Provides:       perl(Heap::Fibonacci) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The Heap collection of modules provide routines that manage a heap of
elements. A heap is a partially sorted structure that is always able to
easily extract the smallest of the elements in the structure (or the
largest if a reversed compare routine is provided).

If the collection of elements is changing dynamically, the heap has less
overhead than keeping the collection fully sorted.

The elements must be objects as described in "Heap::Elem" and all elements
inserted into one heap must be mutually compatible - either the same class
exactly or else classes that differ only in ways unrelated to the
*Heap::Elem* interface.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README TODO

%changelog
