#
# spec file for package python-azure-eventhub
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
Name:           python-azure-eventhub
Version:        5.12.1
Release:        0
Summary:        Azure Event Hubs client library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-eventhub/azure-eventhub-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-typing_extensions >= 4.0.1
Requires:       (python-azure-core >= 1.14.0 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-eventhub < 5.11.6
%endif
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/eventhub
%{python_sitelib}/azure_eventhub-*.dist-info

%changelog
