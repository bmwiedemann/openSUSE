#
# spec file for package swing-worker
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


Name:           swing-worker
Version:        1.2
Release:        0
Summary:        UI updates support for long running tasks
License:        LGPL-2.1+
Group:          Development/Libraries/Java
Url:            https://swingworker.dev.java.net/
Source0:        %{name}-src-%{version}.tar.bz2
Source1:        releasenotes.txt
Patch0:         swing-worker-1.2-nosource.patch
Patch1:         swing-worker-1.2-encoding.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
Requires:       java
BuildArch:      noarch

%description
SwingWorker is designed for situations where you need to have a long
running task run in a background thread and provide updates to the UI
either when done, or while processing. This project is a backport of
SwingWorker included into Java 1.6.

%package javadoc
Summary:        UI updates support for long running tasks
Group:          Development/Libraries/Java

%description		javadoc
SwingWorker is designed for situations where you need to have a long
running task run in a background thread and provide updates to the UI
either when done, or while processing. This project is a backport of
SwingWorker included into Java 1.6.

%package demo
Summary:        UI updates support for long running tasks
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description 		demo
SwingWorker is designed for situations where you need to have a long
running task run in a background thread and provide updates to the UI
either when done, or while processing. This project is a backport of
SwingWorker included into Java 1.6.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1
%patch1 -p1
# remove all third party jars
find . -iname '*.jar' | xargs rm -rf
cp %{SOURCE1} .
# wrong end of line encoding
sed -i -e 's/.$//' releasenotes.txt COPYING

%build
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    bundles

%install
install -d -m 755 %{buildroot}/%{_javadir}
# jars
install -pm 644 dist/bundles/%{name}.jar %{buildroot}/%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir}/ && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
# javadoc
install -d -m 755 %{buildroot}/%{_javadocdir}/%{name}
cp -pr dist/javadoc/* %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}/%{_javadocdir}/%{name}
# demo
install -d %{buildroot}/%{_datadir}/%{name}
cp -pr src/demo %{buildroot}/%{_datadir}/%{name}
%fdupes -s %{buildroot}/%{_datadir}/%{name}

%files
%doc COPYING releasenotes.txt
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
