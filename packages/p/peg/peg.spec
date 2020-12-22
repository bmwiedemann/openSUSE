#
# spec file for package peg
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


Name:           peg
Version:        0.1.18
Release:        0
Summary:        Recursive-Descent parser generators for C
License:        MIT
Group:          Development/Tools/Building
URL:            https://piumarta.com/software/peg/
Source0:        http://piumarta.com/software/peg/peg-%{version}.tar.gz

%description
peg(1) and leg(1) are tools for generating recursive-descent
parsers: programs that perform pattern matching on text. They
processes a Parsing Expression Grammar (PEG) to produce a program
that recognises legal sentences of that grammar. peg(1) processes
PEGs written using the original syntax described by Ford while
leg(1) processes PEGs written using slightly different syntax and
conventions that are intended to make it an attractive replacement
for parsers built with lex(1) and yacc(1). Unlike lex(1) and
yacc(1), peg(1) and leg(1) support unlimited backtracking, provide
ordered choice as a means for disambiguation, and can combine
scanning (lexical analysis) and parsing (syntactic analysis) into a
single activity.

%prep
%setup -q

%build
#   bootstrap tools
touch peg.peg-c leg.c
%make_build \
    CC="gcc" \
    OFLAGS="%{optflags -O}"

#   re-build from scratch
touch peg.peg leg.leg
rm peg.o leg.o
%make_build \
    CC="gcc" \
    OFLAGS="%{optflags -O}"

%install
mkdir -p -m 755 \
    %{buildroot}%{_bindir} \
    %{buildroot}%{_mandir}/man1
install -c -s -m 755 \
    peg leg %{buildroot}%{_bindir}
install -c -m 644 \
    src/peg.1 %{buildroot}%{_mandir}/man1/
install -c -m 644 \
    src/peg.1 %{buildroot}%{_mandir}/man1/leg.1

%files
%license LICENSE.txt
%doc README.txt
%{_bindir}/%{name}
%{_bindir}/leg
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/leg.1%{?ext_man}

%changelog
