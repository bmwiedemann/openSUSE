#
# spec file for package bff4
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           bff4
Version:        1
Release:        0
Summary:        Fast Brainfuck interpreter
License:        SUSE-Public-Domain
Group:          Development/Languages/Other
Url:            http://mazonka.com/brainf/
Source0:        %{name}.c
# bnc#761551
Source1:        license-clarification.txt
# PATCH-FEATURE-OPENSUSE bff4-arg.patch adam@mizerski.pl -- add option to pass input file as command line argument
Patch0:         %{name}-arg.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Optimizing brainfuck implementation of dialect based on Daniel's dbfi (see "A very short self-interpreter")

This interpreter has only one input: program and input to the program have to be separated with ! e.g. ",.!a" prints 'a' To use it in interactive mode paste your program as input.

This program is compiled with optimization of linear loops (where '<>' balanced), e.g. [->+>++<<]. Linear loop is then executed in one step.

Oleg Mazonka 4.12.06  http://mazonka.com/

%prep
cp %{SOURCE0} %{SOURCE1} .
%patch0

%build
gcc %{name}.c -o %{name} %{optflags}

%install
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%doc license-clarification.txt

%changelog
