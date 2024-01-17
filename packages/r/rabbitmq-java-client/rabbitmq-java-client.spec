#
# spec file for package rabbitmq-java-client
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


Name:           rabbitmq-java-client
Version:        3.5.0
Release:        0
Summary:        Java AMQP client library
License:        GPL-2.0-or-later AND MPL-1.1
Group:          Development/Libraries/Java
URL:            https://www.rabbitmq.com/java-client.html
Source0:        %{name}-%{version}.tar.xz
Source1:        rabbitmq-codegen-%{version}.tar.xz
Patch0:         rabbitmq-java-client-3.3.4-disable-bundlor.diff
Patch1:         rabbitmq-java-client-python3.patch
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  jakarta-commons-cli
BuildRequires:  java-devel >= 1.8
BuildRequires:  junit
BuildRequires:  python3-devel
Requires:       apache-commons-io
Requires:       jakarta-commons-cli
BuildArch:      noarch

%description
The RabbitMQ Java client library allows Java code to interface to AMQP servers.

%prep
%setup -q -a1
ln -s rabbitmq-codegen-%{version} codegen
%patch0
%patch1 -p1
find . -name *.jar | xargs rm -f
# Java source and target
sed -i -e 's#1\.6#1\.8#g' build.properties

%build
export CLASSPATH=$(build-classpath commons-io commons-cli junit)
ant dist

%install
mkdir -p %{buildroot}%{_javadir}
install build/lib/rabbitmq-client.jar %{buildroot}%{_javadir}/rabbitmq-client.jar

%files
%license LICENSE LICENSE-APACHE2 LICENSE-GPL2 LICENSE-MPL-RabbitMQ
%doc README.md
%{_javadir}/rabbitmq-client.jar

%changelog
