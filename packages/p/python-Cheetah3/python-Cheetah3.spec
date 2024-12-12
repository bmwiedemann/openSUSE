#
# spec file for package python-Cheetah3
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


%define modname cheetah3
Name:           python-Cheetah3
Version:        3.4.0
Release:        0
Summary:        Template engine and code generation tool
License:        MIT
Group:          Development/Languages/Python
URL:            https://cheetahtemplate.org/
Source:         https://github.com/CheetahTemplate3/cheetah3/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-Markdown
Suggests:       python-Pygments
Conflicts:      python-Cheetah
Provides:       python-Cheetah = %{version}
Provides:       python-cheetah = %{version}
Obsoletes:      python-Cheetah < %{version}
# SECTION test requirements
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module Pygments}
# /SECTION
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

# Disable some tests which fail on Python 3.6
# * GetVar
# * GetVar_MacEOL
# * GetVar_Win32EOL
# TODO: The following disables ~100 tests, and should be optimised
sed -Ei 's/(test6)/_\1/' Cheetah/Tests/SyntaxAndOutput.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cheetah
%python_clone -a %{buildroot}%{_bindir}/cheetah-analyze
%python_clone -a %{buildroot}%{_bindir}/cheetah-compile
%{python_expand rm -r %{buildroot}%{$python_sitearch}/Cheetah/Tests
%fdupes %{buildroot}%{$python_sitearch}
}

%post
%python_install_alternative cheetah cheetah-analyze cheetah-compile

%postun
%python_uninstall_alternative cheetah

%check
mkdir ~/bin
export PATH=~/bin:$PATH
%{python_expand export PYTHONPATH=$PWD
cp %{buildroot}/%{_bindir}/cheetah-%{$python_bin_suffix} ~/bin/cheetah
export PYTHONDONTWRITEBYTECODE=1
$python Cheetah/Tests/Test.py
}

%files %{python_files}
%license LICENSE
%doc ANNOUNCE.rst README.rst BUGS
%python_alternative %{_bindir}/cheetah
%python_alternative %{_bindir}/cheetah-analyze
%python_alternative %{_bindir}/cheetah-compile
%{python_sitearch}/Cheetah
%{python_sitearch}/CT3-%{version}*info

%changelog
