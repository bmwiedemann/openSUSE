#
# spec file for package python-falcon
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python2 1
Name:           python-falcon
Version:        3.1.1
Release:        0
Summary:        A web framework for building APIs and app backends
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://falconframework.org
Source:         https://github.com/falconry/falcon/archive/%{version}.tar.gz#./falcon-%{version}.tar.gz
# The file on pypi misses docs/ext, should be fixed in next version
# Source:         https://files.pythonhosted.org/packages/source/f/falcon/falcon-%%{version}.tar.gz
# github pygments style is not available
Patch0:         python-falcon-sphinx-pygments-style.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinx-tabs}
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
BuildRequires:  %{python_module ujson}
%if 0%{?suse_version} >= 1550
BuildRequires:  %{python_module httpx if (%python-base without python36-base)}
BuildRequires:  %{python_module uvicorn if (%python-base without python36-base)}
BuildRequires:  %{python_module websockets if (%python-base without python36-base)}
%endif
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pygments-style-railscasts
#Requires:       python-Cython
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       %{name}-doc
BuildArch:      noarch
%python_subpackages

%package -n %{name}-doc
Summary:        Documentation files for %{name}
Group:          Documentation/HTML
Provides:       %{python_module falcon-doc = %{version}}

%description
Falcon is a Python framework for building cloud
APIs. It encourages the REST architectural style, and tries to do
as little as possible while remaining effective.

%description -n %{name}-doc
HTML documentation including API documentation and changelog for %{name}.

%prep
%setup -q -n falcon-%{version}
%patch0 -p1
# remove unwanted shebang
sed -i '1s/^#!.*//' falcon/bench/bench.py falcon/cmd/inspect_app.py falcon/bench/dj/manage.py
chmod a-x falcon/bench/dj/manage.py
# we don't want to require rapidjson just for testing
rm tests/test_media_handlers.py
# Hidden files are evil
rm examples/asgilook/.coveragerc

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build
export PYTHONPATH="$(pwd)"
pushd docs
make html
rm _build/html/.buildinfo
popd

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/falcon-bench
%python_clone -a %{buildroot}%{_bindir}/falcon-inspect-app
%python_clone -a %{buildroot}%{_bindir}/falcon-print-routes
%{python_expand rm -rf %{buildroot}%{$python_sitelib}/examples
 %fdupes %{buildroot}%{$python_sitelib}
}

%check
export LANG=en_US.UTF8
# there are no websockets and httpx for python 3.6
python36_donttest=("--ignore" "tests/asgi")
if [ %{python3_version_nodots} -eq 36 ]; then
  python3_donttest=("--ignore" "tests/asgi")
fi
%pytest "${$python_donttest[@]}" tests

%post
%{python_install_alternative falcon-bench falcon-inspect-app falcon-print-routes}

%postun
%python_uninstall_alternative falcon-bench

%files %{python_files}
%doc README.rst CHANGES.rst examples/
%license LICENSE
%python_alternative %{_bindir}/falcon-bench
%python_alternative %{_bindir}/falcon-inspect-app
%python_alternative %{_bindir}/falcon-print-routes
%{python_sitelib}/falcon
%{python_sitelib}/falcon-%{version}*-info

%files -n %{name}-doc
%doc docs/_build/html

%changelog
