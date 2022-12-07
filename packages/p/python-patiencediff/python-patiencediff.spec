#
# spec file for package python-patiencediff
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-patiencediff
Version:        0.2.8
Release:        0
Summary:        Python implementation of the patiencediff algorithm
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/breezy-team/patiencediff
Source:         https://files.pythonhosted.org/packages/source/p/patiencediff/patiencediff-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python implementation of the patiencediff algorithm.

%prep
%setup -q -n patiencediff-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest

%files %{python_files}
%doc AUTHORS README.rst
%license COPYING
%{python_sitearch}/patiencediff
%{python_sitearch}/patiencediff-%{version}*-info

%changelog
