#
# spec file for package python-xsge_tmx
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
Name:           python-xsge_tmx
Version:        1.1.1
Release:        0
Summary:        xSGE TMX Library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://xsge.nongnu.org
Source:         https://files.pythonhosted.org/packages/source/x/xsge_tmx/xsge_tmx-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-sge-pygame >= 1.0
Requires:       python-six >= 1.4.0
Requires:       python-tmx >= 1.9
Requires:       python-xsge_path
BuildArch:      noarch
%python_subpackages

%description
xSGE is a collection of extensions for SGE.
xSGE extensions are not dependent on any particular SGE implementation.
They should work with any implementation that follows the specification.

This extension provides support for loading the Tiled TMX format.  This
allows using Tiled to edit a game's world (e.g. levels), rather
than building a custom level editor.

%prep
%setup -q -n xsge_tmx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README
%license xsge_tmx/COPYING
%{python_sitelib}/*

%changelog
