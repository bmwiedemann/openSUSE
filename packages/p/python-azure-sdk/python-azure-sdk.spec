#
# spec file for package python-azure-sdk
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-azure-sdk
Version:        4.0.0
Release:        0
Summary:        Microsoft Azure bundle
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
BuildRequires:  python-rpm-macros
Requires:       python-azure-appconfiguration < 2.0.0
Requires:       python-azure-appconfiguration >= 1.1.0
Requires:       python-azure-applicationinsights < 1.0.0
Requires:       python-azure-applicationinsights >= 0.1.0
Requires:       python-azure-batch < 10.0.0
Requires:       python-azure-batch >= 9.0.0
Requires:       python-azure-cognitiveservices-anomalydetector < 1.0.0
Requires:       python-azure-cognitiveservices-anomalydetector >= 0.3.0
Requires:       python-azure-cognitiveservices-formrecognizer < 1.0.0
Requires:       python-azure-cognitiveservices-formrecognizer >= 0.1.0
Requires:       python-azure-cognitiveservices-inkrecognizer < 2.0.0
Requires:       python-azure-cognitiveservices-inkrecognizer >= 1.0.0
Requires:       python-azure-cognitiveservices-knowledge-qnamaker < 1.0.0
Requires:       python-azure-cognitiveservices-knowledge-qnamaker >= 0.2.0
Requires:       python-azure-cognitiveservices-language-luis < 1.0.0
Requires:       python-azure-cognitiveservices-language-luis >= 0.7.0
Requires:       python-azure-cognitiveservices-language-spellcheck < 3.0.0
Requires:       python-azure-cognitiveservices-language-spellcheck >= 2.0.0
Requires:       python-azure-cognitiveservices-language-textanalytics < 1.0.0
Requires:       python-azure-cognitiveservices-language-textanalytics >= 0.2.0
Requires:       python-azure-cognitiveservices-personalizer < 1.0.0
Requires:       python-azure-cognitiveservices-personalizer >= 0.1.0
Requires:       python-azure-cognitiveservices-search-autosuggest < 1.0.0
Requires:       python-azure-cognitiveservices-search-autosuggest >= 0.2.0
Requires:       python-azure-cognitiveservices-search-customimagesearch < 1.0.0
Requires:       python-azure-cognitiveservices-search-customimagesearch >= 0.2.0
Requires:       python-azure-cognitiveservices-search-customsearch < 1.0.0
Requires:       python-azure-cognitiveservices-search-customsearch >= 0.3.0
Requires:       python-azure-cognitiveservices-search-entitysearch < 3.0.0
Requires:       python-azure-cognitiveservices-search-entitysearch >= 2.0.0
Requires:       python-azure-cognitiveservices-search-imagesearch < 3.0.0
Requires:       python-azure-cognitiveservices-search-imagesearch >= 2.0.0
Requires:       python-azure-cognitiveservices-search-newssearch < 3.0.0
Requires:       python-azure-cognitiveservices-search-newssearch >= 2.0.0
Requires:       python-azure-cognitiveservices-search-videosearch < 3.0.0
Requires:       python-azure-cognitiveservices-search-videosearch >= 2.0.0
Requires:       python-azure-cognitiveservices-search-visualsearch < 1.0.0
Requires:       python-azure-cognitiveservices-search-visualsearch >= 0.2.0
Requires:       python-azure-cognitiveservices-search-websearch < 3.0.0
Requires:       python-azure-cognitiveservices-search-websearch >= 2.0.0
Requires:       python-azure-cognitiveservices-vision-computervision < 1.0.0
Requires:       python-azure-cognitiveservices-vision-computervision >= 0.6.0
Requires:       python-azure-cognitiveservices-vision-contentmoderator < 2.0.0
Requires:       python-azure-cognitiveservices-vision-contentmoderator >= 1.0.0
Requires:       python-azure-cognitiveservices-vision-customvision < 4.0.0
Requires:       python-azure-cognitiveservices-vision-customvision >= 3.0.0
Requires:       python-azure-cognitiveservices-vision-face < 1.0.0
Requires:       python-azure-cognitiveservices-vision-face >= 0.4.1
Requires:       python-azure-cosmos < 5.0.0
Requires:       python-azure-cosmos >= 4.0.0
Requires:       python-azure-datalake-store < 1.0.0
Requires:       python-azure-datalake-store >= 0.0.48
Requires:       python-azure-eventgrid < 2.0.0
Requires:       python-azure-eventgrid >= 1.2.0
Requires:       python-azure-eventhub < 6.0.0
Requires:       python-azure-eventhub >= 5.0.1
Requires:       python-azure-eventhub-checkpointstoreblob < 2.0.0
Requires:       python-azure-eventhub-checkpointstoreblob >= 1.1.0
Requires:       python-azure-graphrbac < 1.0.0
Requires:       python-azure-graphrbac >= 0.40.0
Requires:       python-azure-keyvault < 5.0.0
Requires:       python-azure-keyvault >= 4.0.0
Requires:       python-azure-keyvault-administration < 5.0.0
Requires:       python-azure-keyvault-administration >= 4.0.0
Requires:       python-azure-keyvault-certificates < 5.0.0
Requires:       python-azure-keyvault-certificates >= 4.0.0
Requires:       python-azure-keyvault-keys < 5.0.0
Requires:       python-azure-keyvault-keys >= 4.0.0
Requires:       python-azure-keyvault-secrets < 5.0.0
Requires:       python-azure-keyvault-secrets >= 4.0.0
Requires:       python-azure-loganalytics < 1.0.0
Requires:       python-azure-loganalytics >= 0.1.0
Requires:       python-azure-mgmt < 5.0.0
Requires:       python-azure-mgmt >= 4.0.0
Requires:       python-azure-monitor < 1.0.0
Requires:       python-azure-monitor >= 0.3.0
Requires:       python-azure-servicebus < 1.0.0
Requires:       python-azure-servicebus >= 0.21.1
Requires:       python-azure-servicefabric < 8.0.0.0
Requires:       python-azure-servicefabric >= 7.0.0.0
Requires:       python-azure-servicemanagement-legacy < 1.0.0
Requires:       python-azure-servicemanagement-legacy >= 0.20.6
Requires:       python-azure-storage-blob < 13.0.0
Requires:       python-azure-storage-blob >= 12.1.0
Requires:       python-azure-storage-file < 3.0.0
Requires:       python-azure-storage-file >= 2.0.0
Requires:       python-azure-storage-queue < 13.0.0
Requires:       python-azure-storage-queue >= 12.1.0

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
