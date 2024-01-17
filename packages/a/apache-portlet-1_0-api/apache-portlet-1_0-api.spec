#
# spec file for package apache-portlet-1_0-api
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define short_name portlet
%define base_name %{short_name}-1.0-api
Name:           apache-portlet-1_0-api
Version:        1.0
Release:        0
Summary:        Portlet API 1.0 from Jetspeed2
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://portals.apache.org/jetspeed-2/
Source0:        apache-portlet-1.0-api.tar.gz
# svn export http://svn.apache.org/repos/asf/portals/jetspeed-2/tags/JETSPEED-RELEASE-2.0/portlet-api/
Source1:        apache-portlet-1.0-api-pom.xml
Source2:        apache-portlet-1.0-api-LICENSE.TXT
Source3:        apache-portlet-1.0-api-build.xml
BuildRequires:  ant >= 1.6
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
Provides:       portlet = %{version}
Provides:       portlet-1.0-api = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Java Standard Portlet API accoring to JSR-168, from Jetspeed-2 .

%package javadoc
Summary:        Portlet API 1.0 from Jetspeed2
Group:          Development/Libraries/Java

%description javadoc
Java Standard Portlet API accoring to JSR-168, from Jetspeed-2 .

%{summary}.

%prep
%setup -q -n apache-portlet-1.0-api
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
cp %{SOURCE1} pom.xml
cp %{SOURCE3} build.xml

%build
ant jar javadoc

%install
install -d -m 755 %{buildroot}%{_javadir}
install -m 0644 target/portlet-api-1.0.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && ln -sf %{name}-%{version}.jar %{base_name}-%{version}.jar)
(cd %{buildroot}%{_javadir} && ln -sf %{name}-%{version}.jar portlet-api-%{version}.jar)
# create unversioned symlinks
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} $(echo $jar | sed -e 's+-%{version}\.jar+.jar+'); done)

#poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-portlet-api.pom
%add_maven_depmap JPP-portlet-api.pom portlet-api.jar

#javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* \
        %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp %{SOURCE2} %{buildroot}%{_docdir}/%{name}-%{version}/LICENSE.TXT

%files
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}/LICENSE.TXT
%dir %{_docdir}/%{name}-%{version}
%{_javadir}/%{name}*.jar
%{_javadir}/%{base_name}*.jar
%{_javadir}/portlet-api*.jar
%{_datadir}/maven-metadata/%{name}.xml
%{_mavenpomdir}/*

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
