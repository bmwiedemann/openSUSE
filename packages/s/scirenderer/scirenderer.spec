#
# spec file for package scirenderer
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


Name:           scirenderer
Version:        1.1.0
Release:        0
Summary:        A Java rendering library based on JoGL
License:        CECILL-2.0
Group:          Development/Libraries/Java
Url:            http://forge.scilab.org/index.php/p/scirenderer
Source0:        http://forge.scilab.org/index.php/p/scirenderer/downloads/get/%{name}-%{version}.tar.gz
Patch0:         %{name}-0000-jogl2.0.2.patch
# PATCH-FIX-UPSTREAM scirenderer-fix-compilation-with-jogl-2.3.patch badshah400@gmail.com -- Fix compilation with jogl 2.3.x
Patch1:         scirenderer-fix-compilation-with-jogl-2.3.patch
Patch2:         scirenderer-1.1.0-javadoc.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  jlatexmath
BuildRequires:  jogl2 >= 2.3
BuildRequires:  jpackage-utils
Requires:       java
Requires:       jpackage-utils
BuildArch:      noarch

%description
SciRenderer is a rendering library based on JoGL. This Java API allows
2-D or 3-D plotting from simple 2-D graph to complex scenes. Independent
library, SciRender is used within Scilab software but is available
for other application and developments.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains the documentation for SciRenderer.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

# Update path according to the openSUSE
tee scirenderer-libs.properties << EOF
jogl2.jar=%{_jnidir}/jogl2.jar
gluegen2-rt.jar=%{_javadir}/gluegen2-rt.jar
jlatexmath.jar=%{_javadir}/jlatexmath.jar
EOF

# fix class-path-in-manifest
sed -i '/Class-Path/I d' build.xml

%build
%{ant} jar doc

%install
install -Dm 644 jar/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%doc README COPYING CHANGES

%files javadoc
%{_javadocdir}/%{name}

%changelog
