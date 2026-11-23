#
# spec file for package httpcomponents-core5
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global base_name httpcomponents-core5
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "extras"
%bcond_without extras
%else
%bcond_with extras
%endif
Version:        5.5
Release:        0
%if %{without extras}
Name:           %{base_name}
%else
Name:           %{base_name}-extras
BuildRequires:  %{base_name}
BuildRequires:  apache-commons-cli
BuildRequires:  reactive-streams-jvm
BuildRequires:  rxjava
BuildRequires:  slf4j
%endif
Summary:        Set of low level Java HTTP transport components for HTTP services
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://hc.apache.org/
Source0:        https://archive.apache.org/dist/httpcomponents/httpcore/source/httpcomponents-core-%{version}-src.tar.gz
Source1:        %{base_name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
HttpCore is a set of low level HTTP transport components that can be
used to build custom client and server side HTTP services with a
minimal footprint. HttpCore supports two I/O models: blocking I/O
model based on the classic Java I/O and non-blocking, event driven I/O
model based on Java NIO.

The blocking I/O model may be more appropriate for data intensive, low
latency scenarios, whereas the non-blocking model may be more
appropriate for high latency scenarios where raw data throughput is
less important than the ability to handle thousands of simultaneous
HTTP connections in a resource efficient manner.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Libraries/Java

%description    javadoc
%{summary}.

%prep
%setup -q -c -a1

# missing dependency
%pom_remove_dep :conscrypt-openjdk-uber httpcore5-h2
rm -f \
    httpcore5-h2/src/main/java/org/apache/hc/core5/http2/ssl/ConscryptClientTlsStrategy.java \
    httpcore5-h2/src/main/java/org/apache/hc/core5/http2/ssl/ConscryptServerTlsStrategy.java \
    httpcore5-h2/src/main/java/org/apache/hc/core5/http2/ssl/ConscryptSupport.java
%pom_remove_dep :httpcore5-jackson3 httpcore5-bom

%build
mkdir -p lib
%if %{with extras}
build-jar-repository -s lib \
    commons-cli \
    reactive-streams/reactive-streams \
    rxjava \
    slf4j/api \
    %{base_name}
%endif
ant \
%if %{with extras}
    -f build-extras.xml \
%endif
    package javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}/%{base_name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{base_name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{base_name}
for i in \
%if %{without extras}
    httpcore5 httpcore5-h2
%else
    httpcore5-reactive
%endif
do
 install -pm 0644 ${i}/target/${i}-%{version}.jar %{buildroot}%{_javadir}/%{base_name}/${i}.jar
 %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}/${i}.pom
 %add_maven_depmap %{base_name}/${i}.pom %{base_name}/${i}.jar
 cp -r ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{base_name}/${i}
done
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc README.md RELEASE_NOTES.txt

%files javadoc
%{_javadocdir}/%{base_name}
%license LICENSE.txt NOTICE.txt

%changelog
