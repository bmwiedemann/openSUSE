#
# spec file for package python-streamz
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
%define         skip_python2 1
Name:           python-streamz
Version:        0.6.0
Release:        0
Summary:        Tool to build continuous data pipelines
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-streamz/streamz/
Source:         https://files.pythonhosted.org/packages/source/s/streamz/streamz-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires:       python-toolz
Requires:       python-tornado
Requires:       python-zict
Recommends:     python-certifi
Recommends:     python-dask
Recommends:     python-dask-dataframe
Recommends:     python-dask-distributed
Recommends:     python-distributed
Recommends:     python-graphviz
Recommends:     python-networkx
Recommends:     python-pandas
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module confluent-kafka}
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module dask-distributed}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module distributed}
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module toolz}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module zict}
BuildRequires:  graphviz
BuildRequires:  graphviz-gnome
# /SECTION
%python_subpackages

%description
Streamz helps you build pipelines to manage continuous streams of data.

%prep
%setup -q -n streamz-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -rf build _build.*
# Tests assume 64bit numbers
%ifarch x86_64
rm -rf build _build.*
%pytest
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/streamz
%{python_sitelib}/streamz-%{version}-py*.egg-info

%changelog
