#
# spec file for package python-funcsigs
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


Name:           python-funcsigs
Version:        1.0.2
Release:        0
Summary:        Python function signatures from PEP362
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://funcsigs.readthedocs.org
Source:         https://files.pythonhosted.org/packages/source/f/funcsigs/funcsigs-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE mcepl@suse.com -- remove unittest2 dependency
Patch0:         remove_unittest2.patch
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools
Provides:       python2-funcsigs = %{version}
BuildArch:      noarch

%description
The funcsigs package is a backport of the PEP 362 function signature
features from Python 3.3's inspect module.

%prep
%setup -q -n funcsigs-%{version}
%patch0 -p1

%build
%python2_build

%install
%python2_install
%fdupes %{buildroot}%{python2_sitelib}

%check
python2 setup.py test

%files
%license LICENSE
%doc CHANGELOG README.rst
%{python2_sitelib}/*

%changelog
