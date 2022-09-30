#
# spec file for package python-azure-sdk
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-sdk
Version:        4.0.0
Release:        0
Summary:        Microsoft Azure bundle
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
BuildRequires:  python-rpm-macros
Requires:       python-adal
Requires:       python-applicationinsights
Requires:       python-azure-agrifood-farming
Requires:       python-azure-ai-anomalydetector
Requires:       python-azure-ai-formrecognizer
Requires:       python-azure-ai-language-conversations
Requires:       python-azure-ai-language-questionanswering
Requires:       python-azure-ai-metricsadvisor
Requires:       python-azure-ai-nspkg
Requires:       python-azure-ai-textanalytics
Requires:       python-azure-ai-translation-document
Requires:       python-azure-appconfiguration
Requires:       python-azure-applicationinsights
Requires:       python-azure-batch
Requires:       python-azure-cognitiveservices-anomalydetector
Requires:       python-azure-cognitiveservices-formrecognizer
Requires:       python-azure-cognitiveservices-inkrecognizer
Requires:       python-azure-cognitiveservices-knowledge-nspkg
Requires:       python-azure-cognitiveservices-knowledge-qnamaker
Requires:       python-azure-cognitiveservices-language-luis
Requires:       python-azure-cognitiveservices-language-nspkg
Requires:       python-azure-cognitiveservices-language-spellcheck
Requires:       python-azure-cognitiveservices-language-textanalytics
Requires:       python-azure-cognitiveservices-nspkg
Requires:       python-azure-cognitiveservices-personalizer
Requires:       python-azure-cognitiveservices-search-autosuggest
Requires:       python-azure-cognitiveservices-search-customimagesearch
Requires:       python-azure-cognitiveservices-search-customsearch
Requires:       python-azure-cognitiveservices-search-entitysearch
Requires:       python-azure-cognitiveservices-search-imagesearch
Requires:       python-azure-cognitiveservices-search-newssearch
Requires:       python-azure-cognitiveservices-search-nspkg
Requires:       python-azure-cognitiveservices-search-videosearch
Requires:       python-azure-cognitiveservices-search-visualsearch
Requires:       python-azure-cognitiveservices-search-websearch
Requires:       python-azure-cognitiveservices-vision-computervision
Requires:       python-azure-cognitiveservices-vision-contentmoderator
Requires:       python-azure-cognitiveservices-vision-customvision
Requires:       python-azure-cognitiveservices-vision-face
Requires:       python-azure-cognitiveservices-vision-nspkg
Requires:       python-azure-common
Requires:       python-azure-communication-administration
Requires:       python-azure-communication-chat
Requires:       python-azure-communication-email
Requires:       python-azure-communication-identity
Requires:       python-azure-communication-networktraversal
Requires:       python-azure-communication-nspkg
Requires:       python-azure-communication-phonenumbers
Requires:       python-azure-communication-sms
Requires:       python-azure-confidentialledger
Requires:       python-azure-containerregistry
Requires:       python-azure-core
Requires:       python-azure-core-tracing-opencensus
Requires:       python-azure-core-tracing-opentelemetry
Requires:       python-azure-cosmos
Requires:       python-azure-data-nspkg
Requires:       python-azure-data-tables
Requires:       python-azure-datalake-store
Requires:       python-azure-digitaltwins-core
Requires:       python-azure-eventgrid
Requires:       python-azure-eventhub
Requires:       python-azure-eventhub-checkpointstoreblob
Requires:       python-azure-eventhub-checkpointstoreblob-aio
Requires:       python-azure-functions-devops-build
Requires:       python-azure-graphrbac
Requires:       python-azure-identity
Requires:       python-azure-iot-deviceupdate
Requires:       python-azure-iot-nspkg
Requires:       python-azure-keyvault
Requires:       python-azure-keyvault-administration
Requires:       python-azure-keyvault-certificates
Requires:       python-azure-keyvault-keys
Requires:       python-azure-keyvault-nspkg
Requires:       python-azure-keyvault-secrets
Requires:       python-azure-loganalytics
Requires:       python-azure-media-videoanalyzer-edge
Requires:       python-azure-messaging-webpubsubservice
Requires:       python-azure-mgmt
Requires:       python-azure-mgmt-appcontainers
Requires:       python-azure-mgmt-confidentialledger
Requires:       python-azure-mgmt-dnsresolver
Requires:       python-azure-mgmt-dynatrace
Requires:       python-azure-mgmt-nginx
Requires:       python-azure-mgmt-scvmm
Requires:       python-azure-mgmt-workloads
Requires:       python-azure-mixedreality-authentication
Requires:       python-azure-monitor
Requires:       python-azure-monitor-ingestion
Requires:       python-azure-monitor-query
Requires:       python-azure-multiapi-storage
Requires:       python-azure-nspkg
Requires:       python-azure-purview-account
Requires:       python-azure-purview-administration
Requires:       python-azure-purview-catalog
Requires:       python-azure-purview-scanning
Requires:       python-azure-schemaregistry
Requires:       python-azure-schemaregistry-avroserializer
Requires:       python-azure-search-documents
Requires:       python-azure-search-nspkg
Requires:       python-azure-security-attestation
Requires:       python-azure-servicebus
Requires:       python-azure-servicefabric
Requires:       python-azure-servicemanagement-legacy
Requires:       python-azure-storage-blob
Requires:       python-azure-storage-common
Requires:       python-azure-storage-file
Requires:       python-azure-storage-file-datalake
Requires:       python-azure-storage-file-share
Requires:       python-azure-storage-nspkg
Requires:       python-azure-storage-queue
Requires:       python-azure-synapse
Requires:       python-azure-synapse-accesscontrol
Requires:       python-azure-synapse-artifacts
Requires:       python-azure-synapse-managedprivateendpoints
Requires:       python-azure-synapse-monitoring
Requires:       python-azure-synapse-nspkg
Requires:       python-azure-synapse-spark
Requires:       python-azure-template
Requires:       python-msal
Requires:       python-msal-extensions
Requires:       python-msrest
Requires:       python-msrestazure
Requires:       python-pydocumentdb
Requires:       python-uamqp
BuildArch:      noarch
%python_subpackages

%description
This is the Microsoft Azure bundle.

This package does not contain any code in itself. It installs a set
of packages that provide Microsoft Azure functionality.

All packages in this bundle have been tested with Python 2.7, 3.4, 3.5, 3.6 and 3.7.

%prep
# Nothing to prep

%build
# Nothing to build

%install
# Nothing to install

%files %{python_files}

%changelog
