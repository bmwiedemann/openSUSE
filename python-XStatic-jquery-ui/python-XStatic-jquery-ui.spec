#
# spec file for package python-XStatic-jquery-ui
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
Name:           python-XStatic-jquery-ui
Version:        1.12.1.1
Release:        0
Summary:        jQuery UI repackaged for the XStatic standard
License:        MIT
Group:          Development/Languages/Python
Url:            http://jqueryui.com/
# https://pypi.python.org/pypi/XStatic-jquery-ui/1.12.0.1
Source:         XStatic-jquery-ui-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/jquery/jquery-ui/master/LICENSE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
jquery-ui javascript library packaged for setuptools (easy_install) / pip.

You can find more info about the xstatic packaging way in the package `XStatic`.

%prep
%setup -q -n XStatic-jquery-ui-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%fdupes %{buildroot}/%{_prefix}

%files %{python_files}
%doc README.txt
%license LICENSE.txt
%{python_sitelib}/*

%changelog
