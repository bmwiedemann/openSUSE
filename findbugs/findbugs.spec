#
# spec file for package findbugs
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global noupdatechecks_version 20140707gitcce19ac
Name:           findbugs
Version:        3.0.1
Release:        0
Summary:        Bug pattern detector for Java
License:        LGPL-2.1-or-later
Group:          Development/Languages/Java
URL:            http://findbugs.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-source.zip
Source1:        findbugs-ant
Source2:        findbugs-tools-README
Source3:        http://repo1.maven.org/maven2/com/google/code/findbugs/findbugs/3.0.1/findbugs-3.0.1.pom
Source4:        http://repo1.maven.org/maven2/com/google/code/findbugs/annotations/3.0.0/annotations-3.0.0.pom
# This archive contains the source for the noUpdateChecks plugin.
# It was created with:
#   $ git clone --bare git@github.com:findbugsproject/findbugs
#   $ git --git-dir=findbugs.git archive --format tgz cce19ac plugins/noUpdateChecks -o noUpdateChecks-plugin-20140707gitcce19ac.tgz
Source5:        noUpdateChecks-plugin-%{noupdatechecks_version}.tgz
Source6:        http://repo1.maven.org/maven2/com/google/code/findbugs/findbugs-ant/3.0.0/findbugs-ant-3.0.0.pom
Source10:       findbugs-16x16.png
Source11:       findbugs-32x32.png
Source12:       findbugs-48x48.png
Source13:       findbugs.desktop
Patch0:         findbugs-build.patch
Patch1:         findbugs-home.patch
# Allow Ant task to work even though findbugs.jar has no Class-Path attribute in its manifest (bug #1080682)
Patch2:         findbugs-ant-task-classpath.patch
Patch3:         findbugs-manual.patch
# Port to dom4j 2.0
Patch4:         findbugs-dom4j.patch
Patch5:         findbugs-jdk11.patch
Patch6:         findbugs-javadoc.patch
BuildRequires:  ant
BuildRequires:  apache-commons-lang
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  dom4j
BuildRequires:  fdupes
BuildRequires:  findbugs-bcel
BuildRequires:  hicolor-icon-theme
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  jaxen
BuildRequires:  jcip-annotations
BuildRequires:  jdepend
BuildRequires:  jformatstring
BuildRequires:  jpackage-utils
BuildRequires:  jsr-305
BuildRequires:  junit
# For generating HTML version of manual using xsltproc
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  objectweb-asm
BuildRequires:  texlive-preprint
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  tex(latex)
Requires:       apache-commons-lang
Requires:       dom4j
Requires:       findbugs-bcel
Requires:       java
Requires:       jaxen
Requires:       jcip-annotations
Requires:       jformatstring
Requires:       jpackage-utils
Requires:       jsr-305
Requires:       junit
Requires:       objectweb-asm
BuildArch:      noarch

%description
Findbugs is a program which uses static analysis to look for bugs in Java code.
It can check for null pointer exceptions, multithreaded code errors, and other
bugs.

%package -n ant-findbugs
Summary:        Ant task for findbugs
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}
Requires:       ant
Provides:       %{name}:%{_sysconfdir}/ant.d/%{name}

%description -n ant-findbugs
This package defines an ant task for findbugs for easy integration of findbugs
into your ant-controlled project.

%package javadoc
Summary:        Javadoc documentation for findbugs
Group:          Documentation/HTML

%description javadoc
Javadoc documentation for findbugs.

%package tools
Summary:        Addon tools for findbugs
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}
Requires:       junit

%description tools
This package contains additional tools for use with findbugs.  See
README.tools for more information.

%prep
%setup -q
%setup -q -a 5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

cp -p %{SOURCE2} README.tools

# Make sure we don't accidentally use any existing JAR files
rm -f lib/*.jar

# Get rid of code for Mac OS X that depends on a jar from Apple
rm -f src/gui/edu/umd/cs/findbugs/gui2/OSXAdapter.java
%pom_remove_dep com.apple:AppleJavaExtensions %{SOURCE3}

%build
# Build the class files and docs
ant docs build

# Build the javadocs
ant apiJavadoc

# Build the architecture PDF
pushd design/architecture
make %{?_smp_mflags} depend
make %{?_smp_mflags}
popd

# Package up the tools
pushd build/classes
jar cf ../../lib/findbugs-tools.jar edu/umd/cs/findbugs/tools
popd

# Build the noUpdateChecks plugin
pushd plugins/noUpdateChecks
ant plugin-jar
popd

%install
# Install the jars
mkdir -p %{buildroot}%{_javadir}
cp -p lib/annotations.jar %{buildroot}%{_javadir}/%{name}-annotations.jar
cp -p lib/%{name}-tools.jar %{buildroot}%{_javadir}/%{name}-tools.jar
cp -p lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# Install the ant task
mkdir -p %{buildroot}%{_javadir}/ant
cp -p lib/%{name}-ant.jar %{buildroot}%{_javadir}/ant/ant-%{name}.jar
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
cp -p %{SOURCE1} %{buildroot}%{_sysconfdir}/ant.d/%{name}

# Install the javadocs
mkdir -p %{buildroot}%{_javadocdir}
cp -a apiJavaDoc %{buildroot}%{_javadocdir}/%{name}

# Install the scripts
mkdir -p %{buildroot}%{_bindir}
for f in $(find bin -maxdepth 1 -type f \! -name '*.bat' \! -name '*.ico'); do
  cp -p $f %{buildroot}%{_bindir}
done

# Install the shared files
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a etc plugin %{buildroot}%{_datadir}/%{name}

# Install the noUpdateChecks plugin
cp -p plugins/noUpdateChecks/build/noUpdateChecks.jar %{buildroot}%{_datadir}/%{name}/plugin

# Create /usr/share/findbugs/lib directory containing symlinks to required JARs (bug #1080682)
# List is based on the Class-Path attribute in etc/MANIFEST-findbugs.MF
mkdir -p %{buildroot}%{_datadir}/%{name}/lib
for i in findbugs findbugs-bcel dom4j jaxen objectweb-asm/asm \
   objectweb-asm/asm-commons objectweb-asm/asm-tree jsr-305 \
  jFormatString apache-commons-lang; do
    ln -s %{_javadir}/$i.jar %{buildroot}%{_datadir}/%{name}/lib
done

# Remove now unnecessary build-only manual files so %%doc doesn't get them
rm -f build/doc/manual*.xml build/doc/manual*.xsl

# Install poms
mkdir -p %{buildroot}%{_mavenpomdir}
sed -i 's/3\.0\.0/3\.0\.1/g' %{SOURCE4} %{SOURCE6}
cp %{SOURCE3} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
cp %{SOURCE4} %{buildroot}%{_mavenpomdir}/JPP-%{name}-annotations.pom
cp %{SOURCE6} %{buildroot}%{_mavenpomdir}/JPP.ant-ant-%{name}.pom

# Add depmaps
%add_maven_depmap -a net.sourceforge.findbugs:findbugs JPP-%{name}.pom %{name}.jar
%add_maven_depmap -a net.sourceforge.findbugs:annotations JPP-%{name}-annotations.pom %{name}-annotations.jar
%add_maven_depmap -a net.sourceforge.findbugs:findbugs-ant JPP.ant-ant-%{name}.pom ant/ant-findbugs.jar -f ant

mkdir -p %{buildroot}%{_datadir}/applications
install -D -p -m 644 %{SOURCE10} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -D -p -m 644 %{SOURCE11} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -p -m 644 %{SOURCE12} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -p -m 644 %{SOURCE13} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file -i %{name}
%fdupes -s %{buildroot}
%fdupes -s build/doc

%files -f .mfiles
%license licenses/LICENSE.txt
%doc design/DecouplingFromBCEL.txt design/VisitingAndCaching.txt
%doc README.txt "design/eclipse findbugs plugin features.sxw"
%doc design/architecture/architecture.pdf build/doc
%{_bindir}/*
%{_datadir}/%{name}
%dir %{_datadir}/icons/hicolor/
%{_datadir}/icons/hicolor/16x16/apps/findbugs.png
%{_datadir}/icons/hicolor/32x32/apps/findbugs.png
%{_datadir}/icons/hicolor/48x48/apps/findbugs.png
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files -n ant-findbugs -f .mfiles-ant
%license licenses/LICENSE.txt
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files javadoc
%{_javadocdir}/*

%files tools
%license licenses/LICENSE.txt
%doc README.tools
%{_javadir}/findbugs-tools.jar

%changelog
