#
# spec file for package jupyter-jupyterlab-server
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


%define skip_python2 1
%define oldpython python
Name:           jupyter-jupyterlab-server
Version:        2.1.3
Release:        0
Summary:        Server components for JupyterLab and JupyterLab-like applications
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyterlab_server
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab_server/jupyterlab_server-%{version}.tar.gz
Source100:      jupyter-jupyterlab-server-rpmlintrc
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module Jinja2 >= 2.10}
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module json5}
BuildRequires:  %{python_module jsonschema >= 3.0.1}
BuildRequires:  %{python_module jupyter_server >= 1.1}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel
Requires:       python-Jinja2 >= 2.10
Requires:       python-json5
Requires:       python-jsonschema >= 3.0.1
Requires:       python-jupyter_server >= 1.1
Requires:       python-packaging
Requires:       python-requests
Provides:       python-jupyterlab-server = %{version}-%{release}
Obsoletes:      python-jupyterlab-server < %{version}-%{release}
Provides:       python-jupyterlab_server = %{version}-%{release}
Obsoletes:      python-jupyterlab_server < %{version}-%{release}
Provides:       python-jupyter_jupyterlab_server = %{version}-%{release}
Obsoletes:      python-jupyter_jupyterlab_server < %{version}-%{release}
Provides:       python-jupyter_jupyterlab_launcher = %{version}-%{release}
Obsoletes:      python-jupyter_jupyterlab_launcher < %{version}-%{release}
Provides:       %{oldpython}-jupyter_jupyterlab_server = %{version}-%{release}
Obsoletes:      %{oldpython}-jupyter_jupyterlab_server < %{version}-%{release}
Provides:       %{oldpython}-jupyter_jupyterlab_launcher = %{version}-%{release}
Obsoletes:      %{oldpython}-jupyter_jupyterlab_launcher < %{version}-%{release}
Provides:       %{oldpython}-jupyterlab-server = %{version}-%{release}
Obsoletes:      %{oldpython}-jupyterlab-server < %{version}-%{release}
BuildArch:      noarch
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter-jupyterlab-launcher = %{version}-%{release}
Obsoletes:      jupyter-jupyterlab-launcher < %{version}-%{release}
Provides:       jupyter-jupyterlab_launcher = %{version}-%{release}
Obsoletes:      jupyter-jupyterlab_launcher < %{version}-%{release}
Provides:       jupyter-jupyterlab-server = %{version}-%{release}
Obsoletes:      jupyter-jupyterlab-server < %{version}-%{release}
Provides:       jupyter-jupyterlab_server = %{version}-%{release}
Obsoletes:      jupyter-jupyterlab_server < %{version}-%{release}
%endif
# SECTION test requirements
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module strict-rfc3339}
BuildRequires:  %{python_module wheel}
# /SECTION
%python_subpackages

%description
This package is used to launch an application built using JupyterLab.

%prep
%setup -q -n jupyterlab_server-%{version}
# don't check code coverage
sed -i '/--cov/ d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# we dont have the language packs installed, supposed to be tested here
donttest+=" or (test_translation_api and (get_locale or backend_locale or get_installed or get_language) and not (_not_ or bad or fails))"
# flaky
donttest+=" or (test_workspaces_api and test_get_non_existant)"
%pytest -ra -k "not (${donttest:4})"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/jupyterlab_server/
%{python_sitelib}/jupyterlab_server-%{version}-py*.egg-info/

%changelog
