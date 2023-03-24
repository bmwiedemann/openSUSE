#
# spec file for package python-jupyter-server-fileid
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


%define plainpython3dist python3dist
%define distversion 0.6
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-jupyter-server-fileid
Version:        0.6.0
Release:        0
Summary:        File IDs for documents in a running Jupyter Server
License:        BSD-3-Clause
URL:            https://github.com/jupyter-server/jupyter_server_fileid
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_server_fileid/jupyter_server_fileid-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       (python-jupyter-events >= 0.5.0 with python-jupyter-events < 1)
Requires:       (python-jupyter-server >= 1.15 with python-jupyter-server < 3)
Requires:       jupyter-server-fileid = %{version}
Recommends:     python-click
Provides:       python-jupyter_server_fileid = %{version}-%{release}
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module jupyter-events >= 0.5.0 with %python-jupyter-events < 1}
BuildRequires:  %{python_module jupyter-server-test >= 1.15 with %python-jupyter-server-test < 3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module traitlets}
# /SECTION
%python_subpackages

%description
A Jupyter Server extension providing an implementation of the File ID service.

%package -n jupyter-server-fileid
Summary:        File IDs for documents in a running Jupyter Server -- Jupyter configuration
Requires:       %{plainpython3dist}(jupyter-server-fileid) = %{distversion}
Provides:       jupyter_server_fileid = %{version}-%{release}

%description -n jupyter-server-fileid
A Jupyter Server extension providing an implementation of the File ID service.

This subpackage provides the jupyter configuration

%prep
%setup -q -n jupyter_server_fileid-%{version}
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-fileid
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative jupyter-fileid

%post
%python_install_alternative jupyter-fileid

%postun
%python_uninstall_alternative jupyter-fileid

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/jupyter-fileid
%{python_sitelib}/jupyter_server_fileid
%{python_sitelib}/jupyter_server_fileid-%{version}.dist-info

%files -n jupyter-server-fileid
%license LICENSE
%{_jupyter_config} %{_jupyter_server_confdir}/jupyter_server_fileid.json

%changelog
