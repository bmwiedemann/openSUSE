#
# spec file for package python2-PyX
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python2-PyX
Version:        0.12.1
Release:        0
Summary:        Python package for the generation of PostScript, PDF, and SVG files
License:        GPL-2.0+
Group:          Development/Languages/Python
Url:            http://pyx.sourceforge.net/
Source:         https://files.pythonhosted.org/packages/source/P/PyX/pyx-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools
Obsoletes:      python-pyx <= %{version}
Provides:       python-pyx = %{version}
Obsoletes:      python-PyX <= %{version}
Provides:       python-PyX = %{version}
BuildRequires:  fdupes
BuildArch:      noarch

%description
PyX is a Python package for the creation of PostScript, PDF, and SVG files. It
combines an abstraction of the PostScript drawing model with a TeX/LaTeX
interface. Complex tasks like 2d and 3d plots in publication-ready quality are
built out of these primitives.

%prep
%setup -q -n PyX-%{version}

%build
%python2_build

%install
%python2_install
%fdupes %{buildroot}%{python2_sitelib}

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGES LICENSE README
%{python2_sitelib}/*

%changelog
