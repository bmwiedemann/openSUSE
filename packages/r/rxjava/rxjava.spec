#
# spec file for package rxjava
#
# Copyright (c) 2025 SUSE LLC
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


Name:           rxjava
Version:        3.1.10
Release:        0
Summary:        Reactive Extensions for the JVM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/ReactiveX/RxJava
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/io/reactivex/%{name}3/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.reactivestreams:reactive-streams)
BuildArch:      noarch

%description
RxJava is a Java VM implementation of Reactive Extensions: a library for
composing asynchronous and event-based programs by using observable sequences.

It extends the observer pattern to support sequences of data/events and adds
operators that allow you to compose sequences together declaratively while
abstracting away concerns about things like low-level threading,
synchronization, thread-safety and concurrent data structures.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n RxJava-%{version}
cp %{SOURCE1} pom.xml

%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin \
'<configuration>
    <source>8</source>
    <target>8</target>
</configuration>'

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- \
	-Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc {README,DESIGN}.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
