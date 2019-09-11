#
# spec file for package gradle
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gradle
Version:        3.2.1
Release:        0
Summary:        Groovy-based build system
License:        Apache-2.0
Group:          Development/Tools
Url:            http://www.gradle.org/
Source0:        https://github.com/gradle/gradle/archive/v%{version}.zip
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A flexible groovy-based build tool.

%package open-api
Summary:        Open API definition for %{name}
Group:          Development/Tools
Requires:       jpackage-utils

%description open-api
Open API definition for gradle. It provides a simple versioned way to
interact with gradle. The open API jar is all that is needed to
develop/distribute a plugin. It provides some static functions that
dynamically load gradle from a directory you specify to do things like
create the UI or execute gradle commands directly (and I think some gradle
debugger information may soon be accessible there). All you need is the
gradle home directory and the open API jar.

%prep
%setup -q

%build
# Build Open API subpackage
pushd subprojects/open-api/src/main/java
find -name '*.java' |xargs javac -source 1.6 -target 1.6
find -name '*.class' |xargs jar cf gradle-open-api.jar
popd

%install
install -d %{buildroot}%{_javadir}
# Open API
pushd subprojects/open-api/src/main/java
install -p -m644 gradle-open-api.jar \
        %{buildroot}%{_javadir}/gradle-open-api-%{version}.jar
ln -s gradle-open-api-%{version}.jar \
        %{buildroot}%{_javadir}/gradle-open-api.jar
popd

%files open-api
%defattr(-,root,root,-)
%{_javadir}/gradle-open-api-%{version}.jar
%{_javadir}/gradle-open-api.jar
%doc LICENSE
%doc subprojects/distributions/src/toplevel/NOTICE

%changelog
