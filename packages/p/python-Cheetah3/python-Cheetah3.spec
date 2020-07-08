#
# spec file for package python-Cheetah3
#
# Copyright (c) 2020 SUSE LLC
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


%define modname Cheetah3
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Cheetah3
Version:        3.2.5
Release:        0
Summary:        Template engine and code generation tool
License:        MIT
Group:          Development/Languages/Python
URL:            https://cheetahtemplate.org/
Source:         https://files.pythonhosted.org/packages/source/C/Cheetah3/Cheetah3-%{version}.tar.gz
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Conflicts:      python-Cheetah
Provides:       python-Cheetah = %{version}
Provides:       python-cheetah = %{version}
Obsoletes:      python-Cheetah < %{version}
%python_subpackages

%description
Cheetah is an open source template engine and code generation tool.

It can be used standalone or combined with other tools and frameworks.
Web development is its principle use, but Cheetah is flexible and can
also be used to generate C++ game code, Java, SQL, form emails and even
Python code.

It is a fork of the original CheetahTemplate library.

%prep
%setup -q -n %{modname}-%{version}
%autopatch -p1
find . -name \*.py -print0 |xargs -0 -t -l sed -i -e '1{\@^#!%{_bindir}/env python@d}'

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitearch}/Cheetah/Tests
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%{python_expand export PYTHONPATH=$(pwd)
export PYTHONDONTWRITEBYTECODE=1
export PATH=%{buildroot}%{_bindir}:$PATH
$python Cheetah/Tests/Test.py
}

%files %{python_files}
%license LICENSE
%doc ANNOUNCE.rst README.rst BUGS
%{_bindir}/cheetah*
%{python_sitearch}/*

%changelog
