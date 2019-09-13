#
# spec file for package apache-commons-exec
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


%global base_name exec
%global short_name commons-%{base_name}
%bcond_with tests
Name:           apache-commons-exec
Version:        1.3
Release:        0
Summary:        Java library to reliably execute external processes from within the JVM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/exec/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         commons-exec-1.3-build_xml.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
%endif

%description
Commons Exec is a library for dealing with external process execution and
environment management in Java.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1

# Fix wrong end-of-line encoding
dos2unix LICENSE.txt NOTICE.txt RELEASE-NOTES.txt STATUS

# Shell scripts used for unit tests must be executable (see
# http://commons.apache.org/exec/faq.html#environment-testing)
chmod a+x src/test/scripts/*.sh

# Skip Exec57Test (it is unstable), see rhbz#1202260
find -name Exec57Test.java -delete

%pom_remove_parent .

%build
%{ant} \
%if %{without tests}
    -Dmaven.test.skip=true \
%endif
    jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc STATUS RELEASE-NOTES.txt
%{_javadir}/%{name}.jar

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
