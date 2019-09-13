#
# spec file for package xml-commons-resolver
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define resolverdir %{_sysconfdir}/java/resolver
Name:           xml-commons-resolver
Version:        1.2
Release:        0
Summary:        Resolver subproject of xml-commons
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://xerces.apache.org/xml-commons/components/resolver/
Source0:        http://www.apache.org/dist/xerces/xml-commons/%{name}-%{version}.tar.gz
Source5:        %{name}-pom.xml
Source6:        %{name}-resolver.1
Source7:        %{name}-xparse.1
Source8:        %{name}-xread.1
Source10:       %{name}-CatalogManager.properties
Patch0:         %{name}-1.2-crosslink.patch
Patch1:         %{name}-1.2-osgi.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
#!BuildIgnore:  xerces-j2 xml-apis xml-resolver
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Conflicts:      xml-commons-resolver-bootstrap
Provides:       %{name}10
Provides:       %{name}11
Provides:       %{name}12
Provides:       xerces-j2-xml-resolver
Provides:       xml-commons
Obsoletes:      %{name}10
Obsoletes:      %{name}11
Obsoletes:      %{name}12
Obsoletes:      xerces-j2-xml-resolver
Obsoletes:      xml-commons
Provides:       xml-resolver = %{version}-%{release}
BuildArch:      noarch

%description
Resolver subproject of xml-commons.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

cp %{SOURCE5} pom.xml

# remove all binary libs and prebuilt javadocs
find . -name "*.jar" -delete
rm -rf docs
sed -i 's/\r//' KEYS LICENSE.resolver.txt NOTICE-resolver.txt

%pom_remove_parent .

%build
%{ant} -f resolver.xml -Dant.build.javac.source=6 -Dant.build.javac.target=6 jar javadocs

%install
# jar
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 build/resolver.jar %{buildroot}%{_javadir}/%{name}.jar
pushd %{buildroot}%{_javadir}
  for i in xerces-j2-xml-resolver xml-resolver %{name}10 %{name}11 %{name}12; do
    ln -s %{name}.jar ${i}.jar
  done
popd

# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -a build/apidocs/resolver/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

# Scripts
mkdir -p %{buildroot}%{_bindir}
%jpackage_script org.apache.xml.resolver.apps.resolver "" "" %{name} xml-resolver true
%jpackage_script org.apache.xml.resolver.apps.xread "" "" %{name} xml-xread true
%jpackage_script org.apache.xml.resolver.apps.xparse "" "" %{name} xml-xparse true

# Man pages
install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE6} %{buildroot}%{_mandir}/man1/xml-resolver.1
install -p -m 644 %{SOURCE7} %{buildroot}%{_mandir}/man1/xml-xparse.1
install -p -m 644 %{SOURCE8} %{buildroot}%{_mandir}/man1/xml-xread.1

# Central CatalogManager.properties
install -d -m 755 %{buildroot}%{resolverdir}
install -m 0644 %{SOURCE10} %{buildroot}%{resolverdir}/CatalogManager.properties

%files -f .mfiles
%license LICENSE.resolver.txt
%doc KEYS NOTICE-resolver.txt
%{_mandir}/man1/*
%{_bindir}/xml-*
%config(noreplace) %{resolverdir}/*
%dir %{resolverdir}
%{_javadir}/*

%files javadoc
%license LICENSE.resolver.txt
%doc NOTICE-resolver.txt
%{_javadocdir}/%{name}

%changelog
