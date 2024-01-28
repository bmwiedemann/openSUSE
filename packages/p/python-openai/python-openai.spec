#
# spec file for package python-openai
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


%define         skip_python2 1
%define         skip_python36 1
Name:           python-openai
Version:        1.10.0
Release:        0
Summary:        OpenAI bindings for python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/openai/openai-python
Source:         https://github.com/openai/openai-python/archive/refs/tags/v%{version}.tar.gz#/openai-%{version}.tar.gz
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module respx}
BuildRequires:  %{python_module sniffio}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 3.5.0
Requires:       python-distro >= 1.7.0
Requires:       python-httpx >= 0.23.0
Requires:       python-pydantic >= 1.9.0
Requires:       python-sniffio
Requires:       python-tqdm > 4
Requires:       python-typing_extensions
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The OpenAI Python library provides convenient access to the OpenAI API
from applications written in the Python language. It includes a
pre-defined set of classes for API resources that initialize
themselves dynamically from API responses which makes it compatible
with a wide range of versions of the OpenAI API.

You can find usage examples for the OpenAI Python library in
 https://beta.openai.com/docs/api-reference?lang=python
 https://github.com/openai/openai-cookbook/.

%prep
%autosetup -p1 -n openai-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/openai

%check
# most of tests/api_resources need registered API key
# test_streaming_response needs network connection
# test_copy_build_request needs "warmed up" machinery and OBS starts always fresh
%pytest --ignore "tests/api_resources" -k "not (test_streaming_response or test_copy_build_request)"

%post
%python_install_alternative openai

%postun
%python_uninstall_alternative openai

%files %{python_files}
%python_alternative %{_bindir}/openai
%{python_sitelib}/openai
%{python_sitelib}/openai-%{version}*-info

%changelog
