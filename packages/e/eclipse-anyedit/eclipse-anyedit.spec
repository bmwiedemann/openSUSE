#
# spec file for package eclipse-anyedit
#
# Copyright (c) 2022 SUSE LLC
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


Name:           eclipse-anyedit
Version:        2.7.1
Release:        0
Summary:        AnyEdit plugin for eclipse
License:        EPL-1.0
Group:          Development/Libraries/Java
URL:            http://andrei.gmxhome.de/anyedit/index.html
Source0:        https://github.com/iloveeclipse/anyedittools/archive/%{version}.tar.gz
BuildRequires:  eclipse-jdt
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  tycho
BuildConflicts: java >= 12
BuildConflicts: java-devel >= 12
BuildConflicts: java-headless >= 12
#!BuildIgnore:  libjawt.so(SUNWprivate_1.1)
#!BuildIgnore:  libjawt.so(SUNWprivate_1.1)(64bit)
BuildArch:      noarch
# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch:    s390 %{arm} %{ix86}

%description
The AnyEdit plugin adds several new actions to the context menu of text-based
Eclipse editors.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
Developer documentation for %{name}.

%prep
%setup -q -n anyedittools-%{version}

xmvn -o org.eclipse.tycho:tycho-pomgenerator-plugin:generate-poms \
  -DgroupId=de.loskutov -Dversion=%{version}

# Use Java 1.8 annotations
sed -i -e '/jdt\.annotation/s/1\.2.\0/3.0.0/' AnyEditTools/META-INF/MANIFEST.MF
sed -i -e 's/JavaSE-1.7/JavaSE-1.8/' AnyEditTools/META-INF/MANIFEST.MF AnyEditTools/build.properties
sed -i -e 's/1.7/1.8/' AnyEditTools/.settings/org.eclipse.jdt.core.prefs

# don't install poms
%{mvn_package} "::pom::" __noinstall

%build
%{mvn_build} -f -- -Dmaven.compiler.release=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md

%changelog
