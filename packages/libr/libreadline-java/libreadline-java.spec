#
# spec file for package libreadline-java
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libreadline-java
Version:        0.8.2
Release:        0
Summary:        Java Wrapper for the EditLine Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Java
URL:            https://github.com/aclemons/java-readline
Source0:        https://github.com/aclemons/java-readline/releases/download/v%{version}/%{name}-%{version}-src.tar.gz
Source1:        baselibs.conf
Patch0:         libreadline-java-ncurses.patch
Patch1:         libreadline-java-libdir.patch
Patch3:         libreadline-java-0.8.0-jdk10.patch
Patch4:         libreadline-java-0.8.0-sourcetarget.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  libedit-devel >= 2.9
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
Requires:       java
Requires:       libedit >= 2.9
Provides:       gnu.readline
Provides:       java_readline

%description
libreadline-java provides Java bindings for libedit though a JNI
wrapper.

%package javadoc
Summary:        Javadoc for libreadline-java
Group:          Development/Libraries/Java

%description javadoc
libreadline-java provides Java bindings for libedit though a JNI
wrapper. This package contains the javadoc documentation for it.

%prep
%setup -q
%patch0
%patch1
%patch3 -p1
%patch4 -p1
find . -name "*.jar" -exec rm -f {} \;
sed -i 's|@LIBDIR@|%{_libdir}|' src/org/gnu/readline/Readline.java

%build
export JAVA_HOME=%{java_home}
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH
make CFLAGS="%{optflags} -fPIC -DPOSIX" T_LIBS=JavaEditline -j1
make apidoc -j1

# fix debuginfo package
rm -f org test
for dir in org test
do
  ln -s src/$dir
done

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m 644 %{name}.jar \
  %{buildroot}%{_libdir}/%{name}/%{name}.jar
install -m 755 libJavaEditline.so %{buildroot}%{_libdir}/%{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%license COPYING.LIB
%doc ChangeLog NEWS README README.1st VERSION
%dir %{_libdir}/%{name}
%attr(-,root,root) %{_libdir}/%{name}/*

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
