#
# spec file for package python-google-genai
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-google-genai
Version:        1.72.0
Release:        0
Summary:        Interface for developers to integrate Google's LLMs
License:        Apache-2.0
URL:            https://github.com/googleapis/python-genai
Source:         https://files.pythonhosted.org/packages/source/g/google-genai/google_genai-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# Core dependencies
BuildRequires:  %{python_module anyio >= 4.8.0}
BuildRequires:  %{python_module distro >= 1.7.0}
BuildRequires:  %{python_module google-auth >= 2.48.1}
BuildRequires:  %{python_module httpx >= 0.28.1}
BuildRequires:  %{python_module pydantic >= 2.9.0}
BuildRequires:  %{python_module requests >= 2.28.1}
BuildRequires:  %{python_module sniffio}
BuildRequires:  %{python_module tenacity >= 8.2.3}
BuildRequires:  %{python_module typing_extensions >= 4.14.0}
BuildRequires:  %{python_module websockets >= 13.0.0}
BuildRequires:  fdupes
BuildArch:      noarch
# Runtime dependencies
Requires:       python-anyio >= 4.8.0
Requires:       python-distro >= 1.7.0
Requires:       python-google-auth >= 2.48.1
Requires:       python-httpx >= 0.28.1
Requires:       python-pydantic >= 2.9.0
Requires:       python-requests >= 2.28.1
Requires:       python-sniffio
Requires:       python-tenacity >= 8.2.3
Requires:       python-typing-extensions >= 4.14.0
Requires:       python-websockets >= 13.0.0

%python_subpackages

%description
Google Gen AI Python SDK provides an interface for developers to integrate
Google's generative models into their Python applications. It supports the
Gemini Developer API and Gemini Enterprise Agent Platform APIs.

%prep
%autosetup -p1 -n google_genai-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/google/genai/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%dir %{python_sitelib}/google
%{python_sitelib}/google/genai
%{python_sitelib}/google_genai-%{version}.dist-info

%changelog
