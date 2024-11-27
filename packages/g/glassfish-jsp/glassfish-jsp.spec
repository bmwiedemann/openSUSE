#
# spec file for package glassfish-jsp
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


%global artifactId javax.servlet.jsp
%global jspspec 2.3
Name:           glassfish-jsp
Version:        2.3.4
Release:        0
Summary:        Glassfish J2EE JSP API implementation
License:        Apache-2.0 AND (CDDL-1.1 OR GPL-2.0-only WITH Classpath-exception-2.0)
Group:          Development/Libraries/Java
URL:            https://glassfish.org
Source0:        %{artifactId}-%{version}.tar.xz
Source1:        https://raw.githubusercontent.com/javaee/javaee-jsp-api/%{artifactId}-%{version}/LICENSE
Source2:        http://www.apache.org/licenses/LICENSE-2.0
Patch0:         %{name}-build-eclipse-compilers.patch
Patch1:         %{name}-port-to-servlet-3.1.patch
Patch2:         %{name}-port-to-servlet-4.0.patch
Patch3:         Tag.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  xmvn-subst
BuildRequires:  mvn(javax.servlet.jsp:javax.servlet.jsp-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(org.glassfish:javax.el)
# make sure the symlinks will be correct
Requires:       glassfish-jsp-api
Provides:       javax.servlet.jsp
Provides:       jsp = %{jspspec}
Provides:       jsp%{jspspec}
BuildArch:      noarch

%description
This project provides a container independent implementation of JSP
2.3. The main goals are:
  * Improves current implementation: bug fixes and performance
    improvements
  * Provides API for use by other tools, such as Netbeans
  * Provides a sandbox for new JSP features; provides a reference
    implementation of next JSP spec.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%autosetup -n %{artifactId}-%{version} -p1

%pom_add_dep org.eclipse.jdt:core::provided
%pom_add_dep org.apache.ant:ant::provided

%pom_remove_plugin :maven-javadoc-plugin

%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:source" "1.8"
%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:target" "1.8"

cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%{mvn_alias} : "org.eclipse.jetty.orbit:org.apache.jasper.glassfish"

# compat symlink
%{mvn_file} : %{name}/javax.servlet.jsp %{name}

%build
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

# install j2ee api symlinks
install -d -m 755 %{buildroot}%{_javadir}/javax.servlet.jsp/
pushd %{buildroot}%{_javadir}/javax.servlet.jsp/
for jar in ../%{name}/*jar; do
    ln -sf $jar .
done
# copy jsp-api so that build-classpath will include dep as well
build-jar-repository -p . glassfish-jsp-api
xmvn-subst -R %{buildroot} -s .
popd

%files -f .mfiles
%{_javadir}/javax.servlet.jsp
%license LICENSE LICENSE-2.0

%files javadoc -f .mfiles-javadoc
%license LICENSE LICENSE-2.0

%changelog
