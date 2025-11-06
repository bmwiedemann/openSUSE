#
# spec file for package xmvn5
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global parent xmvn
%global version_suffix 5
Name:           %{parent}%{version_suffix}
Version:        5.1.0
Release:        0
Summary:        Local Extensions for Apache Maven
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
BuildRequires:  %{name}-api = %{version}
BuildRequires:  %{name}-connector = %{version}
BuildRequires:  %{name}-core = %{version}
BuildRequires:  javapackages-tools
BuildRequires:  kojan-xml
BuildRequires:  maven4
BuildRequires:  maven4-lib
BuildRequires:  xmvn-subst
Requires:       %{name}-minimal = %{version}-%{release}

%description
This package provides extensions for Apache Maven that can be used to
manage system artifact repository and use it to resolve Maven
artifacts in offline mode, as well as Maven plugins to help with
creating RPM packages containing Maven artifacts.

%package        minimal
Summary:        Dependency-reduced version of XMvn
Group:          Development/Tools/Building
Requires:       %{name}-api = %{version}
Requires:       %{name}-connector = %{version}
Requires:       %{name}-core = %{version}
Requires:       kojan-xml
%requires_eq    maven4
%requires_eq    maven4-lib

%description    minimal
This package provides minimal version of XMvn, incapable of using
remote repositories.

%prep

%build

%install
# Please, keep in sync with maven4 package, since the use
# of libalternatives in some distro versions makes it
# more tedious to detect automatically
maven_home=%{_datadir}/maven4

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -aL ${maven_home}/* %{buildroot}%{_datadir}/%{name}/

for i in api core connector; do
    ln -s $(find-jar %{parent}/%{parent}-${i}-%{version_suffix}) %{buildroot}%{_datadir}/%{name}/lib/ext/
done
ln -s $(find-jar kojan-xml/kojan-xml) %{buildroot}%{_datadir}/%{name}/lib/ext/

# Irrelevant Maven launcher scripts
rm -f %{buildroot}%{_datadir}/%{name}/bin/*

for cmd in mvn mvnDebug; do
    cat <<EOF >%{buildroot}%{_datadir}/%{name}/bin/$cmd
#!/bin/sh -e
export _FEDORA_MAVEN_HOME="%{_datadir}/%{name}"
exec ${maven_home}/bin/$cmd "\${@}"
EOF
    chmod 755 %{buildroot}%{_datadir}/%{name}/bin/$cmd
done

# possibly recreate symlinks that can be automated with xmvn-subst
xmvn-subst -s -R %{buildroot} %{buildroot}%{_datadir}/%{name}/

# /usr/bin/xmvn
install -dm 0755 %{buildroot}%{_bindir}
ln -sf %{_datadir}/%{name}/bin/mvn %{buildroot}%{_bindir}/%{name}

# make sure our conf is identical to maven so yum won't freak out
install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf/
cp -P ${maven_home}/conf/settings.xml %{buildroot}%{_datadir}/%{name}/conf/
cp -P ${maven_home}/bin/m2.conf %{buildroot}%{_datadir}/%{name}/bin/

%pre minimal
if [ -L %{_datadir}/%{name}/conf/logging ]; then
    rm -f %{_datadir}/%{name}/conf/logging
fi

%files minimal
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/*.jar
%{_datadir}/%{name}/lib/ext
%{_datadir}/%{name}/lib/jline-native
%{_datadir}/%{name}/bin/m2.conf
%{_datadir}/%{name}/bin/mvn
%{_datadir}/%{name}/bin/mvnDebug
%{_datadir}/%{name}/boot
%{_datadir}/%{name}/conf

%changelog
