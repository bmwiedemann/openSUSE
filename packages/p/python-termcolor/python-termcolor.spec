#
# spec file for package python-termcolor
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
Name:           python-termcolor
Version:        1.1.0
Release:        0
Summary:        ANSII Color formatting for output in terminal
License:        MIT
URL:            https://pypi.python.org/pypi/termcolor
Source:         https://files.pythonhosted.org/packages/source/t/termcolor/termcolor-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Available text colors: grey, red, green, yellow, blue, magenta, cyan, white.
Available text highlights: on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.
Available attributes: bold, dark, underline, blink, reverse, concealed.

%prep
%setup -q -n termcolor-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING.txt
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
