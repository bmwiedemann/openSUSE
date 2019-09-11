#
# spec file for package python-colorspacious
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
Name:           python-colorspacious
Version:        1.1.2
Release:        0
Summary:        Python library for doing colorspace conversions
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/njsmith/colorspacious
Source:         https://files.pythonhosted.org/packages/source/c/colorspacious/colorspacious-%{version}.tar.gz
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
BuildArch:      noarch
%python_subpackages

%description
Colorspacious is a library for performing colorspace conversions.

In addition to the most common standard colorspaces (sRGB, XYZ, xyY,
CIELab, CIELCh), it also includes color vision deficiency ("color
blindness") simulations using the approach of Machado et al (2009), a
complete implementation of CIECAM02
<https://en.wikipedia.org/wiki/CIECAM02>, and the perceptually
uniform CAM02-UCS / CAM02-LCD / CAM02-SCD spaces proposed by Luo et al
(2006).

%prep
%setup -q -n colorspacious-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no tests present

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
