#
# spec file for package xmlbeans-mini
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


##### WARNING: please do not edit this auto generated spec file. Use the xmlbeans.spec! #####
%global bootstrap 1
%global real xmlbeans
Name:           xmlbeans-mini
Version:        2.6.0
Release:        0
Summary:        XML-Java binding tool
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://xmlbeans.apache.org
Source0:        http://archive.apache.org/dist/xmlbeans/source/%{real}-%{version}-src.tgz
Source1000:     pre_checkin.sh
Patch0:         xmlbeans-2.4.0-nodownload.patch
#PATCH-FIX-UPSTREAM: saxon 9.3+ moved VirtualNode interface
Patch1:         xmlbeans-saxon-virtualnode.patch
#PATCH-FIX-UPSTREAM xmlbeans-2.6.0-java8.patch -- Fix build with Java 8
Patch2:         xmlbeans-2.6.0-java8.patch
Patch3:         xmlbeans-2.6.0-jdk9.patch
BuildRequires:  ant >= 1.6
BuildRequires:  bea-stax-api
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  unzip
#!BuildIgnore:  antlr
#!BuildIgnore:  antlr-java
BuildArch:      noarch
%if %{bootstrap}
BuildRequires:  xml-commons-apis-bootstrap
BuildRequires:  xml-commons-resolver-bootstrap
#!BuildIgnore:  xerces-j2
#!BuildIgnore:  xerces-j2-bootstrap
#!BuildIgnore:  xml-commons
#!BuildIgnore:  xml-commons-apis
#!BuildIgnore:  xml-commons-jaxp-1.3-apis
#!BuildIgnore:  xml-commons-resolver
#!BuildIgnore:  xml-commons-resolver12
# we need this to fix requires of rhino and others
Provides:       xmlbeans
%else
BuildRequires:  ant-contrib
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  saxon9
BuildRequires:  xml-commons-resolver >= 1.1
BuildRequires:  xmlbeans-mini
#!BuildIgnore:  xmlbeans
Conflicts:      xmlbeans-mini
%endif

%description
XMLBeans is an XML-Java binding tool that allows accessing XML in a
Java-typical way. The features of XML and XML Schema are mapped to
the equivalent Java language and typing constructs. XMLBeans uses XML
Schema to compile Java interfaces and classes that can then be used
to access and modify XML instance data. XMLBeans is similar to other
Java interface/class, with a number of getFoo or setFoo methods.
There are also APIs that allow you access to the full XML infoset as
well so as to allow you to reflect into the XML schema itself through
an XML Schema Object model.

%package scripts
Summary:        XML-Java binding tool
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description scripts
XMLBeans is an XML-Java binding tool that allows accessing XML in a
Java-typical way. The features of XML and XML Schema are mapped to
the equivalent Java language and typing constructs.

This package contains additional scripts.

%prep
%setup -q -n %{real}-%{version}
%patch0 -p1 -b .nodownload
%patch1 -p1
%patch2
%patch3 -p1

%build
# Piccolo and jam are rebuilt from source and bundled with xbean
# ant clean.jars leaves some dangling jars around, do not use it
find . \( -name '*.jar' -o -name '*.zip' \) \
        -not -name 'piccolo*.jar' -not -name 'jam*.jar' \
%if %{bootstrap}
        -not -name 'oldxbean.jar' \
%endif
        -print -delete

# Replace bundled libraries
mkdir -p build/lib
ln -sf $(build-classpath xml-commons-resolver) build/lib/resolver.jar
ln -sf $(build-classpath xmlbeans/oldxbean) external/lib/oldxbean.jar
ln -sf $(build-classpath bea-stax-api) external/lib/jsr173_1.0_api.jar
ln -sf $(build-classpath saxon9) external/lib/saxon9.jar
ln -sf $(build-classpath saxon9) external/lib/saxon9-dom.jar

# Fix CRLF
sed 's/\r//' -i LICENSE.txt NOTICE.txt README.txt docs/stylesheet.css
%if %{bootstrap}
ant xmlpublic.jar
%else
ant default
%endif

%install
# jar
install -d -m 0755 %{buildroot}%{_javadir}/%{real}
install -p -m 0644 build/lib/xmlpublic.jar %{buildroot}%{_javadir}/%{real}/xmlpublic.jar

%if ! %{bootstrap}
install -p -m 0644 build/lib/xbean_xpath.jar %{buildroot}%{_javadir}/%{name}/xbean_xpath.jar
install -p -m 0644 build/lib/xbean.jar %{buildroot}%{_javadir}/%{name}/xbean.jar

# bin
install -d -m 0755 %{buildroot}%{_bindir}
install -p -m 0755 bin/dumpxsb   %{buildroot}%{_bindir}
install -p -m 0755 bin/inst2xsd  %{buildroot}%{_bindir}
install -p -m 0755 bin/scomp     %{buildroot}%{_bindir}
install -p -m 0755 bin/sdownload %{buildroot}%{_bindir}
install -p -m 0755 bin/sfactor   %{buildroot}%{_bindir}
install -p -m 0755 bin/svalidate %{buildroot}%{_bindir}
install -p -m 0755 bin/validate  %{buildroot}%{_bindir}
install -p -m 0755 bin/xpretty   %{buildroot}%{_bindir}
install -p -m 0755 bin/xsd2inst  %{buildroot}%{_bindir}
install -p -m 0755 bin/xsdtree   %{buildroot}%{_bindir}
install -p -m 0755 bin/xstc      %{buildroot}%{_bindir}

%else
# install oldxbean.jar, which is needed to build xmlbeans itself
install -p -m 0644 external/lib/oldxbean.jar %{buildroot}%{_javadir}/%{real}/oldxbean.jar
%endif #if ! % { bootstrap}

%files
%doc LICENSE.txt NOTICE.txt README.txt
%dir %{_javadir}/xmlbeans/
%{_javadir}/xmlbeans/*.jar

%if ! %{bootstrap}
%files scripts
%attr(0755,root,root) %{_bindir}/*
%endif #!bootstrap

%changelog
