#
# spec file for package python-straight-plugin
#
# Copyright (c) 2018 Neal Gompa <ngompa13@gmail.com>.
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
Name:           python-straight-plugin
Version:        1.5.0
Release:        0
Summary:        Python plugin loader
Group:          Development/Libraries/Python
License:        MIT
URL:            https://github.com/ironfroggy/straight.plugin/

Source0:        https://pypi.python.org/packages/source/s/straight.plugin/straight.plugin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%python_subpackages

%description
straight.plugin is a Python plugin loader inspired by twisted.plugin with two
important distinctions:

 - Fewer dependencies
 - Python 3 compatible

The system is used to allow multiple Python packages to provide plugins within
a namespace package, where other packages will locate and utilize. The plugins
themselves are modules in a namespace package where the namespace identifies
the plugins in it for some particular purpose or intent.


%prep
%autosetup -n straight.plugin-%{version}


%build
%python_build


%install
%python_install


%files %{python_files}
%license LICENSE
%{python_sitelib}/*


%changelog
