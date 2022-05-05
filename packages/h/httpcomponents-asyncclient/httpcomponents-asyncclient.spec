#
# spec file for package httpcomponents-asyncclient
#
# Copyright (c) 2022 SUSE LLC
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


Name:           httpcomponents-asyncclient
Version:        4.1.4
Release:        0
Summary:        Apache components to build asynchronous client side HTTP services
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://hc.apache.org/
Source0:        https://archive.apache.org/dist/httpcomponents/httpasyncclient/source/%{name}-%{version}-src.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
%if 0%{?rhel} >= 9
BuildRequires:  xmvn-tools
BuildRequires:  xmvn-minimal
%endif
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient-cache)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore-nio)
BuildRequires:  mvn(org.apache.httpcomponents:project:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildArch:      noarch

%description
Asynch HttpClient is a HTTP/1.1 compliant HTTP agent implementation based on
HttpCore NIO and HttpClient components. It is a complementary module to
Apache HttpClient intended for special cases where ability to handle
a great number of concurrent connections is more important than performance
in terms of a raw data throughput.

%package cache
Summary:        Apache HttpAsyncClient Cache
Group:          Development/Libraries/Java

%description cache
This package provides client side caching for %{name}.

%package parent
Summary:        Apache HttpAsyncClient Parent POM
Group:          Development/Libraries/Java

%description parent
Apache HttpAsyncClient Parent POM.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# Cleanup
find . -name "*.class" -delete
find . -name "*.jar" -type f -delete

# Use unavalable org.apache.httpcomponents:hc-stylecheck:jar:1
%pom_remove_plugin :maven-checkstyle-plugin
# Unwanted
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
# Unavailable
%pom_remove_plugin :clirr-maven-plugin

%pom_disable_module httpasyncclient-osgi

# Prevent build failure
%pom_remove_plugin -r :apache-rat-plugin

# Unavalable test deps: org.easymock:easymockclassextension org.apache.httpcomponents:httpclient-cache:test-jar
%pom_xpath_remove "pom:dependency[pom:type = 'test-jar']" httpasyncclient-cache
%pom_xpath_remove "pom:dependency[pom:scope = 'test']" httpasyncclient-cache
rm -r httpasyncclient-cache/src/test/java

# Add OSGi support
for p in httpasyncclient httpasyncclient-cache; do
 %pom_remove_plugin :maven-jar-plugin ${p}
 %pom_xpath_set "pom:project/pom:packaging" bundle ${p}
 %pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 ${p} "
 <extensions>true</extensions>
 <configuration>
  <instructions>
    <Export-Package>*</Export-Package>
  </instructions>
  <excludeDependencies>true</excludeDependencies>
 </configuration>"
done

%{mvn_file} org.apache.httpcomponents:httpasyncclient httpasyncclient
%{mvn_file} org.apache.httpcomponents:httpasyncclient-cache httpasyncclient-cache

%build

%{mvn_build} -f -s -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
    -Dsource=8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-httpasyncclient
%doc README.txt RELEASE_NOTES.txt
%license LICENSE.txt NOTICE.txt

%files cache -f .mfiles-httpasyncclient-cache
%license LICENSE.txt NOTICE.txt

%files parent -f .mfiles-%{name}
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
