#
# spec file for package python-pygments-style-railscasts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pygments-style-railscasts
Version:        0.3
Release:        0
Summary:        Pygments version of the "railscasts" vim theme.
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/DrMegahertz/pygments-style-railscasts
Source0:        https://files.pythonhosted.org/packages/source/p/pygments-style-railscasts/pygments-style-railscasts-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/DrMegahertz/pygments-style-railscasts/master/LICENSE
BuildRequires:  %{python_module setuptools}
Requires:       python-pygments
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
A port of the railscasts color scheme for pygments.


%prep
%setup -q -n pygments-style-railscasts-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitelib}/*

%changelog
