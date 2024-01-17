#
# spec file for package proguard
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


Name:           proguard
Version:        6.2.0
Release:        0
Summary:        Java class file shrinker, optimizer, obfuscator and preverifier
License:        GPL-2.0-or-later
Group:          Development/Libraries/Java
URL:            https://www.guardsquare.com/en/proguard
Source0:        http://downloads.sourceforge.net/%{name}/%{name}%{version}.tar.gz
BuildRequires:  java-devel >= 8
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(org.apache.ant:ant)
Requires:       javapackages-tools
Obsoletes:      %{name}-manual

BuildArch:      noarch

%description
ProGuard is a free Java class file shrinker, optimizer, obfuscator and
preverifier. It detects and removes unused classes, fields, methods, and
attributes. It optimizes bytecode and removes unused instructions. It
renames the remaining classes, fields, and methods using short meaningless
names. Finally, it preverifies the processed code for Java 6 or for Java
Micro Edition.

%package gui
Summary:        GUI for %{name}
Group:          Development/Libraries/Java
Requires:       javapackages-tools

%description gui
A GUI for %{name}.

%package -n ant-%{name}
Summary:        Ant task for %{name}
Group:          Development/Libraries/Java

%description -n ant-%{name}
Ant task for %{name}


%prep
%setup -q -n %{name}%{version}

find -name '*.jar' -print -delete
find -name '*.class' -print -delete

%pom_disable_module ../gradle buildscripts
%pom_xpath_remove -r pom:addClasspath buildscripts
%pom_remove_plugin -r :maven-source-plugin buildscripts
%pom_remove_plugin -r :maven-javadoc-plugin buildscripts

%mvn_package :*anttask anttask
%mvn_package :*gui gui
%mvn_file :%{name}-base %{name}/%{name}-base %{name}/%{name}

%build
%mvn_build -f -j -- -f buildscripts/pom.xml -Dsource=8

%install
%mvn_install

mkdir -p %{buildroot}%{_bindir}
%jpackage_script proguard.ProGuard "" "" %{name} %{name} true
%jpackage_script proguard.gui.ProGuardGUI "" "" %{name} %{name}-gui true
%jpackage_script proguard.retrace.ReTrace "" "" %{name} %{name}-retrace true

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "proguard" > %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%{_bindir}/%{name}
%{_bindir}/%{name}-retrace
%doc README.md
%license LICENSE.md LICENSE_exception.md

%files -n ant-%{name} -f .mfiles-anttask
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files gui -f .mfiles-gui
%{_bindir}/%{name}-gui

%changelog
