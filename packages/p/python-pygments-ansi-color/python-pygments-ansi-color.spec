#
# spec file for package python-pygments-ansi-color
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
Name:           python-pygments-ansi-color
Version:        0.0.3
Release:        0
Summary:        ANSI color-code highlighting for Pygments
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/chriskuehl/pygments-ansi-color
Source:         https://github.com/chriskuehl/pygments-ansi-color/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
Requires:       python-pygments
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
An ANSI color-code highlighting lexer for Pygments.

%prep
%setup -q -n pygments-ansi-color-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
