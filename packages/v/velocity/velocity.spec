#
# spec file for package velocity
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


Name:           velocity
Version:        1.7
Release:        0
Summary:        Java-based template engine
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://velocity.apache.org/
Source0:        http://www.apache.org/dist/velocity/engine/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}.pom
Patch0:         velocity-build_xml.patch
BuildRequires:  ant >= 1.6.5
BuildRequires:  ant-junit
BuildRequires:  antlr
BuildRequires:  avalon-logkit
BuildRequires:  commons-collections
BuildRequires:  commons-lang
BuildRequires:  commons-logging
BuildRequires:  fdupes
BuildRequires:  hsqldb
BuildRequires:  javapackages-local
BuildRequires:  jdom >= 1.0-1
BuildRequires:  junit
BuildRequires:  log4j >= 1.1
BuildRequires:  oro
BuildRequires:  plexus-classworlds
BuildRequires:  servletapi4
BuildRequires:  werken-xpath
Requires:       avalon-logkit
Requires:       commons-collections
Requires:       commons-lang
Requires:       java >= 1.6.0
Requires:       jdom >= 1.0-1
Requires:       log4j >= 1.1
Requires:       oro
Requires:       servletapi4
Requires:       werken-xpath
BuildArch:      noarch

%description
Velocity is a Java-based template engine. It permits anyone to use the
simple yet powerful template language to reference objects defined in
Java code.
When Velocity is used for web development, Web designers can work in
parallel with Java programmers to develop web sites according to the
Model-View-Controller (MVC) model, meaning that web page designers can
focus solely on creating a site that looks good, and programmers can
focus solely on writing top-notch code. Velocity separates Java code
from the web pages, making the web site more maintainable over the long
run and providing a viable alternative to Java Server Pages (JSPs) or
PHP.
Velocity's capabilities reach well beyond the realm of web sites; for
example, it can generate SQL and PostScript and XML (see Anakia for more
information on XML transformations) from templates. It can be used
either as a standalone utility for generating source code and reports,
or as an integrated component of other systems. Velocity also provides
template services for the Turbine web application framework.
Velocity+Turbine provides a template service that will allow web
applications to be developed according to a true MVC model.

%package        manual
Summary:        Manual for %{name}
Group:          Development/Libraries/Java

%description    manual
Velocity is a Java-based template engine. It permits anyone to use the
simple yet powerful template language to reference objects defined in
Java code.
When Velocity is used for web development, Web designers can work in
parallel with Java programmers to develop web sites according to the
Model-View-Controller (MVC) model, meaning that web page designers can
focus solely on creating a site that looks good, and programmers can
focus solely on writing top-notch code. Velocity separates Java code
from the web pages, making the web site more maintainable over the long
run and providing a viable alternative to Java Server Pages (JSPs) or
PHP.
Velocity's capabilities reach well beyond the realm of web sites; for
example, it can generate SQL and PostScript and XML (see Anakia for more
information on XML transformations) from templates. It can be used
either as a standalone utility for generating source code and reports,
or as an integrated component of other systems. Velocity also provides
template services for the Turbine web application framework.
Velocity+Turbine provides a template service that will allow web
applications to be developed according to a true MVC model.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description    javadoc
Velocity is a Java-based template engine. It permits anyone to use the
simple yet powerful template language to reference objects defined in
Java code.
When Velocity is used for web development, Web designers can work in
parallel with Java programmers to develop web sites according to the
Model-View-Controller (MVC) model, meaning that web page designers can
focus solely on creating a site that looks good, and programmers can
focus solely on writing top-notch code. Velocity separates Java code
from the web pages, making the web site more maintainable over the long
run and providing a viable alternative to Java Server Pages (JSPs) or
PHP.
Velocity's capabilities reach well beyond the realm of web sites; for
example, it can generate SQL and PostScript and XML (see Anakia for more
information on XML transformations) from templates. It can be used
either as a standalone utility for generating source code and reports,
or as an integrated component of other systems. Velocity also provides
template services for the Turbine web application framework.
Velocity+Turbine provides a template service that will allow web
applications to be developed according to a true MVC model.

%package        demo
Summary:        Demo for %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description    demo
Velocity is a Java-based template engine. It permits anyone to use the
simple yet powerful template language to reference objects defined in
Java code.
When Velocity is used for web development, Web designers can work in
parallel with Java programmers to develop web sites according to the
Model-View-Controller (MVC) model, meaning that web page designers can
focus solely on creating a site that looks good, and programmers can
focus solely on writing top-notch code. Velocity separates Java code
from the web pages, making the web site more maintainable over the long
run and providing a viable alternative to Java Server Pages (JSPs) or
PHP.
Velocity's capabilities reach well beyond the realm of web sites; for
example, it can generate SQL and PostScript and XML (see Anakia for more
information on XML transformations) from templates. It can be used
either as a standalone utility for generating source code and reports,
or as an integrated component of other systems. Velocity also provides
template services for the Turbine web application framework.
Velocity+Turbine provides a template service that will allow web
applications to be developed according to a true MVC model.

%prep
%setup -q
# Remove all binary libs used in compiling the package.
# Note that velocity has some jar files containing macros under
# examples and test that should not be removed.
#find build -name '*.jar' -exec rm -f \{\} \;
for j in $(find . -name "*.jar" | grep -v /test/); do
    mv $j $j.no
done
%patch0 -b .sav0

cp %{SOURCE1} pom.xml

%pom_remove_parent pom.xml

%build
#export JAVA_HOME=%{_jvmdir}/java-1.5.0
# Use servletapi4 instead of servletapi5 in CLASSPATH
mkdir -p bin/test-lib
pushd bin/test-lib
ln -sf $(build-classpath hsqldb)
ln -sf $(build-classpath junit)
popd
mkdir -p bin/lib
pushd bin/lib
ln -sf $(build-classpath ant)
ln -sf $(build-classpath antlr)
ln -sf $(build-classpath avalon-logkit)
ln -sf $(build-classpath commons-collections)
ln -sf $(build-classpath commons-lang)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath jdom)
ln -sf $(build-classpath log4j)
ln -sf $(build-classpath oro)
# Use servletapi4 instead of servletapi5 in CLASSPATH
ln -sf $(build-classpath servletapi4)
ln -sf $(build-classpath werken-xpath)
ln -sf $(build-classpath plexus/classworlds)
popd
export CLASSPATH=$(build-classpath jdom commons-collections commons-lang werken-xpath antlr)
CLASSPATH=$CLASSPATH:$(pwd)/test/texen-classpath/test.jar
export OPT_JAR_LIST="ant/ant-junit junit"
#FIXME: tests failed on CommonsExtPropTestCase
#but resulting files seems to be same
ant \
  -Djavac.source=1.6 -Djavac.target=1.6 \
  -buildfile build/build.xml \
  jar javadocs

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 bin/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a velocity:velocity

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

rm -rf docs/api

# zero-length file
rm -r test/issues/velocity-537/compare/velocity537.vm.cmp
# data
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr examples test %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%license LICENSE NOTICE
%doc README.txt

%files manual
%doc docs/*

%files javadoc
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
