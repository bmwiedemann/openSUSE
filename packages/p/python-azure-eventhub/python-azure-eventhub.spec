#
# spec file for package python-azure-eventhub
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-eventhub
Version:        5.4.0
Release:        0
Summary:        Azure Event Hubs client library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-eventhub/azure-eventhub-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.13.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-uamqp < 2.0
Requires:       python-uamqp >= 1.3.0
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Azure Event Hubs is a highly scalable publish-subscribe service that can ingest millions
of events per second and stream them to multiple consumers. This lets you process and
analyze the massive amounts of data produced by your connected devices and applications.
Once Event Hubs has collected the data, you can retrieve, transform, and store it by using
any real-time analytics provider or with batching/storage adapters. If you would like to
know more about Azure Event Hubs, you may wish to review:
[What is Event Hubs](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-about)?

The Azure Event Hubs client library allows for publishing and consuming of Azure Event
Hubs events and may be used to:

 - Emit telemetry about your application for business intelligence and diagnostic purposes.
 - Publish facts about the state of your application which interested parties may observe
   and use as a trigger for taking action.
 - Observe interesting operations and interactions happening within your business or other
   ecosystem, allowing loosely coupled systems to interact without the need to bind them together.
 - Receive events from one or more publishers, transform them to better meet the needs of
   your ecosystem, then publish the transformed events to a new stream for consumers to observe.

%prep
%setup -q -n azure-eventhub-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-eventhub-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/eventhub
%{python_sitelib}/azure_eventhub-*.egg-info

%changelog
