#
# spec file for package python-changelog-gen
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
Name:           python-changelog-gen
Version:        0.1.2
Release:        0
Summary:        AI-powered changelog generation from code changes
License:        Apache-2.0
URL:            https://github.com/openSUSE/changelog-gen
Source:         https://github.com/openSUSE/changelog-gen/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
Requires:       python-ctranslate2
Requires:       python-requests
Requires:       python-tokenizers
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
An AI-powered changelog generator that uses fine-tuned T5 models to create
human-readable changelog entries from code changes. It integrates with both
OSC (Open Build Service) and Git repositories, providing automated changelog
generation for software development workflows.

%prep
%autosetup -p1 -n changelog-gen-%{version}

%build
%pyproject_wheel
%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/changelog-ai
%python_clone -a %{buildroot}%{_bindir}/osc-ai-vc

%post
%python_install_alternative changelog-ai osc-ai-vc

%postun
%python_uninstall_alternative changelog-ai

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/changelog-ai
%python_alternative %{_bindir}/osc-ai-vc
%{python_sitelib}/changelog_ai/
%{python_sitelib}/changelog_ai-%{version}*.dist-info

%changelog
