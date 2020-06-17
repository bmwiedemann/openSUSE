#
# spec file for package xmlgraphics-batik
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2000-2008, JPackage Project
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


%global classpath xmlgraphics-batik:rhino:xml-commons-apis:xml-commons-apis-ext:xmlgraphics-commons
Name:           xmlgraphics-batik
Version:        1.13
Release:        0
Summary:        Scalable Vector Graphics for Java
License:        Apache-2.0
Group:          Productivity/Graphics/Vector Editors
URL:            https://xml.apache.org/batik/
Source0:        http://archive.apache.org/dist/xmlgraphics/batik/source/batik-src-%{version}.tar.gz
Source1:        batik-build.tar.xz
Source7:        %{name}.security.policy
Patch0:         %{name}-nolinksinjavadoc.patch
Patch1:         0001-Fix-imageio-codec-lookup.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  jython
BuildRequires:  rhino >= 1.6
BuildRequires:  xalan-j2
BuildRequires:  xml-commons-apis >= 1.3.03
BuildRequires:  xmlgraphics-commons
Requires:       %{name}-css = %{version}-%{release}
Requires:       mvn(org.apache.xmlgraphics:xmlgraphics-commons)
Requires:       mvn(xalan:xalan)
Requires:       mvn(xml-apis:xml-apis)
Requires:       mvn(xml-apis:xml-apis-ext)
Obsoletes:      batik < %{version}-%{release}
Provides:       batik = %{version}-%{release}
BuildArch:      noarch

%description
Batik is a Java(tm) technology based toolkit for applications that want
to use images in the Scalable Vector Graphics (SVG) format for various
purposes, such as viewing, generation or manipulation.

%package css
Summary:        Batik CSS engine
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}-%{release}
Requires:       mvn(xml-apis:xml-apis-ext)
Obsoletes:      batik-css < %{version}-%{release}
Provides:       batik-css = %{version}-%{release}

%description css
CSS component of the Apache Batik SVG manipulation and rendering library.

%package squiggle
Summary:        Batik SVG browser
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}-%{release}
Obsoletes:      batik-squiggle < %{version}-%{release}
Provides:       batik-squiggle = %{version}-%{release}

%description squiggle
The Squiggle SVG Browser lets you view SVG file, zoom, pan and rotate
in the content and select text items in the image and much more.

%package svgpp
Summary:        Batik SVG pretty printer
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}-%{release}
Obsoletes:      batik-svgpp < %{version}-%{release}
Provides:       batik-svgpp = %{version}-%{release}

%description svgpp
The SVG Pretty Printer lets developers "pretty-up" their SVG files and
get their tabulations and other cosmetic parameters in order. It can
also be used to modify the DOCTYPE declaration on SVG files.

%package ttf2svg
Summary:        Batik SVG font converter
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}-%{release}
Obsoletes:      batik-ttf2svg < %{version}-%{release}
Provides:       batik-ttf2svg = %{version}-%{release}

%description ttf2svg
The SVG Font Converter lets developers convert character ranges from
the True Type Font format to the SVG Font format to embed in SVG
documents. This allows SVG document to be fully self-contained be
rendered exactly the same on all systems.

%package rasterizer
Summary:        Batik SVG rasterizer
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}-%{release}
Obsoletes:      batik-rasterizer < %{version}-%{release}
Provides:       batik-rasterizer = %{version}-%{release}

%description rasterizer
The SVG Rasterizer is a utility that can convert SVG files to a raster
format. The tool can convert individual files or sets of files, making
it easy to convert entire directories of SVG files. The supported
formats are JPEG, PNG, and TIFF, however the design allows new formats
to be added easily.

%package slideshow
Summary:        Batik SVG slideshow
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}-%{release}
Obsoletes:      batik-slideshow < %{version}-%{release}
Provides:       batik-slideshow = %{version}-%{release}

%description slideshow
Batik SVG slideshow.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Obsoletes:      batik-javadoc < %{version}-%{release}
Provides:       batik-javadoc = %{version}-%{release}

%description    javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}-%{release}
Obsoletes:      batik-demo < %{version}-%{release}
Provides:       batik-demo = %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n batik-%{version} -a1

find -name '*.class' -delete
find -name '*.jar' -delete

%patch0 -p1
%patch1 -p1

cp -p %{SOURCE7} batik-svgrasterizer/src/main/resources/org/apache/batik/apps/rasterizer/resources/rasterizer.policy
cp -p %{SOURCE7} batik-svgbrowser/src/main/resources/org/apache/batik/apps/svgbrowser/resources/svgbrowser.policy

# It's an uberjar, it shouldn't have requires
%pom_xpath_inject pom:dependency '<optional>true</optional>' batik-all

# eclipse expects xmlgraphics to be optional
%pom_xpath_inject 'pom:dependency[pom:artifactId="xmlgraphics-commons"]' '<optional>true</optional>' batik-css

%pom_remove_dep :batik-i18n batik-util

for pom in `find -mindepth 2 -name pom.xml -not -path ./batik-all/pom.xml`; do
    %pom_add_plugin org.apache.felix:maven-bundle-plugin $pom "
        <extensions>true</extensions>
        <configuration>
            <instructions>
                <Bundle-SymbolicName>org.apache.batik.$(sed 's:./batik-::;s:/pom.xml::' <<< $pom)</Bundle-SymbolicName>
            </instructions>
        </configuration>
    "
    %pom_xpath_inject pom:project '<packaging>bundle</packaging>' $pom
done

# for eclipse
%pom_xpath_set pom:Bundle-SymbolicName org.apache.batik.util.gui batik-gui-util

%pom_disable_module batik-test-old

build-jar-repository -s lib js xml-apis xml-commons-apis-ext xalan-j2 xmlgraphics-commons jython

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} \
    -f build-batik.xml -Dtest.skip=true \
	package
%{ant} \
    -Dant.build.javac.source=7 -Dant.build.javac.target=7 \
    all-jar jars javadoc

%install

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}

for dir in batik-%{version} batik-%{version}/lib batik-%{version}/extensions; do
  pushd ${dir}
    for jar in batik-*.jar; do
      basename=`basename ${jar} .jar`
      name=`echo ${basename} | sed -e 's/batik-//' | sed -e 's/-%{version}//' `
      cp -p ${jar} %{buildroot}%{_javadir}/%{name}/${name}.jar
    done
  popd
done

for pkg in squiggle squiggle-ext svgpp ttf2svg rasterizer rasterizer-ext slideshow; do
  ln -s %{name}/${pkg}.jar %{buildroot}%{_javadir}/batik-${pkg}.jar
done

mv %{buildroot}%{_javadir}/%{name}/all.jar %{buildroot}%{_javadir}/%{name}-all.jar
ln -s %{name}-all.jar %{buildroot}%{_javadir}/batik-all.jar

#pom
mkdir -p %{buildroot}%{_mavenpomdir}/%{name}

cp -p pom.xml %{buildroot}%{_mavenpomdir}/%{name}/parent.pom
%add_maven_depmap %{name}/parent.pom

cp -p batik-all/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-all.pom
%add_maven_depmap %{name}-all.pom %{name}-all.jar

for i in anim awt-util bridge codec constants dom ext extension gvt i18n parser script shared-resources svg-dom svgbrowser svggen svgrasterizer swing transcoder util gui-util xml;
do
  cp -p batik-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar
done

cp -p batik-css/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/css.pom
%add_maven_depmap %{name}/css.pom %{name}/css.jar -f css

cp -p batik-svgpp/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/svgpp.pom
%add_maven_depmap %{name}/svgpp.pom %{name}/svgpp.jar -f svgpp

cp -p batik-ttf2svg/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/ttf2svg.pom
%add_maven_depmap %{name}/ttf2svg.pom %{name}/ttf2svg.jar -f ttf2svg

cp -p batik-slideshow/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/slideshow.pom
%add_maven_depmap %{name}/slideshow.pom %{name}/slideshow.jar -f slideshow

for i in squiggle squiggle-ext;
do
  cp -p batik-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar -f squiggle
done

for i in rasterizer rasterizer-ext;
do
  cp -p batik-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar -f rasterizer
done

# scripts
%jpackage_script org.apache.batik.apps.svgbrowser.Main '' '' %{classpath} %{name}-squiggle true
%jpackage_script org.apache.batik.apps.svgpp.Main '' '' %{classpath} %{name}-svgpp true
%jpackage_script org.apache.batik.apps.ttf2svg.Main '' '' %{classpath} %{name}-ttf2svg true
%jpackage_script org.apache.batik.apps.rasterizer.Main '' '' %{classpath} %{name}-rasterizer true
%jpackage_script org.apache.batik.apps.slideshow.Main '' '' %{classpath} %{name}-slideshow true

# demo
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr contrib samples test-resources \
  %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}
ln -s %{name} %{buildroot}%{_datadir}/batik

# policy
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -p %{SOURCE7} %{buildroot}%{_sysconfdir}/%{name}/rasterizer.policy

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr batik-%{version}/docs/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE NOTICE
%doc KEYS MAINTAIN README
%{_javadir}/batik-all.jar

%files css -f .mfiles-css

%files squiggle -f .mfiles-squiggle
%{_javadir}/batik-squiggle-ext.jar
%{_javadir}/batik-squiggle.jar
%{_bindir}/%{name}-squiggle

%files svgpp -f .mfiles-svgpp
%{_javadir}/batik-svgpp.jar
%{_bindir}/%{name}-svgpp

%files ttf2svg -f .mfiles-ttf2svg
%{_javadir}/batik-ttf2svg.jar
%{_bindir}/%{name}-ttf2svg

%files rasterizer -f .mfiles-rasterizer
%{_javadir}/batik-rasterizer.jar
%{_javadir}/batik-rasterizer-ext.jar
%{_bindir}/%{name}-rasterizer
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/rasterizer.policy

%files slideshow -f .mfiles-slideshow
%{_javadir}/batik-slideshow.jar
%{_bindir}/%{name}-slideshow

%files demo
%{_datadir}/%{name}
%{_datadir}/batik
%exclude %{_datadir}/%{name}/contrib/rasterizertask/build.sh
%exclude %{_datadir}/%{name}/contrib/charts/convert.sh
%attr(0755,root,root) %{_datadir}/%{name}/contrib/rasterizertask/build.sh
%attr(0755,root,root) %{_datadir}/%{name}/contrib/charts/convert.sh

%files javadoc
%license LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
