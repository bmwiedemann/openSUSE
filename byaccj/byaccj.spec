#
# spec file for package byaccj
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Summary:        Parser Generator with Java Extension
License:        SUSE-Public-Domain
Group:          Development/Libraries/Java

Name:           byaccj
Version:        1.14
Release:        0
%define jpp_release 3
Url:            http://byaccj.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}%{version}_src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q -n %{name}%{version}_src

%build
pushd src
make linux CFLAGS="$RPM_OPT_FLAGS"
popd
sed -i 's/\r//g' docs/tf.y

%install
# manual
install -d -m 755 %{buildroot}%{_mandir}/man1
mv docs/yacc.cat %{buildroot}%{_mandir}/man1
# jars
mkdir -p %{buildroot}%{_bindir}
cp -p src/yacc.linux \
  %{buildroot}%{_bindir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc docs/* src/readme src/README
%{_mandir}/man1/yacc.cat*
%attr(755, root, root) %{_bindir}/%{name}

%changelog
