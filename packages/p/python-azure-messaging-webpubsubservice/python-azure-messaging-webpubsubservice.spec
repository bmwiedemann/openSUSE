#
# spec file for package python-azure-messaging-webpubsubservice
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-azure-messaging-webpubsubservice
Version:        1.2.2
Release:        0
Summary:        Microsoft Azure WebPubSub Service Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_messaging_webpubsubservice/azure_messaging_webpubsubservice-%{version}.tar.gz
BuildRequires:  %{python_module azure-messaging-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 2.6.0
Requires:       python-azure-messaging-nspkg >= 1.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-isodate >= 0.6.1
Requires:       python-typing_extensions >= 4.6.0
Requires:       (python-azure-core >= 1.30.0 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-messaging-webpubsubservice <= 1.0.1
%endif
BuildArch:      noarch

%python_subpackages

%description
Azure Web PubSub Service is a service that enables you to build real-time messaging web applications
using WebSockets and the publish-subscribe pattern. Any platform supporting WebSocket APIs can connect
to the service easily, e.g. web pages, mobile applications, edge devices, etc. The service manages the
WebSocket connections for you and allows up to 100K concurrent connections. It provides powerful APIs
for you to manage these clients and deliver real-time messages.

Any scenario that requires real-time publish-subscribe messaging between server and clients or among
clients, can use Azure Web PubSub service. Traditional real-time features that often require polling
from server or submitting HTTP requests, can also use Azure Web PubSub service.

We list some examples that are good to use Azure Web PubSub service:

 * High frequency data updates: gaming, voting, polling, auction.
 * Live dashboards and monitoring: company dashboard, financial market data, instant sales update,
   multi-player game leader board, and IoT monitoring.
 * Cross-platform live chat: live chat room, chat bot, on-line customer support, real-time shopping
   assistant, messenger, in-game chat, and so on.
 * Real-time location on map: logistic tracking, delivery status tracking, transportation status
   updates, GPS apps.
 * Real-time targeted ads: personalized real-time push ads and offers, interactive ads.
 * Collaborative apps: coauthoring, whiteboard apps and team meeting software.
 * Push instant notifications: social network, email, game, travel alert.
 * Real-time broadcasting: live audio/video broadcasting, live captioning, translating,
   events/news broadcasting.
 * IoT and connected devices: real-time IoT metrics, remote control, real-time status,
   and location tracking.
 * Automation: real-time trigger from upstream events.

Use the client library to:

 * Send messages to hubs and groups.
 * Send messages to particular users and connections.
 * Organize users and connections into groups.
 * Close connections
 * Grant/revoke/check permissions for an existing connection

%prep
%setup -q -n azure_messaging_webpubsubservice-%{version}

%build
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
%license LICENSE
%{python_sitelib}/azure/messaging/webpubsubservice
%{python_sitelib}/azure_messaging_webpubsubservice-*.dist-info

%changelog
