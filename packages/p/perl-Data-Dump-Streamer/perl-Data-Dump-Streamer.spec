#
# spec file for package perl-Data-Dump-Streamer
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Data-Dump-Streamer
Version:        2.40
Release:        0
%define cpan_name Data-Dump-Streamer
Summary:        Accurately serialize a data structure as Perl code
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Dump-Streamer/
Source0:        http://www.cpan.org/authors/id/Y/YV/YVES/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Utils)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(Module::Build)
Requires:       perl(B::Utils)
Recommends:     perl(Algorithm::Diff)
Recommends:     perl(Compress::Zlib)
Recommends:     perl(JSON::XS)
Recommends:     perl(PadWalker) >= 0.99
%{perl_requires}

%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The contents of each
variable is output using the least number of Perl statements as convenient,
usually only one. Self-referential structures, closures, and objects are
output correctly.

The return value can be evaled to get back an identical copy of the
original reference structure. In some cases this may require the use of
utility subs that Data::Dump::Streamer will optionally export.

This module is very similar in concept to the core module Data::Dumper,
with the major differences being that this module is designed to output to
a stream instead of constructing its output in memory (trading speed for
memory), and that the traversal over the data structure is effectively
breadth first versus the depth first traversal done by the others.

In fact the data structure is scanned twice, first in breadth first mode to
perform structural analysis, and then in depth first mode to actually
produce the output, but obeying the depth relationships of the first pass.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.md

%changelog
