#
# spec file for package icedtea-web
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


Name:           icedtea-web
Version:        2.0.0~alpha36
Release:        0
Summary:        Java Web Start implementation
License:        GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Languages/Java
URL:            https://github.com/AdoptOpenJDK/IcedTea-Web
Source0:        %{name}-%{version}.tar.xz
Source1:        icedtea-web.conf
Patch0:         icedtea-web-suse-desktop-files.patch
Patch1:         0001-Make-IcedTea-Web-build-and-run-on-Java-8-through-25.patch
Patch2:         0002-Port-to-jacoco-0.8.14-and-surefire-3.6.0-to-be-able-.patch
Patch3:         0003-Bring-back-Pack200-support-on-newer-Java-using-commo.patch
Patch4:         0004-Grey-out-the-advanced-policy-editor-button-when-poli.patch
Patch5:         0005-Stop-relying-on-hidden-JDK-certificate-classes-where.patch
Patch6:         0006-Address-SonarCloud-findings-and-fix-JaCoCo-report-in.patch
Patch7:         0007-Stop-opening-JDK-packages-that-no-longer-exist-or-ar.patch
Patch8:         0008-Fix-the-shell-launchers-silently-failing-when-java-c.patch
Patch9:         0009-Ignore-an-invalid-JNLP-file-version-instead-of-refus.patch
Patch10:        0010-Drop-modules-missing-from-this-JVM-from-java-vm-args.patch
Patch11:        0011-Make-the-exception-dialog-test-independent-of-the-cl.patch
Patch100:       reproducible-timestamps.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.seancfoley:ipaddress)
BuildRequires:  mvn(com.github.vatbub:mslinks)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.ccil.cowan.tagsoup:tagsoup)
BuildRequires:  mvn(org.mozilla:rhino)
Requires:       java >= 1.8
Requires:       javapackages-tools
Obsoletes:      java-1_6_0-openjdk-plugin < %{version}-%{release}
Obsoletes:      java-1_7_0-openjdk-plugin < %{version}-%{release}
Obsoletes:      java-1_8_0-openjdk-plugin < %{version}-%{release}
Obsoletes:      java-1_9_0-openjdk-plugin < %{version}-%{release}
Obsoletes:      java-plugin < 1.8.0
Provides:       java-1_6_0-openjdk-plugin = %{version}-%{release}
Provides:       java-1_7_0-openjdk-plugin = %{version}-%{release}
Provides:       java-1_8_0-openjdk-plugin = %{version}-%{release}
Provides:       java-1_9_0-openjdk-plugin = %{version}-%{release}
Provides:       java-plugin = 1.8.0
BuildArch:      noarch

%description
The IcedTea-Web project provides a Free Software web browser plugin running
applets written in the Java programming language and an implementation of Java
Web Start, originally based on the NetX project.

%package javadoc
Summary:        Java Web Start and plugin implementation (API documentation)
Group:          Documentation/Other

%description javadoc
The IcedTea-Web project provides a Free Software web browser plugin running
applets written in the Java programming language and an implementation of Java
Web Start, originally based on the NetX project.
This package contains API documentation for the %{name} Java Web Start
and plugin implementation.

%prep
%autosetup -p1

%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-shade-plugin

%pom_disable_module test-extensions
%pom_disable_module artifact-no-dependencies
%pom_disable_module artifact-all-dependencies
%pom_disable_module integration

%build
%{mvn_build} -f

itw_cp=$(ls {jnlp-api,common,xml-parser,core}/target/*.jar | grep -v -e sources -e javadoc | tr '\n' :)
itw_cp=${itw_cp%:}:$(build-classpath rhino tagsoup IPAddress commons-compress commons-io commons-lang3)

# WARN/ERROR go to syslog via util-linux `logger`, absent from Factory build root
export XDG_CONFIG_HOME=$PWD/gen/config
mkdir -p $XDG_CONFIG_HOME/icedtea-web
echo deployment.log.system=false > $XDG_CONFIG_HOME/icedtea-web/deployment.properties

mkdir -p gen/completions gen/man
for n in javaws itweb-settings policyeditor ; do
  sed "s/@OPTIONS@/$(java -cp $itw_cp net.adoptopenjdk.icedteaweb.commandline.CommandLineOptionsDefinition $n)/" \
    launchers/completion.in/$n.bash.in > gen/completions/$n.bash
  sed "s#PATH_TO_$(echo $n | tr a-z- A-Z_)#%{_bindir}/$n#" \
    launchers/xdesktop.in/$n.desktop.in > gen/$n.desktop
done
# user.language instead of LANG: works without glibc locales in the build root
for l in en_US cs_CZ de_DE pl_PL ; do
  d=gen/man/${l%%_*}/man1 ; [ $l = en_US ] && d=gen/man/man1
  mkdir -p $d
  java -Duser.language=${l%%_*} -Duser.country=${l##*_} -Dfile.encoding=UTF-8 -cp $itw_cp \
    net.sourceforge.jnlp.util.docprovider.TextsProvider man UTF-8 $d false %{version} \
    "-authorString=https://github.com/AdoptOpenJDK/icedtea-web/graphs/contributors"
done

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%jpackage_script net.sourceforge.jnlp.runtime.Boot "" "" icedtea-web javaws true
%jpackage_script net.adoptopenjdk.icedteaweb.client.commandline.CommandLine "" "" icedtea-web itweb-settings true
%jpackage_script net.adoptopenjdk.icedteaweb.client.policyeditor.PolicyEditor "" "" icedtea-web policyeditor true
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/java/icedtea-web.conf
install -Dpm 644 -t %{buildroot}%{_datadir}/icedtea-web launchers/itw-modularjdk.args core/src/main/resources/javaws_splash.png
install -Dpm 644 -t %{buildroot}%{_datadir}/applications gen/*.desktop
install -Dpm 644 -t %{buildroot}%{_datadir}/bash-completion/completions gen/completions/*.bash
install -Dpm 644 launchers/javaws.png %{buildroot}%{_datadir}/pixmaps/javaws.png
install -dm 755 %{buildroot}%{_mandir}
cp -r gen/man/* %{buildroot}%{_mandir}/

%posttrans
update-desktop-database &> /dev/null || :
exit 0

%postun
update-desktop-database &> /dev/null || :
exit 0

%files

%files -f .mfiles
%{_bindir}/javaws
%{_bindir}/itweb-settings
%{_bindir}/policyeditor
%config(noreplace) %{_sysconfdir}/java/icedtea-web.conf
%{_datadir}/icedtea-web
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/*.bash
%{_datadir}/pixmaps/javaws.png
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%license LICENSE
%doc LICENCE_DETAILS.md README.md

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
