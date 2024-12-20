#
# spec file
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


%global base_name       email
%global short_name      commons-%{base_name}
Name:           apache-%{short_name}
Version:        1.5
Release:        0
Summary:        Apache Commons Email Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        build.xml.tar.bz2
Patch0:         commons-email-1.5-sourcetarget.patch
Patch1:         commons-email-1.5-javadoc.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  glassfish-activation-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javamail
BuildRequires:  javapackages-tools
Requires:       java >= 1.8
Requires:       javamail
BuildArch:      noarch

%description
Commons-Email aims to provide an API for sending email. It is built on top of
the JavaMail API, which it aims to simplify.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/Other

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -p1 -n %{short_name}-%{version}-src -a1

%build
ant -Dmaven.mode.offline=true -Dmaven.test.skip=true \
    -lib %{_javadir} javadoc package

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt
%{_javadir}/*

%files javadoc
%license LICENSE.txt NOTICE.txt
%doc %{_javadocdir}/%{name}

%changelog
