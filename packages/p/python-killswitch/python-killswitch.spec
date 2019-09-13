#
# spec file for package python-killswitch
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define skip_python3 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-killswitch
Version:        0.4
Release:        0
Summary:        Python module providing functions for killswitches
License:        WTFPL
Group:          Development/Languages/Python
URL:            http://blog.homac.de
Source:         python-killswitch-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       urfkill
BuildArch:      noarch
%python_subpackages

%description
python-killswitch provides a python module called killswitch. It provides
convenient function/methods for other applications to manage all the
killswitches found in the system. See 'pydoc killswitch.py' for more
information

%prep
%setup -q
sed -i -e '1d' killswitch.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc README
%{python_sitelib}

%changelog
