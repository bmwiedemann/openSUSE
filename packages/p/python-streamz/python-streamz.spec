#
# spec file for package python-streamz
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-streamz
Version:        0.6.4
Release:        0
Summary:        Tool to build continuous data pipelines
License:        BSD-3-Clause
URL:            https://github.com/python-streamz/streamz/
Source:         https://files.pythonhosted.org/packages/source/s/streamz/streamz-%{version}.tar.gz
# PATCH-FIX-UPSTREAM  streamz-pr455-ci-fixes.patch gh#python-streamz/streamz#455
Patch0:         streamz-pr455-ci-fixes.patch
# PATCH-FIX-OPENSUSE streamz-opensuse-python-exec.patch -- call tests with correct flavor
Patch1:         streamz-opensuse-python-exec.patch
# PATCH-FIX-UPSTREAM python-streamz-no-six.patch gh#python-streamz/streamz/commit/33f49417b415deb7ea3c495a404b78c9d3743c03
Patch2:         python-streamz-no-six.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Setuptools is a runtime requirement because of pkg_resources usage
Requires:       python-setuptools
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
BuildRequires:  %{python_module dask >= 2.5}
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module dask-distributed}
BuildRequires:  %{python_module distributed}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
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
%autosetup -p1 -n streamz-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# infinite loop because the automatic skip does not work here; the kafka tests need a docker container with STREAMZ_LAUNCH_KAFKA=true
donttest="test_from_kafka or test_to_kafka"
if [ $(getconf LONG_BIT) -eq 32 ]; then
  # don't test on 32-bit: 64-bit datatypes expected
  donttest+=" or test_dataframes"
fi
# flaky: some tests are very fragile when run server-side
donttest+=" or test_tcp"
%{pytest -m "not network" \
    --pyargs streamz \
    --asyncio-mode auto \
    --force-flaky --max-runs=10 --no-success-flaky-report \
    -rsfE --ignore streamz/tests/test_graph.py -k "not ($donttest)"
}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/streamz
%{python_sitelib}/streamz-%{version}.dist-info

%changelog
