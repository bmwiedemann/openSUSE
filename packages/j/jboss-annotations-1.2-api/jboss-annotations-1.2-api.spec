#
# spec file for package jboss-annotations-1.2-api
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


%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global oname jboss-annotations-api_1.2_spec
Name:           jboss-annotations-1.2-api
Version:        1.0.2
Release:        0
Summary:        Java EE Annotations 1.2 API
License:        CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/jboss/jboss-annotations-api_spec
Source0:        https://github.com/jboss/jboss-annotations-api_spec/archive/%{oname}-%{namedversion}/jboss-annotations-api_spec-%{oname}-%{namedversion}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
The Java EE  Annotations 1.2 API classes.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jboss-annotations-api_spec-%{oname}-%{namedversion}
cp %{SOURCE1} build.xml

# Fix incorrect-fsf-address
sed -i "s,59,51,;s,Temple Place,Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%pom_remove_parent

%{mvn_file} :%{oname} %{name}

%build
%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{oname}-%{namedversion}.jar %{buildroot}%{_javadir}/%{oname}.jar
ln -sf %{oname}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{oname}.pom
%add_maven_depmap %{oname}.pom %{oname}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README
%license LICENSE
%{_javadir}/%{name}.jar

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
