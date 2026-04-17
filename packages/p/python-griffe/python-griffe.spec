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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-griffe%{psuffix}
Version:        2.0.2
Release:        0
Summary:        Signatures for entire Python programs
License:        ISC
URL:            https://mkdocstrings.github.io/griffe
Source0:        https://files.pythonhosted.org/packages/source/g/griffe/griffe-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE static-version.patch mcepl@suse.com
# Don't use uv-dynamic-versioning, just set it statically
Patch0:         static-version.patch
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module mkdocstrings >= 0.29}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module tomli >= 2.0 if %python-base < 3.11}
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  python-rpm-macros
Requires:       python-griffe-inherited-docstrings
Requires:       python-griffecli = %{version}
Requires:       python-griffelib = %{version}
Requires:       python-jsonschema
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module griffecli == %{version}}
BuildRequires:  %{python_module griffe-inherited-docstrings}
BuildRequires:  %{python_module griffelib == %{version}}
BuildRequires:  %{python_module pytest-gitconfig}
BuildRequires:  %{python_module pytest-randomly}
BuildRequires:  %{python_module pytest}
# /SECTION
%endif
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
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/griffe
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# Upstream sdist omits the workspace `packages/` tree, but this test assumes
# a checkout layout and fails with FileNotFoundError on OBS.
# gh#mkdocstrings/griffe#452
%pytest -k 'not test_meson_python_file_handling'
%endif

%post
%python_install_alternative griffe

%postun
%python_uninstall_alternative griffe

%if %{without test}
%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE LICENSE
%python_alternative %{_bindir}/griffe
%{python_sitelib}/griffe-%{version}.dist-info
%endif

%changelog
