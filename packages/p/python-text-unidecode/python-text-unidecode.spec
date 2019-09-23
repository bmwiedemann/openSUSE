#
# spec file for package python-text-unidecode
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
Name:           python-text-unidecode
Version:        1.3
Release:        0
Summary:        The most basic Text::Unidecode port
License:        Artistic-1.0 OR GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/kmike/text-unidecode/
Source:         https://files.pythonhosted.org/packages/source/t/text-unidecode/text-unidecode-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
text-unidecode is the most basic port of the Text::Unidecode Perl library.

There are other Python ports of Text::Unidecode (unidecode and
isounidecode). unidecode is GPL; isounidecode doesn’t support Python 3
and uses too much memory.

This port is licensed under Artistic License and supports both Python
2.x and 3.x.

%prep
%setup -q -n text-unidecode-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
