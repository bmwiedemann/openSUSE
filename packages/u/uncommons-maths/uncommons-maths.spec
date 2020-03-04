#
# spec file for package uncommons-maths
#
# Copyright (c) 2020 SUSE LLC
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


Name:           uncommons-maths
Version:        1.2.3
Release:        0
Summary:        Random number generators library for Java
License:        Apache-2.0
URL:            https://maths.uncommons.org/
Source0:        %{name}-%{version}.tar.xz
Patch0:         uncommons-maths-1.2.3-pom.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jfree:jcommon)
BuildRequires:  mvn(org.jfree:jfreechart)
BuildArch:      noarch

%description
The Uncommons Maths library provides five easy-to-use,
statistically sound, high-performance pseudo-random
number generators (RNGs).

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%patch0
sed -i "s|<version>@VERSION@</version>|<version>%{version}</version>|" core/pom.xml

%build

cd core
%{mvn_file} : %{name}

%{mvn_build} -f

%install

cd core
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f core/.mfiles
%doc CHANGELOG.txt
%license LICENCE.txt NOTICE.txt

%files javadoc -f core/.mfiles-javadoc
%license LICENCE.txt NOTICE.txt

%changelog
