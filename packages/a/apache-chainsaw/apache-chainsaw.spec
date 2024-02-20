#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global short_name chainsaw
%global repo_name logging-%{short_name}
Name:           apache-%{short_name}
Version:        2.1.0
Release:        0
Summary:        Apache Chainsaw
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://logging.apache.org/%{short_name}
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.png
Source2:        %{name}.desktop
Patch0:         %{name}-xstream.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-tools
BuildRequires:  maven-local
BuildRequires:  update-desktop-files
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.thoughtworks.xstream:xstream)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.jmdns:jmdns)
BuildRequires:  mvn(log4j:apache-log4j-extras)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-vfs2)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires:  mvn(org.apache.logging:logging-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
Requires:       apache-commons-logging
Requires:       apache-commons-vfs2
Requires:       apache-log4j-extras
Requires:       javapackages-tools
Requires:       jmdns
Requires:       jsch
Requires:       reload4j
Requires:       slf4j
Requires:       xpp3
Requires:       xpp3-minimal
Requires:       xstream
Recommends:     %{name}-javadoc
Provides:       chainsaw = %{version}-%{release}
Obsoletes:      chainsaw < %{version}-%{release}
BuildArch:      noarch

%description
Graphical Viewer for Logging events from a local or remote log4j event system.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
%{summary}.

%prep
%autosetup -p1

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :appassembler-maven-plugin
%pom_remove_plugin :maven-assembly-plugin

# We don't want classpath in manifest
%pom_xpath_remove pom:plugin/pom:configuration/pom:archive/pom:manifest/pom:addClasspath

# use apache-commons-vfs2 instead of the old apache-commons-vfs
%pom_change_dep :commons-vfs org.apache.commons:commons-vfs2
perl -pi -e 's#org\.apache\.commons\.vfs\.#org\.apache\.commons\.vfs2\.#g' \
  src/main/java/org/apache/log4j/chainsaw/vfs/VFSLogFilePatternReceiver.java
%pom_remove_dep org.apache.openejb:javaee-api
%pom_remove_dep org.projectlombok:lombok

# point chainsaw to our installed Javadoc
sed -i -e 's#\"docs/api\"#\"%{_javadocdir}/%{name}\"#g' \
  src/main/java/org/apache/log4j/chainsaw/help/HelpManager.java

%if %{?pkg_vcmp:%pkg_vcmp maven-antrun-plugin >= 3}%{!?pkg_vcmp:0}
sed -i -e 's#tasks\>#target\>#g' pom.xml
%endif

%build
%{mvn_build} -f -- -Dmaven.compiler.release=9 -Dsource=9

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

# apache-chainsaw has to be the first in order to avoid name classes in apache-log4j-extras
%jpackage_script org.apache.log4j.chainsaw.LogUI "" "" apache-chainsaw:apache-log4j-extras:reload4j:jmdns:slf4j/api:xstream:xpp3:xpp3-minimal:commons-vfs2:commons-logging:jsch %{short_name} true

# freedesktop.org menu entries and icons
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
cp -a %{SOURCE1} \
  %{buildroot}%{_datadir}/pixmaps/%{short_name}.png
cp -a %{SOURCE2} \
  %{buildroot}%{_datadir}/applications/%{short_name}.desktop
%suse_update_desktop_file %{short_name} Development Debugger

%files -f .mfiles
%{_bindir}/%{short_name}
%{_datadir}/applications/chainsaw.desktop
%{_datadir}/pixmaps/chainsaw.png
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
