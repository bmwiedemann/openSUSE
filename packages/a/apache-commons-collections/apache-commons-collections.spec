#
# spec file for package apache-commons-collections
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


%define base_name       collections
%define short_name      commons-%{base_name}
Name:           apache-commons-collections
Version:        3.2.2
Release:        0
Summary:        Commons Collections Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/commons-collections/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         jakarta-commons-collections-javadoc-nonet.patch
Patch1:         commons-collections-3.2-build_xml.patch
# PATCH-FIX-UPSTREAM build with jdk8
Patch2:         java8-compat.patch
# PATCH-FIX-UPSTREAM add missing MANIFEST.MF file
Patch3:         commons-collections-missing-MF.patch
Patch4:         commons-collections-3.2.2-tf.javadoc.patch
Patch5:         commons-collections-jdk11.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  junit
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
BuildArch:      noarch

%description
The introduction of the Collections API by Sun in JDK 1.2
has been a boon to quick and effective Java programming.
Ready access to powerful data structures has accelerated
development by reducing the need for custom container
classes around each core object.  Most Java2 APIs are
significantly easier to use because of the Collections API.
However, there are certain holes left unfilled by Sun's
implementations, and the Jakarta-Commons Collections
Component strives to fulfill them. Among the features of
this package are: - special-purpose implementations of
Lists and Maps for fast access

- adapter classes from Java1-style containers (arrays,
  enumerations) to Java2-style collections

- methods to test or create typical set theory properties
  of collections such as union, intersection, and closure

%package testframework
Summary:        Test framework for %{name}
Group:          Development/Libraries/Java

%description testframework
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Provides:       %{name}-testframework-javadoc = %{version}-%{release}
Obsoletes:      %{name}-testframework-javadoc < %{version}-%{release}

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
# remove all binary libs
find . -name "*.jar" -delete
find . -name "*.class" -delete
# Fix file eof
sed -i 's/\r//' LICENSE.txt PROPOSAL.html README.txt NOTICE.txt

%patch -P 0 -p1
%patch -P 1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1

%build
echo "junit.jar=$(build-classpath junit)" >>build.properties
ant \
    -Dtf.build.docs=build/docs/apidocs/ -Djava.io.tmpdir=. \
    jar javadoc tf.validate tf.jar dist.bin dist.src tf.javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -m 644 build/%{short_name}-testframework-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-testframework.jar
ln -sf %{short_name}-testframework.jar %{buildroot}%{_javadir}/%{name}-testframework.jar

# poms
install -d -m 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a "org.apache.commons:%{short_name}"
%add_maven_depmap %{short_name}:%{short_name}-testframework:%{version} %{short_name}-testframework.jar -f "testframework" -a "org.apache.commons:%{short_name}-testframework"

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/docs/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc PROPOSAL.html README.txt RELEASE-NOTES.txt
%{_javadir}/%{name}.jar

%files testframework -f .mfiles-testframework
%{_javadir}/%{name}-testframework.jar

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
