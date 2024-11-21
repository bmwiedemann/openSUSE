#
# spec file for package python-tiktoken
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
Name:           python-tiktoken
Version:        0.8.0
Release:        0
Summary:        Fast BPE tokeniser for use with OpenAI's models
License:        MIT
URL:            https://github.com/openai/tiktoken
Source:         tiktoken-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-rust}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# For testing
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module requests}
BuildRequires:  fdupes
BuildRequires:  zstd
Requires:       python-regex
Requires:       python-requests

%python_subpackages

%description
Fast Byte Pair Encoding (BPE) tokeniser for use with OpenAI's models.

%prep
%autosetup -p1 -a1 -n tiktoken-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%check
# NOTE: don't run the tests as they required internet access.

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/tiktoken*

%changelog
