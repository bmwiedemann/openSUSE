#
# spec file for package python-filelock
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Matthias Fehring <buschmann23@opensuse.org>
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
Name:           python-filelock
Version:        3.0.12
Release:        0
Summary:        Platform Independent File Lock in Python
License:        Unlicense
Group:          Development/Languages/Python
URL:            https://github.com/benediktschmitt/py-filelock
Source:         https://github.com/benediktschmitt/py-filelock/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package contains a single module, which implements a platform
independent file lock in Python, which provides a simple way of
inter-process communication.

%prep
%setup -q -n py-filelock-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}/%{$python_sitelib}

%check
%pytest test.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
