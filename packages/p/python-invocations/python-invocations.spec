#
# spec file for package python-invocations
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
Name:           python-invocations
Version:        1.4.0
Release:        0
Summary:        Reusable Invoke tasks
License:        BSD-2-Clause
URL:            https://github.com/pyinvoke/invocations
Source:         https://github.com/pyinvoke/invocations/archive/%{version}.tar.gz
Patch0:         invocations-no-bundled.patch
Patch1:         invocations-py3.patch
BuildRequires:  %{python_module blessings >= 1.6}
BuildRequires:  %{python_module invoke >= 1.0}
BuildRequires:  %{python_module lexicon}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-relaxed}
# gh#bitprophet/pytest-relaxed#12
BuildRequires:  %{python_module pytest < 6.1}
BuildRequires:  %{python_module releases >= 1.2}
BuildRequires:  %{python_module semantic_version >= 2.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tabulate >= 0.7.5}
BuildRequires:  %{python_module tqdm >= 4.8.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blessings >= 1.6
Requires:       python-invoke >= 1.0
Requires:       python-lexicon
Requires:       python-releases >= 1.2
Requires:       python-semantic_version >= 2.4
Requires:       python-six
Requires:       python-tabulate >= 0.7.5
Requires:       python-tqdm >= 4.8.1
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-enum34
%endif
%ifpython2
Requires:       python-enum34
%endif
%python_subpackages

%description
Invocations is a collection of reusable `Invoke <http://pyinvoke.org>`_
tasks/task modules, including (but not limited to) Python project management
tools such as documentation building and dependency organization.

It has no stand-alone components and is designed to be imported into your
pre-existing Invoke task files.

Invocations is currently in pre-alpha status and is unsupported. Please follow
the Invoke project's communication channels for updates. Thanks!

%prep
%setup -q -n invocations-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# autodoc: With new sphinx this does not work at all so skip it
# packaging: not applicable to openSUSE
# cannot use --ignore because of pytest-relaxed plugin
rm -r tests/autodoc/ tests/packaging/
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/invocations
%{python_sitelib}/invocations-%{version}*info

%changelog
