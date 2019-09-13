#
# spec file for package python-ansiwrap
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
Name:           python-ansiwrap
Version:        0.8.4
Release:        0
Summary:        Textwrap, but savvy to ANSI colors and styles
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/jonathaneunice/ansiwrap
Source:         https://files.pythonhosted.org/packages/source/a/ansiwrap/ansiwrap-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# SECTION test requirements
BuildRequires:  %{python_module ansicolors >= 1.1.8}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module textwrap3}
BuildRequires:  %{python_module tox}
# /SECTION
Requires:       python-textwrap3
BuildArch:      noarch

%python_subpackages

%description
Ansiwrap wraps text, like the standard textwrap module.
But it also correctly wraps text that contains ANSI control
sequences that colorize or style text.

Where textwrap is fooled by the raw string length of those control codes,
ansiwrap is not; it understands that however much those codes affect color
and display style, they have no logical length.

%prep
%setup -q -n ansiwrap-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix}
}

%files %{python_files}
%doc AUTHORS CHANGES.yml README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
