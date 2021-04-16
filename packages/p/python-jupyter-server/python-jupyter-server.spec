#
# spec file for package python-jupyter-server
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-jupyter-server
Version:        1.6.1
Release:        0
Summary:        The backend to Jupyter web applications
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter_server
Source:         https://github.com/jupyter/jupyter_server/archive/%{version}.tar.gz#/jupyter_server-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Send2Trash}
BuildRequires:  %{python_module anyio >= 2.0.2}
BuildRequires:  %{python_module argon2-cffi}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module jupyter-client >= 6.1.1}
BuildRequires:  %{python_module jupyter-core >= 4.4.0}
BuildRequires:  %{python_module nbclient}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module prometheus_client}
BuildRequires:  %{python_module pyzmq >= 17}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module terminado >= 0.8.3}
BuildRequires:  %{python_module tornado >= 6.1}
BuildRequires:  %{python_module traitlets >= 4.2.1}
# We need the full stdlib
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-Send2Trash
Requires:       python-anyio
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
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-jupyter_server = %{version}-%{release}
Obsoletes:      python-jupyter_server < %{version}-%{release}
# SECTION extras_require test
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
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

%prep
%setup -q -n jupyter_server-%{version}

%build
%python_build

%install
%python_install
%python_clone -a  %{buildroot}%{_bindir}/jupyter-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check

%{python_expand # provide u-a entrypoints in the correct flavor version -- installed packages and jupyter-server
mkdir build/testbin
for bin in %{_bindir}/*-%{$python_bin_suffix} %{buildroot}%{_bindir}/*-%{$python_bin_suffix} ; do
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

%changelog
