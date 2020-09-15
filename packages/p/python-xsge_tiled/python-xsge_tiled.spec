#
# spec file for package python-xsge_tiled
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-xsge_tiled
Version:        1.0
Release:        0
Summary:        xSGE Tiled Library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://python-sge.github.io
Source:         https://files.pythonhosted.org/packages/source/x/xsge_tiled/xsge_tiled-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-sge-pygame >= 1.0
Requires:       python-xsge_path >= 1.0
BuildArch:      noarch
%python_subpackages

%description
xSGE is a collection of extensions for the SGE licensed under the GNU
General Public License.  They are designed to give additional features
to free/libre software games which aren't necessary, but are nice to
have.

xSGE extensions are not dependent on any particular SGE implementation.
They should work with any implementation that follows the specification.

This extension provides support for loading the JSON format of the
Tiled Map Editor. This allows you to use Tiled to edit your game’s world
(e.g. levels), rather than building a level editor yourself.

%prep
%setup -q -n xsge_tiled-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# upstream does not provide any tests

%files %{python_files}
%license xsge_tiled/COPYING
%doc README WHATSNEW
%{python_sitelib}/xsge_tiled*

%changelog
