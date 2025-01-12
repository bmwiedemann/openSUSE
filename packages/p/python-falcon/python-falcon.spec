#
# spec file for package python-falcon
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


%if 0%{?suse_version} > 1600
%bcond_without doc
%else
%bcond_with doc
%endif

%{?sle15_python_module_pythons}
Name:           python-falcon
Version:        4.0.2
Release:        0
Summary:        A web framework for building APIs and app backends
License:        Apache-2.0
URL:            http://falconframework.org
Source:         https://files.pythonhosted.org/packages/source/f/falcon/falcon-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module myst-parser >= 2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinx-design}
BuildRequires:  %{python_module sphinx-tabs}
BuildRequires:  %{python_module sphinxcontrib-copybutton}
BuildRequires:  %{python_module websockets}
BuildRequires:  %{python_module wheel}
# TODO: Cython support
#BuildRequires:  %%{python_module Cython}
# SECTION test requirements
BuildRequires:  %{python_module aiofiles}
BuildRequires:  %{python_module cbor2}
BuildRequires:  %{python_module msgpack-python}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module testtools}
%if 0%{?suse_version} >= 1550
BuildRequires:  %{python_module httpx if (%python-base without python36-base)}
BuildRequires:  %{python_module uvicorn if (%python-base without python36-base)}
BuildRequires:  %{python_module websockets if (%python-base without python36-base)}
%endif
%if %{with doc}
BuildRequires:  %{python_module pydata-sphinx-theme}
%endif
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#Requires:       python-Cython
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       %{name}-doc
BuildArch:      noarch
%python_subpackages

%package -n %{name}-doc
Summary:        Documentation files for %{name}
Provides:       %{python_module falcon-doc = %{version}}

%description
Falcon is a Python framework for building cloud
APIs. It encourages the REST architectural style, and tries to do
as little as possible while remaining effective.

%description -n %{name}-doc
HTML documentation including API documentation and changelog for %{name}.

%prep
%autosetup -p1 -n falcon-%{version}
# remove unwanted shebang
sed -i '1s/^#!.*//' falcon/bench/bench.py falcon/cmd/inspect_app.py falcon/bench/dj/manage.py
chmod a-x falcon/bench/dj/manage.py
# we don't want to require rapidjson just for testing
rm tests/test_media_handlers.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%if %{with doc}
export PYTHONPATH="$(pwd)"
pushd docs
make html
rm _build/html/.buildinfo
popd
%endif

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/falcon-bench
%python_clone -a %{buildroot}%{_bindir}/falcon-inspect-app
%python_clone -a %{buildroot}%{_bindir}/falcon-print-routes
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with doc}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-doc
cp -ar docs/_build/html examples %{buildroot}%{_defaultdocdir}/%{name}-doc/
%fdupes %{buildroot}%{_defaultdocdir}/%{name}-doc/
%endif

%check
export LANG=en_US.UTF8
%pytest

%post
%{python_install_alternative falcon-bench falcon-inspect-app falcon-print-routes}

%postun
%python_uninstall_alternative falcon-bench

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/falcon-bench
%python_alternative %{_bindir}/falcon-inspect-app
%python_alternative %{_bindir}/falcon-print-routes
%{python_sitelib}/falcon
%{python_sitelib}/falcon-%{version}.dist-info

%if %{with doc}
%files -n %{name}-doc
%doc %{_defaultdocdir}/%{name}-doc
%endif

%changelog
