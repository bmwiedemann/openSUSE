#
# spec file for package python-azure-messaging-webpubsubclient
#
# Copyright (c) 2023 SUSE LLC
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

%define realversion 1.0.0b1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-messaging-webpubsubclient
Version:        1.0.0~b1
Release:        0
Summary:        Microsoft Azure Web PubSub Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-messaging-webpubsubclient/azure-messaging-webpubsubclient-%{realversion}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-messaging-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.24.0
Requires:       python-azure-messaging-nspkg >= 1.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-isodate >= 0.6.1
Requires:       python-isodate < 1.0.0
Requires:       python-websocket-client >= 1.4.2
Requires:       python-websocket-client < 2.0.0
Requires:       (python-typing_extensions >= 4.3.0 if python-base < 3.8)
Conflicts:      python-azure-sdk <= 2.0.0

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
%setup -q -n azure-messaging-webpubsubclient-%{realversion}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-messaging-webpubsubclient-%{realversion}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/messaging/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/messaging/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/messaging/webpubsubclient
%{python_sitelib}/azure_messaging_webpubsubclient-*.egg-info

%changelog
