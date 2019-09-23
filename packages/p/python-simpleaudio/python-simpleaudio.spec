#
# spec file for package python-simpleaudio
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-simpleaudio
Version:        1.0.2
Release:        0
Summary:        Asynchronous audio playback for Python
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/hamiltron/py-simple-audio
Source:         https://files.pythonhosted.org/packages/source/s/simpleaudio/simpleaudio-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(alsa)

%python_subpackages

%description
The simplaudio package provides audio playback capability for Python 3
on OSX, Windows, and Linux.


%prep
%setup -q -n simpleaudio-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/*

%changelog
