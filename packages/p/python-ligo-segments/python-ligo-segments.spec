#
# spec file for package python-ligo-segments
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           python-ligo-segments
Version:        1.2.0
Release:        0
License:        GPL-3.0
Summary:        Representations of semi-open intervals
Url:            https://git.ligo.org/lscsoft/ligo-segments
Group:          Development/Languages/Python
Source:         http://software.igwn.org/lscsoft/source/ligo-segments-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-six

%python_subpackages

%description
ligo-segments defines the segment, segmentlist, and segmentlistdict objects for manipulating semi-open intervals.

%prep
%setup -q -n ligo-segments-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc LICENSE README.rst
%{python_sitearch}/*

%changelog
