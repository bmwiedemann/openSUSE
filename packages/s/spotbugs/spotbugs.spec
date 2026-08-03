#
# spec file for package spotbugs
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global desc SpotBugs is the spiritual successor of FindBugs, carrying on from the point\
where it left off with support of its community.
Name:           spotbugs
Version:        4.9.8
Release:        0
Summary:        A tool for static analysis to look for bugs in Java code
License:        LGPL-2.1-only
Group:          Development/Libraries/Java
URL:            https://%{name}.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/com/github/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source2:        https://repo1.maven.org/maven2/com/github/%{name}/%{name}-annotations/%{version}/%{name}-annotations-%{version}.pom
Source3:        https://repo1.maven.org/maven2/com/github/%{name}/%{name}-ant/%{version}/%{name}-ant-%{version}.pom
Source4:        %{name}.script.properties
Source5:        %{name}.pod
Patch0:         00-dont-use-manifest-classpath.patch
Patch1:         01-dom4j-2.1.patch
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  update-desktop-files
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(net.jcip:jcip-annotations)
BuildRequires:  mvn(net.sf.saxon:Saxon-HE) < 11
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.bcel:bcel)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-text)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-slf4j-impl)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:properties-maven-plugin)
BuildRequires:  mvn(org.dom4j:dom4j)
BuildRequires:  mvn(org.junit:junit-bom:pom:)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)
BuildRequires:  mvn(org.slf4j:slf4j-api)
Requires:       javapackages-tools
Requires:       mvn(net.sf.saxon:Saxon-HE) < 11
Requires:       mvn(org.apache.logging.log4j:log4j-api)
Requires:       mvn(org.apache.logging.log4j:log4j-core)
Requires:       mvn(org.apache.logging.log4j:log4j-slf4j-impl)
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
Conflicts:      findbugs
BuildArch:      noarch

%description
%{desc}

%package annotations
Summary:        Annotations the SpotBugs tool supports
Provides:       config(ant-%{name})

%description annotations
%{desc}

This package contains the annotations the SpotBugs tool supports.

%package ant
Summary:        Ant task for %{name}
Provides:       config(ant-%{name})

%description ant
%{desc}

This package contains an Ant task for %{name}.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

cp %{SOURCE1} %{name}/pom.xml
cp %{SOURCE2} %{name}-annotations/pom.xml
cp %{SOURCE3} %{name}-ant/pom.xml
cp %{SOURCE4} %{name}/etc/script.properties

sed -i -e 's#@SPOTBUGS_HOME@#%{_datadir}/%{name}#' %{name}/etc/script.properties

%pom_xpath_remove pom:packaging %{name}
%pom_xpath_remove 'pom:scope[.="runtime"]' %{name}-ant

%pom_change_dep com.github.stephenc.jcip:jcip-annotations net.jcip: %{name}
%pom_remove_dep jaxen:jaxen %{name}
%pom_remove_dep net.sf.saxon:Saxon-HE %{name}
%pom_remove_dep org.apache.logging.log4j:log4j-core %{name}
%pom_remove_dep com.github.%{name}:%{name} %{name}-ant

%pom_add_dep org.apache.ant:ant %{name}-ant
%pom_add_dep com.github.spotbugs:spotbugs:%{version} %{name}-ant

cat >pom.xml <<__POM__
<project
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"
    xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    >
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.github.%{name}</groupId>
    <artifactId>%{name}-parent</artifactId>
    <version>%{version}</version>
    <packaging>pom</packaging>
    <modules>
        <module>%{name}</module>
        <module>%{name}-annotations</module>
        <module>%{name}-ant</module>
    </modules>
</project>
__POM__

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin %{name} \
'<configuration>
    <archive>
        <manifestEntries>
            <Automatic-Module-Name>com.github.spotbugs.spotbugs</Automatic-Module-Name>
            <Main-Class>edu.umd.cs.findbugs.LaunchAppropriateUI</Main-Class>
            <Bundle-Version>%{version}</Bundle-Version>
        </manifestEntries>
    </archive>
</configuration>'

%pom_add_plugin org.codehaus.mojo:build-helper-maven-plugin %{name} \
'<executions>
    <execution>
        <id>add-source</id>
        <phase>generate-sources</phase>
        <goals>
            <goal>add-source</goal>
        </goals>
        <configuration>
            <sources>
                <source>src/gui/main</source>
            </sources>
        </configuration>
    </execution>
    <execution>
        <id>add-resource</id>
        <phase>generate-sources</phase>
        <goals>
            <goal>add-resource</goal>
        </goals>
        <configuration>
            <resources>
                <resource>
                    <directory>src/main/java</directory>
                    <targetPath/>
                    <includes>
                        <include>**/*.properties</include>
                        <include>**/*.db</include>
                    </includes>
                </resource>
                <resource>
                    <directory>src/gui/main</directory>
                    <targetPath/>
                    <includes>
                        <include>**/*.png</include>
                        <include>**/*.html</include>
                    </includes>
                </resource>
                <resource>
                    <directory>src/xsl</directory>
                    <targetPath/>
                    <includes>
                        <include>*.xsl</include>
                    </includes>
                </resource>
                <resource>
                    <directory>etc</directory>
                    <targetPath/>
                    <includes>
                        <include>*.xml</include>
                        <include>*.xsd</include>
                        <include>*.json</include>
                        <include>*.txt</include>
                    </includes>
                    <excludes>
                        <exclude>checkstyle.xml</exclude>
                    </excludes>
                </resource>
            </resources>
        </configuration>
    </execution>
</executions>'

%pom_add_plugin org.codehaus.mojo:properties-maven-plugin %{name} \
'<executions>
    <execution>
        <phase>initialize</phase>
        <goals><goal>read-project-properties</goal></goals>
        <configuration>
            <files>
                <file>etc/script.properties</file>
            </files>
        </configuration>
    </execution>
</executions>'

%pom_add_plugin com.google.code.maven-replacer-plugin:replacer %{name} \
'<executions>
    <execution>
        <phase>prepare-package</phase>
        <goals><goal>replace</goal></goals>
        <configuration>
            <basedir>${basedir}</basedir>
            <includes>src/scripts/standard/*</includes>
            <regex>false</regex>
            <replacements>
                <replacement>
                    <token>@GET_FBHOME@</token>
                    <value>${script.get.fbhome}</value>
                </replacement>
                <replacement>
                    <token>@SET_DEFAULT_JAVA@</token>
                    <value>${script.set.default.java}</value>
                </replacement>
                <replacement>
                    <token>@WRAP_JAVA@</token>
                    <value>${script.wrap.java}</value>
                </replacement>
                <replacement>
                    <token>@DEFINE_ESCAPE_ARG@</token>
                    <value>${script.define.escape_arg}</value>
                </replacement>
            </replacements>
        </configuration>
    </execution>
</executions>'

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin %{name}-annotations \
'<configuration>
    <archive>
        <manifestEntries>
            <Automatic-Module-Name>com.github.spotbugs.annotations</Automatic-Module-Name>
            <Bundle-ManifestVersion>2</Bundle-ManifestVersion>
            <Bundle-Name>%{name}-annotations</Bundle-Name>
            <Bundle-RequiredExecutionEnvironment>J2SE-1.5</Bundle-RequiredExecutionEnvironment>
            <Bundle-SymbolicName>%{name}-annotations</Bundle-SymbolicName>
            <Bundle-Version>%{version}</Bundle-Version>
            <Export-Package>edu.umd.cs.findbugs.annotations</Export-Package>
        </manifestEntries>
    </archive>
</configuration>'

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin %{name}-ant \
'<configuration>
    <archive>
        <manifestEntries>
            <Automatic-Module-Name>com.github.spotbugs.ant</Automatic-Module-Name>
        </manifestEntries>
    </archive>
</configuration>'

%build
%{mvn_build} -f -- \
	-Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
	-Dmaven.compiler.{source,target}=9 -DlegacyMode=true -Dverbose=true

pod2man --release='%{name} %{version}' --section=1 --center='User Commands' --quotes=none -u %{SOURCE5} %{name}.1

for s in 16 22 32 44 48 64 128 150 200; do
    convert -resize $s %{name}/src/doc/%{name}.png %{name}-$s.png
done

%install
%{mvn_package} :%{name}-parent __noinstall
%{mvn_package} :%{name}-ant ant
%{mvn_package} :%{name}-annotations annotations

# Artifacts and API documentation
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

# Licenses
install -dm0755 %{buildroot}%{_defaultlicensedir}/%{name}{,-{javadoc,annotations,ant}}
install -m0644 spotbugs/licenses/LICENSE*.txt %{buildroot}%{_defaultlicensedir}/%{name}
install -m0644 spotbugs/licenses/LICENSE*.txt %{buildroot}%{_defaultlicensedir}/%{name}-javadoc
install -m0644 spotbugs/licenses/LICENSE*.txt %{buildroot}%{_defaultlicensedir}/%{name}-annotations
install -m0644 spotbugs/licenses/LICENSE*.txt %{buildroot}%{_defaultlicensedir}/%{name}-ant
%fdupes %{buildroot}%{_defaultlicensedir}/%{name}
%fdupes %{buildroot}%{_defaultlicensedir}/%{name}-javadoc
%fdupes %{buildroot}%{_defaultlicensedir}/%{name}-annotations
%fdupes %{buildroot}%{_defaultlicensedir}/%{name}-ant

# Data
install -dm0755 %{buildroot}%{_javadir}/%{name}/config
install -m0644 %{name}/log4j2.xml %{buildroot}%{_javadir}/%{name}/config

install -dm0755 %{buildroot}%{_datadir}/%{name}
ln -s %{_javadir}/%{name} %{buildroot}%{_datadir}/%{name}/lib

ln -s $(xmvn-resolve \
        org.apache.bcel:bcel \
        org.apache.commons:commons-{lang3,text} \
        org.dom4j:dom4j \
        com.google.code.gson:gson \
        jaxen:jaxen \
        org.ow2.asm:asm{,-{commons,util,analysis,tree}} \
        net.jcip:jcip-annotations \
        com.google.code.findbugs:jsr305 \
        org.apache.logging.log4j:log4j-{api,core,slf4j-impl} \
        org.slf4j:slf4j-api \
        net.sf.saxon:Saxon-HE \
        ) %{buildroot}%{_javadir}/%{name}/

# Scripts
install -dm0755 %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}/bin
install -m0755 spotbugs/src/scripts/standard/* %{buildroot}%{_datadir}/%{name}/bin
ln -s %{_datadir}/%{name}/bin/{%{name},fb} %{buildroot}%{_bindir}

# Icons and desktop file
for s in 16 22 32 44 48 64 128 150 200; do
    install -dm0755 %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    install -Dm0644 %{name}-$s.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

install -dm0755 %{buildroot}%{_datadir}/applications
cat <<__DESKTOP__ >%{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=SpotBugs
Comment=A tool for static analysis to look for bugs in Java code
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Categories=Development;Debugger;
__DESKTOP__

# Ant stuff
install -dm0755 %{buildroot}%{_sysconfdir}/ant.d
echo %{name}/%{name}-ant >%{buildroot}%{_sysconfdir}/ant.d/%{name}

# Manual page
install -dm0755 %{buildroot}%{_mandir}/man1
install -Dm0644 %{name}.1 %{buildroot}%{_mandir}/man1

%post
%desktop_database_post
%icon_theme_cache_post
:

%postun
%desktop_database_postun
%icon_theme_cache_postun
:

%files -f .mfiles
%license %{_defaultlicensedir}/%{name}
%doc {CHANGELOG,README}.md
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor
%{_javadir}/%{name}
%exclude %{_javadir}/%{name}/%{name}-ant.jar
%exclude %{_javadir}/%{name}/%{name}-annotations.jar
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%files annotations -f .mfiles-annotations
%license %{_defaultlicensedir}/%{name}-annotations
%doc {CHANGELOG,README}.md

%files ant -f .mfiles-ant
%license %{_defaultlicensedir}/%{name}-ant
%doc {CHANGELOG,README}.md
%config %{_sysconfdir}/ant.d/%{name}

%files javadoc -f .mfiles-javadoc
%license %{_defaultlicensedir}/%{name}-javadoc

%changelog
