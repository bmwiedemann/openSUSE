#
# spec file for package schemaspy
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013 Archie L. Cobbs.
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


Name:           schemaspy
Version:        5.0.0
Release:        0
Summary:        Tool for analyzing and graphing database schemas
License:        LGPL-2.1-only
Group:          Productivity/Databases/Tools
URL:            https://schemaspy.sourceforge.net/
Source0:        schemaSpy_%{version}.source.jar
Source1:        schemaspy.1
# PATCH-FIX-OPENSUSE driver-location.patch
Patch0:         driver-location.patch
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  unzip
Requires:       graphviz
Requires:       graphviz-gd
Requires:       java >= 1.8
Requires:       javapackages-tools
Suggests:       mysql-connector-java
BuildArch:      noarch

%description
SchemaSpy is a Java-based tool that analyzes the metadata of a
schema in a database and generates a visual representation of it in a
browser-displayable format. It lets you click through the hierarchy of
database tables via child and parent table relationships as represented
by both HTML links and entity-relationship diagrams. It's also designed
to help resolve the obtuse errors that a database sometimes gives related
to failures due to constraints.

SchemaSpy uses JDBC's database metadata extraction services to gather the
majority of its information, but has to make vendor-specific SQL queries
to gather some information such as the SQL associated with a view and
the details of check constraints. The differences between vendors have
been isolated to configuration files and are extremely limited. Almost
all of the vendor-specific SQL is optional.

%prep
%setup -q -c
%patch -P 0 -p1

%build
mkdir classes
javac -source 1.8 -target 1.8 -d classes `find net -name '*.java' -print`
jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --create --file=%{name}-%{version}.jar \
    META-INF/MANIFEST.MF *.* images -C classes . `find net -name '*.properties'`

%install

# JAR file
install -d %{buildroot}%{_javadir}
install %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# Man page
install -d %{buildroot}%{_mandir}/man1
install %{_sourcedir}/%{name}.1 %{buildroot}%{_mandir}/man1

# Command line script
%jpackage_script net.sourceforge.schemaspy.Main "" "" %{name} %{name}

%files
%attr(0755,root,root) %{_bindir}/%{name}
%defattr(0644,root,root,0755)
%{_javadir}/*
%{_mandir}/man1/*

%changelog
