#
# spec file for package jhighlight
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


Name:           jhighlight
Version:        1.0.1
Release:        0
Summary:        An embeddable pure Java syntax highlighting library
License:        LGPL-2.1-or-later OR CDDL-1.0
Group:          Development/Libraries/Java
URL:            http://svn.rifers.org/jhighlight
Source0:        https://github.com/codelibs/jhighlight/archive/jhighlight-%{version}.tar.gz
Patch0:         servlet31.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
JHighlight is an embeddable pure Java syntax highlighting library that supports
Java, Groovy, C++, HTML, XHTML, XML and LZX languages and outputs to XHTML. It
also supports RIFE (http://rifers.org) templates tags and highlights them
clearly so that you can easily identify the difference between your RIFE markup
and the actual marked up source.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0
%{mvn_alias} : com.uwyn:

%build
%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license COPYING
%doc LICENSE_LGPL.txt LICENSE_CDDL.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE_LGPL.txt LICENSE_CDDL.txt
%license COPYING

%changelog
