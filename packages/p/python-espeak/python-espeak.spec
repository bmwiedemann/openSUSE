#
# spec file for package python-espeak
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-espeak
Version:        0.5
Release:        0
Summary:        Python bindings for espeak
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-espeak
Source0:        https://launchpad.net/python-espeak/trunk/0.5/+download/python-espeak-0.5.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  espeak-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python bindings for the eSpeak speech synthesizer.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%fdupes %{buildroot}

%files %{python_files}
%license COPYING
%doc NEWS
%{python_sitearch}/espeak/
%{python_sitearch}/python_espeak-%{version}-py%{python_version}.egg-info

%changelog
