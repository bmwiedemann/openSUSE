#
# spec file for package python-falcon
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-falcon
Version:        2.0.0
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
BuildRequires:  %{python_module ddt}
# TODO: Cython support
#BuildRequires:  %%{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module fixtures >= 1.3.0}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module msgpack-python}
BuildRequires:  %{python_module pecan}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-mimeparse >= 1.5.2}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.4.0}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module ujson}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-pygments-style-railscasts
#Requires:       python-Cython
Requires:       python-python-mimeparse
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if 0%{?suse_version} >= 1000 || 0%{?fedora_version} >= 24
Suggests:       %{name}-doc
%endif
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
sed -i '1s/^#!.*//' falcon/bench/bench.py falcon/cmd/print_routes.py falcon/bench/dj/manage.py
chmod a-x falcon/bench/dj/manage.py
# we don't want to require rapidjson just for testing
rm tests/test_media_handlers.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build
pushd docs
PYTHONPATH=$PATH:.. make html
rm _build/html/.buildinfo
popd

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/falcon-bench
%python_clone -a %{buildroot}%{_bindir}/falcon-print-routes
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
%pytest

%post
%{python_install_alternative falcon-bench falcon-print-routes}

%postun
%{python_uninstall_alternative falcon-bench falcon-print-routes}

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE
%python_alternative %{_bindir}/falcon-bench
%python_alternative %{_bindir}/falcon-print-routes
%{python_sitelib}/*

%files -n %{name}-doc
%doc docs/_build/html

%changelog
