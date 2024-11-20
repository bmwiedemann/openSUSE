#
# spec file for package python-langfuse
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
Name:           python-langfuse
Version:        2.54.1
Release:        0
Summary:        A client library for accessing langfuse
License:        MIT
URL:            https://github.com/langfuse/langfuse-python
Source:         https://files.pythonhosted.org/packages/source/l/langfuse/langfuse-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio
Requires:       python-backoff
Requires:       python-httpx
Requires:       python-idna
Requires:       python-packaging
Requires:       python-pydantic
Requires:       python-wrapt
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A client library for accessing langfuse, an open-source LLM engineering platform that helps teams
collaboratively debug, analyze, and iterate on their LLM applications.

%prep
%autosetup -p1 -n langfuse-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/release
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative release

%postun
%python_uninstall_alternative release

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/release
%{python_sitelib}/langfuse
%{python_sitelib}/langfuse-%{version}.dist-info

%changelog
