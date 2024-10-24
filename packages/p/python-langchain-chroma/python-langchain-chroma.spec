#
# spec file for package python-langchain-chroma
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
Name:           python-langchain-chroma
Version:        0.1.4
Release:        0
Summary:        An integration package connecting Chroma and LangChain
License:        MIT
URL:            https://github.com/langchain-ai/langchain
Source:         https://files.pythonhosted.org/packages/source/l/langchain-chroma/langchain_chroma-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
# langchain-chroma

This package contains the LangChain integration with Chroma.

## Installation

```bash
pip install -U langchain-chroma
```

## Usage

The `Chroma` class exposes the connection to the Chroma vector store.

```python
from langchain_chroma import Chroma

embeddings = ... # use a LangChain Embeddings class

vectorstore = Chroma(embeddings=embeddings)
```

%prep
%autosetup -p1 -n langchain_chroma-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/langchain_chroma
%{python_sitelib}/langchain_chroma-%{version}.dist-info

%changelog
