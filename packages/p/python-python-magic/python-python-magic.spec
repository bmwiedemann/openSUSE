#
# spec file for package python-python-magic
#
# Copyright (c) 2021 SUSE LLC
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
%define         oldpython python
Name:           python-python-magic
Version:        0.4.18
Release:        0
Summary:        File type identification using libmagic
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ahupp/python-magic
Source:         https://github.com/ahupp/python-magic/archive/%{version}.tar.gz
#PATCH-FIX-OPENSUSE fix-test.patch -- adapt file outputs to opensuse
Patch0:         fix-test.patch
Patch1:         fix-test-tumbleweed.patch
Patch2:         fix-4-file-5.40.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  file
BuildRequires:  python-rpm-macros
Requires:       file
# python-python-magic and python-magic use the same namespace (ie. filename)
# and have a very similar functionality but are incompatible to each other.
#  https://github.com/ahupp/python-magic/issues/21
Conflicts:      python-magic
BuildArch:      noarch
%ifpython2
Conflicts:      %{oldpython}-magic
%endif
%python_subpackages

%description
This module uses ctypes to access the libmagic file type
identification library. It makes use of the local magic database and
supports both textual and MIME-type output.

%prep
%setup -q -n python-magic-%{version}
%if 0%{?suse_version} > 1500
# Tumbleweed
%patch1 -p1
%elif 0%{?sle_version} < 150300 && 0%{?is_opensuse}
# Leap 15.2 and older
%patch0 -p1
%endif
%if %{?pkg_vcmp:%{pkg_vcmp file >= 5.40}}%{!?pkg_vcmp:0}
%patch2 -p0
%endif

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=en_US.UTF-8
%python_expand PYTHONPATH=. $python test/test.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/magic.py*
%pycache_only %{python_sitelib}/__pycache__/magic*.py*
%{python_sitelib}/python_magic-%{version}-py*.egg-info

%changelog
