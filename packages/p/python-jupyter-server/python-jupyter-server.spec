#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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


#
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
Name:           python-jupyter-server%{psuffix}
Version:        1.13.1
Release:        0
Summary:        The backend to Jupyter web applications
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-server/jupyter_server
# need the release tarball for the static stylesheets
Source:         https://github.com/jupyter-server/jupyter_server/releases/download/v%{version}/jupyter_server-%{version}.tar.gz
BuildRequires:  %{python_module jupyter_packaging}
BuildRequires:  %{python_module setuptools}

# We need the full stdlib
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-Jinja2
Requires:       python-Send2Trash
Requires:       python-anyio >= 3.1.0
Requires:       python-argon2-cffi
Requires:       python-ipython_genutils
Requires:       python-jupyter-client >= 6.1.1
Requires:       python-jupyter-core >= 4.4.0
Requires:       python-nbconvert
Requires:       python-nbformat
Requires:       python-prometheus_client
Requires:       python-pyzmq >= 17
Requires:       python-terminado >= 0.8.3
Requires:       python-tornado >= 6.1
Requires:       python-traitlets >= 4.2.1
Requires:       python-websocket-client
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
Provides:       python-jupyter_server = %{version}-%{release}
Obsoletes:      python-jupyter_server < %{version}-%{release}
%if %{with test}
BuildRequires:  %{python_module jupyter-server-test = %{version}}
%endif
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter-jupyter-server = %{version}-%{release}
Obsoletes:      jupyter-jupyter-server < %{version}-%{release}
BuildArch:      noarch
%endif
%python_subpackages

%description
The Jupyter Server is a web application that allows you to create and
share documents that contain live code, equations, visualizations, and
explanatory text. The Notebook has support for multiple programming
languages, sharing, and interactive widgets.

%package test
Summary:        The backend to Jupyter web applications - test requirements
Group:          Development/Languages/Python
Requires:       python-ipykernel
Requires:       python-jupyter-server = %{version}
Requires:       python-pytest >= 6
Requires:       python-pytest-console-scripts
Requires:       python-pytest-mock
Requires:       python-pytest-tornasync
Requires:       python-requests

%description test
Metapackage for the jupyter_server[test] requirement specifier

%prep
%setup -q -n jupyter_server-%{version}

%if ! %{with test}
%build
%python_build

%install
%python_install
%python_clone -a  %{buildroot}%{_bindir}/jupyter-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%{python_expand # provide u-a entrypoints in the correct flavor version -- installed packages and jupyter-server
mkdir -p build/xdgflavorconfig
export XDG_CONFIG_HOME=$PWD/build/xdgflavorconfig
if [ -d /usr/share/libalternatives/ ]; then
  for b in /usr/share/libalternatives/*; do
    if [ -e "${b}/%{$python_version_nodots}.conf" ]; then
        alts -n $(basename ${b}) -p %{$python_version_nodots}
    fi
  done
fi
mkdir -p build/testbin
for bin in %{_bindir}/*-%{$python_bin_suffix}; do
  # four percent into 1 by rpm/python expansions
  ln -s ${bin} build/testbin/$(basename ${bin%%%%-%{$python_bin_suffix}})
done
}
export LANG=en_US.UTF-8
export PATH=$PWD/build/testbin:$PATH
if [ -e ~/.local/share/jupyter ]; then
    echo "WARNING: Not a clean test environment."
    echo "You might need to delete ~/.local/share/jupyter in order to avoid test failures."
fi
%pytest jupyter_server
%endif

%if ! %{with test}
%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jupyter-server

%post
%python_install_alternative jupyter-server

%postun
%python_uninstall_alternative jupyter-server

%files %{python_files}
%doc README.md
%license COPYING.md
%python_alternative %{_bindir}/jupyter-server
%{python_sitelib}/jupyter_server
%{python_sitelib}/jupyter_server-%{version}*-info

%files %{python_files test}
%license COPYING.md
%endif

%changelog
