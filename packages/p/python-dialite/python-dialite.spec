#
# spec file for package python-dialite
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
Name:           python-dialite
Version:        0.5.2
Release:        0
Summary:        Python library to show simple dialogs
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://dialite.readthedocs.io
Source:         https://files.pythonhosted.org/packages/source/d/dialite/dialite-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     zenity
BuildArch:      noarch
%python_subpackages

%description
Dialite is a pure Python package to show dialogs. It provides a
handful of functions, each a verb, that can be used to inform(),
warn() or fail() the user, or to ask_ok(), ask_retry() or
ask_yesno().

Dialite can show graphical dialogs, and falls back to a terminal
interface if dialogs are unavailable (e.g. if not supported by the
platform, or for SSH connections).

%prep
%setup -q -n dialite-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
