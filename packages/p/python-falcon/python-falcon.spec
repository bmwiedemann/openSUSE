#
# spec file for package python-falcon
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


%if 0%{?suse_version} >= 1699
%bcond_without doc
%else
%bcond_with doc
%endif
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-falcon
Version:        4.2.0
Release:        0
Summary:        A web framework for building APIs and app backends
License:        Apache-2.0
URL:            https://falconframework.org
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
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
Suggests:       %{name}-doc
BuildArch:      noarch
# TODO: Cython support
#BuildRequires:  %%{python_module Cython}
#Requires:       python-Cython
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
BuildRequires:  %{python_module websockets >= 13.1 if (%python-base without python36-base)}
%endif
%if %{with doc}
BuildRequires:  %{python_module pydata-sphinx-theme}
%endif
# /SECTION
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
%python_group_libalternatives falcon-bench falcon-inspect-app falcon-print-routes
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with doc}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-doc
cp -ar docs/_build/html examples %{buildroot}%{_defaultdocdir}/%{name}-doc/
%fdupes %{buildroot}%{_defaultdocdir}/%{name}-doc/
%endif

%check
export LANG=en_US.UTF8
%pytest

%pre
%python_libalternatives_reset_alternative falcon-bench

%post
%python_install_alternative falcon-bench falcon-inspect-app falcon-print-routes

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
