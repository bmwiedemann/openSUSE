#
# spec file for package ant-contrib
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


Name:           ant-contrib
Version:        1.0b3
Release:        0
Summary:        Collection of tasks for Ant
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://ant-contrib.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/ant-contrib/ant-contrib-%{version}-src.tar.gz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/%{name}/%{name}/1.0b3/%{name}-1.0b3.pom
# ASL 2.0 Licence text
# Upstream bug at https://sourceforge.net/tracker/?func=detail&aid=3590371&group_id=36177&atid=416920
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         local-ivy.patch
Patch1:         ant-contrib-antservertest.patch
Patch2:         ant-contrib-pom.patch
Patch3:         ant-contrib-1.0b3-enable-for-task.patch
Patch4:         ant-contrib-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  apache-ivy
BuildRequires:  bcel >= 5.1
BuildRequires:  commons-httpclient
BuildRequires:  commons-logging
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  xerces-j2
Requires:       junit >= 3.8.1
Requires:       xerces-j2
%requires_eq    ant
BuildArch:      noarch

%description
The Ant-Contrib project is a collection of tasks (and at one point
maybe types and other tools) for Apache Ant.

%package        manual
Summary:        Manual for %{name}
Group:          Documentation/Other

%description    manual
Documentation for %{name} tasks.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Requires:       jpackage-utils

%description    javadoc
Api documentation for %{name}.

%prep
%setup -q -n %{name}
cp %{SOURCE1} %{name}-1.0b3.pom
cp %{SOURCE2} LICENSE-2.0.txt
%patch0
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1

find . -name '*.jar' -or -name '*.class' -exec rm -rf {} +

sed -i "s|xercesImpl|xerces-j2|g" ivy.xml ||:
# needs porting to latest ivy
rm -fr src/java/net/sf/antcontrib/net/URLImportTask.java

%build
ant dist

%install
# jars
install -Dpm 644 target/%{name}.jar %{buildroot}%{_javadir}/ant/%{name}.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant/ant-contrib" > %{buildroot}%{_sysconfdir}/ant.d/ant-contrib

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{name}-1.0b3.pom %{buildroot}/%{_mavenpomdir}/JPP.ant-%{name}.pom

echo "call add_maven_depmap JPP.ant-%{name}.pom ant/%{name}.jar"
%add_maven_depmap JPP.ant-%{name}.pom ant/%{name}.jar

%files
%defattr(0644,root,root,0755)
%license target/docs/LICENSE.txt
%doc LICENSE-2.0.txt
%config %{_sysconfdir}/ant.d/%{name}
%{_javadir}/ant/%{name}.jar
%{_mavenpomdir}/JPP.ant-%{name}.pom
%{_datadir}/maven-metadata/%{name}.xml

%files manual
%doc target/docs/manual/tasks/*

%files javadoc
%license target/docs/LICENSE.txt
%doc LICENSE-2.0.txt
%doc %{_javadocdir}/%{name}

%changelog
