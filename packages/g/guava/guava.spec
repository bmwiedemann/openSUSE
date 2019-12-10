#
# spec file for package guava
#
# Copyright (c) 2019 SUSE LLC
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


Name:           guava
Version:        25.0
Release:        0
Summary:        Google Core Libraries for Java
License:        Apache-2.0 AND CC0-1.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/guava
Source0:        https://github.com/google/guava/archive/v%{version}.tar.gz
Source1:        %{name}-build.tar.xz
Patch0:         %{name}-%{version}-java8compat.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  jsr-305
BuildRequires:  junit
Requires:       mvn(com.google.code.findbugs:jsr305)
BuildArch:      noarch

%description
Guava is a suite of core and expanded libraries that include
utility classes, Google's collections, io classes, and much
much more.
This project is a complete packaging of all the Guava libraries
into a single jar.  Individual portions of Guava can be used
by downloading the appropriate module and its dependencies.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%package testlib
Summary:        The guava-testlib artifact
Group:          Development/Libraries/Java
Requires:       mvn(com.google.code.findbugs:jsr305)
Requires:       mvn(com.google.guava:guava)
Requires:       mvn(junit:junit)

%description testlib
guava-testlib provides additional functionality for conveninent unit testing

%prep
%setup -q -a1
%patch0 -p1

find . -name '*.jar' -delete

%pom_disable_module guava-gwt
%pom_disable_module guava-tests

%pom_remove_plugin -r :animal-sniffer-maven-plugin
# Downloads JDK source for doc generation
%pom_remove_plugin :maven-dependency-plugin guava

%pom_xpath_inject /pom:project/pom:build/pom:plugins/pom:plugin/pom:configuration/pom:instructions "<_nouses>true</_nouses>" guava/pom.xml

%pom_remove_dep -r :animal-sniffer-annotations
%pom_remove_dep -r :error_prone_annotations
%pom_remove_dep -r :j2objc-annotations
%pom_remove_dep -r org.checkerframework:

annotations=$(
    find -name '*.java' \
    | xargs grep -F -h \
        -e 'import com.google.j2objc.annotations' \
        -e 'import com.google.errorprone.annotation' \
        -e 'import org.codehaus.mojo.animal_sniffer' \
        -e 'import org.checkerframework' \
    | sort -u \
    | sed 's/.*\.\([^.]*\);/\1/' \
    | paste -sd\|
)
# guava started using quite a few annotation libraries for code quality, which
# we don't have. This ugly regex is supposed to remove their usage from the code
find -name '*.java' | xargs sed -ri \
    "s/^import .*\.($annotations);//;s/@($annotations)"'\>\s*(\((("[^"]*")|([^)]*))\))?//g'

for mod in guava guava-testlib; do
  %pom_remove_parent ${mod}
  %pom_xpath_inject pom:project '
    <groupId>com.google.guava</groupId>
    <version>%{version}</version>' ${mod}
done

%pom_change_dep -r -f ::::: :::::

%build
mkdir -p lib
build-jar-repository -s lib junit jsr-305
%ant -Dtest.skip=true package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 %{name}/target/%{name}-%{version}*.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -pm 0644 %{name}-testlib/target/%{name}-testlib-%{version}*.jar %{buildroot}%{_javadir}/%{name}/%{name}-testlib.jar

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 %{name}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar -f %{name}
install -pm 0644 %{name}-testlib/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-testlib.pom
%add_maven_depmap %{name}/%{name}-testlib.pom %{name}/%{name}-testlib.jar -f %{name}-testlib

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r %{name}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/%{name}
cp -r %{name}-testlib/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/%{name}-testlib
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-guava
%doc CONTRIBUTORS README*
%license COPYING

%files javadoc
%{_javadocdir}/%{name}
%license COPYING

%files testlib -f .mfiles-guava-testlib

%changelog
