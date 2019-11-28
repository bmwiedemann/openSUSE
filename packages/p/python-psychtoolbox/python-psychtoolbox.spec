#
# spec file for package python-psychtoolbox
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-psychtoolbox
Version:        3.0.16
Release:        0
# Note: the license text mentions non-FOSS code, but that is not included in this source archive
License:        MIT and BSD-2-Clause AND X11 AND GPL-2.0-or-later AND LGPL-2.1-or-later AND AML
Summary:        Pieces of Psychtoolbox-3 ported to CPython
Url:            http://psychtoolbox.org
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/psychtoolbox/psychtoolbox-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  python-rpm-macros


BuildRequires:  gdb

%python_subpackages

%description
Psychtoolbox is a toolbox for psychophysics experiments.
The PTB core routines provide access to the display frame buffer and color
lookup table, reliably synchronize with the vertical screen retrace, support
sub-millisecond timing, expose raw OpenGL commands, support video playback
and capture as well as low-latency audio, and facilitate the collection of
observer responses. Ancillary routines support common needs like color
space transformations and the QUEST threshold seeking algorithm.

This module contains pieces of Psychtoolbox ported to CPython.

%prep
%setup -q -n psychtoolbox-%{version}
chmod a-x PsychSourceGL/License.txt

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -c 'import psychtoolbox'
$python -c 'from psychtoolbox import *'
}

%files %{python_files}
%doc README
%license PsychSourceGL/License.txt
%{python_sitearch}/psychtoolbox-%{version}-py*
%{python_sitearch}/psychtoolbox/

%changelog
