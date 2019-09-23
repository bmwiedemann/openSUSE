#
# spec file for package python-pyo
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-pyo
Version:        0.9.1
Release:        0
License:        GPL-3.0
Summary:        Python digital signal processing module
Url:            http://ajaxsoundstudio.com/software/pyo/
Group:          Development/Languages/Python
Source:         http://ajaxsoundstudio.com/downloads/pyo_%{version}-src.tar.bz2
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  portmidi-devel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%python_subpackages

%description
PYO is a Python module written in C to help digital signal processing
script creation. 

%prep
%setup -q -n pyo_%{version}-src

%build
export CFLAGS="%{optflags}"
%python_build --use-jack --use-double

%install
%python_install --use-jack --use-double
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc ChangeLog README.md
%license COPYING.txt COPYING.LESSER.txt
%{python_sitearch}/*

%changelog
