#
# spec file for package python-jupyter-events
#
# Copyright (c) 2022 SUSE LLC
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


# This is with alts/libalternatives only and has never been something else
%bcond_without libalternatives
Name:           python-jupyter-events
Version:        0.5.0
Release:        0
Summary:        Jupyter Event System library
License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter_events
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_events/jupyter_events-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-PyYAML >= 6.0
Requires:       python-jsonschema-format-nongpl >= 4.3.0
Requires:       python-python-json-logger >= 2.0.4
Requires:       python-traitlets >= 5.3
Provides:       python-jupyter_events = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 6.0}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module jsonschema-format-nongpl >= 4.3.0}
BuildRequires:  %{python_module pytest >= 6.1.0}
BuildRequires:  %{python_module pytest-asyncio >= 0.19.0}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module python-json-logger >= 2.0.4}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module traitlets >= 5.3}
# /SECTION
%python_subpackages

%description
Jupyter Events enables Jupyter Python Applications (e.g. Jupyter Server,
JupyterLab Server, JupyterHub, etc.) to emit events—structured data
describing things happening inside the application. Other software
(e.g. client applications like JupyterLab) can listen and respond to
these events.

%prep
%autosetup -p1 -n jupyter_events-%{version}
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-events
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# flavored not yet installed libalts are not supported by python-rpm-macros
%{python_expand #
mkdir -p build/flavorbin
ln -s %{buildroot}%{_bindir}/jupyter-events-%{$python_bin_suffix} build/flavorbin/jupyter-events
}
%pytest

%post
%python_install_alternative jupyter-events

%postun
%python_uninstall_alternative jupyter-events

%files %{python_files}
%python_alternative %{_bindir}/jupyter-events
%{python_sitelib}/jupyter_events
%{python_sitelib}/jupyter_events-%{version}.dist-info

%changelog
