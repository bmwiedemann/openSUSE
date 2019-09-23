#
# spec file for package python-sdnotify
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
Name:           python-sdnotify
Version:        0.3.2
Release:        0
Summary:        A pure Python implementation of systemd's service notification protocol (sd_notify)
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/bb4242/sdnotify
Source:         https://files.pythonhosted.org/packages/source/s/sdnotify/sdnotify-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
A pure Python implementation of systemd's service notification protocol (sd_notify)

%prep
%setup -q -n sdnotify-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
