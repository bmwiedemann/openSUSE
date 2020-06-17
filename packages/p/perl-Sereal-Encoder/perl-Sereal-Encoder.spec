#
# spec file for package perl-Sereal-Encoder
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Sereal-Encoder
Version:        4.014
Release:        0
%define cpan_name Sereal-Encoder
Summary:        Binary serialization module for Perl (encoder part)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(Sereal::Decoder) >= 4.002
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
%{perl_requires}

%description
This library implements an efficient, compact-output, and feature-rich
serializer using a binary protocol called _Sereal_. Its sister module
Sereal::Decoder implements a decoder for this format. The two are released
separately to allow for independent and safer upgrading. If you care
greatly about performance, consider reading the Sereal::Performance
documentation after finishing this document.

The Sereal protocol version emitted by this encoder implementation is
currently protocol version 4 by default.

The protocol specification and many other bits of documentation can be
found in the github repository. Right now, the specification is at
https://github.com/Sereal/Sereal/blob/master/sereal_spec.pod, there is a
discussion of the design objectives in
https://github.com/Sereal/Sereal/blob/master/README.pod, and the output of
our benchmarks can be seen at
https://github.com/Sereal/Sereal/wiki/Sereal-Comparison-Graphs. For more
information on getting the best performance out of Sereal, have a look at
the "PERFORMANCE" section below.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
# Don't build with smp_flags!
make

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes

%changelog
