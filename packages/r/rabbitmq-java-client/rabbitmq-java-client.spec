#
# spec file for package rabbitmq-java-client
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


Name:           rabbitmq-java-client
Version:        3.5.0
Release:        0
Summary:        Java AMQP client library
License:        GPL-2.0+ and MPL-1.1
Group:          Development/Libraries/Java
Url:            https://www.rabbitmq.com/java-client.html
Source0:        https://www.rabbitmq.com/releases/rabbitmq-java-client/v%{version}/%{name}-%{version}.tar.gz
Patch0:         rabbitmq-java-client-3.3.4-disable-bundlor.diff
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  jakarta-commons-cli
BuildRequires:  java-devel
BuildRequires:  junit
BuildRequires:  python
Requires:       apache-commons-io
Requires:       jakarta-commons-cli
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The RabbitMQ Java client library allows Java code to interface to AMQP servers.

%prep
%setup -q
%patch0
find . -name *.jar | xargs rm -f

%build
export CLASSPATH=$(build-classpath commons-io commons-cli junit)
ant dist

%install
mkdir -p %{buildroot}%{_javadir}
install build/lib/rabbitmq-client.jar %{buildroot}%{_javadir}/rabbitmq-client-%{version}.jar
ln -s %{_javadir}/rabbitmq-client-%{version}.jar %{buildroot}%{_javadir}/rabbitmq-client.jar

%files
%defattr(-,root,root)
%doc LICENSE LICENSE-APACHE2 LICENSE-GPL2 LICENSE-MPL-RabbitMQ README
%{_javadir}/rabbitmq-client-%{version}.jar
%{_javadir}/rabbitmq-client.jar

%changelog
