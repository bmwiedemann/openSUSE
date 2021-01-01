#
# spec file for package python-pympv
#
# Copyright (c) 2020 SUSE LLC
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


Name:           python-pympv
Version:        0.7.0
Release:        0
Summary:        Python wrapper for libmpv
License:        GPL-3.0-or-later
URL:            https://github.com/marcan/pympv
Source0:        https://files.pythonhosted.org/packages/source/p/pympv/pympv-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(mpv)
%python_subpackages

%description
A python wrapper for libmpv.

%prep
%setup -q -n pympv-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%doc README.md
%{python_sitearch}/*

%changelog
