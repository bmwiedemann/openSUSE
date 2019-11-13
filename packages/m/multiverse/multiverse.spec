#
# spec file for package multiverse
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


Name:           multiverse
Version:        0.7.0
Release:        0
Summary:        A software transactional memory implementation for the JVM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://multiverse.codehaus.org
Source0:        https://github.com/pveentjer/Multiverse/archive/multiverse-0.7.0.tar.gz
# Only the license header is included in the source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildArch:      noarch

%description
A software transactional memory implementation for the JVM. Access (read and
writes) to shared memory is done through transactional references, that can be
compared to the AtomicReferences of Java. Access to these references will be
done under A (atomicity), C (consistency), I (isolation) semantics.

%package javadoc
Summary:        JavaDoc for %{name}
Group:          Documentation/HTML

%description javadoc
JavaDoc for %{name}.

%prep
%setup -q -n Multiverse-%{name}-%{version}

# wagon-webdav
%pom_xpath_remove pom:build/pom:extensions

%pom_remove_plugin :maven-deploy-plugin

cp -p %{SOURCE1} .

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc LICENSE-2.0.txt README.md
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
