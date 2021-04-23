#
# spec file for package radamsa
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


Name:           radamsa
Version:        0.4
Release:        0
Summary:        A test case generator for robustness testing, aka a fuzzer
License:        MIT
Group:          Development/Tools/Other
URL:            https://www.ee.oulu.fi/research/ouspg/Radamsa
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring

%description
Radamsa is a test case generator for robustness testing, aka a fuzzer. It
can be used to test how well a program can stand malformed and potentially
malicious inputs. It operates based on given sample inputs and thus
requires minimal effort to set up. The main selling points of radamsa are
that it is easy to use, contains several old and new fuzzing algorithms, is
easy to script from command line and has already been used to find a slew
of bugs in programs that actually matter.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install

%files
%license LICENCE
%doc readme.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
