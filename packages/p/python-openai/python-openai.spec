#
# spec file for package python-openai
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


%define         skip_python2 1
%define         skip_python36 1
Name:           python-openai
Version:        0.26.2
Release:        0
Summary:        OpenAI bindings for python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/openai/openai-python
Source:         openai-python-%{version}.tar.gz
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp
Requires:       python-requests >= 2.20
Requires:       python-tqdm
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

# test suite only works with network and registered API key

%post
%python_install_alternative openai

%postun
%python_uninstall_alternative openai

%files %{python_files}
%python_alternative %{_bindir}/openai
%{python_sitelib}/openai
%{python_sitelib}/openai-%{version}*-info

%changelog
