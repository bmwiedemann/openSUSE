#
# spec file for package python-azure-messaging-webpubsubclient
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-azure-messaging-webpubsubclient
Version:        1.1.0
Release:        0
Summary:        Microsoft Azure Web PubSub Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-messaging-webpubsubclient/azure-messaging-webpubsubclient-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-messaging-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-messaging-nspkg >= 1.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       (python-azure-core >= 1.26.3 with python-azure-core < 2.0.0)
Requires:       (python-isodate >= 0.6.1 with python-isodate < 1.0.0)
Requires:       (python-websocket-client >= 1.6.0 with python-websocket-client < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-messaging-webpubsubclient < 1.0.0~b1
%endif
BuildArch:      noarch

%python_subpackages

%description
Azure Web PubSub is a cloud service that helps developers easily build real-time features
in web applications with publish-subscribe patterns at scale.

Any scenario that requires real-time messaging between server and clients or among clients
following publish-subscribe patterns can benefit from using Web PubSub. Developers no longer
need to poll the server by sending repeated HTTP requests at intervals, which is wasteful
and hard-to-scale.

As shown in the diagram below, your clients establish WebSocket connections with your Web
PubSub resource. This client library:

 * simplifies managing client connections
 * simplifies sending messages among clients
 * automatically retries after unintended drops of client connection
 * reliably deliveries messages in number and in order after recovering from connection drops

%prep
%setup -q -n azure-messaging-webpubsubclient-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-messaging-webpubsubclient-%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/messaging/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/messaging/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/messaging/webpubsubclient
%{python_sitelib}/azure_messaging_webpubsubclient-*.dist-info

%changelog
