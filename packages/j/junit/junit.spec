#
# spec file for package junit
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


Name:           junit
Version:        4.13.2
Release:        0
Summary:        Java regression test package
License:        EPL-1.0
Group:          Development/Libraries/Java
URL:            https://junit.org/junit4/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
Patch0:         0001-Port-to-hamcrest-2.2.patch
Patch1:         0002-remove-usages-of-deprecated-org.junit.Assert.assertT.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  hamcrest >= 2.0
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
Provides:       %{name}-demo = %{version}-%{release}
Obsoletes:      %{name}-demo < %{version}-%{release}
Provides:       %{name}4-demo = %{version}-%{release}
Obsoletes:      %{name}4-demo < %{version}-%{release}
Provides:       %{name}4 = %{version}-%{release}
Obsoletes:      %{name}4 < %{version}-%{release}
BuildArch:      noarch

%description
JUnit is a regression testing framework written by Erich Gamma and Kent Beck.
It is used by the developer who implements unit tests in Java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Provides:       %{name}4-javadoc = %{version}-%{release}
Obsoletes:      %{name}4-javadoc < %{version}-%{release}

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Documentation/Other
Provides:       %{name}4-manual = %{version}-%{release}
Obsoletes:      %{name}4-manual < %{version}-%{release}

%description manual
Documentation for %{name}.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
cp %{SOURCE1} build.xml

find . -type f -name "*.jar" -or -name "*.class" | xargs -t rm -rf

%build
build-jar-repository -s lib hamcrest
ant jar javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# compat symlink
ln -sf %{_javadir}/%{name}.jar %{buildroot}%{_javadir}/%{name}4.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%check

cat > test.java <<EOF
import org.junit.Assert;
class test {

    public static void main(String[] args) {
        Assert.fail("Hello world from junit");
    }

}
EOF
javac -source 8 -target 8 -cp %{buildroot}/%{_javadir}/%{name}.jar test.java
java -cp %{buildroot}/%{_javadir}/%{name}.jar: test 2>&1 | \
   grep 'Exception in thread "main" java.lang.AssertionError: Hello world from junit'

%files -f .mfiles
%license LICENSE-junit.txt
%doc CODING_STYLE.txt README.md acknowledgements.txt
%{_javadir}/%{name}4.jar

%files javadoc
%license LICENSE-junit.txt
%{_javadocdir}/%{name}

%files manual
%license LICENSE-junit.txt
%doc doc/*

%changelog
