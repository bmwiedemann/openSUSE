#
# spec file for package scala
#
# Copyright (c) 2020 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%global fullversion %{version}
%global release_repository http://nexus.scala-tools.org/content/repositories/releases
%global snapshot_repository http://nexus.scala-tools.org/content/repositories/snapshots
%global jansi_jar %{_javadir}/jansi/jansi.jar
%global jline2_jar %{_javadir}/jline/jline.jar
%global scaladir %{_datadir}/scala
%global base_name scala
%define __requires_exclude .*org\.apache\.ant.*
Version:        2.10.7
Release:        0
Summary:        A hybrid functional/object-oriented language for the JVM
License:        BSD-3-Clause AND CC0-1.0 AND SUSE-Public-Domain
Group:          Development/Libraries/Java
URL:            http://www.scala-lang.org/
Source0:        %{base_name}-%{version}.tar.xz
Source1:        scala-library-2.10.0-bnd.properties
# git log --pretty=format:"%H%n%ci" v%{version} | head -n 2 | sed -e 's/\-//g' -e 's/\s\+.*//g'
Source3:        scala.gitinfo
Source4:        http://www.scala-lang.org/files/archive/%{base_name}-%{version}.tgz
Source23:       scala-mime-info.xml
Source24:       scala.ant.d
# Change the default classpath (SCALA_HOME)
Patch1:         scala-2.10.0-tooltemplate.patch
# Use system jline2 instead of bundled jline2
Patch2:         scala-2.10.3-use_system_jline.patch
# change org.scala-lang jline in org.sonatype.jline jline
Patch3:         scala-2.10.3-compiler-pom.patch
# Patch Swing module for JDK 1.7
Patch4:         scala-2.10.2-java7.patch
# fix incompatibilities with JLine 2.7
Patch6:         scala-2.10-jline.patch
Patch8:         scala-2.10.4-build_xml.patch
# Stop scaladoc from trying to bundle non-existent resources that were
# removed due to being in object form only, whithout sources
Patch9:         scala-2.10.6-scaladoc-resources.patch
Patch10:        scala-2.10.7-source6.patch
Patch11:        scala-2.10.7-lines.patch
Patch12:        scala-2.10.7-java8compat.patch
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  ant-junit
BuildRequires:  aqute-bnd
BuildRequires:  graphviz
BuildRequires:  java-devel >= 1.7
BuildRequires:  javapackages-local
BuildRequires:  jline >= 2.10
BuildRequires:  junit
Requires:       jansi
Requires:       java-headless >= 1.7
# Require full javapackages-tools since scripts use
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Requires:       jline >= 2.10
BuildArch:      noarch
%if %{with bootstrap}
Name:           %{base_name}-bootstrap
%else
Name:           %{base_name}
BuildRequires:  %{base_name}-bootstrap >= %{version}
Provides:       %{base_name}-bootstrap = %{version}-%{release}
Obsoletes:      %{base_name}-bootstrap
%endif

%description
Scala is a general purpose programming language designed to express
common programming patterns in a concise and type-safe way. It
integrates features of object-oriented and functional languages. It
is also interoperable with Java.

%if %{without bootstrap}
%package apidoc
Summary:        Documentation for the Scala programming language
Group:          Documentation/HTML
%if %{without bootstrap}
Obsoletes:      %{base_name}-bootstrap-apidoc
%endif

%description apidoc
Scala is a general purpose programming language for the JVM that blends
object-oriented and functional programming. This package provides
reference and API documentation for the Scala programming language.
%endif

%package swing
Summary:        The swing library for the Scala programming languages
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}
Requires:       java >= 1.7
%if %{without bootstrap}
Obsoletes:      %{base_name}-bootstrap-swing
%endif

%description swing
This package contains the swing library for the Scala programming languages.
This library is required to develop GUI-related applications in Scala.
The release provided by this package is not the original version from upstream
because this version is not compatible with JDK 1.7.

%package -n ant-%{name}
Summary:        Development files for Scala
Group:          Development/Libraries/Java
Requires:       ant
Requires:       scala = %{version}-%{release}
%if %{without bootstrap}
Obsoletes:      ant-%{base_name}-bootstrap
%endif

%description -n ant-%{name}
Scala is a general purpose programming language for the JVM that blends
object-oriented and functional programming. This package enables support for
the Scala ant tasks.

%prep
%setup -q -n %{base_name}-%{version}
%patch1 -p1 -b .tool
%patch2 -p1 -b .sysjline
%patch3 -p1 -b .compiler-pom
%patch4 -p1 -b .jdk7
%patch6 -p1 -b .rvk
%patch8 -p1 -b .bld
%patch9 -p1 -b .scaladoc
%patch10 -p1 -b .source6
%patch11 -p1 -b .jdk11
%patch12 -p1 -b .java8compat

echo "starr.version=2.10.4\nstarr.use.released=0" > starr.number

pushd src
rm -rf jline
popd

sed -i '/is not supported by/d' build.xml
sed -i '/exec.*pull-binary-libs.sh/d' build.xml

%if %{with bootstrap}
%global do_bootstrap -DdoBootstrapBuild=yes
%global docs_target %{nil}
tar -xzvf %{SOURCE4} --strip-components=1 %{base_name}-%{version}/lib
%else
%global do_bootstrap %{nil}
%global docs_target docs
%endif

pushd lib
%if %{without bootstrap}
    rm -rf scala-compiler.jar
    ln -s $(find-jar scala/scala-compiler) scala-compiler.jar
    rm -rf scala-library.jar
    ln -s $(find-jar scala/scala-library) scala-library.jar
    rm -rf scala-reflect.jar
    ln -s $(find-jar scala/scala-reflect) scala-reflect.jar
%endif
  pushd ant
    rm -rf ant.jar
    rm -rf ant-contrib.jar
    ln -s $(build-classpath ant.jar) ant.jar
    ln -s $(build-classpath ant/ant-contrib) ant-contrib.jar
  popd
popd

sed -i -e 's!@JLINE@!%{jline2_jar}!g' build.xml

echo echo $(head -n 1 %{SOURCE3}) > tools/get-scala-commit-sha
echo echo $(tail -n 1 %{SOURCE3}) > tools/get-scala-commit-date
chmod 755 tools/get-scala-*

%build

export ANT_OPTS="-Xms2048m -Xmx2048m %{do_bootstrap}"

# Add the -verbose flag to scalac on zero architectures. The build
# is slow, OBS thinks it is stuck and kills it before it has chance
# to finish
%ant \
	build %{docs_target} || exit 1
pushd build/pack/lib
mv scala-library.jar scala-library.jar.no
bnd wrap --properties %{SOURCE1} --output scala-library.jar \
    --version "%{version}" scala-library.jar.no
popd

%install

install -d %{buildroot}%{_bindir}
for prog in scaladoc fsc scala scalac scalap; do
        install -p -m 755 build/pack/bin/$prog %{buildroot}%{_bindir}
done

install -dm 0755 %{buildroot}%{scaladir}/lib
install -dm 0755 %{buildroot}%{_javadir}/%{base_name}
install -dm 0755 %{buildroot}%{_mavenpomdir}

# XXX: add scala-partest when it works again
for libname in scala-compiler \
    scala-library \
    scala-reflect \
    scalap \
    scala-swing ; do
        sed -i "s|@VERSION@|%{fullversion}|" src/build/maven/$libname-pom.xml
        sed -i "s|@RELEASE_REPOSITORY@|%{release_repository}|" src/build/maven/$libname-pom.xml
        sed -i "s|@SNAPSHOT_REPOSITORY@|%{snapshot_repository}|" src/build/maven/$libname-pom.xml
        install -pm 0644 build/pack/lib/$libname.jar %{buildroot}%{_javadir}/%{base_name}/$libname.jar
        ln -sf $(abs2rel %{_javadir}/%{base_name}/$libname.jar %{scaladir}/lib) %{buildroot}%{scaladir}/lib
        # climbing-nemesis uses the old JPP naming convention
        install -pm 0644 src/build/maven/$libname-pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{base_name}-$libname.pom
        if [ $libname == scala-swing ]; then
          %add_maven_depmap JPP.%{base_name}-$libname.pom %{base_name}/$libname.jar -f swing
        else
          %add_maven_depmap JPP.%{base_name}-$libname.pom %{base_name}/$libname.jar
        fi
done
ln -s $(abs2rel %{jline2_jar} %{scaladir}/lib) %{buildroot}%{scaladir}/lib
ln -s $(abs2rel %{jansi_jar} %{scaladir}/lib) %{buildroot}%{scaladir}/lib

%if %{without bootstrap}
install -d %{buildroot}%{_sysconfdir}/ant.d
install -p -m 644 %{SOURCE24} %{buildroot}%{_sysconfdir}/ant.d/scala
%endif

install -d %{buildroot}%{_datadir}/mime/packages/
install -p -m 644 %{SOURCE23} %{buildroot}%{_datadir}/mime/packages/

sed -i -e 's,@JAVADIR@,%{_javadir},g' -e 's,@DATADIR@,%{_datadir},g' %{buildroot}%{_bindir}/*

%if %{without bootstrap}
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 build/scaladoc/manual/man/man1/* %{buildroot}%{_mandir}/man1
%endif

%files -f .mfiles
%{_bindir}/*
%dir %{_datadir}/%{base_name}
%dir %{_datadir}/%{base_name}/lib
%{_datadir}/%{base_name}/lib/*.jar
%exclude %{_datadir}/%{base_name}/lib/scala-swing.jar
%{_datadir}/mime/packages/*
%license docs/LICENSE
%if %{without bootstrap}
%{_mandir}/man1/*
%endif

%files swing -f .mfiles-swing
%license docs/LICENSE
%{_datadir}/%{base_name}/lib/scala-swing.jar

%if %{without bootstrap}
%files -n ant-%{name}
# Following is plain config because the ant task classpath could change from
# release to release
%config %{_sysconfdir}/ant.d/*
%license docs/LICENSE

%files apidoc
%doc build/scaladoc/library/*
%license docs/LICENSE
%endif

%changelog
