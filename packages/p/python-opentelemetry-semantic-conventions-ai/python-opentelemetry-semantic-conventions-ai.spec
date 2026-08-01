#
# spec file for package python-opentelemetry-semantic-conventions-ai
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


# DO NOT switch Source back to a files.pythonhosted.org URL built from
# %%{version}. This package is released only as part of the traceloop
# openllmetry monorepo: upstream bumped its in-tree version to 0.5.2 on
# 2026-06-15 (commit d7aaf6cc) but never published 0.5.2 to PyPI, whose
# newest sdist is still 0.5.1. A %%{version}-derived PyPI URL therefore
# 404s and the submission is auto-declined. The tarball is the upstream
# monorepo tag v%%{monorepo_ver} and this package lives in %%{pkgsubdir}
# inside it, so %%{monorepo_ver} - not %%{version} - is what moves on the
# next update.
%define monorepo_ver 0.62.1
%define pkgsubdir packages/opentelemetry-semantic-conventions-ai
%{?sle15_python_module_pythons}
Name:           python-opentelemetry-semantic-conventions-ai
Version:        0.5.2
Release:        0
Summary:        OpenTelemetry Semantic Conventions Extension for Large Language Models
License:        Apache-2.0
URL:            https://github.com/traceloop/openllmetry
Source:         https://github.com/traceloop/openllmetry/archive/refs/tags/v%{monorepo_ver}.tar.gz#/openllmetry-%{monorepo_ver}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.42.0}
BuildRequires:  %{python_module opentelemetry-semantic-conventions >= 0.63b1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-opentelemetry-sdk >= 1.42.0
Requires:       python-opentelemetry-semantic-conventions >= 0.63b1
BuildArch:      noarch
%python_subpackages

%description
An extension of the standard OpenTelemetry Semantic Conventions for
generative-AI applications. It defines additional span attributes,
metrics and enums useful for debugging and monitoring prompts,
completions and token usage of large language models.

%prep
%autosetup -p1 -n openllmetry-%{monorepo_ver}

%build
cd %{pkgsubdir}
%pyproject_wheel

%install
cd %{pkgsubdir}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd %{pkgsubdir}
%pytest tests

%files %{python_files}
%doc %{pkgsubdir}/README.md
%{python_sitelib}/opentelemetry/semconv_ai
%{python_sitelib}/opentelemetry_semantic_conventions_ai-%{version}.dist-info

%changelog
