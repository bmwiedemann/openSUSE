#
# spec file for package python-pymad
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2008 Pascal Bleser <guru@unixtech.be>
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


Name:           python-pymad
Version:        0.11.3
Release:        0
Summary:        Python Module to use the MPEG Audio Decoder Library
License:        LGPL-2.0-or-later
URL:            http://spacepants.org/src/pymad
Source:         https://files.pythonhosted.org/packages/source/p/pymad/pymad-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(mad)
%python_subpackages

%description
pymad is a Python module that allows Python programs to use the MPEG Audio
Decoder library. pymad provides a high-level API, similar to the pyogg module,
allowing to read PCM data from MPEG audio streams.

%prep
%autosetup -p1 -n pymad-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%doc AUTHORS NEWS README.md THANKS
%license COPYING
%{python_sitearch}/mad.cpython-*-linux-gnu.so
%{python_sitearch}/pymad-%{version}.dist-info

%changelog
