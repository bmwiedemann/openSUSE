#
# spec file for package xmlstreambuffer
#
# Copyright (c) 2024 SUSE LLC
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


Name:           xmlstreambuffer
Version:        1.5.4
Release:        0
Summary:        XML Stream Buffer
License:        CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://java.net/projects/xmlstreambuffer/
Source0:        https://github.com/kohsuke/xmlstreambuffer/archive/streambuffer-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
#!BuildRequires:  stax-ex
BuildArch:      noarch

%description
A stream buffer is a stream-based representation of an XML
info-set in Java. Stream buffers are designed to: provide
very efficient stream-based memory representations of XML
info-sets; and be created and processed using any Java-based
XML API.
Conceptually a stream buffer is similar to the representation
used in the Xerces deferred DOM implementation, with the crucial
difference that a stream buffer does not store hierarchical
information like parent and sibling information. The deferred
DOM implementation reduces memory usage when large XML documents
are parsed but only a subset of the document needs to be processed.
(Note that using deferred DOM will be more expensive than
non-deferred DOM in terms of memory and processing if all
the document is traversed.)
Stream buffers may be used as an efficient alternative to DOM where:
* most or all of an XML info-set will eventually get traversed; and/or
* targeted access to certain parts of an XML info-set are required
 and need to be efficiently processed using stream-based APIs like
 SAX or StAX.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-streambuffer-%{version}
find ./ -name '*.class' -delete
find ./ -name '*.jar' -delete
find ./ -name '*.zip' -delete

%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

rm -r test/com/sun/xml/stream/buffer/stax/InscopeNamespaceTest.java

%{mvn_file} :streambuffer %{name}

%build

%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license copyright.txt

%files javadoc -f .mfiles-javadoc
%license copyright.txt

%changelog
