#
# spec file for package httpcomponents-client5
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


Name:           httpcomponents-client5
Version:        5.6.5
Release:        0
Summary:        HTTP agent implementation based on httpcomponents HttpCore
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://hc.apache.org/
Source0:        https://archive.apache.org/dist/httpcomponents/httpclient/source/httpcomponents-client-%{version}-src.tar.gz
Source1:        %{name}-build.tar.xz
Patch0:         %{name}-conscrypt.patch
BuildRequires:  ant
BuildRequires:  apache-commons-compress
BuildRequires:  brotli4j
BuildRequires:  fdupes
BuildRequires:  httpcomponents-core5
BuildRequires:  javapackages-local >= 6
BuildRequires:  publicsuffix
BuildRequires:  slf4j
BuildRequires:  zstd-jni
Requires:       publicsuffix
BuildArch:      noarch

%description
HttpClient is a HTTP/1.1 compliant HTTP agent implementation based on
httpcomponents HttpCore. It also provides reusable components for
client-side authentication, HTTP state management, and HTTP connection
management. HttpComponents Client is a successor of and replacement
for Commons HttpClient 3.x. Users of Commons HttpClient are strongly
encouraged to upgrade.

%package        cache
Summary:        Cache module for %{name}
Group:          Development/Libraries/Java

%description    cache
This package provides client side caching for %{name}.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
%{summary}.

%prep
%setup -q -c -a1

# Missing dependencies
rm -r httpclient5-cache/src/main/*/org/apache/hc/client5/http/impl/cache/memcached
%pom_remove_dep :spymemcached httpclient5-cache

rm -r httpclient5-cache/src/main/*/org/apache/hc/client5/http/impl/cache/ehcache
%pom_remove_dep :ehcache-api httpclient5-cache

rm -f httpclient5/src/main/java/org/apache/hc/client5/http/ssl/ConscryptClientTlsStrategy.java
%pom_remove_dep org.conscrypt:conscrypt-openjdk-uber httpclient5
%patch -P 0 -p1

# Fix incorrect conscrypt internal imports in upstream files
sed -i 's/import org.conscrypt.Internal;/import org.apache.hc.core5.annotation.Internal;/' \
    httpclient5/src/main/java/org/apache/hc/client5/http/impl/TunnelRefusedException.java \
    httpclient5/src/main/java/org/apache/hc/client5/http/impl/auth/SaslPrep.java

%build
mkdir -p lib
build-jar-repository -s lib \
    brotli4j/brotli4j \
    zstd-jni/zstd-jni \
    commons-compress \
    httpcomponents-core5/httpcore5-h2 \
    httpcomponents-core5/httpcore5 \
    slf4j/api

ant package javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}

for i in httpclient5 httpclient5-fluent; do
  install -pm 0644 ${i}/target/${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
  %mvn_install_pom ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar
  cp -r ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
done

install -pm 0644 httpclient5-cache/target/httpclient5-cache-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}/httpclient5-cache.jar
%mvn_install_pom httpclient5-cache/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/httpclient5-cache.pom
%add_maven_depmap %{name}/httpclient5-cache.pom %{name}/httpclient5-cache.jar -f cache
cp -r httpclient5-cache/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/httpclient5-cache

%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc README.md RELEASE_NOTES.txt

%files cache -f .mfiles-cache

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt NOTICE.txt

%changelog
