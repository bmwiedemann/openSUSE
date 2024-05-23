#
# spec file for package python-azure-ai-translation-text
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
Name:           python-azure-ai-translation-text
Version:        1.0.0
Release:        0
Summary:        Azure Text Translation Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-ai-translation-text/azure-ai-translation-text-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-ai-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-ai-translation-nspkg >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-azure-ai-nspkg >= 1.0.0
Requires:       python-azure-ai-translation-nspkg >= 1.0.0
Requires:       (python-azure-common >= 1.1 with python-azure-common < 2.0.0)
Requires:       (python-azure-core >= 1.30.0 with python-azure-core < 2.0.0)
Requires:       (python-isodate >= 0.6.1 with python-isodate < 1.0.0)
Requires:       (python-typing_extensions >= 4.6.0 if python-base < 3.8)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-ai-translation-text < 1.0.0~b1
%endif
BuildArch:      noarch
%python_subpackages

%description
Text Translation is a cloud-based REST API feature of the Translator service that uses
neural machine translation technology to enable quick and accurate source-to-target
text translation in real time across all supported languages.

Use the Text Translation client library for Python to:

* Return a list of languages supported by Translate, Transliterate, and Dictionary operations.
* Render single source-language text to multiple target-language texts with a single request.
* Convert text of a source language in letters of a different script.
* Return equivalent words for the source term in the target language.
* Return grammatical structure and context examples for the source term and target term pair.

%prep
%setup -q -n azure-ai-translation-text-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-ai-translation-text-%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/ai/translation/text
%{python_sitelib}/azure_ai_translation_text-*.dist-info

%changelog
