#
# spec file for package byaccj
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%define jpp_release 3
Name:           byaccj
Version:        1.15
Release:        0
Summary:        Parser Generator with Java Extension
License:        SUSE-Public-Domain
Group:          Development/Libraries/Java
URL:            http://byaccj.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}%{version}_src.tar.gz
Requires:       man-pages

%description
BYACC/J is an extension of the Berkeley v 1.8 YACC-compatible parser
generator. Standard YACC takes a YACC source file, and generates one or
more C files from it, which if compiled properly, will produce a
LALR-grammar parser. This is useful for expression parsing, interactive
command parsing, and file reading. Many megabytes of YACC code have
been written over the years. This is the standard YACC tool that is in
use every day to produce C/C++ parsers. I have added a "-J" flag which
will cause BYACC to generate Java source code, instead. So there
finally is a YACC for Java now!

%prep
%setup -q -n %{name}%{version}

chmod -c -x src/* docs/*
sed -i -e 's|-arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -mmacosx-version-min=10.4|$(LDFLAGS)|g' src/Makefile

%build
pushd src
%make_build yacc CFLAGS="%{optflags}" LDFLAGS="$RPM_LD_FLAGS"
popd

#Fix wrong-file-end-of-line-encoding
sed -i 's/\r//g' docs/tf.y

%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 src/yacc %{buildroot}%{_bindir}/%{name}

%files
%doc docs/* src/README
%{_bindir}/%{name}

%changelog
