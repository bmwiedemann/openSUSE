#
# spec file for package pmccabe
#
# Copyright (c) 2021 SUSE LLC
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

Name:           pmccabe
Version:        2.8
Release:        0
Summary:        McCabe-style complexity and line counting for C and C++
License:        GPL-2.0-or-later
Group:          Development/Languages/C and C++
Url:            https://gitlab.com/jas/pmccabe
Source:         https://gitlab.com/jas/pmccabe/-/archive/v%{version}/%{name}-v%{version}.tar.gz

%description
Pmccabe calculates McCabe-style cyclomatic complexity for C and C++
source code.  Per-function complexity may be used for spotting likely
trouble spots and for estimating testing effort.

Pmccabe also includes a non-commented line counter compatible with anac,
'decomment' which only removes comments from source code; 'codechanges',
a program to calculate the amount of change which has occurred between
two source trees or files; and 'vifn', to invoke 'vi' given a function
name rather than a file name.

Pmccabe attempts to calculate the apparent complexity rather
than the complexity following the C++ and/or cpp preprocessors.
This causes Pmccabe to become confused with cpp constructs which
cause unmatched curly braces - most of which can profitably be
rewritten so they won't confuse prettyprinters anyway.  Pmccabe prints
C-compiler-style error messages when the parser gets confused so they
may be browsed with standard tools.

Two types of cyclomatic complexity are generated - one type counts
each switch() statement as regardless of the number of cases included and
the other more traditional measure counts each case within the switch().
Pmccabe also calculates the starting line for each function, the number of
lines consumed by the function, and the number of C statements within the
function.

%prep
%setup -q -n %{name}-v%{version}

%build
make %{?_smp_mflags}

%install
%make_install INSTALL=install

%files
%license COPYING
%doc
%{_bindir}/codechanges
%{_bindir}/decomment
%{_bindir}/pmccabe
%{_bindir}/vifn
%{_mandir}/man1/codechanges.1*
%{_mandir}/man1/decomment.1*
%{_mandir}/man1/pmccabe.1*
%{_mandir}/man1/vifn.1*

%changelog
