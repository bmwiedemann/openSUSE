#
# spec file for package python-wyoming
#
# Copyright (c) 2024 SUSE LLC
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
%define         skip_python36 1
%define         skip_python38 1
Name:           python-wyoming
Version:        1.5.4
Release:        0
License:        MIT
Summary:        Peer-to-peer protocol for voice assistants
Group:          Development/Languages/Python
URL:            https://github.com/rhasspy/wyoming
#Source:         https://files.pythonhosted.org/packages/source/w/wyoming/wyoming-%{version}.tar.gz
Source:         wyoming-%{version}.tar.xz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Peer-to-peer protocol for voice assistants

%prep
%setup -q -n wyoming-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*

%changelog
