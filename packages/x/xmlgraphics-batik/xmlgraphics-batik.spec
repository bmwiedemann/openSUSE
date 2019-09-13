#
# spec file for package xmlgraphics-batik
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xmlgraphics-batik
Version:        1.10
Release:        0
Summary:        Scalable Vector Graphics for Java
License:        Apache-2.0
Group:          Productivity/Graphics/Vector Editors
URL:            http://xml.apache.org/batik/
Source:         http://archive.apache.org/dist/xmlgraphics/batik/source/batik-src-%{version}.tar.gz
Source1:        %{name}.squiggle.script
Source2:        %{name}.svgpp.script
Source3:        %{name}.ttf2svg.script
Source4:        %{name}.rasterizer.script
Source5:        %{name}.slideshow.script
Source6:        %{name}-squiggle.desktop
Source7:        %{name}.rasterizer.policy
Patch0:         %{name}-nolinksinjavadoc.patch
Patch1:         %{name}-manifests.patch
Patch2:         %{name}-policy.patch
Patch3:         %{name}-securitymanager.patch
Patch4:         0001-Fix-imageio-codec-lookup.patch
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
%setup -q -n batik-%{version}

find -name '*.class' -delete
find -name '*.jar' -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

cp -p %{SOURCE1} batik-svgrasterizer/src/main/resources/org/apache/batik/apps/rasterizer/resources/rasterizer.policy
cp -p %{SOURCE1} batik-svgbrowser/src/main/resources/org/apache/batik/apps/svgbrowser/resources/svgbrowser.policy
rm -rf batik-script/src/main/java/org/apache/batik/script/jacl

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
ant \
    -Dant.build.javac.source=6 -Dant.build.javac.target=6 \
	all-jar jars javadoc

%install

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}

# This one is empty and useless...
rm batik-%{version}/batik-%{version}.jar

for dir in batik-%{version} batik-%{version}/lib batik-%{version}/extensions; do
  pushd ${dir}
    for jar in batik-*.jar; do
      basename=`basename ${jar} .jar`
      name=`echo ${basename} | sed -e 's/batik-//'`
      cp -p ${jar} %{buildroot}%{_javadir}/%{name}/${name}.jar
    done
  popd
done

for pkg in squiggle squiggle-ext svgpp ttf2svg rasterizer rasterizer-ext slideshow; do
  ln -s %{name}/${pkg}-%{version}.jar %{buildroot}%{_javadir}/batik-${pkg}-%{version}.jar
done

mv %{buildroot}%{_javadir}/%{name}/all-%{version}.jar %{buildroot}%{_javadir}/%{name}-all-%{version}.jar
ln -s %{name}-all-%{version}.jar %{buildroot}%{_javadir}/batik-all-%{version}.jar

for dir in %{buildroot}%{_javadir} %{buildroot}%{_javadir}/%{name}; do
  pushd ${dir}
    for jar in *-%{version}*.jar; do
      ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`;
    done
  popd
done

#pom
mkdir -p %{buildroot}%{_mavenpomdir}/%{name}

cp -p pom.xml %{buildroot}%{_mavenpomdir}/%{name}/parent.pom
%add_maven_depmap %{name}/parent.pom

cp -p batik-all/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-all.pom
%add_maven_depmap %{name}-all.pom %{name}-all-%{version}.jar

for i in anim awt-util bridge codec constants dom ext extension gvt i18n parser script svg-dom svgbrowser svggen svgrasterizer swing transcoder util gui-util xml;
do
  cp -p batik-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}-%{version}.jar
done

cp -p batik-css/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/css.pom
%add_maven_depmap %{name}/css.pom %{name}/css-%{version}.jar -f css

cp -p batik-svgpp/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/svgpp.pom
%add_maven_depmap %{name}/svgpp.pom %{name}/svgpp-%{version}.jar -f svgpp

cp -p batik-ttf2svg/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/ttf2svg.pom
%add_maven_depmap %{name}/ttf2svg.pom %{name}/ttf2svg-%{version}.jar -f ttf2svg

cp -p batik-slideshow/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/slideshow.pom
%add_maven_depmap %{name}/slideshow.pom %{name}/slideshow-%{version}.jar -f slideshow

for i in squiggle squiggle-ext;
do
  cp -p batik-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}-%{version}.jar -f squiggle
done

for i in rasterizer rasterizer-ext;
do
  cp -p batik-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}-%{version}.jar -f rasterizer
done

# scripts
mkdir -p %{buildroot}%{_bindir}
cp -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}-squiggle
cp -p %{SOURCE2} %{buildroot}%{_bindir}/%{name}-svgpp
cp -p %{SOURCE3} %{buildroot}%{_bindir}/%{name}-ttf2svg
cp -p %{SOURCE4} %{buildroot}%{_bindir}/%{name}-rasterizer
cp -p %{SOURCE5} %{buildroot}%{_bindir}/%{name}-slideshow

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

%files
%defattr(0644,root,root,0755)
%license LICENSE NOTICE
%doc KEYS MAINTAIN README
%dir %{_javadir}/%{name}
%{_javadir}/%{name}-all-%{version}.jar
%{_javadir}/%{name}-all.jar
%{_javadir}/batik-all-%{version}.jar
%{_javadir}/batik-all.jar
%{_javadir}/%{name}/anim-%{version}.jar
%{_javadir}/%{name}/anim.jar
%{_javadir}/%{name}/awt-util-%{version}.jar
%{_javadir}/%{name}/awt-util.jar
%{_javadir}/%{name}/bridge-%{version}.jar
%{_javadir}/%{name}/bridge.jar
%{_javadir}/%{name}/codec-%{version}.jar
%{_javadir}/%{name}/codec.jar
%{_javadir}/%{name}/constants-%{version}.jar
%{_javadir}/%{name}/constants.jar
%{_javadir}/%{name}/dom-%{version}.jar
%{_javadir}/%{name}/dom.jar
%{_javadir}/%{name}/ext-%{version}.jar
%{_javadir}/%{name}/ext.jar
%{_javadir}/%{name}/extension-%{version}.jar
%{_javadir}/%{name}/extension.jar
%{_javadir}/%{name}/gui-util-%{version}.jar
%{_javadir}/%{name}/gui-util.jar
%{_javadir}/%{name}/gvt-%{version}.jar
%{_javadir}/%{name}/gvt.jar
%{_javadir}/%{name}/i18n-%{version}.jar
%{_javadir}/%{name}/i18n.jar
%{_javadir}/%{name}/parser-%{version}.jar
%{_javadir}/%{name}/parser.jar
%{_javadir}/%{name}/script-%{version}.jar
%{_javadir}/%{name}/script.jar
%{_javadir}/%{name}/svg-dom-%{version}.jar
%{_javadir}/%{name}/svg-dom.jar
%{_javadir}/%{name}/svgbrowser-%{version}.jar
%{_javadir}/%{name}/svgbrowser.jar
%{_javadir}/%{name}/svggen-%{version}.jar
%{_javadir}/%{name}/svggen.jar
%{_javadir}/%{name}/svgrasterizer-%{version}.jar
%{_javadir}/%{name}/svgrasterizer.jar
%{_javadir}/%{name}/swing-%{version}.jar
%{_javadir}/%{name}/swing.jar
%{_javadir}/%{name}/transcoder-%{version}.jar
%{_javadir}/%{name}/transcoder.jar
%{_javadir}/%{name}/util-%{version}.jar
%{_javadir}/%{name}/util.jar
%{_javadir}/%{name}/xml-%{version}.jar
%{_javadir}/%{name}/xml.jar
%dir %{_mavenpomdir}/%{name}
%{_mavenpomdir}/%{name}-all.pom
%{_mavenpomdir}/%{name}/anim.pom
%{_mavenpomdir}/%{name}/awt-util.pom
%{_mavenpomdir}/%{name}/bridge.pom
%{_mavenpomdir}/%{name}/codec.pom
%{_mavenpomdir}/%{name}/constants.pom
%{_mavenpomdir}/%{name}/dom.pom
%{_mavenpomdir}/%{name}/ext.pom
%{_mavenpomdir}/%{name}/extension.pom
%{_mavenpomdir}/%{name}/gui-util.pom
%{_mavenpomdir}/%{name}/gvt.pom
%{_mavenpomdir}/%{name}/i18n.pom
%{_mavenpomdir}/%{name}/parent.pom
%{_mavenpomdir}/%{name}/parser.pom
%{_mavenpomdir}/%{name}/script.pom
%{_mavenpomdir}/%{name}/svg-dom.pom
%{_mavenpomdir}/%{name}/svgbrowser.pom
%{_mavenpomdir}/%{name}/svggen.pom
%{_mavenpomdir}/%{name}/svgrasterizer.pom
%{_mavenpomdir}/%{name}/swing.pom
%{_mavenpomdir}/%{name}/transcoder.pom
%{_mavenpomdir}/%{name}/util.pom
%{_mavenpomdir}/%{name}/xml.pom
%if %{defined _maven_repository}
%config(noreplace) %{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml
%endif
%dir %{_sysconfdir}/%{name}

%files css
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/css-%{version}.jar
%{_javadir}/%{name}/css.jar
%{_mavenpomdir}/%{name}/css.pom
%if %{defined _maven_repository}
%config(noreplace) %{_mavendepmapfragdir}/%{name}-css
%else
%{_datadir}/maven-metadata/%{name}-css.xml
%endif

%files squiggle
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/squiggle-%{version}.jar
%{_javadir}/%{name}/squiggle.jar
%{_javadir}/%{name}/squiggle-ext-%{version}.jar
%{_javadir}/%{name}/squiggle-ext.jar
%{_javadir}/batik-squiggle-%{version}.jar
%{_javadir}/batik-squiggle.jar
%{_javadir}/batik-squiggle-ext-%{version}.jar
%{_javadir}/batik-squiggle-ext.jar
%{_mavenpomdir}/%{name}/squiggle.pom
%{_mavenpomdir}/%{name}/squiggle-ext.pom
%if %{defined _maven_repository}
%config(noreplace) %{_mavendepmapfragdir}/%{name}-squiggle
%else
%{_datadir}/maven-metadata/%{name}-squiggle.xml
%endif
%attr(0755,root,root) %{_bindir}/%{name}-squiggle

%files svgpp
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/svgpp-%{version}.jar
%{_javadir}/%{name}/svgpp.jar
%{_javadir}/batik-svgpp-%{version}.jar
%{_javadir}/batik-svgpp.jar
%{_mavenpomdir}/%{name}/svgpp.pom
%if %{defined _maven_repository}
%config(noreplace) %{_mavendepmapfragdir}/%{name}-svgpp
%else
%{_datadir}/maven-metadata/%{name}-svgpp.xml
%endif
%attr(0755,root,root) %{_bindir}/%{name}-svgpp

%files ttf2svg
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/ttf2svg-%{version}.jar
%{_javadir}/%{name}/ttf2svg.jar
%{_javadir}/batik-ttf2svg-%{version}.jar
%{_javadir}/batik-ttf2svg.jar
%{_mavenpomdir}/%{name}/ttf2svg.pom
%if %{defined _maven_repository}
%config(noreplace) %{_mavendepmapfragdir}/%{name}-ttf2svg
%else
%{_datadir}/maven-metadata/%{name}-ttf2svg.xml
%endif
%attr(0755,root,root) %{_bindir}/%{name}-ttf2svg

%files rasterizer
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/rasterizer-%{version}.jar
%{_javadir}/%{name}/rasterizer.jar
%{_javadir}/%{name}/rasterizer-ext-%{version}.jar
%{_javadir}/%{name}/rasterizer-ext.jar
%{_javadir}/batik-rasterizer-%{version}.jar
%{_javadir}/batik-rasterizer.jar
%{_javadir}/batik-rasterizer-ext-%{version}.jar
%{_javadir}/batik-rasterizer-ext.jar
%{_mavenpomdir}/%{name}/rasterizer.pom
%{_mavenpomdir}/%{name}/rasterizer-ext.pom
%if %{defined _maven_repository}
%config(noreplace) %{_mavendepmapfragdir}/%{name}-rasterizer
%else
%{_datadir}/maven-metadata/%{name}-rasterizer.xml
%endif
%attr(0755,root,root) %{_bindir}/%{name}-rasterizer
%config(noreplace) %{_sysconfdir}/%{name}/rasterizer.policy

%files slideshow
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/slideshow-%{version}.jar
%{_javadir}/%{name}/slideshow.jar
%{_javadir}/batik-slideshow-%{version}.jar
%{_javadir}/batik-slideshow.jar
%{_mavenpomdir}/%{name}/slideshow.pom
%if %{defined _maven_repository}
%config(noreplace) %{_mavendepmapfragdir}/%{name}-slideshow
%else
%{_datadir}/maven-metadata/%{name}-slideshow.xml
%endif
%attr(0755,root,root) %{_bindir}/%{name}-slideshow

%files demo
%defattr(0644,root,root,0755)
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
