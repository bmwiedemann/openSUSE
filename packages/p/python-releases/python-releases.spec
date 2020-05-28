#
# spec file for package python
#
# Copyright (c) 2020 SUSE LLC
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
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-releases%{psuffix}
Version:        1.6.3
Release:        0
Summary:        A Sphinx extension for changelog manipulation
License:        BSD-2-Clause
URL:            https://github.com/bitprophet/releases
Source:         https://files.pythonhosted.org/packages/source/r/releases/releases-%{version}.tar.gz
Patch0:         semanticversioning.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.3
Requires:       python-semantic_version
Requires:       python-six >= 1.4.1
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Sphinx >= 1.3}
BuildRequires:  %{python_module invocations}
BuildRequires:  %{python_module invoke}
BuildRequires:  %{python_module mock >= 1.0.1}
BuildRequires:  %{python_module semantic_version}
BuildRequires:  %{python_module six >= 1.4.1}
BuildRequires:  %{python_module spec >= 0.11.3}
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
%setup -q -n releases-%{version}
%patch0 -p1

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export NOSE_NO_SPEC_COLOR=1
%python_expand invoke-%{$python_bin_suffix} test
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
