#
# spec file for package python-flexx
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


%bcond_without libalternatives
Name:           python-flexx
Version:        0.8.4
Release:        0
Summary:        Python toolkit for creating graphical user interfaces
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/flexxui/flexx
Source:         https://files.pythonhosted.org/packages/source/f/flexx/flexx-%{version}.tar.gz
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module dialite >= 0.5.2}
BuildRequires:  %{python_module imageio}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pscript}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 4}
BuildRequires:  %{python_module webruntime >= 0.5.6}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       alts
Requires:       python-dialite >= 0.5.2
Requires:       python-pscript
Requires:       python-tornado
Requires:       python-webruntime >= 0.5.6
Recommends:     python-imageio
Recommends:     python-numpy
Recommends:     python-vispy
BuildArch:      noarch
%python_subpackages

%description
Flexx is a pure Python toolkit for creating graphical user interfaces
(GUIs), that uses web technology for its rendering. Apps are written
purely in Python; Flexx's transpiler generates the necessary JavaScript
on the fly.

Flexx can be used to create (cross platform) desktop applications, web
applications, and (if designed well) export an app to a standalone HTML
document. It also works in the Jupyter notebook.

%prep
%setup -q -n flexx-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/flexx
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Do not run tests, they require online access to jquery/etc.
#%%pytest

%pre
# Removing old update-alternatives entries.
%python_libalternatives_reset_alternative flexx

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/flexx
%{python_sitelib}/flexx
%{python_sitelib}/flexxamples
%{python_sitelib}/flexx-%{version}*-info

%changelog
