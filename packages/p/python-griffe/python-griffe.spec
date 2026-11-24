#
# spec file for package python-griffe
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


Name:           python-griffe
# Must be upgraded in lockstep with griffelib and griffecli
Version:        2.4.1
Release:        0
Summary:        Signatures for entire Python programs
License:        ISC
URL:            https://mkdocstrings.github.io/griffe
Source0:        https://files.pythonhosted.org/packages/source/g/griffe/griffe-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE static-version.patch mcepl@suse.com
# Don't use uv-dynamic-versioning, just set it statically
Patch0:         static-version.patch
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-griffecli = %{version}
Requires:       python-griffelib = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages
#    "duty>=1.6",
#    "griffe-inherited-docstrings>=1.1.2",
#    "pysource-codegen>=0.7",
#    "pysource-minimize>=0.10",
#    "ty>=0.0.14",
#    "types-markdown>=3.6",
#    "types-pyyaml>=6.0",
#    "code2flow>=2.5",
#    "markdown-callouts>=0.4",
#    "markdown-exec[ansi]>=1.8",
#    "mkdocs>=1.6",
#    "mkdocs-coverage>=1.0",
#    "mkdocs-gen-files>=0.5",
#    "mkdocs-git-revision-date-localized-plugin>=1.2",
#    "mkdocs-llmstxt>=0.2",
#    "mkdocs-material>=9.5",
#    "mkdocs-minify-plugin>=0.8",
#    "mkdocs-section-index>=0.3",
#    "mkdocs-redirects>=1.2",
#    "pydeps>=1.12",

%description
Signatures for entire Python programs. Extract the structure, the frame,
the skeleton of your project, to generate API documentation or find
breaking changes in your API.

Griffe, pronounced "grif" (`/ɡʁif/`), is a french word that means
"claw", but also "signature" in a familiar way. "On reconnaît bien là sa
griffe."

%prep
%autosetup -p1 -n griffe-%{version}

# set the version
sed -i -e '/^version =/s/@VERSION@/%{version}/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/griffe
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests now run in griffelib and griffecli

%post
%python_install_alternative griffe

%postun
%python_uninstall_alternative griffe

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/griffe
%{python_sitelib}/griffe-%{version}.dist-info

%changelog
