#
# spec file for package python-releases
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-releases%{psuffix}
Version:        2.1.1
Release:        0
Summary:        A Sphinx extension for changelog manipulation
License:        BSD-2-Clause
URL:            https://github.com/bitprophet/releases
Source:         https://files.pythonhosted.org/packages/source/r/releases/releases-%{version}.tar.gz
Patch0:         semanticversioning.patch
# PATCH-FIX-OPENSUSE remove-icecream.patch to remove icecream dependency
Patch1:         remove-icecream.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 4
Requires:       python-semantic_version
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Sphinx >= 3}
BuildRequires:  %{python_module invocations}
BuildRequires:  %{python_module invoke}
BuildRequires:  %{python_module pytest-relaxed}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module semantic_version}
%endif
%python_subpackages

%description
Releases is a Python 2+3 compatible `Sphinx <http://sphinx-doc.org>`_ extension
designed to help you keep a source control friendly, merge friendly changelog
file & turn it into useful, human readable HTML output.

Specifically:

* The source format (kept in your Sphinx tree as ``changelog.rst``) is a
  stream-like timeline that plays well with source control & only requires one
  entry per change (even for changes that exist in multiple release lines).
* The output (when you have the extension installed and run your Sphinx build
  command) is a traditional looking changelog page with a section for every
  release; multi-release issues are copied automatically into each release.
* By default, feature and support issues are only displayed under feature
  releases, and bugs are only displayed under bugfix releases. This can be
  overridden on a per-issue basis.

%prep
%autosetup -p1 -n releases-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# https://github.com/bitprophet/releases/issues/103
%pytest tests -k "not unused_kwargs_become_releases_config_options"
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/releases
%{python_sitelib}/releases-%{version}.dist-info
%endif

%changelog
