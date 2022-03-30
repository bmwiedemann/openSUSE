#
# spec file for package stax-ex
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


Name:           stax-ex
Version:        1.8
Release:        0
Summary:        StAX API extensions
License:        CDDL-1.0 OR GPL-2.0-only
Group:          Development/Libraries/Java
URL:            https://stax-ex.dev.java.net
Source0:        https://github.com/javaee/metro-%{name}/archive/%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  mvn(javax.activation:activation)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
This project develops a few extensions to complement JSR-173 StAX API in the
following area.

* Enable parser instance reuse (which is important in the
  high-performance environment like JAXB and JAX-WS)
* Improve the support for reading from non-text XML infoset,
  such as FastInfoset.
* Improve the namespace support.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n metro-%{name}-%{version}

# Remove bundled jar files:
find . -name '*.jar' -print -delete
find . -name '*.class' -print -delete

pushd %{name}

%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_add_dep javax.xml.bind:jaxb-api::provided

# Convert the license to UTF-8:
mv LICENSE.txt LICENSE.txt.tmp
iconv -f ISO-8859-1 -t UTF-8 LICENSE.txt.tmp > LICENSE.txt
dos2unix LICENSE.txt

%{mvn_file} :stax-ex %{name}

popd

%build
pushd %{name}

%{mvn_build} -f -- -Dproject.build.sourceEncoding=UTF-8 -Dsource=8
popd

%install
pushd %{name}
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f %{name}/.mfiles
%license %{name}/LICENSE.txt

%files javadoc -f %{name}/.mfiles-javadoc
%license %{name}/LICENSE.txt

%changelog
