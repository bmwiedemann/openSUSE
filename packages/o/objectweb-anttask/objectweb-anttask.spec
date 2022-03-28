#
# spec file for package objectweb-anttask
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


Name:           objectweb-anttask
Version:        1.2
Release:        0
Summary:        ObjectWeb Ant task
License:        LGPL-2.1-or-later
Group:          Development/Languages/Java
URL:            http://forge.objectweb.org/projects/monolog/
Source0:        ow_util_ant_tasks_1.2.zip
Patch1:         objectweb-anttask-ant17.patch
Patch2:         objectweb-anttask-java5.patch
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  unzip
BuildRequires:  xalan-j2
BuildRequires:  xml-commons-apis
Provides:       owanttask
BuildArch:      noarch

%description
ObjectWeb Ant task

%prep
%setup -q -c -n %{name}
%patch1
%patch2 -p1
find . -name "*.class" -exec rm {} \;
find . -name "*.jar" -exec rm {} \;

%build
export CLASSPATH=$(build-classpath xalan-j2)
ant \
    -Dbuild.compiler=modern \
    -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
    jar

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 output/lib/ow_util_ant_tasks.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%{_javadir}/*

%changelog
