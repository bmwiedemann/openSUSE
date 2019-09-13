#
# spec file for package icu4j
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2007, JPackage Project
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


%global majorver 63
%global minorver 1
%global oldmajorver 62
Name:           icu4j
Version:        %{majorver}.%{minorver}
Release:        0
Summary:        International Components for Unicode for Java
License:        MIT AND EPL-1.0
Group:          Development/Libraries/Java
URL:            http://site.icu-project.org/
#CAUTION
#to create a tarball use following procedure
#svn co http://source.icu-project.org/repos/icu/tags/release-%{majorver}-%{minorver}/icu4j icu4j-%{majorver}.%{minorver}
#tar caf icu4j-%{majorver}.%{minorver}.tar.xz icu4j-%{majorver}.%{minorver}/
Source0:        %{name}-%{version}.tar.xz
Patch0:         icu4j-jdk10plus.patch
# Add better OSGi metadata to core jar
Patch1:         improve-osgi-manifest.patch
Patch2:         icu4j-63.1-java8compat.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-javadoc
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
The International Components for Unicode (ICU) library provides robust and
full-featured Unicode services on a wide variety of platforms. ICU supports
the most current version of the Unicode standard, and provides support for
supplementary characters (needed for GB 18030 repertoire support).

Java provides a very strong foundation for global programs, and IBM and the
ICU team played a key role in providing globalization technology into Sun's
Java. But because of its long release schedule, Java cannot always keep
up-to-date with evolving standards. The ICU team continues to extend Java's
Unicode and internationalization support, focusing on improving
performance, keeping current with the Unicode standard, and providing
richer APIs, while remaining as compatible as possible with the original
Java text and internationalization API design.

%package charset
Summary:        Charset converter library of %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description charset
Charset converter library of %{name}.

%package localespi
Summary:        Locale SPI library of %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description localespi
Locale SPI library of %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc documentation for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1
%patch2 -p1

sed -i 's/\r//' APIChangeReport.html
sed -i 's/\r//' readme.html

sed --in-place "s/ .*bootclasspath=.*//g" build.xml
sed --in-place "s/<date datetime=.*when=\"after\"\/>//" build.xml
sed --in-place "/javac1.3/d" build.xml
sed --in-place "s:%{_prefix}/lib:%{_libdir}:g" build.xml

rm tools/build/src/com/ibm/icu/dev/tool/docs/ICUTaglet*

# The versions in build.properties were not updated since some time
rm build.properties
echo "api.doc.version=%{version}" >> build.properties
echo "maven.pom.ver=%{version}" >> build.properties
echo "release.file.ver=%{majorver}_%{minorver}" >> build.properties
echo "api.report.version=%{majorver}" >> build.properties
echo "api.report.prev.version=%{oldmajorver}" >> build.properties
echo "jar.spec.version=%{majorver}" >> build.properties
echo "jar.impl.version=%{version}" >> build.properties
echo "jar.impl.version.string=%{version}.0" >> build.properties

%build
ant \
    -Dicu4j.javac.source=1.6 -Dicu4j.javac.target=1.6 \
    -Dj2se.apidoc=%{_javadocdir}/java -Dicu4j.api.doc.jdk.link=%{_javadocdir}/java \
    jar docs

%install
# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
cp -ap %{name}*.jar %{buildroot}%{_javadir}/
for jar in icu4j icu4j-charset icu4j-localespi ; do
  ln -sf %{_javadir}/${jar}.jar %{buildroot}%{_javadir}/%{name}/${jar}.jar
done
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# maven stuff
install -d -m 755 %{buildroot}%{_mavenpomdir}
for jar in icu4j icu4j-charset icu4j-localespi ; do
  sed -i -e 's/@POMVERSION@/%{version}/' maven/$jar/pom.xml
  cp maven/$jar/pom.xml %{buildroot}%{_mavenpomdir}/JPP-$jar.pom
done
%add_maven_depmap JPP-icu4j.pom icu4j.jar
%add_maven_depmap JPP-icu4j-charset.pom icu4j-charset.jar -f charset
%add_maven_depmap JPP-icu4j-localespi.pom icu4j-localespi.jar -f localespi

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc readme.html APIChangeReport.html
%{_javadir}/%{name}/%{name}.jar

%files charset -f .mfiles-charset
%{_javadir}/%{name}/%{name}-charset.jar

%files localespi -f .mfiles-localespi
%{_javadir}/%{name}/%{name}-localespi.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
